This python script scrapes the distance and duration from origin => destination from an online map service.

## Project Requirements:
* Has to be free and lightweight => therefore non-usage of external API is preferred; Only duration and distance is needed 
* Used only twice a year

* Output to csv?

## Technical tool considerations
* Tried to use the requests_html library, but had difficulty rendering the js of our particular Third Party map service so resorted to Selenium.
* Python is one of the best and easiest web scraping languages. Besides that, it has a simple syntax and is fast to develop, suitable for our non-complex mini project

## Future Improvements
Optimize time spent waiting for each render after click  