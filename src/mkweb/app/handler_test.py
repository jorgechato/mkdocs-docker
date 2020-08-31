import unittest
import os
from contextlib import redirect_stdout

from app import handler

ROOT_DIR = os.getcwd()
MKDOCS_DIR = ROOT_DIR+"/res/test"
PRODUCE_TMP_DIR = ROOT_DIR+"/res/test-html"
PRODUCE_FILE = ROOT_DIR+"/res/test-aux.tar.gz"
BASE_TAR = ROOT_DIR+"/res/test.tar.gz"


class TestHandlerMethods(unittest.TestCase):

    def test_produce_is_file(self):
        #  Dependency injection for stdout
        handler.produce(
            MKDOCS_DIR,
            PRODUCE_TMP_DIR,
            fileobj=None,
            fileto=PRODUCE_FILE
        )

        self.assertTrue(os.path.isfile(PRODUCE_FILE))

    def test_serve(self):
        #  TODO: test server with valid http response
        pass


if __name__ == '__main__':
    unittest.main()
