import json
from .content import MainPage


class Scraper:
    def __init__(self, main_page, redis, kafka_producer):
        assert isinstance(main_page, MainPage)
        self.main_page = main_page
        self.redis = redis
        self.kafka_producer = kafka_producer

    def run(self):
        articles = self.main_page.get_articles()
        print("source {}: Found {} articles".format(self.main_page.source, len(articles)))
        skipped = 0
        for article in articles:
            # if self.redis.get(article.article_id):
            #     skipped += 1
            #     continue
            self.kafka_producer.send(
                topic=article.topic(),
                value=json.dumps(article.serialize())
            )
            self.redis.set(article.article_id, True)
        self.kafka_producer.flush()
        print("source {}: {} articles were old".format(self.main_page.source, skipped))
