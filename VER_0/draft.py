
Node_Base = {
    'CONSTANT|H' : [0.0],
    'CONSTANT|E' : [0.0],
    'CONSTANT|L' : [0.0],
    'CONSTANT|O' : [0.0],

    }

N_Links = {
    "CONSTANT|H" : {
        'CONSTANT|E' : [1.0,1.0],
        'CONSTANT|I' : [1.5,1.5]
        
    },
}


Node_Group = {
    'HELLO' : {
        "H" : [Node_Base['CONSTANT|H'],N_Links['CONSTANT|H']['CONSTANT|E']],
        "E" : Node_Base['CONSTANT|E'],
        "L" : Node_Base['CONSTANT|L'],
        "L_2" : Node_Base['CONSTANT|L'],
        "O" : Node_Base['CONSTANT|O'],
    },    
}

NG_Hello = Node_Group['HELLO']
H_Link = N_Links['CONSTANT|H']['CONSTANT|E']

N_Links['CONSTANT|H']['CONSTANT|E'] = [1.2,1.2,1.2]

print(N_Links)