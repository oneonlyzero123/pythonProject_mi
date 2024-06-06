current_users=['tom','jack','john','jenny','admin']
new_users=['Tom','Jack','lucy','jerry','rose']

for name in current_users:
    current_users.remove(name)
    current_users.append(name.lower())

for name in new_users:
    if name.lower()  in current_users:
            print(name + " had been used!u need to ues other name!")

    else:
            print('the new name')
