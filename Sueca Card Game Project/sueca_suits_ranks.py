def valid_suit(s):
    
    if s == "H" or s == "C" or s =="S" or s =="D":
        return True
    else:
        return False
    
    

def valid_rank(r):
    
    if r == "A" or r == "Q" or r == "J" or r == "K" or r == "2" or r == "3" or r == "4" or r == "5" or r == "6" or r == "7":
        return True
    else:
        return False
    
def suit_full_name(s):
    
    if s == "H":
        return("Hearts")

    if s == "C":
        return("Clubs")

    if s == "S":
        return("Spades")
    
    if s == "D":
        return("Diamonds")
    
    if s != "H" or "C" or "S" or "D":
        raise ValueError(f"Invalid suit symbol: {s}")
       

def rank_points(r):
    
    
    if valid_rank(r) == False:
        raise ValueError(f"Invalid rank symbol: {r}")
        
    else:
    
        if r == "A":
            return(11)
        
        if r == "7":
            return(10)
        
        if r == "K":
            return(4)
        
        if r == "J":
            return(3)
        
        if r == "Q":
            return(2)
        
        if r == "2" or r == "3" or r == "4" or r == "5" or r == "6":
            return(0)
    

    


def rank_higher_than(r1,r2):
    
    
    if valid_rank(r1) == False:
        raise ValueError(f"Invalid rank symbol: {r1}")
    elif valid_rank(r2) == False:
        raise ValueError("Invalid rank symbol: {r2}")
        
    else:
        
    
        points = {"A": 11,
              "7": 10,
              "K": 4,
              "J": 3,
              "Q": 2,
              "6": 0,
              "5": 0,
              "4": 0,
              "3": 0,
              "2": 0
              }
    

    #INDIVIDUAL NUMBER ORDER
        if r1 == "6" and r2 == "5":
            return True
    
        if r1 == "6" and r2 == "4":
            return True
    
        if r1 == "6" and r2 == "3":
            return True
    
        if r1 == "6" and r2 == "2":
            return True
    
        if r1 == "5" and r2 == "4":
            return True
    
        if r1 == "5" and r2 == "3":
            return True
    
        if r1 == "5" and r2 == "2":
            return True
    
        if r1 == "4" and r2 == "3":
            return True
    
        if r1 == "4" and r2 == "2":
            return True
    
        if r1 == "3" and r2 == "2":
            return True

    
     
    #r1 point system
        if r1 == "A":
            r1 = points["A"]
        
        if r1 == "7":
            r1 = points["7"]

        if r1 == "K":
            r1 = points["K"]
        
        if r1 == "J":
            r1 = points["J"]
        
        if r1 == "Q":
            r1 = points["Q"]
        
        if r1 == "2":
            r1 = points["2"]
        
        if r1 == "3":
            r1 = points["3"]
        
        if r1 == "4":
            r1 = points["4"]
        
        if r1 == "5":
            r1 = points["5"]
        
        if r1 == "6":
            r1 = points["6"]  
        
    #r2 point system    
        if r2 == "A":
            r2 = points["A"]
        
        if r2 == "7":
            r2 = points["7"]

        if r2 == "K":
            r2 = points["K"]
        
        if r2 == "J":
            r2 = points["J"]
        
        if r2 == "Q":
            r2 = points["Q"]
        
        if r2 == "2":
            r2 = points["2"]
        
        if r2 == "3":
            r2 = points["3"]
        
        if r2 == "4":
            r2 = points["4"]
        
        if r2 == "5":
            r2 = points["5"]
        
        if r2 == "6":
            r2 = points["6"] 
    
    
    
        if r1>r2:
            return True
        else:
            return False
