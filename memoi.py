class Cards:
    def __init__(self, front, back, hstrSum, hstrCrct):
        ''' historySum, historyCorrect'''
        self.front = front
        self.back = back
        self.hstrSum = hstrSum
        self.hstrCrct = hstrCrct
    def crct():
        self.hstrSum += 1
        self.hstrCrct += 1
    def wrng():
        self.hstrSum += 1