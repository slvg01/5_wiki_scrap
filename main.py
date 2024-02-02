from src.scraper import WikiScraper


if __name__ == "__main__":
    # to create the WikiScraper instance with API related parameters
    a = WikiScraper(
        "https://country-leaders.onrender.com", "/countries/", "/leaders/", "/cookie/"
    )

    # to get the cookie necessary to get into the website
    a.get_cookie()

    # to get the list of country from API
    a.get_country_list()

    # to get  all the main leaders data (country, name, wikipedia url)
    a.get_leaders_data()

    # get the leader basic bio (the 1st paragraph of wikipedia)
    a.get_leaders_paragraph()

    # save to json all those leaders info
    a.go_to_json()
