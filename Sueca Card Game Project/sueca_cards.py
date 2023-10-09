import sueca_suits_ranks



class CardInvalid(Exception):
    pass



class Card:
    
    def __init__(self,rank,suit):
        
        self.rank = rank
        self.suit = suit
       
        
       

    def points(self):
        return sueca_suits_ranks.rank_points(self.rank)
        
        

    def higher_than(self,other,s,t):
        if self.suit == other.suit:
            #Both cards are the same suit, compare ranks
            return sueca_suits_ranks.rank_higher_than(self.rank,other.rank)
        #If they are not the same suit, and the first card follows the lead, but other is not trump, first wins
        elif self.suit == s and other.suit != t:
            return True
        #If first card is trump and they are not the same, first wins
        elif self.suit == t:
            return True
        #If first card is not trump, and they are not the same, then the other card must be a trump
        else:
            return False
        
        
        
    def show(self):
        return self.rank+self.suit
        
        
        
def parseCard(cs):
    
   
    rank = cs[0]
    suit = cs[1]
    x = rank+suit
    
    if len(cs) != 2:
        raise CardInvalid(f"Card '{cs}' is invalid! \nA card string representation must contain 2 characters only.")
        
        
    if sueca_suits_ranks.valid_suit(suit)==False:
       raise CardInvalid(f"Card '{x}' is invalid! \nInvalid suit symbol: {suit}")
       
    
    if sueca_suits_ranks.valid_rank(rank)==False:
        raise CardInvalid(f"Card '{x}' is invalid! \nInvalid rank symbol: {rank}")
        
    return Card(rank,suit)
    
    
    
    