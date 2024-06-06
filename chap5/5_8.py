user_names=['tom','jack','john','jenny','admin']
for name in user_names:
    if name=='admin':
        print('hello admin,would you like to see a status report')
    else:
        print('hello '+name+',would you like to see a status report')