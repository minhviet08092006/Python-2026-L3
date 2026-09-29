list = ["Red", "Blue", "Green", "Purple","Silver","Yellow"]
color = str(input("What is your favourite color?"))
if color in list:
    print("Your color is at index", list.index(color), " in my list")
else:
    print("Sorry, I could not find your color.")