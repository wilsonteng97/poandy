from enum import Enum, auto
import requests

from poandy.util.objectless import Objectless

class RequestType(Enum):
    GET = auto()

class RequestSender(Objectless):
    @staticmethod
    def send(endpoint, headers, method, params=[]):
        if method == RequestType.GET:
            return requests.get(endpoint, headers=headers, params=params)