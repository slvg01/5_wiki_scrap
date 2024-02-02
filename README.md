# Wikipedia Scraper

## Main Task
The main task of the code is to scrape global leaders' information from Wikipedia by:
- Fetching country, name, Wikipedia page URL from [an API](https://country-leaders.onrender.com/docs).
- Scraping their respective Wikipedia pages to fetch the first paragraph of their biography.
- Including all this information in a JSON file as the final output.

## Installation and Running
- Virtual environment information  in `requirements.txt`  >>>>  (`pip install -r requirements.txt`).
- Run `python main.py`
- Python version: 3.11.5.
- The `src` folder contains the class and functions script.


## additional Features (On the nice_to_have branch) - ON GOING
- A switch to store the output as CSV instead of JSON.
- Speed up the execution using multiprocessing.

