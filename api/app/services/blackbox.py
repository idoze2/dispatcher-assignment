import re
from time import sleep


class BlackBox:
    @staticmethod
    def process(url: str) -> None:
        if '.' not in url:
            raise Exception("BadDomainException")
        sleep(20)
        return True
