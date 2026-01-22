# python-web-scraper
# Hybrid Web Scraper Framework (Requests + Selenium)

## 📌 Project Overview
This project is a **hybrid Python web scraping framework** that automatically determines the best scraping strategy for a given URL.

It can:
- Detect if a website exposes an **API (JSON response)**
- Use **Requests** for API-based scraping
- Fall back to **Selenium** for dynamic or JavaScript-rendered pages
- Handle scrolling, pagination, retries, logging, and structured data storage

This project is built as a **portfolio-ready scraper**, following real-world scraping patterns and best practices.

Target site used for testing: **Books to Scrape** (public demo website).

---

## 🎯 Features
- Automatic API detection
- Requests-based scraping for APIs
- Selenium-based scraping for dynamic pages
- Infinite scroll handling
- Pagination via “Next” button
- Retry logic for failed requests
- Duplicate page detection
- Centralized logging (file + console)
- Save scraped data to JSON and CSV
- Modular, reusable architecture

---

## 🧠 Scraping Logic Flow
Start
└── Check if URL returns JSON
├── Yes → Use Requests → Save JSON
└── No → Use Selenium
├── Scroll page
├── Handle pagination
├── Collect HTML pages
├── Parse data
└── Save JSON & CSV

---

## 🛠 Tech Stack
- Python 3
- Requests
- Selenium (Chrome WebDriver)
- BeautifulSoup (bs4)
- Logging
- CSV / JSON

---

## 📂 Project Structure
project/
│
├── base_scrap.py # Requests-based scraper
├── base_selenium.py # Selenium scraper (scroll & pagination)
├── api_check.py # API detection logic
├── parse.py # HTML parsing logic
├── save.py # JSON & CSV saving utilities
├── log.py # Logging configuration
├── main.py # Main entry point
│
├── Results/
│ ├── selenium_products.json
│ └── selenium_products.csv
│
└── scrap.log # Log file


---

## ⚙️ How It Works

### 1️⃣ API Detection
The scraper first checks whether the URL returns a valid JSON response.

If JSON data is detected, the scraper switches to **Requests** for faster and cleaner data extraction.

---

### 2️⃣ Requests-Based Scraping
- Used only when an API is detected
- Parses JSON directly
- Saves output as a `.json` file

---

### 3️⃣ Selenium Scraping
Used when no API is detected.

Features:
- Headless Chrome browser
- Safe page loading with retries
- Infinite scrolling support
- Pagination handling using a “Next” button
- Duplicate HTML page detection

---

### 4️⃣ Data Parsing
HTML pages are parsed using **BeautifulSoup** to extract:
- Book title
- Price
- Availability
- Product link

---

### 5️⃣ Data Storage
Scraped data is saved as:
- **JSON** (structured storage)
- **CSV** (analysis-ready format)

All files are stored inside the `Results/` directory.

---

## ▶️ How to Run

### Requirements
- Python 3.9+
- Google Chrome
- ChromeDriver available in system PATH

### Install dependencies


pip install requests selenium beautifulsoup4


⚠️ Disclaimer

This project is for educational and portfolio purposes

Target site is a public scraping demo

Always respect robots.txt and site terms when scraping real websites
