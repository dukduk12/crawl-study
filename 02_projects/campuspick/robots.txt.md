## 🛡️ Campuspick robots.txt 분석 및 수집 가이드

### 1️⃣ 사이트 기본 정보
- **URL**: [campuspick.com](https://www.campuspick.com)
- **Robots.txt**: [Link](https://www.campuspick.com/robots.txt)
- **대상**: 공모전(Contest) 데이터 수집

---

### 2️⃣ Robots.txt 규약 분석
모든 User-agent(`*`)에 대해 아래 경로의 접근을 금지함:
- **접근 불가(❌)**: `/download`, `/linkclick`, `/login`, `/page/*` (약관 및 고객지원)
- **접근 가능(✅)**: `/contest`, `/activity`, `/club` 등 주요 리스트 및 상세 페이지

> **결론**: 서비스 이용 약관 및 개인정보 페이지를 제외한 실제 데이터 영역은 크롤링이 가능함.

---
### 3️⃣ 상세 크롤링 전략

| 단계 | 수행 내용 | 비고 |
| :--- | :--- | :--- |
| **A. 탐색** | 카테고리별 URL 파라미터 분석 (`category=101~109`) | - |
| **B. 수집** | 무한 스크롤 대응 (Selenium 활용 스크롤링) | API 호출 방식 권장 |
| **C. 파싱** | 상세 페이지 내 제목, 주최, 이미지 URL, 마감일 추출 | BeautifulSoup4 활용 |
| **D. 저장** | JSON/CSV 저장 및 이미지 로컬 다운로드 | `time.sleep` 필수 적용 |

---

### 4️⃣ 기술적 주의사항 (Ethical Scraping)
- **Rate Limiting**: `time.sleep(1)` 또는 `2` 정도의 간격을 두어 IP 차단 방지.
- **User-Agent 설정**: 요청 헤더에 브라우저 정보(User-Agent)를 포함하여 봇 감지 우회.
- **서버 부하**: 가급적 이용자가 적은 시간대(새벽 등)에 수행