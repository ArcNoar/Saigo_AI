"""
Our resources:
1. Correct Sentences 
2. Components ID's
3. Letter's ID's
4. Component Type
5. Bag of Words
"""
from lib2to3.pytree import Node
import pickle # For data saving
from random import randint


#User_Entry = input()

# Our Goal to reach 100 I score

per = []
freq = 1.0


i_score = 0

Supervisor_TF = 1 # Trust Factor (Can we trust supervisor?)

# If STF is low, we prefer to ask supervisor about trustworthy of information he provides


# Compare Sector

Letters_id = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26,
}
Symbols_id = {
    '.' : 0,
    ',' : 1,
    ':' : 2,
    '?' : 3,
    '!' : 4,
    '-' : 5,
    '(' : 6,
    ')' : 7,
    ' ' : 8,
    }
Digits_id = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    
    }


# we can't recognize float digit?

Constant_id = {
    'Letter' : Letters_id,
    'Symbol' : Symbols_id,
    'Digit' : Digits_id,

    }


Node_Base = {}


# Мы остановились на тесте нод генератора, и того как вообще эти ноды заполняются и как поступать с данным и их заполнением.
# По сути это все, потому что я перестал вдуплять в тот момент когда как раз начал думать как же эту хуйню делать
# Надо еще сразу Группировщик реализовать, ведь нод сам по себе это ничто


# Functional Sector

def node_generator(Node_Object='Abstract'): # Creates Node for new data

    Node_Class = 'Unknown'

    if Node_Object == 'Abstract':
        Node_Class = Node_Object
    else:
        Node_Class = f'Constant : {Node_Object}'

    Node_Name = f'{Node_Class} - {randint(0,10000)} ' 

    return Node_Name


def action_module(): # Chosing action to proceed

    # We wanna try to repeat that
    # We don't wanna respong anything
    # We wanna respond something
    # We wanna listen what's next

    pass

def response_module(): # Chosing what we think about entry

    # We met that before
    # We partly understand entry
    # We know what it is but don't know how to react
    # We don't know what it is but we know how to react
    # We don't know what is this and we don't know how react
    # We prefer to let Supervisor continue
    # We prefer to ask for help Supervisor
    # It's first time we met this
    

    pass

def react_module(): # Chosing what we feel about entry

    # We afraid of it
    # We feeling fine with it
    # We are happy to see it
    # We are angry about it
    # We love it
    # It makes us sad
    # We don't feel anything about it
    # We feel uncomfable
    # We are puzzled
    # We think it's funny
    # We are embarrassed
    # We are shy

    pass

def comparing_module(): # Trying to understand entry
    pass

"""
def LTI(word): # Letter_to_ID # 
    word = word.lower()
    id_list = []
    output = ''
    for i in word:
        id_list.append(str(alphs_id[f'{i}']))
     
    output = '-'.join(id_list)
    return output
"""

ramazan_chislo = 7.5

def probability_nod():
    for x in per:
        freq = x * freq

        pass


# Entry Sector

Our_Entry = 'Hello mate'

print(node_generator(Node_Object='H'))


