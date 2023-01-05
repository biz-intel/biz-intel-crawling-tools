class ikon:
    def __init__(self, query, connection, driver, By, bs4, randint, requests, time, exception, action, callback):
        self.query = query
        self.connection = connection
        self.all_links = []
        self.site = 'ikon'
        self.connection.reset_count()
        self.driver = driver
        self.select_by=By
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
            if ('ikon.mn/n' in link or 'opinion' in link) and link not in links:
                links.append(link)
        self.all_links.append(links)

    def start_download(self):
        def wait(duration = 30):
            self.driver.implicitly_wait(duration)
        self.driver.get('https://ikon.mn/search?q=' +self.query)
        wait()
        print("->       Сайт:", self.site)
        print("->       Холбоосуудын авч байна................")
        self.get_links()
        for i in range(1, 11):
            try:
                paginator = self.driver.find_elements(self.select_by.CLASS_NAME, 'gsc-cursor-page')
                self.time.sleep(self.random(4, 9))
                self.get_links()
                paginator[i].click()
                self.time.sleep(self.random(5, 15))
            except self.exception as err:
                pass
            except IndexError as err:
                pass

        
        print("->       Амжилттай авлаа.......................")
        print("->       Мэдээнүүдийг татаж байна..............")
        
        for links in self.all_links:
            for link in links:
                try:
                    req = self.requests.get(link)
                    bs = self.bs4(req.text, "html.parser") 
                    news_div = bs.find('div', class_='inews')
                    title = (news_div.find('h1')).text.strip()
                    body_div = news_div.find('div', class_='icontent')
                    img = (body_div.find('img')).get('src')
                    body = ''
                    p_tags = body_div.find_all('p')
                    for p in p_tags:
                        body+=p.text.strip()
                    body = body.replace('\n', ' ')
                    news_created = bs.find('div', class_='time').text.strip().replace(' ', '').replace('оны', '-').replace('сарын', '-')
                    news_created = self.callback(news_created)
                    data = {}
                    data['Гарчиг'] = title, 
                    data['Зураг'] = img
                    data['Мэдээ'] = body
                    data['Холбоос'] = link
                    data['Нийтлэгдсэн огноо'] = news_created
                    self.connection.build_data(data)
                    self.connection.print_data()
                    self.time.sleep(self.random(1,3))
                    
                except AttributeError as err:
                    continue
        self.connection.insert_data(collection_name = self.query, key_word = "ikon")
        print("->       Ажмилттай дууслаа!      .......", self.connection.get_inserted(), "тооны мэдээ цуглалаа...!")