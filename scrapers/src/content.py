import hashlib
import requests
import time
from lxml import html


class HtmlContent:
    def __init__(self, url):
        self.url = url
        self.tree = None

    def get_tree(self):
        if self.tree is not None:
            return self.tree
        page = requests.get(self.url)
        self.tree = html.fromstring(page.content)
        return self.tree

    def parse_xpath(self, xpath):
        return self.get_tree().xpath(xpath)


class MainPage(HtmlContent):

    def __init__(self, base_url, article_class, source):
        self.article_class = article_class
        self.source = source
        super(MainPage, self).__init__(base_url)

    def get_article_urls(self):
        raise NotImplementedError()

    def get_article_titles(self):
        raise NotImplementedError()

    def get_articles(self):
        main_articles_urls = self.get_article_urls()
        main_article_titles = self.get_article_titles()
        
        return [
            self.article_class(url=url, title=title, source=self.source)
            for url, title in zip(main_articles_urls, main_article_titles)
        ]


class Article(HtmlContent):
    article_id = None

    def __init__(self, url, title, source):
        self.set_title(title)
        self.title = title
        self.source = source
        super(Article, self).__init__(url)

    def set_title(self, title):
        if not title:
            return None
        self.title = title
        self.article_id = self.id_from_title(title)

    def content(self):
        raise NotImplementedError()

    def topic(self):
        return "press"

    def serialize(self):
        return {
            'article_id': self.article_id,
            'title': self.title,
            'timestamp': time.time(),
            'source': self.source
        }

    @staticmethod
    def id_from_title(title):
        return hashlib.sha224(
            title.lower().replace(" ", "").encode('utf-8')
        ).hexdigest()

