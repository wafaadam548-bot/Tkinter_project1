while True:
    print("Welcom to Mad Libs game ")
    num=int(input("chose a number from 1 to 6: "))
    emothion=input("Enter an Emotion ")
    name=input("Please Enter a name ")
    place=input("Please Enter a place ")
    verb=input("Please enter a verb ")
    obj=input("Please Enter an object ")
    adjective=input("Please enter an adjective ")
    for i in num:
        if i==1:
            print("This Mad lib called A Crazy Day ")
            print(f"""I went to the{place} with my {name}. We saw a very {adjective} 
            dog that started to {verb} Loudly. I was so {emothion} that I dropped {obj}""")
        elif i==2:
            print("This mad lib called The Weirdest Teacher Ever")
            print(f""" My teacher {name } is very {adjective}. Every day they make us {verb} in the {place}. Yesterday I accidentally brought a 
            {obj} and everyone started to laugh  """)
        elif i ==3:
            animal=input("Enter an animal : ")
            print ("THis Mad lib called The Animal In My House !")
            print(f"""I woke up and I found {animal} in {place} It was {adjective} and started to {verb}.
            I screamed and threw my {obj} at it! """) 
        elif i==4:
            print("This Mad Lib called I turned into animal")
            print(f""" One day, I turned into a {animal}.
            I went to {place} and started to {verb}.
            Everyone thought I was {adjective}, but I just wanted my {obj} back!""")    
        elif i==5:
            print("This Mab libs called Embersing moment")
            print(f"""One day, I was walking in the {place} when I tripped over a {obj}.
            I accidentally {verb} in front of everyone.
            People thought it was {adjective}, but I felt very {emothion}.""")
        else:
            print("Plase follow instructions =( ")
            continue
    replay=input("Do you want to play again yes or no : ")
    if replay.lower()=="yes" :
        continue       
    else:
        exit(0)