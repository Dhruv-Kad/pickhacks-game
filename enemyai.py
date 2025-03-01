
import random
def enemyturn(playerfactories,playerbunkers,enemybunkersdestroyed,difficulty,tension):
    nuke_weight = (enemybunkersdestroyed * difficulty*2) * (playerbunkers * 0.6) * (playerfactories * 0.1) * tension/2
    spy_weight = (enemybunkersdestroyed * difficulty) * (playerbunkers * 0.4) * (tension/2.5) 
    factory_weight = (enemybunkersdestroyed * difficulty) * (enemybunkersdestroyed) * (abs(tension-10)-1) 

    possible_actions = ['nuke/coup','spy','factory']
    weights = [nuke_weight, spy_weight, factory_weight]
    selected_action = random.choices(possible_actions, weights=weights, k=1)[0]
    return selected_action
#input weight for testing the weights
def weighttester():
    seedy = random.seed()
    bunkersgone = random.randint(1,10) 
    playerbunkers =random.randint(1,10) 
    playerfactories =random.randint(1,20) 
    difficulty =random.randint(1,3) 
    tension =random.randint(1,10) 
    storagedict = {}
    inputlist=(f"Destroyed bunkers: {bunkersgone} playerbunkers: {playerbunkers} playerfactories: {playerfactories} difficulty: {difficulty} tension: {tension}")
    output=(enemyturn(bunkersgone, playerbunkers,bunkersgone,difficulty,tension))
    storagedict[output] = inputlist
    return storagedict
if __name__ == "__main__":
    x = 15
    while x > 0:
        print(weighttester())
        x -= 1

