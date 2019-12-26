from twitter import Twitter, OAuth, TwitterHTTPError
from config.config import Config

""" Module that contains the Connection class """


class Connection(object):
    """ Singleton class that manages the TWitter connection 
    """

    def __init__(self):
        """ Initialises the twiter connection through OAuth
        """
        
        self.connection = Twitter(auth=OAuth(Config.get_oath()))

    def get(self):
        """ Returns the connection 

        Returns: 
            Twitter: The twitter connection

        """

        return self.connection