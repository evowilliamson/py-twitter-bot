""" Module that contains the class that serves as a facade to the twitter api.
"""

from twitter import Twitter, OAuth, TwitterHTTPError
from util.singleton import Singleton
from connection import Connection
from config.config import Config
import json

class Twitter(object):

    def __init__(self):
        """ Initalises this object by storing the Twitter connection
        """
        
        self.connection = Connection.get()

    def sync_follows_to_from(self):
        """ Syncs people known to the twitter user, both followers and
        people following this user
        """

        self._sync_ids(
            twitter_function=self.connection.followers.ids, 
            ids_file=Config().get_followers_file())
        self._sync_ids(
            twitter_function=self.connection.friends.ids, 
            ids_file=Config().get_followings_file())            

    def _sync_ids(self, twitter_function, ids_file):
        """ Private method that gets ids from twitter api, given the
        function that is provided. It writes the ids to the file that enters
        this function

        Args:
            twitter_function(Function): the twitter function that retrieves the ids
            ids_file(json): The file to which the ids will be written
        
        """

        ids = self._get_ids(twitter_function)
        people = set(ids["ids"])
        while ids["next_cursor"] != 0:
            ids = self._get_ids(twitter_function, ids["next_cursor"])
            people = people|set(ids["ids"])

        with open(ids_file, "a") as __file:
            json.dump(people, __file)

    def _get_ids(self, func, cursor=None):
        """ Gets the ids using the function that is provided, and applying the cursor
        Args:
            func(function): The function that should be applied
            cursor: The cursor that is being used to continue where the batch ended
        """
    
        func(screen_name=Config().get_handle(), cursor=cursor)
