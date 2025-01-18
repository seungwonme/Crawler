from selenium import webdriver
from selenium.webdriver.common.by import By
import dotenv
import os
import time

dotenv.load_dotenv()

username = os.getenv("LINKEDIN_USERNAME")
password = os.getenv("LINKEDIN_PASSWORD")

# ChromeDriver 설정
driver = webdriver.Chrome()

# LinkedIn 로그인
driver.get("https://www.linkedin.com/login")
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# time.sleep(10)

# 페이지 스크롤
last_height = driver.execute_script("return document.body.scrollHeight")

for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

see_more_buttons = driver.find_elements(
    By.CLASS_NAME, "feed-shared-inline-show-more-text__see-more-less-toggle"
)
for button in see_more_buttons:
    try:
        button.click()
        time.sleep(1)
    except Exception as e:
        print(f"Error clicking button: {e}")


# 데이터 추출
posts = driver.find_elements(By.CLASS_NAME, "fie-impression-container")
for post in posts:
    author = post.find_element(By.CLASS_NAME, "update-components-actor__title").text
    content = post.find_element(By.CLASS_NAME, "update-components-text").text
    print(f"author: {author}")
    print(f"content: {content}")


# 브라우저 종료
# driver.quit()

time.sleep(100)
