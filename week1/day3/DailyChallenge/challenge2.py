# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

#=================================================
# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100" 

#=================================================
items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

#=================================================

afford = []
wallet = int(wallet.strip("$"))
total_cost = 0
         
for item in sorted(items_purchase):
    price = int(items_purchase[item].strip("$").replace(",", ""))

    if total_cost + price <= wallet:
        afford.append(item)
        total_cost += price


print(afford if afford else "Nothing")