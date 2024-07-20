# Map route duration scraper
This python script scrapes the time duration it takes for a map route, given the origin and destination.
It can output those values into an Excel file

## How to use
1. Create an Excel sheet similar to input.xlsx. Write Origins from B1 rightwards, destinations from A2 downwards
2. Run distance_scrape_with_excel.py
3. The output will be created in output.xlsx

For modifying and testing, use `distance_scrape_with_excel.ipynb`. 
`distance_scrape_with_excel.py` is an excerpt of the code from `distance_scrape_with_excel.ipynb`
for convenience of use if you just want to run the script without starting Jupyter Notebook

## Requirements

- Python
- Python packages: selenium, openpyxl  (Download with pip or conda)
- Chromedriver (Put chromedriver.exe in the rootdirectory) 

## Technical tool considerations
* Python is one of the best and easiest web scraping languages. Besides that, it has a simple syntax and is fast to develop, suitable for this non-complex mini project 
* Tried to use the requests_html library, but had difficulty rendering the js of our particular Third Party map service so resorted to Selenium. 

## Future Improvements

## Notes 
Currently distance_scrape_with_excel.py is manually created using the ipynb file.