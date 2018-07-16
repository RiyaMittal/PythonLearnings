import pandas as pd

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

#print data


meat_to_animal={'bacon':'pig','pulled pork':'pig','pastrami':'cow','corned beef':'cow','honey ham':'pig','nova lox':'salmon'}

def meat_2_animal(series):
    if series['food']=='bacon':
        return 'pig'
    elif series['food']=='pulled pork':
        return 'pig'
    elif series['food']=='pastrami':
        return 'cow'
    elif series['food']=='corned beef':
        return 'cow'
    elif series['food'] == 'honey ham':
        return 'pig'
    else:
        return 'salmon'
#first method:

#data['animal']=data['food'].map(str.lower).map(meat_to_animal)
#print data

#second method:

lower=lambda x:x.lower()
data['food']=data['food'].apply(lower)
#print data
data['animal2']=data.apply(meat_2_animal,axis='columns')
#print data

# to add new variable:

print(data.assign(new_variable=data['ounces']*9))
#print data