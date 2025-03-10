from selenium.webdriver.common.by import By
import os
import time
import getpass
from driver import driver


def CrawlingLinkedIn():
    username = os.getenv("LINKEDIN_USERNAME")
    password = os.getenv("LINKEDIN_PASSWORD")

    if not username:
        username = input("Enter your LinkedIn username: ")

    if not password:
        password = getpass.getpass("Enter your LinkedIn password: ")

    # LinkedIn 로그인
    driver.get("https://www.linkedin.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(30)

    # 페이지 스크롤
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    see_more_buttons = driver.find_elements(
        By.CLASS_NAME, "feed-shared-inline-show-more-text__see-more-less-toggle"
    )

    for button in see_more_buttons:
        try:
            driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
        except Exception as e:
            print(f"Error clicking button: {e}")

    # 데이터 추출
    posts = driver.find_elements(By.CLASS_NAME, "fie-impression-container")
    with open("linkedin_posts.md", "w", encoding="utf-8") as f:
        for post in posts:
            try:
                author = post.find_element(
                    By.CSS_SELECTOR, ".update-components-actor__title span"
                ).text
                img = post.find_element(
                    By.CSS_SELECTOR, ".ivm-view-attr__img--centered"
                )
                content = post.find_element(
                    By.CSS_SELECTOR, ".update-components-text"
                ).text
                f.write(f"Author: {author}\n")
                f.write(f"Content: {content}\n")
                f.write(f"![]({img.get_attribute('src')})\n\n")
                f.write("---\n\n")
            except Exception as e:
                print(f"Error extracting post data: {e}")
