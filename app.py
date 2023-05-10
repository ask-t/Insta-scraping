from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import csv,os,time

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

if __name__ == "__main__":
    driver = webdriver.Chrome(options=set_chrome_options())
    # Do stuff with your driver
    shortURL = input("ShortURL >>>" )
    url = f"https://www.instagram.com/p/{shortURL}"
    driver.get(url)
    time.sleep(4)
    parse_html= BeautifulSoup(driver.page_source,"html.parser") # Scrape url
    date = parse_html.find(class_="_aaqe")
    like= parse_html.find(class_="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj")
    content = parse_html.find(class_ ="_aacl _aaco _aacu _aacx _aad7 _aade")
    date = BeautifulSoup(str(date),'html.parser').text # remove html tags
    like = BeautifulSoup(str(like),'html.parser').text.replace('likes','')
    content = BeautifulSoup(str(content),'html.parser').text
    print(f"Date:{date}\n Likes: {like}\n Text: {content}")

    # create or update csv file
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
    driver.close()