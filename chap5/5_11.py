list_number=list(range(1,10))
print(list_number)
for number in list_number:
    if number==1:
        print('1st')
    elif number==2:
        print('2nd')
    elif number==3:
        print('3rd')
    else:
        print(str(number)+'th')