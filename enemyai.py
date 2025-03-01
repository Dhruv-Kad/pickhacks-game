
import random
def enemyturn(playerfactories,playerbunkers,enemybunkersdestroyed,difficulty,tension):
    nuke_weight = (enemybunkersdestroyed * difficulty) * (playerbunkers * 0.6) * (playerfactories * 0.1) * tension/2
    spy_weight = (enemybunkersdestroyed * difficulty) * (playerbunkers * 0.4) * (tension/2.5) 
    factory_weight = (enemybunkersdestroyed * difficulty) * (enemybunkersdestroyed) * (abs(tension-10)-1) 

    possible_actions = ['nuke/coup','spy','factory']
    weights = [nuke_weight, spy_weight, factory_weight]
    print(f"{nuke_weight} nuke_weight")
    print(f"{spy_weight} spy_weight")
    print(f"{factory_weight} factory_weight")
    selected_action = random.choices(possible_actions, weights=weights, k=1)[0]
    return selected_action
#input weight for testing the weights
def weighttester():
    seedy = random.seed()
    bunkersgone = random.randint(1,100) 
    playerbunkers =random.randint(1,100) 
    playerfactories =random.randint(1,100) 
    difficulty =random.randint(1,10) 

    print(f"{bunkersgone} {playerbunkers} {playerfactories} {difficulty}")
    print(enemyturn(bunkersgone, playerbunkers,bunkersgone,difficulty,8))

if __name__ == "__main__":
    weighttester()

