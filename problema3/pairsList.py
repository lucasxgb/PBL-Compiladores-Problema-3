class  PairList():
    def __init__(self):
        self.pairList = []
        
   #adicionando na lista de pares
   # Index - Faz referencia ao index da tabela anterior, o pointer aponta para a tabela atual
    def addinList(self, index, pointer):
        self.pairList.append((index, pointer))

    
    # Atualizando valores dessa tabela de símbolos especifica
    def updateValues(self, token):
        self.table.update(self.assigning(token))
    
   

