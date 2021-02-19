class Ticker(object):
    def __init__(self, symbol = "", totalRemarks = 0, bullish = 0, bearish = 0, neutral = 0):
        self.symbol = symbol
        self.totalRemarks = totalRemarks
        self.bullish = bullish
        self.bearish = bearish
        self.neutral = neutral

    def incBullish(self):
        bullish += 1
        totalRemarks += 1

    def incBearish(self):
        bearish += 1
        totalRemarks += 1

    def incNeutral(self):
        neutral += 1
        totalRemarks += 1

    def display(self):
        print("$" + "symbol\n")
        bull = "{:.2%}".format(bullish / totalRemarks)
        neut = "{:.2%}".format(neutral / totalRemarks)
        bear = "{:.2%}".format(bearish / totalRemarks)
        print("Bullish: " + bull + "\n")
        print("Neutral: " + neut + "\n")
        print("Bearish: " + bear + "\n")


