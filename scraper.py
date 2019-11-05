from core.selenium_scraper import SeleniumScraper
from core.soup_scraper import SoupScraper

reddit_home = 'https://www.reddit.com'
slash = '/r/'
subreddit = 'MachineLearning'

SelScraper = SeleniumScraper()
BSoupScraper = SoupScraper()

SelScraper.setup_chrome_browser("/Users/casperbogeskovhansen/Downloads/chromedriver")

# Selects all the a elements that have a "data-click-id" attribute with a value of "body"
# https://stackoverflow.com/questions/36019544/if-double-slash-is-used-2-times-in-xpath-what-does-it-mean
xpath = "//a[@data-click-id='body']"
scroll_n_times = 5

links = SelScraper.collect_links(page = reddit_home + slash + subreddit,
                         scroll_n_times = scroll_n_times,
                         xpath = xpath)

script_data = BSoupScraper.get_scripts_from_urls(links)

data = SelScraper.reddit_data_to_dict(script_data, subreddit)

# Upvote ratio
#json.loads(json_str)['posts']['models']['t3_dkox1s']['upvoteRatio']

# All comment ids
# commentsPage -> keyToChatCommentLinks -> commentsPage--[post:'t3_dkox1s'] -> id