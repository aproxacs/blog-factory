#!/usr/bin/env python3
"""AI Studio prompts.json에서 대화 내용만 추출하여 prompt.md로 변환한다.

사용법:
    python scripts/extract-prompts.py drafts/prompts.json
    python scripts/extract-prompts.py drafts/2026-03-27-지능-진화-문어/prompts.json

출력: 같은 디렉토리에 prompt.md 생성
"""

import json
import sys
from pathlib import Path


def extract(src: Path) -> str:
    data = json.loads(src.read_text(encoding="utf-8"))
    chunks = data.get("chunkedPrompt", {}).get("chunks", [])

    lines: list[str] = []
    for chunk in chunks:
        role = chunk.get("role", "unknown")
        text = chunk.get("text", "").strip()

        # thinking 블록은 건너뛰기
        if chunk.get("isThought"):
            continue

        if not text:
            continue

        label = "🧑 사용자" if role == "user" else "🤖 AI"
        lines.append(f"## {label}\n\n{text}\n")

    return "\n---\n\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("사용법: python scripts/extract-prompts.py <prompts.json>")
        sys.exit(1)

    src = Path(sys.argv[1])
    if not src.exists():
        print(f"파일 없음: {src}")
        sys.exit(1)

    md = extract(src)
    dest = src.parent / "prompt.md"
    dest.write_text(md, encoding="utf-8")

    src_kb = src.stat().st_size / 1024
    dest_kb = dest.stat().st_size / 1024
    ratio = (1 - dest_kb / src_kb) * 100

    print(f"✅ {dest}")
    print(f"   {src_kb:.0f}KB → {dest_kb:.0f}KB ({ratio:.0f}% 감소)")


if __name__ == "__main__":
    main()
