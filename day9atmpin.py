atm_pin='1376'
user_pin=''
attempt =0

while atm_pin !=user_pin :
    if attempt>0:
        print(f"Invalid pin code. Total Attempt{attempt}")
    user_pin=input("Enter ATM pin:")
    attempt=attempt+1
print("Access Granted. How Much you wannt to withdraw")
