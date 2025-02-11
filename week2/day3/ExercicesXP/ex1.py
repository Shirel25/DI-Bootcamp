class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #Your code starts HERE
    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __add__(self, other): # create a new object
        if isinstance(other, (int, float)): # if adding a number
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency): # if adding another currency
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError(f"Cannot add {type(other)} to Currency")
    
    def __iadd__(self, other): # modify the object directly
        if isinstance(other, (int, float)): # If adding a number
            self.amount += other
        elif isinstance(other, Currency): # If adding another currency
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            raise TypeError(f"Cannot add {type(other)} to Currency")
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1)) # 5 dollars
print(int(c1)) # 5
print(repr(c1)) # 5 dollars

print("\n================================================")
print(c1 + 5) # 10 dollars
print(c1 + c2) # 15 dollars

print("\n================================================")
print(c1) # 5 dollars
c1 += 5
print(c1) # 10 dollars

c1 += c2
print(c1) # 20 dollars
print("\n================================================")

try:
    c = c1 + c3
    print(c)
except TypeError as e:
    print(e) # Cannot add between Currency type <dollar> and <shekel>