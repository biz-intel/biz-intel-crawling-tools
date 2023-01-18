import os
import requests
import time
# os.environ['PATH'] = r"".join('./assets/')
# from bzi_facebook_crawl.assets.configures                       import facebook_configss
from bzi_linkedin_crawl.assets.configures                       import linkedin_configs
# from bzi_reddit_crawl.assets.configures                         import reddit_configs
# from bzi_quora_crawl.assets.configures                          import quora_configs
from bzi_twitter_crawl.assets.configures                        import twitter_configs
from biz_intel_news_site_search_automation.assets.configures    import news_configs

class start_crawl:

    def __init__(self):
        self.configures = { 
                            # 'news'      :   news_configs(),
                            # 'facebook'  :   facebook_configs(),
                            'linkedin'  :   linkedin_configs(),
                            # 'reddit'    :   reddit_configs(),
                            # 'quora'     :   quora_configs(),
                            'twitter'   :   twitter_configs(),
                        }

    def start(self, key_word):
        for configure in self.configures.values():
            configure.start(key_word)

    def run_news(self):
        self.configures['news'].run()

    def run_facebook(self):
        self.configures['facebook'].run()

    def run_linkedin(self):
        self.configures['linkedin'].run()

    def run_twitter(self):
        self.configures['twitter'].run()

    def run_reddit(self):
        self.configures['reddit'].run()

    def run_quora(self):
        self.configures['quora'].run()
        
crawler = start_crawl()

# crawler.run_news()

# crawler.run_facebook()

# crawler.run_linkedin()

# crawler.run_twitter()

# crawler.run_reddit()

# crawler.run_quora()

# crawler.start()

while True:
    try:
        data = requests.get("https://api.biz-intel.tech/status?status_type=crawl_status")
        key_words = data.json()['key_words']
        for key_word in key_words:
            crawler.start(key_word=key_word)
            print(key_word, ":", "амжилттай татагдлаа...!")
        # data = {"status_type":"crawl_status"}
        # requests.post("https://api.biz-intel.tech/status", data=data)
        break
    except TypeError as err:
        print("Sleeping...! for 30 minutes |========| error :", err)
        time.sleep(1800)