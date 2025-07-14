mine_string = input("напишите фразу: ")
unique_string = set(mine_string)
count_string = len(unique_string)

if count_string > 10:
    print(True)
else:
    print( False)