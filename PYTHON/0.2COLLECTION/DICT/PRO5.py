s={
    's1':
    {'name':'hiren',
    'score':76,
    'sub':'python'
    },
    's2':
    {
        'name':'ketan',
        'score':67,
        'sub':'java'
    },
    's3':
    {'name':'nchetan',
    'score':90,
    'sub':'php'
    }
}


for i in range(1,len(s)+1):
    print(s[f's{i}']['name'],s[f's{i}']['sub'],s[f's{i}']['score'])