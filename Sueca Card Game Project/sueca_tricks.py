import sueca_cards

class Trick:
    def __init__(self,ts):
        
        self.pointsTotal = 0
        self.ts = ts
    
    def points(self):
        
        cards = self.ts.split(" ")
        
        for x in range(len(cards)):
            self.pointsTotal += sueca_cards.parseCard(cards[x]).points()
            
        return self.pointsTotal 
        
    def trick_winner(self,t):
        
        cards = self.ts.split(" ")
        
        trumps = []
        winner = cards[0]
        
        for x in range(len(cards)):
            if t in cards[x]:
                trumps.append(cards[x])
            
            else:
                if sueca_cards.parseCard(cards[x]).higher_than(sueca_cards.parseCard(winner), cards[0][1], t):
                    winner = cards[x]
                                                       
        if trumps:
            winner = trumps[0]
            for x in range(len(trumps)):
                if sueca_cards.parseCard(trumps[x]).higher_than(sueca_cards.parseCard(winner), cards[0][1], t):
                    winner = trumps[x]
                    
        return(cards.index(winner)+1)
                
                
            
    
    def show(self):
        return self.ts



def parseTrick(ts):
    
    cards = ts.split(" ")
    
    if len(cards) == 4:
        for x in range(len(cards)):
            sueca_cards.parseCard(cards[x])
        return Trick(ts)
    else:
        raise ValueError(f"A trick string must comprise four cards only; the given trick is: {ts}")
        
    
    
def parseGameFile(fname):
    
    tricksList = []
    
    f = open(fname, "r")
    
    lines = f.read().splitlines()
    
    tc = sueca_cards.parseCard(lines[0])
            
    for x in lines[1:]:
        parseTrick(x)
        tricksList.append(parseTrick(x))

    
    return (tc, tricksList)

    f.close()


