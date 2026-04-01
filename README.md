# Blog Factory

AI 에이전트 팀과 함께 에세이를 쓰는 블로그 프로젝트.

LLM과의 대화에서 시작된 아이디어를 여러 스타일의 작가 에이전트가 초안으로 쓰고, 편집장 에이전트가 고유한 톤으로 통합하여 최종본을 만든다. 한글과 영문 두 버전으로 [Substack](https://aproxacs.substack.com)에 게시한다.

## 워크플로우

```
AI Studio 대화 (prompts.json)
    ↓
summary.md 생성 (글 방향 + 활용할 소재)
    ↓
작가 에이전트 2~3명이 각자 다른 스타일로 초안 작성 (병렬)
    ↓
편집장 에이전트가 심사 → 고유 톤으로 통합 → 최종본
    ↓
팩트체크 → 메타데이터 생성 → 영문 번역 → 게시
```

## 프로젝트 구조

```
├── .claude/skills/blog-write/   # 글쓰기 스킬 (워크플로우 정의)
│   ├── SKILL.md                 # 전체 프로세스
│   └── agents/                  # 작가, 편집장 에이전트 정의
├── styles/                      # 참고 스타일 라이브러리
├── drafts/                      # 작성 중인 글
│   └── YYYY-MM-DD-주제/
│       ├── summary.md           # 글 방향 + 활용할 소재
│       ├── draft-{스타일}.md    # 스타일별 초안
│       ├── review.md            # 편집장 심사 결과
│       └── draft-final.md       # 최종본
├── published/                   # 게시 완료된 글
│   └── YYYY-MM-DD-주제/
│       ├── post-ko.md           # 한글 최종본
│       ├── post-en.md           # 영문 번역
│       ├── meta.md              # 제목, 태그, SNS 텍스트
│       └── image-prompt.md      # 커버 이미지 프롬프트
├── reviews/feedback-log.md      # 편집장 피드백 누적 로그
└── scripts/                     # 유틸리티
```

## 게시된 글

| 날짜 | 한글 | English |
|------|------|---------|
| 2026-03-31 | [광고는 어디로 갔을까](https://substack.com/home/post/p-192696829) | [Where Did All the Ads Go?](https://substack.com/home/post/p-192697123) |
| 2026-03-29 | [길리 섬의 말과 나의 도덕적 원](https://substack.com/home/post/p-192475759) | [The Horse on Gili Island and My Moral Circle](https://substack.com/home/post/p-192475891) |
| 2026-03-27 | [물고기는 왜 좌우가 같을까](https://substack.com/home/post/p-192288746) | [Why Do Fish Look the Same on Both Sides?](https://substack.com/home/post/p-192289185) |

## 셋업 (새 머신)

Claude Code의 메모리가 `.claude/memory/`에 저장되어 있다. 새 머신에서 클론한 후 심링크를 걸어야 메모리가 연결된다:

```bash
# 프로젝트 클론 후
ln -s "$(pwd)/.claude/memory" ~/.claude/projects/-Users-$(whoami)-$(pwd | sed 's|/|-|g' | sed 's|^-||')/memory
```

또는 프로젝트 경로에 맞게 직접 지정:

```bash
# Claude Code가 사용하는 메모리 경로 확인 후
ln -s /path/to/blog-factory/.claude/memory ~/.claude/projects/<project-key>/memory
```

> `<project-key>`는 프로젝트 절대 경로에서 `/`를 `-`로 치환한 값 (예: `-Users-changshin-work-blogger`)

## 도구

- [Claude Code](https://claude.ai/claude-code) — 에이전트 오케스트레이션
- [Substack](https://aproxacs.substack.com) — 게시 플랫폼
- [Google AI Studio](https://aistudio.google.com/) — 브레인스토밍용 대화
