class  TypeTable():
    def __init__(self):
        self.typeTable = []
        
    def __assigning(self, token):
        dicTemp ={
            "Lexeme": token.lexeme,
            "Type": token.type,
            "Value": token.value,
        }
        return dicTemp
    
    # Adicionando valores na tabela de símbolos
    def addinTable(self, token):
        self.typeTable.append(self.__assigning(token))

    
    # Atualizando valores dessa tabela de símbolos especifica
    def updateValues(self, index, token):
        self.typeTable[index] = self.__assigning(token)
        
    # Receber o index da tabela atual
    def getIndex(self):
        return len(self.typeTable) - 1