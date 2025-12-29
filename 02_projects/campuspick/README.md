1️⃣ 왜 Selenium이어야 했나?

캠퍼스픽 메인 페이지의 카테고리 <a data-category>는 브라우저에서 JS가 실행된 후 DOM에 삽입되는 구조입니다.

즉, 페이지 로드 직후 HTML 문서 자체에는 해당 태그가 없음.

requests.get()처럼 단순 HTTP 요청으로 가져온 HTML에는 JS 실행이 되지 않기 때문에, BeautifulSoup으로 파싱해도 카테고리 <a>가 없는 상태가 됩니다.

결과적으로, requests만으로는 len(category_elements) == 0이 나옵니다.
---
2️⃣ 정적 HTML로 가져오면 안 되는 이유

정적 HTML = 서버가 처음 내려주는 HTML 코드 그대로

동적 요소(카테고리 링크, 스크롤 로딩 공모전 카드 등)는 JS가 DOM을 조작해서 추가하기 때문에 포함되지 않음

requests로 확인해보면 <div class="wrap"> 안에 a[data-category]가 없거나 빈 상태로 존재할 수 있음
---

3️⃣ Selenium을 쓰는 이유

브라우저를 띄워 실제 JS 실행

JS가 DOM 조작 → 카테고리 <a> 태그 생성

이후 driver.find_elements(...)로 안정적으로 선택 가능

즉, 동적 렌더링 페이지에서는 Selenium이 필수적