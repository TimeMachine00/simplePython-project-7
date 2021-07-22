print("created by hussainatphysics@gmail.com(hussainsha syed)")
print("welcome to place holder")

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
holder = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
place = input("Where do you want to put the treasure baby darling? ")


a= int(place[0])
b=int(place[1])
holder[a-1][b-1]='X'


print(f"{row1}\n{row2}\n{row3}")

print()

but1= print(input("press enter for bye..........."))