import json 

def unfold_content(roll_no,no_back):
    data=[]
    for i in range(no_back):
        roll= (roll_no - no_back) +i
        data.append(roll)
    return data
    
Roll = input(" Enter roll no : ")
Back = input(" Enter how many girl : ")
content = unfold_content(int(Roll),int(Back))
print("\n",content)

with open('Regsheet.txt','w') as file:
    for i in content:
        file.write(str(i)+'\n')
    print('')
    print('complete data entered in datasheet ')