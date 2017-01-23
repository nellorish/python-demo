def get_order():
    print("[command] [item] (command is a to add, d to delete, q to quit)")
    line = input()
    command = line[:1]
    item = line[2:]

    return command,item


def process_order(item, cart):
    command, item = item

    if command == "a":
        cart.append(item)
    elif command == "d" and item in cart:
        cart.remove(item)
    elif command == "q":
        return False

    return True


def go_shopping():
    cart = []
    while True:
        order = get_order()

        if not process_order(order, cart):
            break

    print(cart)
    print("Finished Shopping")


go_shopping()
