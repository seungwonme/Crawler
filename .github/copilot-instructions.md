# Product Requirements Document (PRD)

## Project Overview

This project aims to crawl updated content from various platforms once a day, store it, and curate high-quality content of interest to show users core summaries and organized information.

## Goals

1. Crawl and store data from multiple platforms
2. Curate high-quality content from crawled data
3. Provide summarized curated content to users

## Platform List

- GeekNews
- LinkedIn
- YouTube
- Reddit
- X (Twitter)
- HackerNews

## Functional Requirements

### 1. Crawler Implementation

Implement crawlers for each platform. Each crawler should include functionality to fetch and store the latest updates from its respective platform.

#### Example: LinkedIn Crawler

```python
# linkedInCrawler/app.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import dotenv
import os
import time

dotenv.load_dotenv()

username = os.getenv("LINKEDIN_USERNAME")
password = os.getenv("LINKEDIN_PASSWORD")

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/login")
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Add page scrolling and data extraction logic
```

### 2. 데이터 저장

크롤링된 데이터를 저장할 데이터베이스를 설계하고 구현합니다. 각 플랫폼의 데이터 구조에 맞게 테이블을 설계합니다.

### 3. 큐레이팅 및 요약

크롤링된 데이터를 분석하여 관심있어할만한 퀄리티 높은 내용을 큐레이팅합니다. 이를 위해 openai의 GPT-3와 같은 자연어 처리 모델을 사용할 수 있습니다.

## 비기능 요구 사항

### 1. 성능

- 크롤러는 각 플랫폼에서 데이터를 효율적으로 가져와야 합니다.
- 데이터베이스는 대량의 데이터를 빠르게 처리할 수 있어야 합니다.

### 2. 보안

- 사용자 데이터는 안전하게 저장되고 전송되어야 합니다.
- 크롤러는 각 플랫폼의 이용 약관을 준수해야 합니다.

### 3. 확장성

- 새로운 플랫폼을 쉽게 추가할 수 있어야 합니다.
- 시스템은 증가하는 사용자 수와 데이터 양을 처리할 수 있어야 합니다.

### 4. 유지보수성

- 코드베이스는 이해하기 쉽고 유지보수하기 쉬워야 합니다.
- 테스트 커버리지가 높아야 합니다.
