import time
from config import BASE_URL, CATEGORIES
from utils.fetcher import Browser
from utils.parser import extract_news_links, extract_news_data
from utils.exporter import save_to_csv

def crawl_category(slug, name, browser):
    print(f"\n📂 Crawling {name} ...")
    category_url = f"{BASE_URL}/service/{slug}"
    links = extract_news_links(category_url, browser)
    print(f"Found {len(links)} news links.")

    all_news = []
    for i, link in enumerate(links[:20], start=1):  
        print(f"🔎 [{i}] {link}")
        data = extract_news_data(link, browser)
        if data:
            print(f"✅ {data['title']}")
            all_news.append(data)
        else:
            print(f"❌ Failed to extract from {link}")
        time.sleep(1)  

    save_to_csv(all_news, f"{name}.csv")

def main():
    browser = Browser()
    for slug, name in CATEGORIES.items():
        crawl_category(slug, name, browser)
    browser.close()

if __name__ == "__main__":
    main()
