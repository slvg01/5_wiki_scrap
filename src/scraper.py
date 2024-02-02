    import requests
    from bs4 import BeautifulSoup
    import json
    from concurrent.futures import ThreadPoolExecutor 


    class WikiScraper:

        """allow to create an instance of a scraper that will :
        -  fetch world leaders information from an API, and notably their wikipedia URL
        -  scrap this url to retrieve the 1st paragraph of their biography
        -  load those information into a json file
        """

        def __init__(
            self,
            root_url: str,
            country_endpoint: str,
            leaders_endpoint: str,
            cookies_endpoint: str,
        ):
            self.root_url = root_url
            self.session = requests.Session()
            self.cookies_endpoint = cookies_endpoint
            self.cookie = self.get_cookie()
            self.country_endpoint = country_endpoint
            self.leaders_endpoint = leaders_endpoint
            self.country4prez_list = []
            self.name_list = []
            self.wiki_url_list = []
            self.first_paragraph_list = []
            self.run_scraping = self.run_scraping
            self.soup_list =[]

        def get_cookie(self):
            # allow to fetch a cookie to get access to the website & keep it active with session use
            try:
                cookie_req = self.session.get(f"{self.root_url}{self.cookies_endpoint}")
                cookie = cookie_req.cookies
                return cookie
            except Exception:
                print(f"get_cookie API issue,  code : {cookie_req.status_code}")
                return None

        def get_country_list(self):
            # allow to fetch the available countries list through the api
            try:
                country_req = self.session.get(
                    f"{self.root_url}{self.country_endpoint}", cookies=self.cookie
                )
                country_list = country_req.json()
            except Exception:
                print(f"api get_country_list issue,  code : {country_req.status_code}")
                return None
            return country_list

        def get_leaders_data(self):
            # allow to fetch all leaders info and gather them in a list of tuple
            leaders_main_data_list = []
            for country in self.get_country_list():  # looping through all countries
                params = {"country": f"{country}"}
                try:
                    leaders_req = self.session.get(  # fetching all leaders info
                        f"{self.root_url}{self.leaders_endpoint}",
                        cookies=self.cookie,
                        params=params,
                    )
                    leaders_data = leaders_req.json()
                    leaders_main_data_list.extend(  # store them in list of tuple
                        [
                            (
                                country,
                                item["first_name"] + " " + item["last_name"],
                                item["wikipedia_url"],
                            )
                            for item in leaders_data
                        ]
                    )
                except Exception:
                    print(f"api get_leaders_data issue, code : {leaders_req.status_code}")
            return leaders_main_data_list

#with ThreadPoolExecutor() as pool:
# toute_page_wiki = list(pool.map(self.session.get, list(tuple[2])))
#... process the list of the soup objects... (find tags...) 

   for tuple in self.get_leaders_data():  # loop through the leaders_main_data_list
            try:
                url_req = self.session.get(tuple[2])  # to scrap all the wikipedia pages
                content = url_req.text
                soup = BeautifulSoup(content, "html.parser")

        def run_scraping(self, url):
            url_req = self.session.get(url)
            content = url_req.text
            soup = BeautifulSoup(content, "html.parser")
            self.soup_list = self.soup_list.append(soup)
            return self.soup_list
    
with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(self.run_scraping, tuple[2]) for tuple in self.get_leaders_data()]
    



    def get_leaders_paragraph(self):
        # get 4 lists of country, name, wikipedia url and wikipedia page 1st paragraph for all leaders
        self.country4prez_list = []
        self.name_list = []
        self.wiki_url_list = []
        self.first_paragraph_list = []
        counter = 0

        for soup in soup_list:

                for tag in soup.find_all(
                    "p"
                ):  # subloop through all of the § to find the first one
                    if "<b>" in str(
                        tag
                    ):  # id of the first paragraph through the bold tag
                        first_paragraph = tag
                        counter += 1
                        self.country4prez_list.append(
                            tuple[0]
                        )  # create the country by president list
                        self.name_list.append(
                            tuple[1]
                        )  # create the name by president list
                        self.wiki_url_list.append(
                            tuple[2]
                        )  # create the wikipedia url by president list
                        self.first_paragraph_list.append(
                            first_paragraph.get_text()
                        )  # create the 1st paragraph by president list
                        print(counter)
                        print(f"Ladies and Gentlmen, Welcome to President \033[1m\033[4m{tuple[1]}\033[0m\033[0m")
                        print(f"Country : {tuple[0].upper()}")
                        print(f"Bio extract : (Full bio on wiki_url : {tuple[2]})")
                        print(first_paragraph.get_text())
                        break
            except Exception as e:
                print(f"Unexpected error in fetching URL for {tuple}: {str(e)}")
        return (
            self.country4prez_list,
            self.name_list,
            self.wiki_url_list,
            self.first_paragraph_list,
        )

    def go_to_json(self):
        # store the 4 abobe list in a json file
        data_to_store = {}
        for country, name, wiki_url, first_paragraph in zip(
            self.country4prez_list,
            self.name_list,
            self.wiki_url_list,
            self.first_paragraph_list,
        ):
            if country not in data_to_store:
                data_to_store[country] = []
            president_info = {
                "name": name,
                "wiki_url": wiki_url,
                "first_paragraph": first_paragraph,
            }
            data_to_store[country].append(president_info)

        with open("leader_data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_to_store, json_file, ensure_ascii=False, indent=2)
