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
    
    def get_handle(self):
        """ Get the twitter handle
        """

        return self.config["handle"]    

    def load(self):
        with open(os.path.join(pt.get_user_home, "config.json")) as f:
            config = json.load(f)
        return config        

    def get_oath_token(self):
        return self.config["oauth_token"]        

    def get_oath_secret(self):
        return self.config["oauth_secret"]

    def get_consumer_token(self):
        return self.config["consumer_key"]    

    def get_consumer_secret(self):
        return self.config["consumer_secret"]

    def get_oath(self):
        """ Method that retrieves the tokens and secrets as a four-itemed tuple 
        """
        
        return (self.get_oath_token, self.get_oath_secret, 
                self.get_consumer_token, self.get_consumer_secret)

    def get_followers_file(self):
        """ Returns the name of the file where the followers are stored 
        """

        return self.config["followers"]

    def get_followings_file(self):
        """ Returns the name of the file where the followings are stored 
        """

        return self.config["followings"]

