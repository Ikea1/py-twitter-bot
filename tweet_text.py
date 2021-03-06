"""Construct messages to be sent as tweet text"""

# Allows using time related functions
from datetime import datetime
# convert times according to time zones
from pytz import timezone

def reply(tweet):
    """Return text to be used as a reply"""
    message = tweet['text']
    user = tweet['user']['screen_name']

def idle_text():
    """Return text that is tweeted when not replying"""
    # Construct the text we want to tweet out (280 chars max)
    text = "Hallo, HPI! Die ist der Bot Ikea1!"
    return text
