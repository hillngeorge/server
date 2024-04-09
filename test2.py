def colors():
    all_colors = ["white", "red", "blue", "white", "purple", "red", "black", "white", "black"]

    # 1st - print every color
    # count - how many times we have "white"
    count = 0
    for color in all_colors:
        print(color)

        if color == "white" or color == "black":
            count += 1

    print("The result is " + str(count))        


# fn calls
colors()