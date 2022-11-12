for i in range(int(input())):
    n = input()
    if n[-1]=="8" and int(n)%9==0:
        print("-7")
    elif n[-1]=="8":
        print("-3")
    elif int(n)%9==0:
        print("-6")
    else:
        print(n)
