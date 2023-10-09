import sueca_cards, sueca_tricks


class CardAlreadyPlayed(Exception):
    pass


class Game:
    
    def __init__(self,tc,ts):
        
        self.tc = tc
        self.ts = ts
        
        self.team1_points = 0
        self.team2_points = 0
    
    def gameTrump(self):
        return self.tc
        
        
    def score(self):
        return (self.team1_points,self.team2_points)
    
    
    def playTrick(self,t):
       
       tList = t.show().split()
       
       
       self.tricksPlayed = []
       self.cardsPlayed = []
       self.playersCardsUsed = {1:[], 2:[], 3:[], 4:[]}
       self.playerOrder = [1,2,3,4]
       
         
       for x in tList:
               if x in self.cardsPlayed:
                   raise CardAlreadyPlayed(f"Card {x} has already been played in a previous round of the game.")
               else:
                   self.cardsPlayed.append(sueca_cards.parseCard(x))
                   

       for y, z in zip(tList, self.playerOrder):
              if y in self.playersCardsUsed[z] and y in self.cardsPlayed[z]:
                  raise CardAlreadyPlayed(f"Card {y} has already been played in a previous round of the game.")
                  
              else:
                  self.playersCardsUsed[z].append(sueca_cards.parseCard(y))
                  self.cardsPlayed.append(sueca_cards.parseCard(y))
                  
              
                  
              
                   
            
       self.tricksPlayed.append(t) 
       tWinner = t.trick_winner(self.tc.show()[1])
       self.playerOrder = self.playerOrder[tWinner-1:] + self.playerOrder[:tWinner-1]  
       
       if tWinner == 1 or 3:
           self.team1_points += t.points()
       else:
           self.team2_points += t.points()
       
         
       
    def cardsOf(self,p):
        
        valid_p = [1,2,3,4]
        if p not in valid_p:
            raise ValueError("Invalid player number '{p}")
        return self.playersCardsUsed[p]
    
    def gameTricks(self):
        return(self.tricksPlayed)
