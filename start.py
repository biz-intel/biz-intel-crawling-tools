from threading import Thread
from biz_intel_news_site_search_automation.assets.configures    import news_configs
from bzi_facebook_crawl.assets.configures                       import facebook_configs
from bzi_instagram_crawl.assets.configures                      import instagram_configs
from bzi_linkedin_crawl.assets.configures                       import linkedin_configs
from bzi_twitter_crawl.assets.configures                        import twitter_configs

class start_crawl:

    def run_crawl(self, configure):
        configure.run()

    def __init__(self):
        self.configures = [news_configs(), facebook_configs(), instagram_configs(), linkedin_configs(), twitter_configs()]
        for configure in self.configures:
            configure_thread = Thread(target=self.run_crawl, args=[configure])
            configure_thread.start()

start_crawl()