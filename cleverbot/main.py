#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    This lib is an offcicial API of Cleverbot

    Usage:
        >>> bot = Cleverbot()
        >>> bot.send('Hello')
        >>> print(bot.get())

        "Hi !"
"""

__version__ = "1.0"
__all__ = ["Cleverbot"]

class Cleverbot(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get("http://www.cleverbot.com/")

    def get(self):
        return self.driver.execute_script("return cleverbot.reply")

    def send(self, reply):
        return self.driver.execute_script("cleverbot.sendAI('%s')" % (reply))
