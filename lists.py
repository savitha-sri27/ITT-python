    n = int(input())
    list=[]
    for _ in range(n):
        com_input=input().split()
        command=com_input[0]
        if command=="insert":
            index=int(com_input[1])
            element=int(com_input[2])
            list.insert(index,element)
        elif command =="print":
            print(list)
        elif command == "remove":            
            element=int(com_input[1])
            list.remove(element)
        elif command == "append":
            element=int(com_input[1])
            list.append(element)
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
