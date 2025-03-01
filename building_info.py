import map_tools
import key

class building:
    # buidling type can either be "bunker" or "factory"
    # visibility can be True or False
    # ownership should be a 1 or 2

    def __init__(self,xcoord,ycoord,buildingType,visibility, ownership):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.buildingType = buildingType
        self.visibility = visibility
        self.ownership = ownership
        
    def putOnMap(self,worldMap = map_tools.worldMap):
        if(self.buildingType == "factory"):
            if(self.ownership == 1):
                map_tools.swapchar(self.xcoord,self.ycoord, key.p1_factory)
            else:
                map_tools.swapchar(self.xcoord,self.ycoord, key.p2_factory)

        elif(self.visibility):
            if(self.ownership == 1):
                map_tools.swapchar(self.xcoord,self.ycoord, key.p1_base)
            else:
                map_tools.swapchar(self.xcoord,self.ycoord, key.p2_base)
