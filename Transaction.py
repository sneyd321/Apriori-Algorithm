class Transaction:

    def __init__(self):
        self._transaction = []

    def addItemToTransaction(self, item):
        self._transaction.append(item)

    def getSize(self):
        return len(self._transaction)

    def getTransaction(self):
        return self._transaction

