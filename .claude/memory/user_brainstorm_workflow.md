---
name: Brainstorm Workflow Preference
description: 블로그 소재 브레인스토밍 시 대화 내용 저장 방식 — AI 스튜디오 대비 Claude Code 워크플로우
type: user
---

블로그 주제 브레인스토밍을 LLM 대화로 진행. 평소에는 Google AI 스튜디오를 사용하며 대화 내역을 구글 드라이브로 다운로드해서 보관.

Claude Code에서는 대화 도중/끝에 "파일로 저장해줘"라고 요청하는 방식을 선호:
- 대화 중 아이디어가 정리되면 → `drafts/` 폴더에 저장 요청
- 대화 끝에 → `drafts/summary.md`로 정리 요청
- 이후 `/blog-write` 스킬로 글 작성 연계
