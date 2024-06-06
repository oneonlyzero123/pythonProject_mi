name_list=['jack','tom','rose','jen','sarah','edward']
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    }

for name in name_list:
    if name in favorite_languages.keys():
        print('hi '+name+" ,thank u for your answer!")
    else:
        print('dear '+name+" ,can u tell me what is your favorite language?")