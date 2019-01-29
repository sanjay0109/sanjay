val=input("Enter The Password:")
print("length of password:", len(val))

mlist=list(val)

#python#
for pwd in mlist:
    if ("$" in  pwd  or "@" in pwd or "#" in pwd )and ( len(val) >=6 and len(val)<=12):
        print("Valid password")
    else:
        print("Invalid Password")

