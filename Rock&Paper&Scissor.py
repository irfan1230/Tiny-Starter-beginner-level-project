import random
def rps():
    rps=["r","p","s"]
    hp=0.0
    ep=0.0
    ch=10
    nch=0
    a=("You 😎")
    b="Computer 🤖"
    print("Only Enter r,p,s\nr is rock\np is paper\ns is scissor\n")
    print(a.center(1),b.center(45),"\n\t..Let's Start Go..")
    while(nch<ch):
        print(f"Your Score:- {hp}  Computer Score:- {ep}")
        I=input(f"Your Chance Enter :-")
        rand = random.choice(rps)
        print(f"Computer Guess :- {rand}")
        if I == rand:
            print("Tie Each One point")
            hp+=1
            ep+=1
            #paper weak rock
        elif  I == "p" and rand == "r" :
            print("You Win")
            hp+=1
        elif  I == "r" and rand == "p" :
            print("You Win")
            ep+=1
            #rock weak scissors
        elif  I == "r" and rand == "s" :
            print("You Win")
            hp+=1    
            
        elif  I == "s" and rand == "r" :
            print("You lose")
            ep+=1
           # scissorsweak paper    
        elif  I == "p" and rand == "s" :
            print("You lose")
            ep+=1    
        elif  I == "s" and rand == "p" :
            print("You Win")
            hp+=1    
        else:
            print("only enter r,s,p \n you lose -1 point")
            hp-=1
            ep+= 0.5   
        nch+=1
    if hp > ep:
        print("\n🥳You Win Over the Mathch 🥳")
    elif hp < ep :
    	print("\nSorry Better Luck Next")  
    else  :
        print("\n😎=Match is Tie=🤖")
    print("\n New Match Start \n\n") 
rps()    