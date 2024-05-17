import json 

def unfold_content(roll_no,argv):
    data=[]
    if str(argv[0])=='-':
        argv= int(argv[0:])
        for i in range(-argv):
            roll= (roll_no + i)
            data.append(roll)
    elif int(argv) >  0:
        argv =int(argv)
        for i in range(argv):
            roll= (roll_no - argv) +i
            data.append(roll)
    return data

print(" Welcome to regno render :","\n")
Roll = input(" Regno -> ")
Arg = input("  move(+,-) -> ")
content = unfold_content(int(Roll),Arg)
print("\n",content)

with open('Regsheet.txt','w') as file:
    for i in content:
        file.write(str(i)+'\n')
    print('')
    print('Completed : data entered in datasheet ')
