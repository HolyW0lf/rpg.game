

print("there will be some spelling mistakes ples ignore them TY !")

name = input("Enter your name! ")
print(f"greetings {name} welcome to the game of game")

start = input(f"{name} Do you chose to ,play, the game or ,die,? ")
#starting the game with some f string hah
if start == "play":
    print(f"great lets play the game {name}  and have some fun ")
    whare_1 = input("do you want to travel to, the desert or the jungle ")
else:
    print("lame. you are dead new poff:=) ")#add a number 1
    quit()#leand that you can write this and not have a cone shape and more branching and it is simpler 


if whare_1 == "desert":
    print("you are exploring the savanna desert you are with a guide")
    print("you notice that the guide has been missing for a while now ")
    d_choice_1 = input("Do you go follow guide footsteps to look what happened to him ,yes, or ,no,? ")
    if d_choice_1 == "yes":
        print("you follow the footsteps but that suddenly disappear and you have no idea where he went")
        print("and you start floating there's aliens they are trying to take you to thare ship ")
        d_choice_2 = input("what do you do try to ,run, ore just ,let them take you, ")
    elif d_choice_1 == "no":
        print("stay in the car and he comes back after 2 hours and he looks like someone tried to kill him")
        print("And he is telling you about some aliens they took him in the thare ship and tried to kill him but he killed them instead ")
        print("GAME OVER ?") #add number  
else:
    print("invalid respons") 
    quit()




# the hardest one to write 
if whare_1 == "jungle":
    print("You have entered the big and mighty jungle with 3 friends, and one of them went to take a piss but that was a long time ago... ")
    choice_1 = input("Do you ,follow, him or do you ,wait, for him hare? ")
    if choice_1 == "follow":

        print("while you were looking for you´r friend, suddenly and you noticed that you are lost now")
        choice_2 = input("you find a river and you see a boat do you choise the take the ,boat, down the river or do you ,walk, ? ")
    elif choice_1 == "wait":
        print("you wait another 10 mins, But he is still not hare")
        print("and you hear a roar in the distance it is heading for you and it is a big tiger, it tares you and your friend to pieces!!:(")
        print("GAME OVER /")#add number 3
else:
    print("invaliud choice")
    quit()

if d_choice_2 == "run":
    print("you wore seccesfull with runing away and you got back to the car and ")
    print("you drive awey but noticed thets thare is some one following you ")
    d_choice_3 = input("will you stop the car to confront the creep ore do you speed upp")
elif d_choice_2 == "let them take you":
    print("you got captured by the alines and you wore kill for the graiter good")
    print("GAME OVER / ")#add number 
else:
    print("invalid answore you are shit")
    quit()

    

if choice_2 == "walk":
    print("you retch the end of the river and you see that the river is going  dawn to a waterfall, ")
    print("Good that you did not take the boat!")
    choice_3 = input("you have been walking for a while now, do you choose to ,set up camp, or ,keep walking, ?  ")
elif choice_2 == "boat":
    print("while going down the river in the boat you see that you heading for a waterfall and you can't stop it!! you fell down and you're dead")
    print("GAME OVER /")#add a count 2
else:
    print("invaliud choice")
    quit()

if choice_3 == "set up camp":
    print("You some hove know how to set up camp and you did a good job ")
    choice_4 = input("Now it's dark and you see a cave near you will you ,enter the cave, or ,stay, in your camp? ")
elif choice_3 == "keep walking":
    print("you walk when suddenly a you touch a plant and you die of heart attack!")
    print("GAME OVER ")#add number
else:
    print("invaliud choice")
    quit()


#i will not be doing the quiet thing i forget time new is 01:24 am yayayayayayaya
if choice_4 == "stay":
    print("You have some good survival instincts you see a tiger leaving the cave and after a couple of mins, fall a sleep, hungry")
    print("you wake up hungry and you decide to go and check out the cave, and you find some meat thet the tiger left")
    choice_5 = input("do you ,take the meat, back grill it or ,leave it, and die of hunger? ")
    if choice_5 == "take the meat":
        print("you grill the meat over the fire you maid ")
        choice_6 = input("while eating you spot a fire in the distance do you ,go to the fire, ore ,stay,? ")
elif "enter the cave":
    print("there's a tiger eating meat and tiger spot you, and you try to run but you can't get away and tiger eats you")
    print("GAME OVER / ")#add numbers4
else:
    print("invalid choice. you dead start over")
    quit()

if choice_6 == "go to the fire":
    print("you walk for about 2 hours and find your friend that you left 1 day earlier he got a rescue team ")
    print("congrats you survived the jungle!!!!!! good job ")
elif choice_6 == "stay":
    print("the fire disappears and you never leave the jungle and become tarsan. ")
    print("GAME OVER !!")#add a number
else:
    print("invalid choice. you suck!!")
    quit()
