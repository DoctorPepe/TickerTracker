import DiscordBot
from DiscordBot import *
import Ticker
from Ticker import *
import sqlite3

#create database or find an existing one
conn = sqlite3.connect('tickers.db')
cursor = conn.cursor()

conn.close()
