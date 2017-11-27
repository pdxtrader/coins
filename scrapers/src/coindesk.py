from .content import Article, MainPage


class CoinDeskMainPage(MainPage):
    def __init__(self):
        super(CoinDeskMainPage, self).__init__(
            'https://www.coindesk.com', CoinDeskArticle, 'coindesk'
        )

    def get_article_urls(self):
        return self.parse_xpath(
            '//div[@class="article article-featured"]//a/@href'
        )

    def get_article_titles(self):
        return [title.strip() for title in self.parse_xpath(
            '//div[@class="article article-featured"]//a//h3/text()'
        )]


class CoinDeskArticle(Article):
    source = "Coindesk"

    def content(self):
        return ' '.join(
            self.parse_xpath('//div[@class="article-content-container noskimwords"]//p/text()')
        )
