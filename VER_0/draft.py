
from dataclasses import dataclass
import numpy as np

import time 

total_charge = 100

total_activations = 229

#start_time = time.time() # TIMER


#time.sleep(1.5)
Node_Base = {
    'CONSTANT|H' : [35],
    'CONSTANT|E' : [83],
    'CONSTANT|L' : [44],
    'CONSTANT|O' : [67],

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



#Simulation___





#print(1**0.9)


#print(Node_Base['CONSTANT|H'])
