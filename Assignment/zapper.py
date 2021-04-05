def main():

    zap(
        [0, 1, 2, 3],
        [5, 6, 7, 8]
    )

def zap(a,b):
    l = []
    for i in range(4):
        x=a[i]
        y=b[i]
        t=(x,y)
        l.append(t)
    print(l)



    #print(l)

        #z=list(zip(a,b))
        #print(z)

if  __name__ =="__main__":
    main()
