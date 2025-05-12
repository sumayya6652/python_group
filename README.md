📰 News Aggregator using Web APIs and Web Scraping

This Python project is a modern information aggregator that fetches and visualizes news articles using both Web APIs and web scraping. It incorporates object-oriented programming, unit testing, and a user-friendly GUI built entirely with Tkinter, styled to resemble a web dashboard.

📌 Features

🔍 Fetch real-time news headlines by category (e.g., Technology, Sports, Health)

🌐 Uses NewsAPI.org to fetch articles

🧽 Scrapes full article content using BeautifulSoup

📊 Visualizes:

Article count by source (Bar Chart)

Word cloud of article titles

🖥️ Modern GUI with sidebar navigation, styled article cards, and responsive layout

🧪 Built-in unit testing for core components

🗂️ Project Structure

information_aggregator/
├── aggregator.py          # Combines API + Scraping
├── api_handler.py         # Handles NewsAPI integration
├── config.py              # Stores your API key and endpoint
├── gui.py                 # Main GUI interface using Tkinter
├── main.py                # Entry point for the application
├── scraper.py             # Extracts article content
├── visualizer.py          # Bar chart + Word cloud
├── tests/
│   └── test_aggregator.py # Unit tests using unittest

⚙️ Setup Instructions

✅ Step 1: Install Required Libraries

pip install requests beautifulsoup4 matplotlib wordcloud

🔐 Step 2: Configure API Key

Register at https://newsapi.org

Get your API key.

Paste it into config.py:

API_KEY = "your_actual_api_key_here"

🚀 How to Run the App

From your terminal or VS Code:

python main.py

Use the sidebar to:

Select a news category

Fetch styled news cards

Visualize news source distribution or generate a title word cloud

🧪 Running Unit Tests

python -m unittest tests/test_aggregator.py

This tests if the aggregator successfully fetches and combines API + scraped data.

📊 Sample Visuals (optional to include in your final repo)

✅ News Source Distribution (Bar Chart)

✅ Word Cloud of Headlines

📹 Video Demonstration

Add your video presentation link here:

[Click to Watch Demo](https://your-video-link.com)

💡 Bonus Features (Included)

Category dropdown for filtering news ✅

Scrollable UI for articles ✅

Flat modern UI with fonts, colors, spacing ✅

Visuals with Matplotlib and WordCloud ✅

⚠️ Ethical Use Notice

Always respect API usage terms and robots.txt when scraping content.

Refer to:

NewsAPI.org Terms

Website-specific terms before scraping

👨‍💻 Author

Sumayya Maqdoom Makkiya, sumayyamaqdoom1@gmail.com 

