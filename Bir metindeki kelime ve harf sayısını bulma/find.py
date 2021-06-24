while True:
    text = input("Enter a text:")
    space_counter = 0
    for words in text:
        if words == " ":
            space_counter+=1
    print(f"Number of words:{space_counter+1}")
    print(f"Number of letters:{len(text)-space_counter}")
