import time
import key
def brief():
    para1 = """Hello commander. As you may have known, tensions with our neighbour, the Bloviet Munion have been approaching a boiling point.
    Our spies have been reporting rapid troop movements and nuclear silo deployments in the Munion and their satellite states. 
    Your job is to stop the spread of their influence by any means necessary. This includes nukes.
    To this end, we have provided you a training simulation to practice what actions to take in the severly unlikely
    case nuclear war breaks out. """
    
    para2 = f"""In this simulation you will be provided with a tactical map accessed through a terminal.
The key for this terminal is as follows.
Water = {key.water}
Land = {key.land}
Irradiated Land= {key.land_nuked}
Your factories = {key.p1_factory}
The factories controlled by the Munion = {key.p2_factory}
Your base(s) = {key.p1_base}
Enemy bases = {key.p2_base}
    """
    para3=f"""Your map will contain an y cordinate, represented by the alphabet, and x cordinates, 
which have marks at every tenths place. Below is an example:
012345678901234567890123456789012345678901234567890123456789012345678901234567890123456)
0---------1---------2---------3---------4---------5---------6---------7---------8------)
A
B                    #########
C               ######################################
D                               #############################
E                       ############################################
F                   #####################################################
G                       ############{key.p1_base}################################
H                        ##########################################
I                               ##########################
G
"""
    para4= """To place a factory, start a coup, or launch a nuke at the point G42, first select the action you want to take. 
Then, type in the cordinates based on the alphabet in the same format as above (Letter Y)(Numerical X).

1.Placing a factory increases the amount of money you recive per round by $250 dollars per factory built
    You can only place a factory within a ten unit radius of a base. The same rule applies to the Munion.
    (I would suggest using the position of their factories to get a rough idea of their base location

2.Starting a coup means you fund our 'overseas interest groups' to have them build up a base with nuclear capablities
    Be warned, if the enemy has a base nearby, our proxy groups will be drawn into a conflict, which we may or may not win
    You can spend more money on funding our 'friends overseas' in order to reduce the radius to where the enemy can interfere

3. If you don't know what launching a nuke does, I seriously question your ability to lead us.

4.We simulate our real-world spy network through giving you the ability to hire spies to reveal Munion bases.
    These spies become more effective the more money you invest into them
    Be warned, the Munion is not without it's own skilled Spies, and they are hungry for the blood of the free world

5. You also have the ability to pass your turn, should you so need
"""
    para5="""Our anaylsts predict that the Munion will not launch nuclear strikes without just cause, and this simulation
aims to reflect that. There will be a tension bar at the bottom of your map representing the amount of time before the war goes nuclear
every action you take, besides building factories increases your tension by one. Be warned that if you go nuclear, the Munion will 
retaliate with nuclear fire."""
    para6 = """I would advise aiming to build up your bases and factories before striking suddenly and blowing them all to high
heaven. Long live liberty, and let the simulated sun rise on a new free virtual world. (P.S Do not consider any ethical quandries)"""
    
    track = 0
    alllist = [para1,para2,para3,para4,para5,para6]
    while track < 6:
        currentpara = alllist[track]
        for line in currentpara.splitlines():
            print(line)
            time.sleep(0.02)
        input("Press enter to continue:")
        track += 1

if __name__ == "__main__":
    brief()
