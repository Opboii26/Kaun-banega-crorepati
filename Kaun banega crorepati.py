qa = [
    "1. What is the capital of India?\n a) Mumbai\n b) Kolkata\n c) New Delhi\n d) Chennai\n",
    "2. Who wrote the National Anthem of India?\n a) Rabindranath Tagore\n b) Mahatma Gandhi\n c) Subhas Chandra Bose\n d) Bankim Chandra Chatterjee\n",
    "3. What is the square root of 144?\n a) 12\n b) 14\n c) 16\n d) 18\n",
    "4. Which planet is known as the Red Planet?\n a) Venus\n b) Mars\n c) Jupiter\n d) Saturn\n",
    "5. Who is known as the Father of the Nation in India?\n a) Bhagat Singh\n b) Subhas Chandra Bose\n c) Mahatma Gandhi\n d) Jawaharlal Nehru\n"
]

print("Welcome, This is KBC \"Kaun Banega Crorepati\"\n")
print("Answer questions like this: a, b, c, d\n")

ruppee = 0

if input(qa[0]) == "c":
    print("Correct Answer!")
    ruppee += 500
    if input(qa[1]) == "a":
        print("Correct Answer!")
        ruppee += 500
        if input(qa[2]) == "a":
            print("Correct Answer!")
            ruppee += 500
            if input(qa[3]) == "b":
                print("Correct Answer!")
                ruppee += 500
                if input(qa[4]) == "c":
                    print("Correct Answer!")
                    ruppee += 500
                    print(f"You won {ruppee} and this money will be added to your bank balance!")
                else:
                    print("Wrong Answer!")
            else:
                print("Wrong Answer!")
        else:
            print("Wrong Answer!")
    else:
        print("Wrong Answer!")
else:
    print("Wrong Answer!")