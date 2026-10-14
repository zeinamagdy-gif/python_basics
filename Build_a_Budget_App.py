class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount, 'description': description})
    def withdraw(self,amount,description=""):
        self.ledger.append({'amount': -amount, 'description': description})
        if amount<self.get_balance():
            return True
        return False
    def get_balance(self):
        return sum(item['amount']for item in self.ledger)
    def transfer(self,amount,category):
        if self.get_balance()>=amount:
            self.withdraw(amount,f"Transfer to {category.name}")
            category.deposit(amount,f"Transfer from {self.name}")
            return True
        return False
    def check_funds(self,amount):
        # self.amount=amount
        if amount >self.get_balance():
            return False
        return True
    def __str__(self):
        title = self.name.center(30, '*')
        lines=""
        for item in self.ledger:
            description=item["description"][:23]
            amount=item["amount"]
            lines+=f"{description:<23}{amount:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"

        return title + "\n" + lines + total
def create_spend_chart(categories):
    
    spending=[]
    for category in categories:
        spend=0
        for item in category.ledger:
            if item['amount']<0:
                spend+=abs(item["amount"])
        spending.append(spend)
    total_spend=sum(spending)
    percentages=[]
    for spend in spending:
        if total_spend==0:
            percentage=0
        else:
            percentage=int(spend/total_spend*100)
        percentages.append(percentage)
    chart="Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Print category names vertically
    max_length = max((len(category.name) for category in categories), default=0)

    for i in range(max_length):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        if i < max_length - 1:
            chart += "\n"

    return chart




food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

# Add transactions
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

# Transfer money
food.transfer(50, clothing)

# Print categories
print(food)
print()
print(clothing)
categories = [food, clothing, entertainment]
print(create_spend_chart(categories))
