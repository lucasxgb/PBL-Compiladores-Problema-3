class Token():
    def __init__(self, data):
        self.lexeme = data.get('Lexeme')
        self.type = data.get('Type')
        self.value = data.get('Value')
        self.returnType = data.get('returnType')
        self.parameters = data.get('parameters')
        self.length = data.get('length')
        

class  TableStructure():
    def __init__(self):
        self.table = []
        
    def __assigning(self, token):
        dicTemp = {
            "Lexeme": token.lexeme,
            "Type": token.type,
            "Value": token.value,
            "ReturnType": token.returnType,
            "Parameters": token.parameters,
            'Length': token.length
        }
        return dicTemp
    
    # Adicionando valores na tabela de símbolos
    def addinTable(self, token):
        self.table.append(self.__assigning(token))
    
    # Atualizando valores dessa tabela de símbolos especifica
    def updateValues(self, index, token):
        self.table[index] = self.__assigning(token)
        
    # Receber o index da tabela atual
    def getIndex(self):
        return len(self.table) - 1
    