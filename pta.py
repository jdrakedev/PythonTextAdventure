#Python Text Adventure
#by Jason Drake

from pLib import Player
from clrprint import *
import sqlite3

#imports for fancy text
import sys
from time import sleep
import time
import os

  
#connect/create database
conn = sqlite3.connect('inventory.db')

#create a cursor to execute commands
curs = conn.cursor()

#player object
obj = Player()

def showstats():
    print(f"\n{obj.name}'s stats: ")
    print("+--------------------+")
    print(f" attack:{obj.atk}")
    print(f" health:{obj.health}")
    print(f" coins:{coins}")
    print("+--------------------+")

def showinventory():    
    print('\nin your inventory, you currently have:')
    
    print('------------------------\n')
    
    curs.execute("SELECT * FROM items")
    items = curs.fetchall()
    for i in items:
        print(f"Item: {i[0]}\nHealth: {i[1]}\nCost: {i[2]}\n") 

    curs.execute("SELECT * FROM charms")
    charms = curs.fetchall()
    for i in charms:
        print(f"charm: {i[0]}\nCost: {i[1]}\n")
        
    print('------------------------')

def cont():
    clrinput('\n(Press enter to continue)', clr='blue')

#########################################################################################################################
while True:
    #remove acquired items from database
    curs.execute("DELETE FROM charms")
    
    #reset class vars if player plays again
    obj.setname('')
    obj.setatk(5)
    obj.sethealth(100)
    coins = 60

    print("\nhello! welcome to the python text adventure!")

    name = input("\nwhat is your name stranger? ").strip()

    obj.setname(name)
    #obj.playername(name)

    showstats()
    
    cont()
    
    print('\nyou are on a quest to vanquish rogue slimes past the woods outside town.')
    print('but you must first venture through the woods to reach your destination')
    
    cont()
    
    #call inventory
    showinventory()
    
    cont()

    print("\nthere is a vendor selling upgrades on the edge of town.")
    #####################################################################################################################
    while True:
        atkboost = input('\npay 20 coins for a 10pt attack upgrade? (y/n) '.lower())
        if atkboost == 'y':
            obj.atk += 10
            coins -= 20
            clrprint('\nyou got a 10pt attack increase!', clr='green')
            cont()
            break
        elif atkboost == 'n':
            print('\ndecided to save your coins')
            cont()
            break
        else:
            print("'y' or 'n' please...")
    #####################################################################################################################
    showstats()
    
    cont()
    
    print("\nyou arrive at the edge of the woods, which are shrouded in darkness")
    print("the trees are so densely packed that its impossible to see past the entryway")
    
    cont()
    
    print("\nyou make your way through the first row of trees, led only by a decrepit old path")
    print("and eventually arrive at a fork in the path...")
    
    cont()
    
    print("\nto the right, a sign reads 'hidden village' ")    
    print("\nto the left, a sign reads 'dark cave' ")

    #get player attack
    playerattack = obj.getatk()
    #####################################################################################################################
    while True:
        choice1 = input("\nwhich path do you take? (r/l) ")
        if choice1 == 'r':
        
            clrprint('\non your way to the hidden village you are ambushed by a ninja!', clr='yellow')
            
            cont()
            print('')
            
            n0="               /  "
            n1="              /   "
            n2="    _/\___   /    "
            n3="      |- -|//`    "
            n4="   _|//|_|        "
            n5="    | // //       "

            ninja = [n0,n1,n2,n3,n4,n5]

            for i in ninja:
                sleep(0.10)
                clrprint(i, clr='purple')
            
            #############################################################################################################
            while True:
                engage = input('\nwill you engage the ninja? (y/n) ')
                if engage == 'y':
                    if playerattack > 8:
                        print('\nninja attacks!')
                        cont()
                        print('\nyou defeat ninja!')
                        cont()
                        print('\nyou won 20 coins!')
                        coins += 20
                        showstats()
                        break
                    elif playerattack < 8:
                        print('\nninja attacks!')
                        cont()
                        clrprint('\nninja inflicts 40 damage!',clr='red')
                        #subtract health from player class
                        obj.health -= 40 
                        cont()
                        print('\nninja stole 30 coins and vanished...')
                        coins -= 30
                        showstats()
                        break
                elif engage == 'n':
                    print('\nyou ran away and hid in a big hole in the ground...')
                    cont()
                    print('\nyou notice a large shadowy figure moving towards you...')
                    cont()
                    clrprint('\nsuddenly a massive spider appears before you!',clr='yellow')
                    cont()
                    
                    t1="         ____           "
                    t2="   \____/ __ \____/     "
                    t3="  _____| \  / |_____    "
                    t4=" / ____| /__\ |____ \   "
                    t5="  /   __\____/__   \    "
                    t6="     /   X--X   \       "
                    t7="          ^^            "

                    tranantula = [t1,t2,t3,t4,t5,t6,t7]

                    for i in tranantula:
                        sleep(0.10)
                        clrprint(i, clr='red')
                        
                    cont()
                    clrprint('\nthe massive spider pounces on you!', clr='yellow')
                    clrprint('\nGAME OVER', clr='red')
                    quit()
                else:
                    print("'y' or 'n' please...")
                 
            break
            #############################################################################################################
        elif choice1 == 'l':
        
            print('\nyou peacefully make your way to the foot of the dark cave')
            
            cont()
            
            print('\nanother vendor is stationed outside')
            
            #############################################################################################################
            while True:
                lightcharm = input('\nbuy a lightcharm from vendor for 60 coins? (y/n) ')
                got_lightcham = False
                if coins >= 60:
                    if lightcharm == 'y':
                        clrprint('\nyou received a lightcharm!', clr='green')
                        curs.execute("INSERT INTO charms VALUES('lightcharm', 60)")
                        conn.commit()
                        coins -= 60
                        got_lightcham = True
                        break
                    elif lightcharm == 'n':
                        print('\ndecided to save your coins...')
                        got_lightcham = False
                        break
                    else:
                        print("'y' or 'n' please...")
                else:
                    print('\nnot enough coins...')
                    got_lightcham = False
                    break
            #############################################################################################################
            cont()
            
            showinventory()
            
            cont()
            
            #without the charm player walks right off a cliff in the darkness :( 
            print('\nyou venture into the dark cave...')
            
            cont()
            
            #if player deoesnt have the light charm GAME OVER
            if got_lightcham == False:
                print('\nyou stumbled through the darkness, unable to see anything until')
                print('you eventually walked right off a cliff...')
                clrprint('\nGAME OVER', clr='red')
                quit()
            elif got_lightcham == True:
                print('\nyou proceed with caution through the dark cave...')
                print('only able to see about 3 meters around you')
                cont()
                #continue with cave path
                clrprint('\nsuddenly a giant bat appears before you!',clr='yellow')
                cont()
                print('')
                
                b1="    /\        /\    "
                b2="   /  \|\  /|/  \   "
                b3="  /  /--\\''/--\  \  "
                b4=" /^-'   (  )   '-^\ " 
                b5="        /^^\        "
                   
                bat = [b1,b2,b3,b4,b5]

                for i in bat:
                    sleep(0.10)
                    clrprint(i, clr='red')
                
                cont()
                print('\nbat attacks!')
                cont()
                
                if playerattack > 10:
                    print('you defeated the bat!')
                    cont()
                else:
                    clrprint('\nbat inflicts 60 damage!',clr='red')
                    #subtract health from player class
                    obj.health -= 60 
                    cont()
                
                #continue with cave path
                print('\nyou managed to escape and continue through the cave until finding an exit...')
                
                cont()
                
                print('\nshortly after exiting the cave,')
                print('you spot a patch of light shining through the dense vegetation on the forest')
                
                cont()
                
                clrprint('\nyou have finally made it past the woods!', clr='green')
                
                cont()
                
                print('\nanother vendor is stationed outside...')
                
                cont()
                
                print('\nyou are out of coins but need an attack upgrade to slay the slimes')
                
                cont()
                
                #########################################################################################################
                while True:
                    replacesteak = False
                    tradecave = input('\ntrade a steak for a 20pt attack upgrade? (y/n) ')
                    if tradecave == 'y':
                        curs.execute("DELETE FROM items WHERE name = 'steak'")
                        conn.commit()
                        obj.atk += 20
                        clrprint('\nyou got a 20pt attack increase!', clr='green')
                        replacesteak = True
                        break
                    elif tradecave == 'n':
                        print('\ndecided to save your coins...')
                        replacesteak = False
                        break
                    else:
                        print("'y' or 'n' please...")
                #########################################################################################################
                newplayerattck = obj.getatk()
                
                showinventory()
                
                if replacesteak == True: #TEST!!!
                    curs.execute("INSERT INTO items VALUES('steak', 15, 20)")
                    conn.commit()
                else:
                    pass
                
                cont()
                
                showstats()
                
                cont()
                
                print('\nyou approach the rogue group of slimes that you are on a quest to slay...')

                cont()
                print('')
                
                s1="          ________          "
                s2="      ___(  +   + )         "
                s3="   ____             ______  "
                s4=" _( ^ ^)         __(  *  *) "
                s5="                            "

                slimes = [s1,s2,s3,s4,s5]

                for i in slimes:
                    sleep(0.10)
                    clrprint(i, clr='green')
                
                cont()
                
                clrprint('\nyou launch your attack on the slimes!!!', clr='yellow')
                
                cont()
                
                if newplayerattck > 20:
                    print('\nyou killed all the slimes!!!')
                    cont()
                    clrprint('\nQUEST COMPLETE', clr='green')
                    clrprint('\nthank you for playing!!!', clr='purple')
                    quit()
                else:
                    clrprint('\nyour attack is too low to take on the slimes!', clr='yellow')
                    print('\nthe slimes slowly devour you over the course of 1000 years')
                    clrprint('\nGAME OVER', clr='red')
                    quit()
                
                cont()
            
            break
            
        else:
            print("'r' or 'l' please...")
    #####################################################################################################################
    cont()
    
    print('\nYou proceed to the hidden village...')
    
    cont()
    
    print('\nwhile passing through a small market, a vendor asks if you want to purchase')
    print('a rabbits foot charm for 30 coins...')
    
    cont()
    #####################################################################################################################
    while True:
        rabbitcharm = input('\nbuy the charm (y/n) ')
        got_rabbitcharm = False
        if coins >= 30:
            if rabbitcharm == 'y':
                got_rabbitcharm = True
                clrprint('\nyou received a rabbits foot charm!', clr='green')
                curs.execute("INSERT INTO charms VALUES('rabbitcharm', 30)")
                conn.commit()
                coins -= 30
                break
            elif rabbitcharm == 'n':
                got_rabbitcharm = False
                print('\ndecided to save your coins...')
                break
            else:
                print("'y' or 'n' please...")
        else:
            print('not enough coins...')
            break
    #####################################################################################################################
    cont()
    
    showinventory()
    
    cont()
    
    if got_rabbitcharm == True:
        clrprint('\nthe rabbits foot charm turned out to be cursed!', clr='yellow')
        cont()
        print('\nyou were turned into a defenseless rabbit!')
        clrprint('\nGAME OVER', clr='red')
        quit()
    else:
        pass
    
    print('\nafter exiting the hidden village you are approached by a shaman...')
    
    cont()
    
    showstats()
    
    print('\nthe shaman makes you an offer...')
    print('to answer a riddle for a free 10pt attack upgrade')
    
    cont()
    
    print('\nwith dire consequences if you answer incorrectly...')
    
    #####################################################################################################################
    while True:
        try:
            riddle = input('\nanswer the shamans riddle? (y/n) ')
            if riddle == 'y':
                answer = int(input('\nwhat plus itself equals four? '))
                if answer == 2:
                    print('correct!')
                    obj.atk += 10
                    clrprint('\nyou got a 10pt attack increase!', clr='green')
                else:
                    print('')
                    m0="       ^  <<|>> "
                    m1="      / \   |   "
                    m2="     {-'-}__|   "
                    m3="     /|*|   |   "
                    m4="      ] [       "

                    mage = [m0,m1,m2,m3,m4]

                    for i in mage:
                        sleep(0.10)
                        clrprint(i, clr='yellow')
                    
                    clrprint('\nthe shaman chanted a spell that turned you into a literal dunce cap!', clr='yellow')
                    clrprint('\nGAME OVER', clr='red')
                    quit()
                break
            elif riddle == 'n':
                print('\nyou declined the shady offer')
                break
            else:
                print("'y' or 'n' please...")
        except Exception:
            print("answer must be a number...")
    #####################################################################################################################
    #get player attack
    playerattack = obj.getatk()
    
    cont()
    
    print('you continue on the old path until arriving at the outer rim of the forest...')
    
    cont()
    
    clrprint('\nyou have finally made it past the woods!', clr='green')
    
    showstats()
    
    cont()
    
    print('\nyou approach the rogue group of slimes that you are on a quest to slay...')
    
    cont()
    print('')
    
    s1="          ________          "
    s2="      ___(  +   + )         "
    s3="   ____             ______  "
    s4=" _( ^ ^)         __(  *  *) "
    s5="                            "

    slimes = [s1,s2,s3,s4,s5]

    for i in slimes:
        sleep(0.10)
        clrprint(i, clr='green')
    
    cont()
    
    clrprint('\nyou launch your attack on the slimes!!!', clr='yellow')
    
    cont()
    
    if playerattack > 20:
        print('\nyou killed all the slimes!!!')
        cont()
        clrprint('\nQUEST COMPLETE', clr='green')
        clrprint('\nthank you for playing!!!', clr='purple')
        quit()
    else:
        clrprint('\nyour attack is too low to take on the slimes!', clr='yellow')
        print('\nthe slimes slowly devour you over the course of 1000 years')
        clrprint('\nGAME OVER', clr='red')
        quit()
    
    
    again = input('\nplay again? (y/n) ')
    if again == 'n':
        print('lata!')
        break
#########################################################################################################################
