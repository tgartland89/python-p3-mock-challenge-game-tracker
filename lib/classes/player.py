class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

      
        
    def results(self, new_result=None):
        from classes.result import Result
       
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results

# mirrored above like the customer class from Coffee challenge- clears the follwong two tests 
# FAILED 1 Player in player.py Player has many results. - TypeError: object of type 'NoneType' has no len()
# FAILED 2 Player in player.py player results are of type Result - TypeError: 'NoneType' object is not subscriptable
    
    def games_played(self, new_game=None):
        from classes.game import Game
        
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played

# mirrored above like customer class from coffee challenge and clears the following 2:
# FAILED 3 Player in player.py Player has many games played. - TypeError: argument of type 'NoneType' is not iterable
# FAILED 4 Player in player.py Player's games played are of type Game - TypeError: 'NoneType' object is not subscriptable
    
    def played_game(self, game):
        return game in self._games_played
    
# researched through google how to get the above and clear the fail- it looked simmilar to the def_num_orders(self), 
# but is also passing game through 
# FAILED Player in player.py Player has played the game. - assert None == True

# The above  code defines a method called played_game within a class and takes the paramaters self and game to check if the game is present 
# in the _games_played attribute of the class from the result.py.
# the purpose of this method is to check whether a specific game has been played using the instance of the class and returns True if the game has 
# been played and False otherwise.

    
    def num_times_played(self, game):
        return len([r for r in self._results if r.game == game])
    
# also resaearched on how to clear- this one was simmilar to the def average_score in the game.py
# FAILED Player in player.py Player has played the game. - assert None == True

# the purpose of this method is to count the number of times a specific game has been played. 
# It iterates over the _results list, checks for matching games, and returns the count of the occurrence
# like the def above for played_game,num_times_played also takes in the slef and game paramanters to creates a list using a list comprehension. 

# It then iterates over each element r in the _results attribute of the class and for each r, it appends the r element to the list 
# if the game associated with r matches the game parameter.
# It also calculates the length of the list created in the previous step using the len function. 

# This gives the number of times the specified game has been played, as it represents the count of matching elements in _results.
# The method returns the count of times the game has been played as an integer value.

# *******************************************************************************************************************************************

# This is what I mirrored to clear the first four Fails for the player pytest 

# class Customer:
#     def __init__(self, name):
#         self.name = name
#         self._orders = []
#         self._coffees = []
        
        
#     def orders(self, new_order=None):
#         from classes.order import Order
#         if new_order and isinstance(new_order, Order):
#             self._orders.append(new_order)
            
#         return self._orders

    
#     def coffees(self, new_coffee=None):
#         from classes.coffee import Coffee        
#         if new_coffee and isinstance(new_coffee, Coffee) and new_coffee not in self._coffees:        
#             self._coffees.append(new_coffee)
            
#         return  self._coffees