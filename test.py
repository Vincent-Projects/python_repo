tab = [[3.2, 5.4, 7.7, 9.5, 8.3, 9.4],
       [2.3, 4.5, 6.5, 4.3, 7.5, 4.5],
       [1.2, 3.4, 5.4, 5.4, 3.4, 5.4]]

rooms = [["John", "Steve", "Daniel"],
         ["Doo", "Foo", "Bar"],
         ["Me", "You"]]

# Array room
for room in rooms:
    print("Room :");
    for person in room:
        print(person);
    print("");


# Method 1 with array tab
for row in tab:
    for number in row:
        print(number, end="  ");
    print("")

# Method 2 with array tab
for row in range(len(tab)):
    for col in range(len(tab[row])):
        print(tab[row][col], end="  ");
    print("")
