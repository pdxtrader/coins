"""
Shared parsing classes
"""
import json
from .content import MainPage


class Scraper:
    """
    Generic parser
    """
    def __init__(self, main_page, redis, kafka_producer):
        assert isinstance(main_page, MainPage)
        self.main_page = main_page
        self.redis = redis
        self.kafka_producer = kafka_producer

    def run(self):
        """
        Runs the job
        """
        articles = self.main_page.get_articles()
        print("source {}: Found {} articles".format(self.main_page.source, len(articles)))
        skipped = 0
        for article in articles:
            if self.redis.hmget("articles", article.article_id)[0]:
                skipped += 1
                continue
            self.kafka_producer.send(
                topic="press",
                value=json.dumps(article.serialize())
            )
            print(article.serialize())
            self.redis.hmset("articles", {article.article_id: 1})
        print("source {}: {} articles were old".format(self.main_page.source, skipped))
        self.kafka_producer.flush()
