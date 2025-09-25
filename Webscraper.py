import requests
from bs4 import BeautifulSoup

# URL of the news website (using BBC as an example)
URL = "https://www.bbc.com/news"

# Send GET request
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract headlines (BBC uses <h2> for headlines)
headlines = []
for h2 in soup.find_all("h2"):
    text = h2.get_text(strip=True)
    if text and text not in headlines:  # avoid duplicates
        headlines.append(text)

# Save to a .txt file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, title in enumerate(headlines, start=1):
        f.write(f"{i}. {title}\n")

print(f"✅ {len(headlines)} headlines scraped and saved to headlines.txt")
