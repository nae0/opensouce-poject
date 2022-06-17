def scrape_it_news():
    print("[[ 오늘의 IT 뉴스 ]]\n")
    url=""
    news_list = find("ul",attrs={}).find_all("li", limit=5)
    for index, news in enumerate(news_list):
        a_idx=0
        img=news.find("img")
        if img:
            a_idx=1

        title=news.find_all("a")[a_idx].get_text().strip()
        link=news.find_all("a")[a_idx]["href"]
        print("{}. {}".format(index, title))
        print("   (링크 : {})".format(link)) 
    print()
