# Hero's Inventory
# Demonstrates Tuple Creation

# This will work very well as an inventory system in something like a text adventure game

# Create an empty tuple
inventory = ('sword',
             'armor',
             'shield',
             'healing potion')

# Treat the tuple as a condition
if not inventory:
    print('You are empty handed.')
else:
    # The inventory is not empty so we can continue
    print('\nThe tuple inventory is:')
    print(inventory)
    
    # Inventory item count
    print(f'\nYou have {len(inventory)} items in your inventory.')

# Print each element in the tuple
    print('\nYour items:')
    for item in inventory:
        print(item)

    # Showcasing membership by giving personalised messages for certain items
    if 'healing potion' in inventory:
        print('\nYou will live to fight another day.')
    
    if 'sword' in inventory:
        print('\nYou have a nice sword.')
    
    # Searching the inventory for a specific item
    searchIndex = int(input('Enter an index to search for an inventory item:\n'))
    if searchIndex >= 0 and searchIndex <= len(inventory):
        print(f'At index {searchIndex} the item is a {inventory[searchIndex]}')
    else:
        print(f'This is not a valid Inventory item.')
    
    # Adding chest loot to inventory
    chest = ('Gold', 'Gems')
    print(f'You find a chest while exploring, you open it and it contains: {chest}.\nAdding these to your inventory.')

    inventory += chest
    
    print(f'Your inventory now contains: {inventory}')