import os
os.environ['PATH'] = r"".join('assets/')

from threading import Thread
from bzi_facebook_crawl.assets.configures                       import facebook_configs
# from bzi_instagram_crawl.assets.configures                      import instagram_configs
# from bzi_linkedin_crawl.assets.configures                       import linkedin_configs
from bzi_twitter_crawl.assets.configures                        import twitter_configs
# from biz_intel_news_site_search_automation.assets.configures    import news_configs

class start_crawl:

    def run_crawl(self, configure):
        configure.run()

    def __init__(self):
        self.configures = { 
                            # 'news'      :   news_configs(),      
                            'facebook'  :   facebook_configs(),
                            # 'instagram' :   instagram_configs(),
                            # 'linkedin'  :   linkedin_configs(),
                            'twitter'   :   twitter_configs(),
                        }

    def start(self):
        for configure in self.configures.values():
            configure_thread = Thread(target=self.run_crawl, args=[configure])
            configure_thread.start()

    def run_news(self):
        self.configures['news'].run()

    def run_facebook(self):
        self.configures['facebook'].run()

    def run_instagram(self):
        self.configures['instagram'].run()

    def run_linkedin(self):
        self.configures['linkedin'].run()

    def run_twitter(self):
        self.configures['twitter'].run()
        
crawler = start_crawl()

crawler.start()