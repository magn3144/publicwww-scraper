from bs4 import BeautifulSoup
import csv
import re


def extract_table_to_csv(html_path: str, csv_path: str) -> int:
    """
    Parse the HTML file and extract the table with columns Rank, Url, Snippets.
    Save the extracted rows to a CSV file.
    Returns the number of rows written.
    """
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    table = soup.find("table", class_="table")
    if not table:
        raise ValueError("Could not find table with class 'table'")
    rows = table.find_all("tr")
    data = []
    for row in rows[1:]:  # skip header
        cols = row.find_all("td")
        if len(cols) < 3:
            continue
        rank_raw = cols[0].get_text(strip=True)
        rank = re.sub(r"\D", "", rank_raw)
        url = cols[1].get_text(strip=True)
        snippets = cols[2].get_text(" ", strip=True)
        data.append([rank, url, snippets])
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Rank", "Url", "Snippets"])
        writer.writerows(data)
    return len(data)