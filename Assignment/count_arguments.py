


def main():
    arg = input("enter arugments").split()
    num = count_user_arguments(arg)
    print(" Number of arguments given by user are: ", num)
    print()
    count2=count_arguments(1,2,3,4,5)
    print("Number of arguments passed in the method are",count2)


def count_user_arguments(args):
    return len(args)

def count_arguments(*args):
    return len(args)

if __name__ == "__main__":

    main()