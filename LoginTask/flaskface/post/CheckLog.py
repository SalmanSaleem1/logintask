import logging
from flaskface.post.Routes import mytest
logging.basicConfig(filename='simple.log', level=logging.DEBUG)


def add(x, y):
    return x + y


plus1 = mytest
logging.debug(f'Add {plus1}')
