

def check_user_input(input):
    try:
        # Convert it into integer
        val1 = float(input)
        return val1


        #return val1
        #print("Input is an integer number. Number = ", val)
    except ValueError:
        print("No.. input is not a number. It's a string")
        area()


def area():
    input1 = input("Enter the base of triangle ")
    base = check_user_input(input1)

    input2 = input("Enter the height of the triangle")
    height = check_user_input(input2)

    area = base * height /2
    print("The calculated area is {}".format(area))

if __name__ == "__main__" :
    area()




