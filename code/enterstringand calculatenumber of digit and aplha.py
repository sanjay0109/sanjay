val=input("Enter any String:")

slist=list(val)

print ("length of string:", len(slist))

digit=0
alpha=0
for cal in val:
    if cal.isdigit():
        digit=digit+1
    if cal.isalpha():
        alpha=alpha+1
print("number of aplhabets:",alpha)
print("number of digits:",digit)
