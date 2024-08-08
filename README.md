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
2. **Install the required Python packages:**

   Create a `requirements.txt` file with the following content:

   ```
   Flask
   selenium
   webdriver-manager
   ```

   Then run:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application:**

   Start the Flask server by running:

   ```bash
   python app.py
   ```

   This will start a local web server on `http://127.0.0.1:5000/`.

2. **Access the scraper endpoint:**

   Open your web browser and navigate to `http://127.0.0.1:5000/`. The scraper will be triggered, and data from the Swish Analytics website will be processed.

## How It Works

- The Flask application starts a web server and listens for incoming requests.
- Upon accessing the root endpoint (`/`), the `selenium_run` function is triggered.
- Selenium navigates to the Swish Analytics MLB stats page for the current date.
- The scraper waits for the page to load and then extracts data from the table.
- The data is formatted into a JSON-compatible structure and returned.

## Notes

- The scraper uses headless Chrome mode, which means the browser runs in the background without a graphical user interface.
- Adjust the sleep duration (`time.sleep(3)`) if the data takes longer to load on the webpage.

## Troubleshooting

- If you encounter issues with ChromeDriver, ensure that your Chrome browser version is compatible with the installed ChromeDriver.
- Check the console output for any errors during the scraping process.

## Contributing

Feel free to submit issues or pull requests if you have improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to replace placeholders like the GitHub repository URL with actual information relevant to your project.
