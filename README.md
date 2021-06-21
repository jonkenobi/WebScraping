This python script scrapes the distance and duration for a map route, given origin and destination. 

## How to use
Create an Excel sheet with the same columns as defined in input.xlsx.
Replace C1-E1 with the 3 addresses you want to lookup.
Then just run the BCM_scrape.
The output will be created in output.xlsx

## Project Requirements:
* Has to be free and lightweight => therefore non-usage of external API is preferred; Only duration and distance is needed 
* Used only twice a year => No performance requirements

I/O use excel sheets
inputs: zipcode 
outputs: the walking distance to each destination, in kilometers

## Preqrequisites to Install
Python
Python packages: selenium, openpyxl
Chromedriver 

## Technical tool considerations
*Python is one of the best and easiest web scraping languages. Besides that, it has a simple syntax and is fast to develop, suitable for our non-complex mini project 
*Tried to use the requests_html library, but had difficulty rendering the js of our particular Third Party map service so resorted to Selenium. 

## Future Improvements
