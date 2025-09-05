from playwright.sync_api import sync_playwright


def fetch_html_headless(url: str, out_path: str) -> str:
    """
    Fetch the HTML of a web page using a headless Chromium browser and save it to a file.
    Returns the HTML as a string.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        html = page.content()
        browser.close()
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        return html