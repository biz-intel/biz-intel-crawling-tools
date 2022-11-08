class updown:
    def __init__(self, query, action, connection, driver, By, bs4, randint, requests, time, exception):
        self.query = query
        self.connection = connection
        self.links=[]
        self.site = 'updown'
        self.connection.reset_count()
        self.driver = driver
        self.action = action
        self.select_by = By
        self.bs4 = bs4
        self.random = randint
        self.requests = requests
        self.time = time
        self.exception = exception
        
    def start_download(self):
        def wait(duration = 30):
            self.driver.implicitly_wait(duration)
        self.page = 1
        print("->       Сайт:", self.site)
        print("->       Холбоосуудын авч байна................")
        while self.page < 41:
            try:
                self.driver.get('https://updown.mn/page/'+str(self.page)+'?s=' + self.query)
                wait()
                self.page+=1
                div = self.driver.find_element(self.select_by.CLASS_NAME, 'btContent')
                a_tags = div.find_elements(self.select_by.TAG_NAME, 'a')
                for a_tag in a_tags:
                    href = a_tag.get_attribute('href')
                    if href not in self.links and 'author' not in href and 'page' not in href and 'category' not in href and '#' not in href:
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
                title = (bs.find('span', class_='headline')).text
                image_div = bs.find('div', class_='btRegularMediaPosition')
                img =( image_div.find('img')).get('src')
                body = (bs.find('div', class_='bt_bb_wrapper')).text
                self.connection.insert_data(title=title, img=img, body=body, site=self.site, link=link, key_word=self.query)
                self.time.sleep(self.random(1, 3))
            except AttributeError as err:
                self.connection.insert_error_logs(site = self.site, key_word = self.query, error = str(err))
                continue
        self.connection.insert_count_logs(site=self.site, key_word=self.query)
        print("->       Ажмилттай дууслаа!      .......", self.connection.get_inserted(), "тооны мэдээ цуглалаа...!")