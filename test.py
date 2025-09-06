from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv


load_dotenv()
email = os.getenv("PUBLICWWW_EMAIL")
password = os.getenv("PUBLICWWW_PASSWORD")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://publicwww.com/profile/login.html")
    page.fill('input[name="email"]', email)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"]')
    page.wait_for_load_state("networkidle")
    page.goto("https://publicwww.com/websites/zsiqscript/20", timeout=60000)
    html = page.content()
    with open("data/html/page_20.html", "w", encoding="utf-8") as f:
        f.write(html)