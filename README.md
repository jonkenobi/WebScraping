This python script scrapes the distance and duration for a map route, given origin and destination. 

## How to use
1. Create an Excel sheet with the same columns as defined in input.xlsx.
2. Replace C1-E1 with the 3 addresses you want to lookup.
3. Run distance_scrape_with_excel.py
4. The output will be created in output.xlsx

## Preqrequisites to Install
- Python
- Python packages: selenium, openpyxl  (Download with pip or conda)
- Chromedriver (Have chromedriver.exe) 

## Technical tool considerations
* Python is one of the best and easiest web scraping languages. Besides that, it has a simple syntax and is fast to develop, suitable for our non-complex mini project 
* Tried to use the requests_html library, but had difficulty rendering the js of our particular Third Party map service so resorted to Selenium. 

## Future Improvements

## Notes 
Currently distance_scrape_with_excel.py is manually created using the ipynb file.