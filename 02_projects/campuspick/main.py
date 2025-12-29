# main.py
# Campuspick 크롤러 모듈 : 카테고리별 대회 정보 추출 및 CSV 저장 + 처리 시간 기록
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

class CampuspickCrawler:
    def __init__(self, driver_path=None, data_dir="./data/"):
        self.driver_path = driver_path
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        self.driver = webdriver.Chrome(self.driver_path) if self.driver_path else webdriver.Chrome()
        print("[INFO] Chrome driver started")
        self.time_records = []  # 각 카테고리 시간 기록용 리스트

    def load_categories(self, csv_path="./data/contest_categories.csv"):
        self.categories = pd.read_csv(csv_path)
        print(f"[INFO] Loaded {len(self.categories)} categories")

    def scroll_page(self, times=10, pause=1):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        start_scroll = time.time()
        for _ in range(times):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        end_scroll = time.time()
        scroll_elapsed = end_scroll - start_scroll
        print(f"[INFO] Scrolling done in {scroll_elapsed:.2f} seconds")
        return scroll_elapsed

    def extract_cards(self):
        start_extract = time.time()
        cards = self.driver.find_elements(By.CSS_SELECTOR, "a.top")
        results = []

        for card in cards:
            try:
                title = card.find_element(By.TAG_NAME, "h2").text
                company = card.find_element(By.CSS_SELECTOR, "p.company").text
                dday = card.find_element(By.CSS_SELECTOR, "p.info span.dday").text
                views = card.find_element(By.CSS_SELECTOR, "p.info span.viewcount").text
                badges = [span.text for span in card.find_elements(By.CSS_SELECTOR, "p.badges span")]
                img_url = card.find_element(By.TAG_NAME, "figure").get_attribute("data-image")

                results.append({
                    "title": title,
                    "company": company,
                    "dday": dday,
                    "views": views,
                    "badges": badges,
                    "img_url": img_url
                })
            except Exception as e:
                print(f"[WARNING] Failed to extract card: {e}")

        end_extract = time.time()
        extract_elapsed = end_extract - start_extract
        print(f"[INFO] Extracted {len(results)} cards in {extract_elapsed:.2f} seconds")
        return results, extract_elapsed

    def crawl_category(self, category_id, category_name, scroll_times=10):
        url = f"https://www.campuspick.com/contest?category={category_id}"
        self.driver.get(url)
        print(f"[INFO] Loaded category '{category_name}' at {url}")
        time.sleep(2)  # 렌더링 대기

        start_total = time.time()
        scroll_time = self.scroll_page(times=scroll_times)
        data, extract_time = self.extract_cards()
        end_total = time.time()
        total_elapsed = end_total - start_total

        # CSV 저장
        csv_path = os.path.join(self.data_dir, f"category_{category_id}.csv")
        pd.DataFrame(data).to_csv(csv_path, index=False)
        print(f"[INFO] Saved {len(data)} cards to {csv_path}")
        print(f"[INFO] Total category '{category_name}' processing time: {total_elapsed:.2f} seconds\n")

        # 시간 기록 리스트에 저장
        self.time_records.append({
            "category_id": category_id,
            "category_name": category_name,
            "scroll_time": scroll_time,
            "extract_time": extract_time,
            "total_time": total_elapsed,
            "num_cards": len(data)
        })

    def run(self, scroll_times=10):
        for _, row in self.categories.iterrows():
            self.crawl_category(row["category_id"], row["category_name"], scroll_times=scroll_times)

        # 모든 카테고리 완료 후 시간 기록 CSV 저장
        time_csv_path = os.path.join(self.data_dir, "crawl_times.csv")
        pd.DataFrame(self.time_records).to_csv(time_csv_path, index=False)
        print(f"[INFO] Saved crawl times to {time_csv_path}")

    def close(self):
        self.driver.quit()
        print("[INFO] Chrome driver closed")


if __name__ == "__main__":
    crawler = CampuspickCrawler()
    crawler.load_categories()
    crawler.run(scroll_times=10)
    crawler.close()
