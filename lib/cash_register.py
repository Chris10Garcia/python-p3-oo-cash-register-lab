#!/usr/bin/env python3

class CashRegister:
  total = 0
  items = None
  costs = None
  def __init__ (self, discount=0):
    self.discount = discount

  def add_item (self, item, cost, qty = 1):
    if self.items == None and self.costs == None:
      self.items = []
      self.costs = []
    for i in range(0, qty):
      self.items.append(item)
      self.costs.append([cost, qty])
    self.total = self.total + cost * qty
  
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = (1 - self.discount/100) * self.total
      print(f"After the discount, the total comes to ${self.total:.0f}.")

  def void_last_transaction(self):
    self.items.pop()
    last_cost = self.costs.pop()
    self.total = self.total - last_cost[0] * last_cost[1] 

# new_register = CashRegister()
# new_register.add_item("eggs", 1.99)
# new_register.add_item("tomato", 1.76)

# print(new_register.items)