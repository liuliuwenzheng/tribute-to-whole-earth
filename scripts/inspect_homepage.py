#!/usr/bin/env python3
"""Re-extract publication catalog from https://wholeearth.info/ homepage HTML."""
from __future__ import annotations

import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SOURCE = "https://wholeearth.info/"
SECTIONS = [
    ("whole-earth-catalogs", "Whole Earth Catalogs", "①"),
    ("coevolution-quarterly", "CoEvolution Quarterly", "②"),
    ("whole-earth-software-review", "Whole Earth Software Review", "③"),
    ("whole-earth-review", "Whole Earth Review", "④"),
    ("whole-earth-magazine", "Whole Earth Magazine", "⑤"),
    ("special-publications", "Special Publications", "⑥"),
]


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "wholeearth-i18n/0.1 (+research)"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return resp.read().decode("utf-8", "replace")


def parse_publications(page: str) -> list[dict]:
    pubs: list[dict] = []
    for block in re.split(r'(?=<a[^>]+href="/p/)', page)[1:]:
        m = re.match(r'<a[^>]+href="(/p/([^"]+))"', block)
        if not m:
            continue
        path, slug = m.group(1), m.group(2)
        title_m = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", block[:4000], re.S)
        if title_m:
            title = " ".join(re.sub(r"<[^>]+>", " ", title_m.group(1)).split())
        else:
            title = slug.replace("-", " ").title()
        aid_m = re.search(r'archive\.org/(?:details|download)/([^/"\']+)', block[:8000])
        pubs.append(
            {
                "slug": slug,
                "path": path,
                "title": title,
                "archive_id": aid_m.group(1) if aid_m else None,
                "url": f"https://wholeearth.info{path}",
            }
        )
    return pubs


def assign_collections(page: str, pubs: list[dict]) -> list[dict]:
    by_slug = {p["slug"]: p for p in pubs}
    sec_pos = []
    for sid, name, idx in SECTIONS:
        p = page.find(f'id="{sid}"')
        if p < 0:
            p = page.find(f"/#{sid}")
        sec_pos.append((p if p >= 0 else 10**9, sid, name, idx))
    sec_pos.sort()
    collections = []
    for i, (pos, sid, name, idx) in enumerate(sec_pos):
        end = sec_pos[i + 1][0] if i + 1 < len(sec_pos) else len(page)
        chunk = page[pos:end]
        entries = []
        for s in re.findall(r'href="/p/([^"]+)"', chunk):
            if s in by_slug:
                e = dict(by_slug[s])
                e["collection"] = sid
                entries.append(e)
        collections.append(
            {
                "id": sid,
                "index": idx,
                "name_en": name,
                "count": len(entries),
                "publications": entries,
            }
        )
    return collections


def main() -> None:
    page = fetch(SOURCE)
    pubs = parse_publications(page)
    catalog = {
        "source": SOURCE,
        "extracted_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "publication_count": len(pubs),
        "collections": assign_collections(page, pubs),
    }
    out = Path(__file__).resolve().parents[1] / "data" / "catalog.json"
    out.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({catalog['publication_count']} publications)")


if __name__ == "__main__":
    main()
