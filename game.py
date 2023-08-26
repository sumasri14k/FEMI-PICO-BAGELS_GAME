original_number = "501"
x = True
while x == True:
    output = []
    t = input("guess the 3 digit number: ")
    if int(original_number) - int(t) == 0:
        print("Femi " * len(t))
        print("YOU WON")
        x = False
    elif len(set(t)) < len(original_number):
        t = input("enter different numbers only: ")

    elif len(t) < len(original_number):
        t = input("enter 3 digit number only: ")
    else:

        for i in range(len(original_number)):
            for j in range(len(t)):
                if original_number[i] == t[j]:
                    if i == j:
                        output.append("femi")



                    else:
                        output.append("Pico")

                        break
        if output==[]:
            print('!!BAGELS')
            print("NO DIGIT MATCHED")
        else:
            print(output)

