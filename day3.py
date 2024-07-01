#H.W Write a Python program to add the names of your 5 friends 
# to a list and their corresponding addresses to another list. 
# Then, print the names and addresses in the format: "Name lives in Address."
name=['Shyam','Rita','Krishna','Barsha','Padam']
address=['America','Nepal','India','China','Uk']
for i in range(len(name)):
    print(f"{name[i]}live in {address[i]}")