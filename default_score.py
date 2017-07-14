import logging
from loopchain.blockchain import ScoreBase


class UserScore(ScoreBase):
    """ 기본 스코어
        기본 스코어는 아무런 역할을 하지 않는다
    """
    def invoke(self, transaction, block):
        pass

    def query(self, params):
        logging.debug("in UserScore Query...")
        return params

    def info(self):
        # TODO Score info (package.json) 을 로드하여 json object 를 리턴하여야 한다.
        return None
