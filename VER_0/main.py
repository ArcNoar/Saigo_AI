
import pickle # For data saving
from random import randint
from socket import NI_NAMEREQD
import numpy as np

#User_Entry = input()

# Our Goal to reach 100 I score
i_score = 0

STF = 0.9 # SuperVisor Trust Factor (Can we trust supervisor?)
AISC = 0.2 # AI Self Confidence  Can AI create nodes and trust it himself?


# For calculating conductivity!!!
NAS = 0 # Node Activation SUM
NLAS = 0 # Node Link Activation SUM

# If STF is low, we prefer to ask supervisor about trustworthy of information he provides
"""
!!! Two types of node generating, AI Proc, and Supervisor Proc,
 if it info from super, our conductivity and force are scaled to STF,
that's mean it should be higher but not 100%

!!! If it's data that created by AI, 
conductivity and force are unstable and should be tested in practice
"""

# Storage Sector


Recent_Memory = []


# Constant - 1 | Abstract - 0

# Nodes
Node_Base = {
    "DATA" : ["Value","Type"],
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
    "NODE" : {
        "NODE" : ['Correct Activation','Activation Amount'],
    },
    
}


Node_Group = {
    "NG_Name" : {
        "Node" : ['Node_Source','Node_Link'],
    }
}



# Constructing Sector (Only for element first init)

def node_generator(Node_Object='Abstract',NCV=1.0): # Creates Node for new data
    """
        NCV :
            Node Charge Value (Residual perception)
            Should decrease with each successive Node 
        Node_Object - Constant\Abstarct
    """
    faint_Node = False

    if NCV < 0.5:
        faint_Node = True

    if Node_Object == 'Abstract':
        Node_Class = 2
        # Old var, it's not working, i'll remake it later
        Node_Class = f'{Node_Object}|{randint(0,100000)}'
        Node_Base[f'{Node_Class}'] = [0.3] #Temporal Solution

        #Here should be description of what kind of abstraction it
    else:
        if faint_Node == True:
            Node_Class = 0
            Node_Base[f'{Node_Object}'] = [round(NCV,3),Node_Class] 
        else:
            Node_Class = 1
            Node_Base[f'{Node_Object}'] = [round(NCV,3),Node_Class] 
        


#Node Link Formator (Only for first init)
def NL_Formator(Node_A,Node_B,Source='Unknown'):
    global NLAS
    """
    Source = SV(SuperVisor) or AI
    """

    # Amplifier Parameter
    #This parameter affects the link , not the charge of the node
    

    Default_Amp = 0.5

    if Source == 'SV':
        Default_Amp = Default_Amp * (2 * STF)

    elif Source == 'AI':
        Default_Amp = Default_Amp * (2 * AISC)

    else:
        Default_Amp = Default_Amp * 0.5
    
    
    AFN = False # Activating Faint Node

    Root_Node = Node_Base[f'{Node_A}']
    Sup_Node = Node_Base[f'{Node_B}']
    print(Root_Node[0])
    print(Sup_Node[0])


    Extension = False

    if Sup_Node[0] < 0.5:
        AFN = True

    if Node_A in N_Links.keys():
        Extension = True
    
        

    if Root_Node[1] == 1:
        #Init Params for link
        NLAS += 1
        CNLA = 1 #Current Node link Activations
        if Extension == True:
            local_link = N_Links[f'{Node_A}']
            CNLA = len(local_link.keys()) + 1
        

        # First time activation so that's why there is 1
        Conductivity = (CNLA / NLAS) * Default_Amp
        Force = 0

        OF = 0 # Overflow
        
        

        #We taking root node energy to form link to Sup_Node

        Consumed_Energy = Root_Node[0] * 0.25


        if AFN == True:
            Consumed_Energy += (0.50 - Sup_Node[0])

        Root_Node[0] -= Consumed_Energy
        print(Root_Node[0])
        if Root_Node[0] < 0.5:
            print('Not enough charge to form link')
            Root_Node[0] += round(Consumed_Energy * 0.9,3) # Returning charge
        
        else:
            
            print(Consumed_Energy * Conductivity)
            
            
            Sup_Node[0] += Consumed_Energy * Conductivity # Energy Loss
            
            if Sup_Node[0] > 0.5:

                
                if AFN == True:
                    print(f'Node - ({Node_B}) gained constant status during link forming ')
                    Sup_Node[1] = 1
                if Sup_Node[0] > 1.0:
                    OF += Sup_Node[0] - 1.0
                    Sup_Node[0] -= OF
                Force += OF # OverFlow converts to Force
                if Extension == False:
                    N_Links[f'{Node_A}'] = {
                        f"{Node_B}" : [round(Conductivity,3),round(Force,3)]
                        }
                else:
                    
                    print(CNLA)
                    local_link[f'{Node_B}'] = [round(Conductivity,3),round(Force,3)]

                print(Sup_Node[0])
                print(f"Link formed Succesfully")
            else:
                Sup_Node[0] -= Consumed_Energy
                Root_Node[0] += round(Consumed_Energy * 0.9,3)

                print('Link forming failed, maybe initial conductivity is not good enough ')



    elif Root_Node[1] == 2:
        print('We met abstraction')

    else:
        print("We can't form a link from faint Node")














    


    
# Action Sector

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
    global NAS

    Temporal_Proc = [] 

    NCV = 1.0

    Our_Entry = Entry
    #NG - Node Group



    for i in Our_Entry:
        NAS += 1
        if len(Temporal_Proc) != 0: # NCV Decrease
            NCV = round(NCV / 1.2,3)

        
        if Our_Entry not in Recent_Memory:
            if i not in Node_Base.keys():
                node_generator(Node_Object=i,NCV=NCV)

            else:
                local_node = Node_Base[f'{i}']
                local_node[0] += round((local_node[0] * 0.1),2) 


        
        

        Temporal_Proc.append(i)

    print(f'\n TP : {Temporal_Proc} \n')     

    # Link proccessing (Temporal)

    for i in range(len(Temporal_Proc) - 1):
        #print(Temporal_Proc)
        if i != len(Temporal_Proc) - 1:
            NL_Formator(Temporal_Proc[i],Temporal_Proc[i + 1],Source='SV')

            

        



    Recent_Memory.append(Our_Entry)

Entry_Proccesing('Hello')  
    
#print(NAS)
print(f' NB : {Node_Base} \n')
print(f' N_Links : {N_Links} \n')
    

