
import random
def enemyturn(playerfactories,playerbunkers,enemybunkersdestroyed,difficulty,tension,money,spy_price,factory_price,nuke_price):
    nuke_weight = 1+((enemybunkersdestroyed * difficulty*1) * (playerbunkers * 0.6) * (playerfactories * 0.1) * tension*1.5)*(money/3)
    spy_weight = 1+((enemybunkersdestroyed * difficulty) * (playerbunkers * 0.4) * (abs(tension-9)+1)*(money/3))
    factory_weight = 1+((enemybunkersdestroyed * difficulty) * (enemybunkersdestroyed) * (abs(tension-10)+1)*(money/2))
    print(f"nuke_weight {nuke_weight} spy_weight {spy_weight} factory_weight {factory_weight}")
    
    #possible_actions = ['nuke/coup','spy','factory']
    possible_actions = [1,2,3]
    weights = [nuke_weight, spy_weight, factory_weight]
    selected_action = random.choices(possible_actions, weights=weights, k=1)[0]
    return [selected_action,priceofselectedaction]
#input weight for testing the weights
def weighttester():
    converted_actions = ['nuke/coup','spy','factory']
    seedy = random.seed()
    bunkersgone = random.randint(1,10) 
    playerbunkers =random.randint(1,10) 
    playerfactories =random.randint(1,20) 
    difficulty =random.randint(1,3) 
    tension =random.randint(1,10) 
    money =random.randint(10,10000)
    storagedict = {}
    inputlist=(f"Destroyed bunkers: {bunkersgone} playerbunkers: {playerbunkers} playerfactories: {playerfactories} difficulty: {difficulty} tension: {tension} money: {money}")
    output=(enemyturn(bunkersgone, playerbunkers,bunkersgone,difficulty,tension,money))
    storagedict[converted_actions[output-1]] = inputlist
    return storagedict
if __name__ == "__main__":
    x = 150
    while x > 0:
        print(weighttester())
        x -= 1

