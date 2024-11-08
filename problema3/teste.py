from tableStructure import Token, TableStructure
from typeTable import TypeTable
from pairsList import PairList


'''
register my_register {
  integer reg1; 
  boolean reg2; 
}
''' 
    
token = Token({
            "Lexeme": "my_register",
            "Type": "integer",
            "Value": "reg1",
        })

typeTable = TypeTable()
typeTable.addinTable(token)
token = Token({
            "Lexeme": "my_register",
            "Type": "boolean",
            "Value": "reg2",
        })

typeTable.addinTable(token)



for item in typeTable.typeTable:
    print(f"{item}")
    print(type(item))

