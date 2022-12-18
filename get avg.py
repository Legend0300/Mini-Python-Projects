def get_avg_marks(D , x):
    sum = 0
    counter = 0
    for i in D[x]:
        sum = sum + int(i)
        counter += 1
    avg = sum/(counter+1)
    print(counter)
    print(avg)


def getdata():
    marks = []
    D = {}
    get_input =  True
    while True:
        id = input("enter the id: ")
        marks = input("enter the marks sep by comma(,): ").split(",")
        D[id] = marks
        get_input = input("do you want to take more students? (y/n): ")
        if get_input == "y":
            continue
        else:
            break
    for x in D:
        print(f"ID: {x}" , end=" \n")
        print("Marks: " , end=" ")
        for i in D[x]:
            print(i , end=" ")
        print("\n")
        get_avg_marks(D , x)



getdata()

