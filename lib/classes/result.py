# adding Result.all.append(self) clears this pytest 

# FAILED Result in result.py test Result class all attribute - assert 0 == 2

# I then set up Results like I did for the Orders class in the Coffee Challenge
# this class Result will look like the class Owner from Coffe Challenge where  Orders will now equal Results  
# I then changed what was passing through init to mirror the changes and get it to work- 
# customer is now player, coffee is now game, and price is now score
# adding the game.results, game.players, players.results, and players.games_played  will set me up so I can stat clearing the other pytes- 

# I moved on to game.py from here to start clearing those ones   

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
        game.results(self)
        game.players(player)
        player.results(self)
        player.games_played(game)
        

# Sample of what I mirrored 
# class Order:


#     all = []

#     def __init__(self, customer, coffee, price):
#         self.customer = customer
#         self.coffee = coffee
#         self.price = price
#         Order.all.append(self)
#         coffee.orders(self)
#         coffee.customers(customer)
#         customer.orders(self)
#         customer.coffees(coffee)



