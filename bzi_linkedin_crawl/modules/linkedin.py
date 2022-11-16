class linkedin:
    def __init__(self, query, action, connection, driver, By, bs4, randint, requests, time, exception, callback):
        self.query = query
        self.connection = connection
        self.links = []
        self.connection.reset_count()
        self.action = action
        self.driver = driver
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
        self.driver.get('https://gogo.mn/search?q=' + self.query)
        wait(duration = 30)
        isLast = False
        print("->       Сайт:", self.site)
        print("->       Холбоосуудын авч байна................")
        while not isLast:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait(duration = 30)
            divs = self.driver.find_elements(self.select_by.CLASS_NAME, 'article-list')
            for a in divs[1].find_elements(self.select_by.TAG_NAME, 'a'):
                if '#' in a.get_attribute('href'):
                    self.action.move_to_element(a).click().perform()
                    isLast = False
                    continue
                isLast = True
        try:
            div = self.driver.find_elements(self.select_by.CLASS_NAME, 'article-list')
            a_tags = div[1].find_elements(self.select_by.TAG_NAME, 'a')
        
            for a_tag in a_tags:
                self.links.append(a_tag.get_attribute('href'))
        except IndexError as err:
            pass
        print("->       Амжилттай авлаа.......................")
        print("->       Мэдээнүүдийг татаж байна..............")
        for link in self.links:
            response = self.requests.get(link)
            bs = self.bs4(response.text, "html.parser")
            try:
                print(link)
                title_div = bs.find_all('h2', class_ = "news-detail-title")
                title = (title_div[0].get_text()).strip()
                image_a = bs.find('a', class_='gogo-zoom')
                a = self.bs4(str(image_a), "html.parser")
                img = (a.find('img')).get('src')
                body = (bs.find('div', class_='news-cont-container')).text.strip()
                date_div = bs.find('div', class_='content-detail-author-container')
                news_created = date_div.find('span').text.strip()
                news_created = self.callback(news_created)

                self.connection.insert_data(title = title, img = img, body = body, site = self.site, link = link, key_word = self.query, news_created = news_created)
            except AttributeError as err:
                self.connection.insert_error_logs(site = self.site, key_word = self.query, error = str(err))
                continue
            except IndexError as err:
                self.connection.insert_error_logs(site = self.site, key_word = self.query, error = str(err))
                continue
            self.time.sleep(self.random(1, 3))
        self.connection.insert_count_logs(site = self.site, key_word = self.query)
        print("->       Ажмилттай дууслаа!      .......", self.connection.get_inserted(), "тооны мэдээ цуглалаа...!")