from twitterapi.twitter import Twitter
import shutil
import unittest
from pathlib import Path
import os
import json

TWITTER_TEST_DIR = "twitter_tests"
IDS_FILE = "ids_file.json"

class TestTwitter(unittest.TestCase):

    def setUp(self):
        TestTwitter.create_dir_in_home()
        self.twitter = Twitter()
        #TODO Mock Connection

    def test_sync_ids(self):
        ids_file = os.path.join(
            TestTwitter.get_dir_in_user_home(TWITTER_TEST_DIR, IDS_FILE))
        created_ids = TestTwitter.create_ids()
        self.twitter._sync_ids(created_ids, ids_file)
        with open(ids_file, "r") as __file:
            ids = json.load(ids_file)
            self.assertListEqual(created_ids == ids)
    
    def tearDown(self):
        TestTwitter.clean_dir_in_home(TWITTER_TEST_DIR)

    @staticmethod
    def create_ids():
        return []

    @staticmethod
    def create_dir_in_home(dir, overwrite=True):
        if overwrite:
            TestTwitter.clean_dir_in_user_home(dir)
        os.mkdir(Path(get_user_home(), dir))

    @staticmethod
    def get_user_home():
        return str(Path.home())

    @staticmethod
    def clean_dir_in_home(dir):
        if Path(str(TestTwitter.get_user_home()), dir).exists() and \
            Path(str(get_user_home()), dir).is_dir():
            shutil.rmtree(Path(get_user_home(), dir))        

    @staticmethod
    def get_dir_in_user_home(dir):
        return str(Path(TestTwitter.get_user_home(), dir))            