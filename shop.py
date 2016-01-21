player_gold = 1000

player_inv=[]
shop_prices = [250,100,150,175]

shop_stock = ["Iron Sword", "Rusted Sword","Potion","Mana Potion"]

def shop_intro():

    choice = raw_input("Would you like to buy, sell or leave?")

    if choice == "buy":
        print  "Funds:   %sg" % (player_gold)

        return True

    elif choice == "sell":

        return False

    else:

        print "I'm sorry, what would you like to do?"

        shop_intro()

def prices(item):

    price = 0

    b = shop_stock.index(item)

    price = shop_prices[b]

    return price
def shop_body():

    print "What do you want to buy?"

    prices_id = 0

    for i in shop_stock:

        prices_id = prices(i)

        if type(prices_id) == int:

            print i + view_correction(i) + str(prices(i))

        elif type(prices_id) == str:

            print i + view_correction(i) + prices(i)

            purchase = raw_input()

    return purchase

def view_correction(current_item):

    str_length = len(current_item)

    indt_length = 0
    j = 35

    shop_stock_index = shop_stock.index(current_item)

    shop_prices_index = shop_prices[shop_stock_index]

    price_len = len(str(shop_prices_index))

    new_length = 0

    if price_len >= 3:

        price_len -= 3

        indt_length = j - str_length - price_len

    elif price_len < 3:

        price_len += 3

        indt_length = j - str_length + price_len

    return indt_length * "-"

def add_shop_item(item_to_add,price_to_add):

    shop_stock.append(item_to_add)

    shop_prices.append(price_to_add)

def shop_buying(i):

    item_cost = prices(i)

    print "So you want to buy some %ss?" % (i)

    buy_amount = raw_input("How many do you want?")

    total_cost = item_cost * int(buy_amount)

    print "%s right?, that'll be %s ok? (y/n)" % (buy_amount, total_cost)

    true_false = raw_input()

    if true_false == "yes" or true_false == "y":

        if player_gold < total_cost:

            print "You don't have enough for that."

        else:

            print "Thanks alot."

            return player_gold - total_cost

    elif true_false == "no" or true_false == "n":

        print "See you around."

add_shop_item("Magic Leaf",1000)

add_shop_item("Ultra Rare Mushroom",10000)

add_shop_item("Cc",100000)

add_shop_item("Test Dummy","???")

intro_value = shop_intro()

if intro_value:

    player_gold = int(shop_buying(shop_body()))

    print  "Funds:   %sg" % (player_gold)

elif intro_value == False:

    print "THIS FEATURE IS UNDER CONSTRUCTION!!"