def extract_news_links(url, browser):
    soup = browser.get_soup(url)
    print("----- PAGE HTML START -----")
    print(soup.prettify()[:500])  
    print("----- PAGE HTML END -----")
    if not soup:
        return []

    links = []
    for a in soup.select("a[href^='/news/1404']"):
        href = a.get("href")
        if href:
            full_link = "https://www.isna.ir" + href
            links.append(full_link)
    return list(set(links))  


def extract_news_data(url, browser):
    soup = browser.get_soup(url)
    if not soup:
        return None

    try:
        title = soup.find("h1", class_="first-title").text.strip()
        date = soup.find("span", class_="text-meta").text.strip()
        content = " ".join(p.text.strip() for p in soup.select("div[itemprop='articleBody'] p"))
        return {
            "url": url,
            "title": title,
            "date": date,
            "content": content,
        }
    except Exception as e:
        print(f"[⚠️] Failed to parse {url}: {e}")
        return None
