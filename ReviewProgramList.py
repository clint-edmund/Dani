myList = []

print("Enter items to add to the list. Enter 'done' when finished.")

while True:
    item = input("Enter item: ")
    if item.lower() == 'done':
        print("Terminating input process.")
        break
    elif item in myList:
        print("It's already in List.")
    else:
        myList.append(item)
        print("It has been added to the List")

print("Final list:", myList)
