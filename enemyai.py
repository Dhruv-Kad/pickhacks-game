import random
import key
import map_tools

def enemyturn(playerfactories, playerbunkers, difficulty, tension, money, spy_price, factory_price, nuke_price):
    nuke_weight = 1 + abs(((1 * difficulty * 1) * (playerbunkers * 0.6) * (playerfactories * 1.1) * tension * 1.5) * (money / 3))
    spy_weight = 1 + abs(((1 * difficulty) * (playerbunkers * 0.4) * (abs(tension - 10) + 1) * (money / 3)))
    factory_weight = 1 + abs(((1 * difficulty) * (1.1) * (abs(tension - 10) + 1) * (money / 2)))
    
    
    prices = [nuke_price, spy_price, factory_price]
    possible_actions = [1, 2, 3]
    cpossible_actions = {1: nuke_price, 2: spy_price, 3: factory_price}

    weights = [nuke_weight, spy_weight, factory_weight]
    selected_action = random.choices(possible_actions, weights=weights, k=1)[0]
    priceofsel = prices[selected_action - 1]  # Fixing index because selected_action starts from 1
    
    if money < priceofsel:
        for action, price in cpossible_actions.items():
            if money >= price:
                return action, price
    
    return selected_action, priceofsel

# input weight for testing the weights
def weighttester():
    converted_actions = ['nuke/coup', 'spy', 'factory']
    playerbunkers = random.randint(1, 10)
    playerfactories = random.randint(1, 20)
    difficulty = random.randint(1, 3)
    tension = random.randint(1, 10)
    money = random.randint(10, 10000)
    
    inputlist = (f" playerbunkers: {playerbunkers} playerfactories: {playerfactories} difficulty: {difficulty} "
                 f"tension: {tension} money: {money}")
    
    output, price = enemyturn(playerfactories, playerbunkers, difficulty, tension, money, 10, 100, 1000)
    
    storagedict = {converted_actions[output - 1]: inputlist}  # Storing result with the selected action name
    return storagedict
def confirmarea():
    water = key.water 
    land_nuked = key.land_nuked 
    p2_factory = key.p2_factory 
    p2_base = key.p2_base 
    invalids = [water,land_nuked,p2_factory,p2_base]
    runs = 0
    randx = random.randint(0,85)
    randy = random.randint(0,23)
    underchar = map_tools.get_char(randx,randy)
    while (underchar in invalids):    
        randx = random.randint(0,85)
        randy = random.randint(0,23)
        underchar = map_tools.get_char(randx,randy)
        runs += 1
    return randx,randy 

def aibomb():
    x, y = confirmarea()
    #Add in a better check for if bomb is in safe radius
    map_tools.bomb(x,y,2)



if __name__ == "__main__":
    w = 15
    while w > 0:
        print(weighttester())
        w -= 1
