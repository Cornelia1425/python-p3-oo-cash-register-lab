#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount =0): #initialising soemthing
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = {} #technically don't need it, to keep track
    
    def add_item(self, title, price, quantity=1):
        self.total += (price * quantity)
        self.last_transaction ={
           'title': title,
           'price': price,
           'quantity':quantity
        }

        for _ in range (quantity): #_, i don't really care about the names inside the list, range
           self.items.append(title)
          
    

    def apply_discount(self):
        if self.discount ==0:
          print("There is no discount to apply.")
        else:
          self.total = ((1-self.discount/100) * self.total )
          print (f"After the discount, the total comes to ${int(self.total)}.")
        
    def void_last_transaction(self):
       for _ in range (self.last_transaction['quantity']):
          self.total -= self.last_transaction['price']
          self.items.pop()
            


#optional parameter
        
        


# best_buy_register = CashRegister (100)
        
        
  
