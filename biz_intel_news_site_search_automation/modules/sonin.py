class sonin:
    def __init__(self, query, connection, driver, By, bs4, randint, requests, time, exception, action, callback):
        self.query = query
        self.connection = connection
        self.all_links = []
        self.site = 'sonin'
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
        
    def get_links(self):
        links = []
        div = self.driver.find_element(self.select_by.CLASS_NAME, 'gsc-expansionArea')
        a_tags = div.find_elements(self.select_by.TAG_NAME, 'a')
        for a_tag in a_tags:
            link = a_tag.get_attribute('href')
            if 'sonin' in link and link not in links and '#' not in link:
                links.append(link)
        self.all_links.append(links)
    def start_download(self):
        def wait(duration = 30):
            self.driver.implicitly_wait(duration)
        self.driver.get('https://www.sonin.mn/search?q=' +self.query)
        wait(20)
        print("->       Сайт:", self.site)
        print("->       Холбоосуудын авч байна................")
        self.get_links()
        for i in range(1, 11):
            try:
                paginator = self.driver.find_elements(self.select_by.CLASS_NAME, 'gsc-cursor-page')
                paginator[i].click()
                self.time.sleep(self.random(4, 9))
                self.get_links()
                self.time.sleep(self.random(5, 15))
            except self.exception as err:
                pass
            except IndexError as err:
                pass
        
        print("->       Амжилттай авлаа.......................")
        print("->       Мэдээнүүдийг татаж байна..............")
        for links in self.all_links:
            for link in links:
                response = self.requests.get(link)
                bs = self.bs4(response.text, "html.parser")
                try:
                    title = bs.find('h3', class_='title').text.strip()
                    img = bs.find('img', class_='img-responsive').text.strip()
                    body = bs.find('div', class_='sonin-nctext').text.strip().replace('\n', ' ')
                    news_created = bs.find('span', class_='dateago red').text
                    news_created = self.callback(news_created)

                    data = {}
                    data['Гарчиг'] = title, 
                    data['Зураг'] = img
                    data['Мэдээ'] = body
                    data['Холбоос'] = link
                    data['Нийтлэгдсэн огноо'] = news_created
                    self.connection.build_data(data)
                    self.connection.print_data()
                    break
                    self.time.sleep(self.random(1, 3))
                except AttributeError as err:
                    continue
            break
        self.connection.insert_data(collection_name = self.query, key_word = "sonin")
        print("->       Ажмилттай дууслаа!      .......", self.connection.get_inserted(), "тооны мэдээ цуглалаа...!")