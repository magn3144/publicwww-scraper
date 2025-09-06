from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv
from extract_table import extract_table_to_csv


def fetch_html_headless(page, url: str, out_path: str) -> str:
    """
    Fetch the HTML of a web page using a headless Chromium browser and save it to a file.
    Returns the HTML as a string.
    """
    page.goto(url, timeout=60000)
    html = page.content()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return page

def scrape_pages(base_url, page_number_start, page_number_end):
    """
    Scrape a range of paginated URLs and extract table data to CSV files.
    For each page in the range, fetch HTML and save it, then extract the table and save as CSV.
    """
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

        for i in range(page_number_start, page_number_end):
            page = fetch_html_headless(page, f"{base_url}/{str(i)}", f"data/html/page_{i}.html")
            print(f"Saved page {i} to data/html/page_{i}.html")
            n_rows = extract_table_to_csv(f"data/html/page_{i}.html", f"data/csv/page_{i}.csv")
            print(f"Extracted {n_rows} rows to data/csv/page_{i}.csv")