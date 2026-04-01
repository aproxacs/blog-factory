---
name: Blog Project Overview
description: Substack 블로그 프로젝트 개요 — GitHub 리포, Substack URL, 워크플로우, 현재 상태
type: project
---

Substack 블로그 프로젝트. 일상의 생각/호기심을 LLM과 대화하며 발전시킨 후 블로그 글로 완성.

**Why:** AI 시대에 개인 브랜드를 만들어가는 과정. 사고를 글로 정리하고 공유하는 습관 형성.

**How to apply:**
- GitHub: https://github.com/aproxacs/blog-factory (2026-03-31 공개)
- Substack: https://aproxacs.substack.com
- 워크플로우: AI Studio 대화 → prompts.json → summary.md 생성(prompt 삭제) → 작가 에이전트 병렬 초안 → 편집장이 고유 톤으로 통합 → 팩트체크 → 메타데이터/번역 → Substack 수동 게시
- 주 1~2회 게시 목표
- 2026-04-01 기준 3편 게시 완료
- CLAUDE.md 추가됨 (2026-04-01) — 프로젝트 가이드, 고유 톤, 핵심 피드백 요약
- 메모리가 프로젝트 내부(`.claude/memory/`)에 저장됨 — `~/.claude/projects/` 에서 심링크로 참조. 새 머신에서는 심링크 설정 필요 (README 참조)
