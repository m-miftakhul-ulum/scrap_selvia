

# Sellvia Product Scraper

A Python script to scrape product details (titles, links, prices, and descriptions) from the Sellvia catalog website and export the data into CSV and Excel formats.

---

## Features
- Scrapes product data from the Sellvia website.
- Extracts the following details for each product:
  - **Title**: Product name.
  - **Product Link**: Direct link to the product page.
  - **Price**: The sale price of the product.
  - **Description**: Detailed description of the product.
- Saves the scraped data into both `.csv` and `.xlsx` formats.
- Prints a success message after exporting.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/sellvia-scraper.git
   cd sellvia-scraper
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Dependencies
This project uses the following Python libraries:
- **BeautifulSoup4**: For HTML parsing and web scraping.
- **Requests**: For making HTTP requests.
- **Pandas**: For creating and exporting structured data.

You can install them with:
```bash
pip install beautifulsoup4 requests pandas
```

---

## Usage

1. Open the script file and ensure the `url` variable points to the desired Sellvia catalog page.
   ```python
   url = requests.get("https://sellviacatalog.com/products?s=phone&page=3")
   ```

2. Run the script:
   ```bash
   python scraper.py
   ```

3. After successful execution, you will find the following files in the directory:
   - `datanya.csv`: CSV file containing scraped product data.
   - `datanya.xlsx`: Excel file containing scraped product data.

4. A success message will be printed to the console:
   ```
   success
   ```

---

## Example Output
Example of the saved CSV/Excel file structure:

| **judul**                                    | **product link**                           | **price**  | **description**                                                                                                                                      |
|----------------------------------------------|--------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 360° Rotatable Aluminum Tablet and Phone Stand | https://sellviacatalog.com/product/123456 | US $14.08  | Revolutionize how you use your devices. Take your productivity and entertainment to the next level with our 360° Rotatable Aluminum Tablet Stand... |

---

## Notes
- Ensure you have an active internet connection when running the script.
- The Sellvia website structure might change over time, which may break the scraper. If this happens, update the selectors used in the script (`class` or `name` attributes).

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

---

Let me know if you'd like help generating the `requirements.txt` file or adding more sections.