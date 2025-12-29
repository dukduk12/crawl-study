# 🕷️ crawl-study

웹 데이터 수집(Web Crawling & Scraping) 기술을 학습하는 repo

---

## 📖 Theory Summary

### 1. scraping vs crawling
- **scraping**: 특정 페이지에서 타겟 데이터를 발췌하는 것 (핀셋 추출).
- **crawling**: 봇이 링크를 타고 돌아다니며 여러 페이지를 긁어모으는 것 (그물 수집).

### 2. Static vs Dynamic Site
- **정적(Static)**: 서버에서 이미 완성된 HTML을 보내줌. `requests` + `bs4` 조합으로 해결 가능. 빠름.
- **동적(Dynamic)**: JS가 브라우저에서 실행된 뒤 데이터가 나타남 (예: 스크롤 시 추가 로딩). `Selenium`이나 `Playwright` 필요. 상대적으로 느림.

### 3. 스크래핑 프로세스 (3 Step)
1. **Request**: `requests`를 통해 대상 URL의 HTML 데이터 수집.
2. **Parse**: `BS4`를 이용하여 HTML 문자열을 객체 구조로 변환.
3. **Extract**: CSS Selector나 XPath를 활용하여 필요한 데이터만 추출.


### 4. 주요 라이브러리 
- **Requests**: 파이썬용 HTTP 라이브러리. 날것의 HTML을 가져올 때 사용함.
- **BS4 (BeautifulSoup)**: HTML 텍스트를 파이썬 객체로 바꿔줌. 원하는 태그 찾기 장인.
- **Selenium**: 진짜 브라우저를 띄워서 제어함. 로그인, 클릭, 스크롤 등 인간인 척 해야 할 때 씀.

### 5. robots.txt 
- 사이트 루트 경로 뒤에 `/robots.txt` 붙여서 확인 가능 
- `User-agent: *`: 모든 로봇에게 적용.
- `Disallow: /`: 여기는 긁어가지 마라.
- **주의**: 수집 허용 구역이라도 짧은 시간에 미친 듯이 요청 보내면 IP 차단됨. (DDoS 취급 주의)
  
---
## 📁 Repository Structure

- `01_basic/` : requests, BeautifulSoup, Selenium 기초 실습
- `02_projects/` : 실제 사이트를 대상으로 한 크롤링 프로젝트
- `00_docs/` : 공통 이미지 및 참고 자료

---

## 🛠️ 실전 프로젝트 현황

| 사이트 | 카테고리 | 도구 | 상태 |
| :--- | :--- | :--- | :--- |
| campuspick | 커뮤니티 | Selenium | 🚧 |

* 🚧: 진행 중 | ✅ 완료
---

## 🚀 실행 가이드
1. 가상환경 생성: `uv venv`
2. 의존성 설치 : `uv sync`
3. 가상환경 활성화 : `.venv\Scripts\activate` (Windows)
4. 패키지 추가: `uv add [package_name]`
5. 스크립트 실행: `uv run python [file_name]`