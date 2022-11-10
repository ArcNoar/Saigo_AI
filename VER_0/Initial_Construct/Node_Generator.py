
from random import randint

class Node_Manager():
    def __init__(self,NS,NCV,TP):
        self.NB = NS
        self.NCV = NCV
        self.TP = TP
        


    def node_generator(self,Node_Object='Abstract'): # Creates Node for new data
        """
            NB = Node_Base
            NCV :
                Node Charge Value 
                Should decrease with each successive Node 
            Node_Object - Constant\Abstarct
        """
        
        
    
        faint_Node = False
    
        if self.NCV < 0.5:
            faint_Node = True
    
        if Node_Object == 'Abstract':
            Node_Class = 2
            # Old var, it's not working, i'll remake it later
            Node_Class = f'{Node_Object}|{randint(0,100000)}'
            self.NB[f'{Node_Class}'] = [0.3] #Temporal Solution
    
            #Here should be description of what kind of abstraction it
        else:
            # [Charge,Class,Act_Amount]
    
            if faint_Node == True:
                Node_Class = 0
                self.NB[f'{Node_Object}'] = [round(self.NCV,3),Node_Class,1] 
            else:
                Node_Class = 1
                self.NB[f'{Node_Object}'] = [round(self.NCV,3),Node_Class,1] 


    def Node_Proc(self):
        for i in self.TP:
            if self.TP.index(i) != 0:
                self.NCV = round(self.NCV / 1.2,3)


            if i not in self.NB.keys():
                self.node_generator(Node_Object=i)
            else:
                local_node = self.NB[f'{i}']
                local_node[0] += round((local_node[0] * 0.1),2)
                local_node[2] += 1
            
