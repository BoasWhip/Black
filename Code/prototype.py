# -*- coding: utf-8 -*-

def generateID():
    ID = 0
    ID += 0
    return ID

class trade(object):

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.ID = generateID()
        self.position = 0
        self.price = 0.0

    def trade(self, amount, price):
        self.position = amount
        self.price = float(price)
        return (self.position, self.price)

'''
    def __str__(self):
        return (self.strategy, self.name, self.position, self.price)
'''

ticket = trade("RX","Long")
trade = ticket.trade(1000, 25.0)

print(trade)
print(ticket.position)
print(ticket.price)
print(ticket)
