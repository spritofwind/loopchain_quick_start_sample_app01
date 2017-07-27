import logging
from loopchain.blockchain import ScoreBase


class UserScore(ScoreBase):
    """ Basic User SCORE code.
    Keep 'UserScore' name.
    """
    def invoke(self, transaction, block):
        """ Use trasactiion data and manipulate blockchain.

        @param trasaction loopchain.blockchain.Transaction class.
        @param block  loopchain.blockchain.Block class.
        @return Score result. It's dictionary with 'code' and 'message' like below.
            {
              'code' : integer value.
                * Success is 0.
                * Not found is 2.
                * Exception is 9000.
              'message' : 'error_message when code not success'
            }
        """

        pass

    def query(self, params):
        """ Return the result by invoke().

        @param params in dictionary from query request.
        @return Score result. Convert Dictionary type as JSON string.
        """


        return params

    def info(self):
        """ Return the result by invoke().

        @param params in dictionary from query request.
        @return Score result. Convert Dictionary type as JSON string.
        """

        return None
