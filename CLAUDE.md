# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

AI 에이전트 팀(작가 2~3명 + 편집장)이 협업하여 에세이를 쓰는 Substack 블로그 프로젝트. 코드 프로젝트가 아니라 **콘텐츠 생산 파이프라인**이다.

## 핵심 워크플로우

블로그 작성은 `/blog-write` 스킬로 실행한다. 전체 프로세스는 `.claude/skills/blog-write/SKILL.md`에 정의되어 있다.

```
drafts/prompts.json → summary.md 생성 → 작가 에이전트 병렬 초안 → 편집장 심사·통합 → 팩트체크 → 메타데이터 → 영문 번역 → published/
```

- 작가 에이전트: `agents/writer.md` (model: sonnet, 스타일별 병렬 실행)
- 편집장 에이전트: `agents/editor.md` (model: opus, 고유 톤으로 통합)
- 스타일 라이브러리: `styles/` (기법 참고용, 모방이 아님)
- 피드백 누적: `reviews/feedback-log.md` (작가가 매회 참조)

## 유틸리티

```bash
# AI Studio prompts.json → prompt.md 변환 (thinking 블록 제거)
python scripts/extract-prompts.py drafts/prompts.json
```

## 글의 고유 톤 (모든 에이전트가 인지해야 함)

- **건조한 관찰 + 슬쩍 웃기는 전환**: 진지한 관찰 → 예상 못한 비유나 자기비하
- **체험 > 관찰**: "현상이 있다"보다 "내가 경험했을 때" — 대체 불가능한 문장의 핵심
- **관찰에서 멈추는 결론**: 낙관/비관/해결책 제시 금지. "모르겠다"가 더 정직
- **정보보다 문장의 맛**: 통계 나열보다 날카로운 비유 하나

## 디렉토리 규칙

- `drafts/YYYY-MM-DD-{주제}/` — 작업 중인 글 (summary, 초안들, 리뷰, 최종본)
- `published/YYYY-MM-DD-{주제}/` — 완성된 글 (post-ko.md, post-en.md, meta.md, image-prompt.md)
- 영문 번역은 `published/`에 직접 저장. `drafts/`에 넣지 않는다
- summary.md 생성 후 prompt.md는 삭제한다 — 이후 모든 단계에서 summary.md만 사용

## 누적된 핵심 피드백

- 사용자는 **가독성과 자연스러운 전개**를 문장의 밀도보다 우선시함
- 사실이 아닌 체험 꾸며내기 금지. 팩트체크 필수
- 글이 가치 판단이나 낙관적 결론을 내리지 않도록 주의
- 사용자는 특정 스타일을 고정 선호하지 않음 — 편집장이 가정하지 말 것
- 서양/동양 이분법, 학술 용어 반복 금지
