resultset= {
    'oo41144A': '4'
    'oo41194C': '3.3'
    'oo41164N': '2.9'
    'oo41144P': '1.9'
    'oo41164R': '3.2'
    'oo41144T': '2'
    'oo41184Y': '4'
    'oo41124Z': '3.1'
    'oo41114O': '1.8'
    'oo41174L': '1.6'

}
symbol_no=input("Enter your symbol number:")
for i in resultset.keys():
    if symbol_no==i:
        result=resultset[i]
    else:
        result =''
if result !="":
    print(f"Your result is {result}")
else :
    print("You symbol number not found.")