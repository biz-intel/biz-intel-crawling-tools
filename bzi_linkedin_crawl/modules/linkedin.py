class linkedin:
    def __init__(self, query, connection, driver, By, time, callback, email, pass_word, Key, randint):
        self.query = query
        self.connection = connection
        self.links = []
        self.connection.reset_count()
        self.driver = driver
        self.select_by=By
        self.time = time
        self.callback = callback
        self.email = email
        self.pass_word = pass_word
        self.keys = Key
        self.random = randint
        
    def start_download(self):
        def wait(duration = 30):
            self.driver.implicitly_wait(duration)
        self.driver.get('https://linkedin.com/login')

        wait(duration = 180)
        # form = self.driver.find_element(by=self.select_by.CSS_SELECTOR, value="form.sign-in-form")
        email_form = self.driver.find_element(by=self.select_by.NAME, value="session_key")
        password_form = self.driver.find_element(by=self.select_by.NAME, value="session_password")
        login = self.driver.find_element(by=self.select_by.TAG_NAME, value='button')
        email_form.send_keys(self.email)
        password_form.send_keys(self.pass_word)
        login.click()

        wait(duration = 180)
        self.driver.get('https://linkedin.com')
        wait(duration = 60)

        search = self.driver.find_element(self.select_by.CLASS_NAME, value="search-global-typeahead__input")
        search.click()
        search.send_keys(self.query)
        search.send_keys(self.keys.ENTER)

        wait(duration = 180)

        filter_div = self.driver.find_element(self.select_by.CLASS_NAME, value="search-reusables__filters-bar-grouping")
        posts = filter_div.find_elements(self.select_by.TAG_NAME, value="li")[0]
        posts.click()

        wait(duration = 180)
        try:
            self.driver.find_element(self.select_by.CLASS_NAME, "reusable-search-filters__no-results")
            print("->       Мэдээлэл олдсонгүй...!")
            return
        except:
            pass

        reached_page_end = False
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while not reached_page_end:
            self.driver.find_element(self.select_by.XPATH, value='//body').send_keys(self.keys.END)   
            self.time.sleep(self.random(1, 3))
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if last_height == new_height:
                reached_page_end = True
            else:
                last_height = new_height

        divs = self.driver.find_elements(self.select_by.CLASS_NAME, value="search-results__no-cluster-container")
        for i in range(len(divs)):
            while True:
                try:
                    element = divs[i].find_element(self.select_by.TAG_NAME, "div")
                    try:
                        data = {}
                        """user data"""
                        # user_image_div = element.find_element(self.select_by.CLASS_NAME, "update-components-actor__image")
                        
                        # data["user_image"] = user_image_div.find_element(self.select_by.TAG_NAME, "img").get_attribute("src")
                        data["user_name"] = element.find_element(self.select_by.XPATH, "//span[@dir='ltr']").text.strip()
                        """ post data """
                        data["created_date"] = self.callback(element.find_element(self.select_by.CSS_SELECTOR, "span.update-components-actor__sub-description")\
                                                                        .find_element(self.select_by.TAG_NAME, "span").text.replace("•", "").replace("\n", "").strip())
                        data["body"] = element.find_element(self.select_by.CSS_SELECTOR, "span.break-words").text.replace("\n", " ").replace(" ( )", "")\
                                                                                                                  .replace("  ", " ").replace(" .", ".").strip()
                        try:
                            content_image_div = element.find_element(self.select_by.CLASS_NAME, "update-components-image")
                            data["image"] = content_image_div.find_element(self.select_by.TAG_NAME, "img").get_attribute("src")
                        except:
                            data["image"] = None
                        data["key_word"] = self.query
                        data["site"] = "linkedin"
                        # """Social metrics"""
                        # social_div = element.find_element(self.select_by.CSS_SELECTOR, "div.social-details-social-activity")
                        # lis = social_div.find_elements(self.select_by.TAG_NAME, "li")
                        # data["Хариу үйлдлийн тоо"] = lis[0].text
                        # data["Сэтгэгдэлийн тоо"] = lis[1].text.replace(" comment", "")
                        # data["Хуваалцсан тоо"] = lis[2].text.replace(" reposts", "")
                        self.connection.build_data(data)
                        self.connection.insert_data()
                    except:
                        print("Мэдээлэл олдсонгүй...!", element)
                    self.driver.execute_script("arguments[0].remove();", element)
                except:
                    break
        
        # self.connection.insert_data()
        print("->       Ажмилттай дууслаа!      .......", self.connection.get_inserted(), "тооны мэдээ цуглалаа...!")