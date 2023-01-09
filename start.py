import os
os.environ['PATH'] = r"".join('./assets/')
from configures                       import linkedin_configs

class start_crawl:

    def __init__(self):
        self.configures = {
                            'linkedin'  :   linkedin_configs()
                        }

    def start(self):
        self.configures['linkedin'].run()
        
crawler = start_crawl()

crawler.start()