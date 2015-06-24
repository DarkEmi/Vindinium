__author__ = 'Emi'

import requests
from GameClass import Game

userKey = "red87raz"

payload = {'key': userKey}
r = requests.post("http://vindinium.org/api/training", params=payload)

game = Game(r.json())

