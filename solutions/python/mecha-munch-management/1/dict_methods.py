"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    cart = current_cart.copy()
    for item in items_to_add:
        cart[item] = cart.get(item, 0) + 1
    return cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}
    for item in notes:
        cart[item] = 1
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    updated_ideas = ideas.copy()
    for recipe, new_contents in recipe_updates:
        updated_ideas[recipe] = new_contents
    return updated_ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for item in cart:
        info = aisle_mapping[item]
        fulfillment_cart[item] = [cart[item], info[0], info[1]]
    return dict(sorted(fulfillment_cart.items(), reverse = True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    updated_inventory = store_inventory.copy()
    for item, (qty, aisle, refrigeration) in fulfillment_cart.items():
        if item in updated_inventory:
            old_qty = updated_inventory[item][0]
            new_qty = old_qty - qty
            if new_qty <= 0:
                updated_inventory[item][0] = 'Out of Stock'
            else:
                updated_inventory[item][0] = new_qty
    return updated_inventory