from bs4 import BeautifulSoup
import selenium.webdriver as se
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import csv,os


def collect_info(shortURL):
    url = f"https://www.instagram.com/p/{shortURL}"
    option = se.ChromeOptions()
    option.add_argument('headless')
    option.add_experimental_option("detach", False)
    browser = se.Chrome('path/to/chromedriver',options=option)
    browser.get(url)
    parse_html= BeautifulSoup(browser.page_source,"html.parser")
    date = parse_html.find(class_="_aaqe")
    like= parse_html.find(class_="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj")
    content = parse_html.find(class_ ="_aacl _aaco _aacu _aacx _aad7 _aade")
    date = BeautifulSoup(str(date),'html.parser').text
    like = BeautifulSoup(str(like),'html.parser').text.replace('likes','')
    content = BeautifulSoup(str(content),'html.parser').text
    print(f"Date:{date}\n Likes: {like}\n Text: {content}")

    CurrentPath = os.getcwd()
    file_path = f'{CurrentPath}/instainfo.csv'
    if os.path.isfile(file_path) == False:
      with open(file_path, 'w', newline='') as f:
        header = ["Date","LikeCount","info","URL"]
        writer = csv.writer(f)
        writer.writerow(header)

    csvPath = file_path
    with open(csvPath, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date,like,content,url])

collect_info(input("ShortURL >>>" ))
