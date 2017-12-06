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
    def __init__():
        super(ThrottledApiException, self).__init__("Request throttled")


class JsonApi:
    """
    Json api class
    """

    def __init__(self, redis, base, available_resources=None):
        assert base is not None
        self.available_resources = available_resources or []
        self.redis = redis
        self.base = base

    def get(self, resource):
        """
        get request to a resource
        """
        assert resource in self.available_resources

        url = '{}/{}'.format(self.base, resource)
        response = requests.get(url)
        if not response.ok:
            raise ApiException("Got {} from {}".format(response.status, url))
        try:
            return json.load(response.text)
        except json.JSONDecodeError:
            raise ApiException("Not json response form {}".format(url))


class ThrottledJsonApi(JsonApi):
    """
    Throttle the request rate based on redis
    """
    REDIS_BASE_KEY = "throttles"

    def __init__(self, redis, requests_per_minute, identifier, *args, **kwargs):
        self.redis = redis
        self.requests_per_minute = requests_per_minute
        self.identifier = identifier
        super(ThrottledJsonApi, self).__init__(*args, **kwargs)

    def should_allow(self):
        """
        check redis for last request
        """
        last_request_ts = self.redis.shmget(self.REDIS_BASE_KEY, self.identifier)
        return time.time() - last_request_ts > 60 / self.requests_per_minute

    def get(self, resource):
        """
        override to respect throttle
        """
        if not self.should_allow():
            raise ThrottledApiException
        self.redis.shmset(self.REDIS_BASE_KEY, self.identifier)