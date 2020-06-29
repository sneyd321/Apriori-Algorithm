from Transaction import Transaction

class FileLoader:

    def loadTransactions(self):
        
        with open("transactions.txt", "r") as file:
            transactionList = []
            for line in file:
                transaction = Transaction()
                line = line.replace("\n", "")
                for character in line.split(" "):
                    if (character != "\n"):
                        transaction.addItemToTransaction(int(character))

                transactionList.append(transaction)
        return transactionList


fl = FileLoader()
fl.loadTransactions()

