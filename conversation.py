# 4. 해커스토익에서 오늘의 영어회화 가져오기
def scrape_english():
  print("[오늘의 영어회화]")
  hackers_url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
  soup = create_soup(hackers_url)

  eng = soup.find_all("div", attrs={"class": "conv_txt"})[1].get_text().strip().replace("\n\n", "\n").replace("\n\n", "\n")
  kor = soup.find_all("div", attrs={"class": "conv_txt"})[0].get_text().strip().replace("\n\n", "\n").replace("\n\n", "\n")

  message = f"[오늘의 영어회화]\n(영어지문)\n{eng}\n\n(한글지문)\n{kor}\n"
  save_to_txt(message)
