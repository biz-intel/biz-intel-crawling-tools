class isee:
    def __init__(self, query, action, connection, driver, By, bs4, randint, requests, time, exception, callback):
        self.query = query
        self.connection = connection
        self.links=[]
        self.site = 'isee'
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
                self.driver.get('https://isee.mn/archive?q=' + self.query + '&page='+str(self.page))
                wait(duration=30)
                self.page+=1
                div = self.driver.find_element(self.select_by.CLASS_NAME, 'main_side')
                a_tags = div.find_elements(self.select_by.TAG_NAME, 'a')
                for a_tag in a_tags:
                    href = a_tag.get_attribute('href')
                    try:
                        if href not in self.links and 'archive' not in href:
                            self.links.append(href)
                    except:
                        pass
                self.time.sleep(self.random(3, 15))
            except self.exception:
                break
        
        print("->       Амжилттай авлаа.......................")
        print("->       Мэдээнүүдийг татаж байна..............")
        for link in self.links:
            try:
                response = self.requests.get(link)
                bs = self.bs4(response.text, "html.parser")
                title = (bs.find('h1', class_='title')).text.strip()
                image_div = bs.find('figure', class_='image')
                img = (image_div.find('img')).get('src')
                body = (bs.find('div', class_='content-div')).text.strip().replace('\n', ' ')
                news_created = bs.find('span', class_='meta-date').text.strip()
                news_created = self.callback(news_created)

                self.connection.insert_data(title=title, img=img, body=body, site=self.site, link=link, key_word=self.query, news_created=news_created)
            except AttributeError as err:
                self.connection.insert_error_logs(site = self.site, key_word = self.query, error = str(err))
                continue
            self.time.sleep(self.random(1, 3))
        self.connection.insert_count_logs(site=self.site, key_word=self.query)
        print("->       Ажмилттай дууслаа!      .......", self.connection.get_inserted(), "тооны мэдээ цуглалаа...!")