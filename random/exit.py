def user_input_loop():
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print(user_input)

user_input_loop()
