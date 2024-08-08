# Flask-Selenium MLB Stats Scraper

This project uses Flask to serve a web endpoint that triggers a Selenium-based web scraping process to fetch MLB batter vs. pitcher statistics from the Swish Analytics website. The scraper extracts data from a table and processes it for further use.

## Overview

- **Flask** is used to create a web server.
- **Selenium** is used to automate web browser interaction and scrape data.
- **webdriver_manager** helps manage the browser driver binaries.
- The data is scraped from the Swish Analytics site and formatted as JSON.

## Prerequisites

- Python 3.x
- Chrome browser installed

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/flask-selenium-stats-scraper.git
   cd flask-selenium-stats-scraper
