from biz_intel_news_site_search_automation.assets.configures    import news_configs
from bzi_facebook_crawl.assets.configures                       import facebook_configs
from bzi_instagram_crawl.assets.configures                      import instagram_configs
from bzi_linkedin_crawl.assets.configures                       import linkedin_configs
from bzi_twitter_crawl.assets.configures                        import twitter_configs
from mongolian_nlp.assets.configures                            import nlp_configs


news_configs().run()
facebook_configs().run()
instagram_configs().run()
linkedin_configs().run()
twitter_configs().run()
nlp_configs().run()