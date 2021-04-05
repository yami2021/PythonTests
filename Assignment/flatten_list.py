

def main():

    entered_list = [[1, 2], [3, 4],[5,6,7],4]
    new_list=[]

    for item in entered_list:
        if type(item) == list:
            for each in item:
                new_list.append(each)
               # print(each)
        else:
            new_list.append(item)
    print(new_list)

if __name__ == "__main__":
    main()