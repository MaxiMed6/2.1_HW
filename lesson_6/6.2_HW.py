while True:
    users_string = input("Enter the word with \"h\": ")
    if 'h' in users_string.lower():
        print("The 'h' was found")
        break
    else:
      print("No 'h' found. Try again!")