# once result was set up, I worked from bottom to top to clear Game pytests: 

class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results

# adding the if new_result and isinstance passing new_result with Result- append the self and retrun .self_reulults so it won't itterate  
# FAILED 1 Game in game.py Game has many results. - TypeError: object of type 'NoneType' has no len()
# FAILED 2 Game in game.py game results are of type Result - TypeError: 'NoneType' object is not subscriptable
    
    def players(self, new_player=None):
        from classes.player import Player
      
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players

# mirrors from the results exampke aboce, swapping out "new_player, Player,and _.players" with corresponding "new_result, Result, and _.results"
# FAILED 3 Game in game.py game has many players. - TypeError: argument of type 'NoneType' is not iterable
# FAILED 4 Game in game.py game players are of type player - TypeError: 'NoneType' object is not subscriptable

    def average_score(self, player):
        player_scores = [r.score for r in self._results if r.player == player]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0


# FAILED 5 Game in game.py test average_score() - assert None == 4999.5

# I had to google and research what to do for the above, since I wasn't having luck trying to mirror it from the coffee example
# The method above returns a calculated average score or 0, depending on whether there are scores available for players.
# I passed two parameters of self and player that then creates a list called player_scores using a list comprehension. 
# It then iterates over each r element in the _results attribute of the class and for each r element, it appends r.score to player_scores to the player associated with the r element matching the player parameter.

# It also checks if the player_scores list is not empty and contains at least one score from a player  
# If it is not empty it will calculate the average score using a sum function adding all the scores in player_scores 
# It then divides the sum by the length of player_scores to give an average.
# finally if the player_scores list is empty with no score it returns 0

# ***************************************************************
# sample of what I mirrored to clear the first four fails in the game pytest 

# class Coffee:
#     def __init__(self, name):
#         self.name = name
#         self._orders =[]
#         self._customers = []
        
#     def orders(self, new_order=None):
#         from classes.order import Order     
#         if new_order and isinstance(new_order, Order):
#             self._orders.append(new_order)
        
#         return self._orders
    
#     def customers(self, new_customer=None):
#         from classes.customer import Customer
#         if new_customer not in self._customers and isinstance(new_customer, Customer):
#             self._customers.append(new_customer)
        
#         return self._customers 
