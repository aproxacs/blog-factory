# Blog Project Plan

## Overview
하루 동안 떠오르는 생각과 호기심을 LLM(Claude, Gemini 등)과의 대화를 통해 발전시키고, 이를 블로그 글로 완성하여 게시하는 프로젝트.

## Content Pillars (주요 주제)
- 철학적 사고
- 뇌과학
- AI
- (필요시 확장)

## Workflow

### 1. 아이디어 발전
- 일상에서 떠오르는 생각, 호기심, 질문을 LLM과 대화하며 전개
- 여러 LLM(Claude, Gemini 등)을 활용 가능
- 질문과 토론을 통해 아이디어를 깊이 있게 탐구
- 어떤 LLM을 사용했는지 기록 — LLM별 차이 비교 콘텐츠로도 활용 가능

### 2. 글쓰기
- 대화 내용을 바탕으로 블로그 글 작성
- 글쓰기 스타일 라이브러리에서 선택 (styles/ 폴더 참고)
- 초안 작성 → 수정 → 완성

### 3. 메타데이터
- 제목 및 부제 결정
- 태그 선정
- 블로그 이미지용 프롬프트 생성

### 4. 게시
- 한글 + 영문 두 버전 작성
- Substack에 수동 게시 (공식 API 없음, 비공식 Python 라이브러리 존재)
- Substack: https://substack.com/@changshin2/posts
- 추후 Ghost 등 API 지원 플랫폼 검토

### 5. 홍보 (추후)
- X/Twitter: 핵심 인사이트를 쓰레드로
- LinkedIn: 전문적 주제
- Reddit/커뮤니티: 관련 서브레딧 공유

## Writing Styles (글쓰기 스타일 라이브러리)
styles/ 폴더에 각 스타일별 특징과 예시 정리 예정:
- 버트런드 러셀: 논리적, 명쾌, 위트
- 에세이: 개인적, 성찰적
- 설명문: 쉽고 친근하게
- (추가 예정)

## 목표
- 주 1~2회 글 게시
- 구독자 확보 (구체적 숫자는 추후 설정)
- 추후 고려: 홍보 전략, 반응 분석, 데이터 기반 개선

## 트래킹
글마다 기록:
- 게시일, 주제, 스타일, 사용한 LLM
- 조회수, 좋아요, 댓글 수, 신규 구독자
- 패턴 분석으로 콘텐츠 전략 개선

## 플랫폼 전략
- **현재**: Substack (수동 게시) — 구독/추천 기반이라 AI 시대에 유리
- **추후 검토**: Ghost (공식 API 지원, 뉴스레터 내장, 오픈소스)
- SEO/검색 유입에 의존하지 않음 — zero-click search 시대
- 능동적 독자 확보: SNS 공유, Substack Notes/추천, 커뮤니티 참여

## 파일 구조
```
blogger/
├── PLAN.md              # 이 문서
├── styles/              # 글쓰기 스타일 라이브러리
├── drafts/              # 작성 중인 글
│   └── YYYY-MM-DD-제목/
│       ├── prompt.md    # LLM 대화 전체 기록 (사용한 LLM 명시)
│       ├── summary.md   # 대화 요약 및 핵심 아이디어
│       ├── draft-ko.md  # 한글 초안
│       ├── draft-en.md  # 영문 초안
│       └── image-prompt.md  # 이미지 생성 프롬프트
├── published/           # 게시 완료된 글
│   └── YYYY-MM-DD-제목/
│       ├── post-ko.md
│       ├── post-en.md
│       └── image-prompt.md
└── tracking.md          # 게시 트래킹 시트
```
