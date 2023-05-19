import math
print("NOTE: this height calculator draws on the fact that children inherit genes from both parent.It takes the average height from both parents and and 6.5cm for boys  and subtract 6.5 for girls.....note that this su a prediction")

patient=int(input("ENTER THE NUMBER OF PATIENT: "))
for i in range(1,patient+1):
    age=float(input(" enter your age: ")) 
    fathers_height=float(input("enter your fathers height in cm: "))
    mothers_height=float(input("enter your mothers height in cm: "))
    height=input(" enter your height cm: ")
    gender=input("male or female : ")

    if gender=="male" and age ==12:
        male=(fathers_height + mothers_height)/2+(6.5)
        height_1=(male/2.54/12)+0.333
        height_in_feet_for_male=f'predicted adult height in feet: {height_1}'
        print(height_in_feet_for_male)
    
    elif gender=="male" and age ==13:
        male=(fathers_height + mothers_height)/2+(6.5)
        height_2=(male/2.54/12)+0.292
        height_in_feet_for_male=f' predicted adult height in feet: {height_2}'
        print(height_in_feet_for_male)

    elif gender=="male" and age ==14:
        male=(fathers_height + mothers_height)/2+(6.5)
        height_3=(male/2.54/12)+0.25
        height_in_feet_for_male=f' predicted adult height in feet: {height_3}'
        print(height_in_feet_for_male)

    elif gender=="male" and age ==15:
        male=(fathers_height + mothers_height)/2+(6.5)
        height_4=(male/2.54/12)+0.208
        height_in_feet_for_male=f' predicted adult height in feet: {height_4}'
        print(height_in_feet_for_male)
    
    elif gender=="male" and age ==16:
        male=(fathers_height + mothers_height)/2+(6.5)
        height_5=(male/2.54/12)+0.167
        height_in_feet_for_male=f' predicted adult height in feet: {height_5}'
        print(height_in_feet_for_male)

    elif gender=="male" and age ==17:
        male=(fathers_height + mothers_height)/2+(6.5)
        height_6=(male/2.54/12)+0.125
        height_in_feet_for_male=f' predicted adult height in feet: {height_6}'
        print(height_in_feet_for_male)

    elif gender=="male" and age ==18:
        male=(fathers_height + mothers_height)/2+(6.5)
        height_7=(male/2.54/12)+0.0833
        height_in_feet_for_male=f' predicted adult height in feet: {height_7}'
        print(height_in_feet_for_male)

    elif gender=="female" and age==12:
        female=(fathers_height + mothers_height)/2-(6.5)
        height_8=(female/2.54/12)+0.292
        height_in_feet_for_female=f'predicted adult height in feet: {height_8}'
        print(height_in_feet_for_female)

    elif gender=="female" and age==13:
        female=(fathers_height + mothers_height)/2-(6.5)
        height_9=(female/2.54/12)+0.25
        height_in_feet_for_female=f'predicted adult height in feet: {height_9}'
        print(height_in_feet_for_female)

    elif gender=="female" and age==14:
        female=(fathers_height + mothers_height)/2-(6.5)
        height_10=(female/2.54/12)+0.233
        height_in_feet_for_female=f'predicted adult height in feet: {height_10}'
        print(height_in_feet_for_female)

    elif gender=="female" and age==15:
        female=(fathers_height + mothers_height)/2-(6.5)
        height_11=(female/2.54/12)+0.208
        height_in_feet_for_female=f'predicted adult height in feet: {height_11}'
        print(height_in_feet_for_female)

    elif gender=="female" and age==16:
        female=(fathers_height + mothers_height)/2-(6.5)
        height_12=(female/2.54/12)+0.192
        height_in_feet_for_female=f'predicted adult height in feet: {height_12}'
        print(height_in_feet_for_female)

    elif gender=="female" and age==17:
        female=(fathers_height + mothers_height)/2-(6.5)
        height_13=(female/2.54/12)+0.167
        height_in_feet_for_female=f'predicted adult height in feet: {height_13}'
        print(height_in_feet_for_female)

    elif gender=="female" and age==18:
        female=(fathers_height + mothers_height)/2-(6.5)
        height_14=(female/2.54/12)+0.15
        height_in_feet_for_female=f'predicted adult height in feet: {height_14}'
        print(height_in_feet_for_female)
    
    else:
        print("CAN'T CALCULATE...CONTACT ENGINEER PRAISE FOR HELP")
