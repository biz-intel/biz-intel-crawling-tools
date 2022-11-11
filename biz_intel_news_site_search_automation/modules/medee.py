class medee:
    def __init__(self, query, action, connection, driver, By, bs4, randint, requests, time, exception, callback):
        self.query = query
        self.connection = connection
        self.links=[]
        self.site = 'medee'
        self.connection.reset_count()
        self.driver = driver
        self.action = action
        self.select_by=By
        self.bs4 = bs4
        self.random = randint
        self.requests = requests
        self.time = time
        self.exception = exception
        self.callback = callback
    
    def start_download(self):
        def wait(duration = 30):
            self.driver.implicitly_wait(duration)
        self.page = 1
        print("->       Сайт:", self.site)
        print("->       Холбоосуудын авч байна................")
        while self.page < 41:
            try:
                self.driver.get('https://medee.mn/search/'+self.query+'?page=' + str(self.page))
                wait()
                self.page+=1
                div = self.driver.find_element(self.select_by.ID, 'posts')
                a_tags = div.find_elements(self.select_by.TAG_NAME, 'a')
                for a_tag in a_tags:
                    href = a_tag.get_attribute('href')
                    if href not in self.links and 'search' not in href:
                        self.links.append(href)
                self.time.sleep(self.random(3, 15))
            except self.exception:
                break
        
        print("->       Амжилттай авлаа.......................")
        print("->       Мэдээнүүдийг татаж байна..............")
        for link in self.links:
            response = self.requests.get(link)
            bs = self.bs4(response.text, "html.parser")
            try:
                title = (bs.find('h1', attrs={'class':'single-font'})).text.strip()
                image_div = bs.find('div', attrs={'id':'single-cover'})
                img ='https://medee.mn'+ (image_div.find('img')).get('src')
                body = (bs.find('div', attrs={'class':'wordwrap'})).text.strip()
                article  = bs.find('article', class_="panel")
                news_created = article.find('time').text.strip()
                news_created = self.callback(news_created)

                self.connection.insert_data(title=title, img=img, body=body, site=self.site, link=link, key_word=self.query, news_created=news_created)
                self.time.sleep(self.random(1, 3))
            except AttributeError as err:
                self.connection.insert_error_logs(site = self.site, key_word = self.query, error = str(err))
                continue
        self.connection.insert_count_logs(site=self.site, key_word=self.query)
        print("->       Ажмилттай дууслаа!      .......", self.connection.get_inserted(), "тооны мэдээ цуглалаа...!")