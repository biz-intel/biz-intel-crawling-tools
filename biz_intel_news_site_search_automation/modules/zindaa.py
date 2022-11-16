class zindaa:
    def __init__(self, query, connection, driver, By, bs4, randint, requests, time, exception, action, callback):
        self.query = query
        self.connection = connection
        self.links=[]
        self.site = 'zindaa'
        self.connection.reset_count()
        self.driver = driver
        self.select_by = By
        self.bs4 = bs4
        self.random = randint
        self.requests = requests
        self.time = time
        self.exception = exception
        self.action = action
        self.callback = callback
        
    def start_download(self):
        def wait(duration = 30):
            self.driver.implicitly_wait(duration)
        self.page = 1
        wait()
        print("->       Сайт:", self.site)
        print("->       Холбоосуудын авч байна................")
        while self.page < 41:
            try:
                self.driver.get('https://news.zindaa.mn/news/search?q='+self.query+'&q='+self.query+'&offset='+str(self.page))
                wait()
                self.page+=1
                div = self.driver.find_element(self.select_by.CLASS_NAME, 'news-list-groups')
                a_tags = div.find_elements(self.select_by.TAG_NAME, 'a')
                for a_tag in a_tags:
                    href = a_tag.get_attribute('href')
                    if href != None:
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
                parent_div = bs.find('div', class_='news-more-area')
                title = (parent_div.find('h1')).text.strip()
                img = (parent_div.find('img')).get('src')
                body = (parent_div.find('div', class_='desc')).text.strip().replace('\n', ' ')
                date_parent_div = parent_div.find('div', class_='pull-left')
                news_created = date_parent_div.find_all('span')[1].text.strip()
                news_created = self.callback(news_created)

                self.connection.insert_data(title=title, img=img, body=body, site=self.site, link=link, key_word=self.query, news_created=news_created)
                self.time.sleep(self.random(1, 3))
            except AttributeError as err:
                self.connection.insert_error_logs(site = self.site, key_word = self.query, error = str(err))
                continue
        self.connection.insert_count_logs(site=self.site, key_word=self.query)
        print("->       Ажмилттай дууслаа!      .......", self.connection.get_inserted(), "тооны мэдээ цуглалаа...!")