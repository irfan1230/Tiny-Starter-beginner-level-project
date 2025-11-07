print("                    WELCOME TO FLAMES \n")
a , b= input("Enter name Your Name :- ").lower(),input("Enter Your Crush Name :- ").lower()
la,lb=list(a),list(b)
ur = set()
crsh = set()
ur.update(la),crsh.update(lb)
cut = len(ur ^ crsh)
f=["f","l","a","m","e","s"]
while (len(f) > 1):
    index = len(f) % cut
    if index == 0:
        index = len(f)
    f.pop(index-1)    
if "f" in f:
    print("Friend")
elif "l" in f:
    print("Love")
elif "a" in f:
    print("Affection (or) Attraction")
elif "m" in f:
    print("marrage")
elif "e" in f:
    print("enemy")
elif "s" in f:
    print("siblings")                