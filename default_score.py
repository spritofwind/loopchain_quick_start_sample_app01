import logging
from loopchain.blockchain import ScoreBase


class UserScore(ScoreBase):
    """ Basic User SCORE file.

    Keep 'UserScore' name.
    """
    def invoke(self, transaction, block):
        """ Use trasactiion data and manipulate blockchain.

        @param trasaction loopchain.blockchain.Transaction class.
        @param block  loopchain.blockchain.Block class.
        @return return Score result.
        """

        pass

    def query(self, params):
        """
        @params 
        @return
        """

        return params

    def info(self):

        return None
