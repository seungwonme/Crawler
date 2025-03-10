from selenium import webdriver
import dotenv
import time

dotenv.load_dotenv()

driver = webdriver.Firefox()
# driver = webdriver.Chrome()

time.sleep(10000)

# 브라우저 종료
# driver.quit()
