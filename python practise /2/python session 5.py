a = int(input("please enter the number of students : "))

for i in range(a):
    x = int(input('Enter the score: '))
    
    if 20>=x>=10:
        print("Passed")
    else:
        if x>20 : 
            print("not valide")
        else:
            print("failed")
    