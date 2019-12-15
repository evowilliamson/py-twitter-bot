from util.singleton import Singleton
import os
from util import path_tools as pt
import json

""" Module that contains a singleton class that wraps configuration information """


@Singleton
class Config(object):
    """ Singleton class that wraps configuration information and provides methods to 
    retrieve items """
    
    def __init__(self):
        self.config = self.load()
    
    def load(self):
        with open(os.path.join(pt.get_user_home, "config.json")) as f:
            config = json.load(f)
        return config        

    def get_oath_token(self):
        return self.config["OAUTH_TOKEN"]        

    def get_oath_secret(self):
        return self.config["OAUTH_SECRET"]

    def get_consumer_token(self):
        return self.config["CONSUMER_KEY"]    

    def get_consumer_secret(self):
        return self.config["CONSUMER_SECRET"]

    def get_oath(self):
        """ Method that retrieves the tokens and secrets as a four-itemed tuple 
        """
        
        return (self.get_oath_token, self.get_oath_secret, 
                self.get_consumer_token, self.get_consumer_secret)