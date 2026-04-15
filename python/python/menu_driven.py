items =['milk','bread','paneer']
while True:
    print("1. Add item")
    print("2. View items")
    print("3. update items")
    print("4. delete items")
    print("5. search items")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        item = input("Enter the item : ")
        items.append(item)
        print(f"{item} added to the list.")
        print(items)
        
    elif choice=='2':
        if item:
            print("Shopping list:", items)

    elif choice== '3':
        old_item = input("Enter the item to update: ")
        if old_item in items:
            new_item = input("Enter the new item: ")
            index = items.index(old_item)
            items[index] = new_item
            
            print(f"{old_item} updated.") 
        else:
            print(f"{old_item} not found.")  

    elif choice == '4':
        item = input("Enter the item to delete: ")
        if item in items:
            items.delete(item)
            print(f"{item} deleted.")
        else:
            print(f"{item} not found.")     
            
    elif choice == '5':
        item = input("Enter the item to search: ")
        if item in items:
            print(f"{item} found in the list.")
        else:
            print(f"{item} not found in the list.")
    
    elif choice == '6':
        print("Exiting the program.")
        break