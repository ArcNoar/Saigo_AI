
import pickle # For data saving
from random import randint


#User_Entry = input()

# Our Goal to reach 100 I score
i_score = 0

Supervisor_TF = 1 # Trust Factor (Can we trust supervisor?)

Node_Activation_SUM = 0 # For calculating conductivity!!!

# If STF is low, we prefer to ask supervisor about trustworthy of information he provides
"""
!!! Two types of node generating, AI Proc, and Supervisor Proc,
 if it info from super, our conductivity and force are scaled to STF,
that's mean it should be higher but not 100%

!!! If it's data that created by AI, 
conductivity and force are unstable and should be tested in practice
"""

Recent_Memory = []


# Nodes
Node_Base = {
    "DATA - Type" : ["Value"],
}

#Only Node Data (For Comparing)
NB_Nav = {
    "Constant_Nodes" : [],
    "Abstract_Nodes" : [],
}

# Node Links
"""
Node_A : {
    Variations of Node_B
    'Node_B' : [Params],
    'Node_B' : [Params],
    'Node_B' : [Params],
}
"""
N_Links = {
    "TYPE|NODE" : {
        "TYPE|NODE" : ['Correct Activation','Activation Amount'],
    },
    
}


Node_Group = {
    "NG_Name" : {
        "Node" : ['Node_Source','Node_Link'],
    }
}



# Functional Sector

def node_generator(Node_Object='Abstract',NCV=1.0): # Creates Node for new data
    """
    NCV :
        Node Charge Value (Residual perception)
        Should decrease with each successive Node 
    Node_Object - Constant\Abstarct
    """
    


    Node_Class = 'Unknown'

    if Node_Object == 'Abstract':
        Node_Class = f'{Node_Object}|{randint(0,100000)}'
        Node_Base[f'{Node_Class}'] = [0.3] #Temporal Solution

        #Here should be description of what kind of abstraction it
    else:
        Node_Class = f'{Node_Object} : Constant'
        

        Node_Base[f'{Node_Class}|{len(Node_Base) }'] = [NCV] 
        NB_Nav['Constant_Nodes'].append(Node_Object)

def Link_Welder(Source='SV',Node_A,Node_B):
    """
    Source = SV(SuperVisor\User) | AI
    """
    


    


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



# Entry Sector




Temporal_Proc = [] # Iteration temporal proc

def Entry_Proccesing(Entry):
    Temporal_Proc = [] 

    NCV = 1.0

    Our_Entry = Entry
    #NG - Node Group



    for i in Our_Entry:
        
        if len(Temporal_Proc) != 0: # NCV Decrease
            NCV = round(NCV / 1.5,3)

        
        if Our_Entry not in Recent_Memory:
            if i not in NB_Nav['Constant_Nodes']:
    
                node_generator(Node_Object=i,NCV=NCV)
        
        

        Temporal_Proc.append(i)

    print(f'\n TP : {Temporal_Proc} \n')     

    Recent_Memory.append(Our_Entry)

Entry_Proccesing('Hello')  
    

print(f' NB : {Node_Base} \n')
    

