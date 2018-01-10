"""
Generic api classes
"""
import json
import time
import requests


class ApiException(Exception):
    """
    Exceptions thrown by this module
    """
    pass


class ThrottledApiException(Exception):
    """
    Exception for Throttled
    """
    def __init__(self):
        super().__init__("Request throttled")


class JsonApi:
    """
    Json api class
    """

    def __init__(self, base, available_resources):
        assert isinstance(available_resources, list), "available resources should be a list"
        self.available_resources = available_resources or []
        self.base = base if base.endswith("/") else base + "/"

    def get(self, resource, data=None):
        """
        get request to a resource
        """
        assert resource in self.available_resources

        url = '{}{}'.format(self.base, resource)
        response = requests.get(url, data)
        if not response.ok:
            raise ApiException("Got {} from {}".format(response.status, url))
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            raise ApiException("Not json response form {}".format(url))


class ThrottledJsonApi(JsonApi):
    """
    Throttle the request rate based on redis
    """
    REDIS_BASE_KEY = "throttles"

    def __init__(self, redis, requests_per_minute, identifier, *args, **kwargs):
        assert requests_per_minute > 0, "requests per minute cannot be <=0"
        self.redis = redis
        self.requests_per_minute = requests_per_minute
        self.identifier = identifier
        super(ThrottledJsonApi, self).__init__(*args, **kwargs)

    def should_allow(self):
        """
        check redis for last request
        """
        last_request_ts = self.redis.hmget(self.REDIS_BASE_KEY, self.identifier)[0]
        if not last_request_ts:
            return True
        return time.time() - float(last_request_ts) > 60 / self.requests_per_minute

    def get(self, resource, data=None):
        """
        override to respect throttle
        """
        if not self.should_allow():
            raise ThrottledApiException
        self.redis.hmset(self.REDIS_BASE_KEY, {
            self.identifier: time.time()
        })
        response = super().get(resource, data)
        return response


class Producer:
    """
    produces messages to kafka
    """
    def __init__(self, kafka_producer, api):
        self.kafka_producer = kafka_producer
        self.api = api
        assert isinstance(api, JsonApi)

    def produce(self):
        """
        parsing here override
        """
        raise NotImplementedError
