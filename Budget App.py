class Category():

  # class attributes 
  def __init__ (self, category):
    self.category = category 
    self.balance = 0.0
    self.ledger = []

  # prints out descriptions and corresponding amount deposited/withdrown
  def __str__(self):
    x = f"{self.category:*^30}\n"
    for item in self.ledger:
      amount = format(item['amount'], '.2f')
      if len(item['description']) > 23:
        x += f"{(item['description'])[:23]:<0}{amount:>{30-len((item['description'])[:23])}}\n"
      else:
        x += f"{item['description']:<0}{amount:>{30-len(item['description'])}}\n"
    x += f"Total: {format(self.balance, '.2f')}"
    return x

  # compares an amount and the current balance 
  def check_funds(self, amount):
    if amount > self.balance:
      return False
    elif amount <= self.balance:
      return True

  # deposits an amount and logs the amount & its description 
  def deposit(self, amount, description=""):
    x = {"amount":amount,"description":description}
    self.balance += amount 
    self.ledger.append(x)

  # withdrawls an amount and an logs the amount & its description 
  def withdraw(self, amount, description=""):
    x = {"amount":-amount, "description":description}
    if self.check_funds(amount) == True:
      self.ledger.append(x)
      self.balance -= amount
    return self.check_funds(amount)
  
  # get the current balance
  def get_balance(self):
    return self.balance 

  # transfers an amount from one category to another
  def transfer(self, amount, other_category):
    if self.check_funds(amount) == True:
      other_category.deposit(amount, f"Transfer from {self.category}")
      self.withdraw(amount, f"Transfer to {other_category.category}")
    return self.check_funds(amount)

# displays the percentage spent by each category
def create_spend_chart(categories):
  category_names = []
  categories_spent = []
  category_percentage = []
  total_spent = 0.0
  for category in categories:
    category_names.append(category.category)
    spent = 0.0
    for item in category.ledger:
      if item['amount'] < 0.0:
        total_spent += abs(item['amount'])
        spent += abs(item['amount'])
    categories_spent.append(spent)
  
  for amount in categories_spent:
    percentage = round(((amount /total_spent) * 100), 2)
    category_percentage.append(percentage)

  output = "Percentage spent by category\n"
  for n in range(100, -1, -10):
    output += f"{str(n)+'| ':>5}" 
    for value in category_percentage:
      if value >= n:
        output += 'o  '
      else:
        output += '   '
    output += '\n'
      
  L = len(category_names)
  output += f"    {L*'---'+'-'}\n"

  longest_name_length = 0
  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)
      
  for i in range(longest_name_length):
    output += "     "
    for name in category_names:
      if len(name) > i:
        output += name[i] + "  "
      else:
        output += "   "
    if i < longest_name_length-1:
      output += "\n" 
      
  return output