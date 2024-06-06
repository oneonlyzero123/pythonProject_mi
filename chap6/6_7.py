people={'friend':{
    'first':'one',
    'last':'two',
    'location':'beijing'
    },
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',

    },
}
for name,info in people.items():
    print('name:'+name)
    first=info['first']
    last=info['last']
    location=info['location']
    print('information:'+first+" "+last+"\nlocation:"+location+"\n")