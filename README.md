# PublicWWW Scraper

This project scrapes paginated results from PublicWWW for a given query (e.g., `zsiqscript`), saves each page's HTML, and extracts tabular data (Rank, URL, Snippets) to CSV files.

## Features
- Uses a headless browser (Playwright) to fetch HTML, bypassing anti-scraping measures.
- Parses tables from each page and saves them as CSVs.
- Cleans the Rank column to ensure it contains only integers.

## Limitation
If you want to access data after page 19 on the site you have to log in.

## Usage
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    python -m playwright install
    ```
2. Run the main script to scrape and extract tables:
    ```bash
    python main.py
    ```
   - Adjust `base_url`, `page_number_start`, and `page_number_end` in `main.py` as needed.

## File Structure
- `scrape_html.py`: Fetches HTML using Playwright.
- `extract_table.py`: Extracts table data from HTML and saves as CSV.
- `main.py`: Orchestrates scraping and extraction for multiple pages. Also includes utilities to combine CSVs and filter for .com domains.
## Filtering for .com domains

After combining CSVs, you can filter the results to only include rows where the URL contains `.com`:

```python
sort_com("data/data_combined.csv", "data/data_combined_sorted.csv")
```
This will save only rows with `.com` in the URL to a new CSV file.
- `data/html/`: Saved HTML files.
- `data/csv/`: Saved CSV files.

## Notes
- Make sure Chromium is installed via Playwright before running.
- The project is designed for simple, robust scraping and extraction. For advanced error handling or parallel scraping, extend as needed.
