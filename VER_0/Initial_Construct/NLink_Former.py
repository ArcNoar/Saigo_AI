
class NL_Manager():
    def __init__(self,TP,NS,NLS,STF,AISC,NLAS, SRC='Unknown'):

        self.Node_Base = NS
        self.N_Links = NLS

        self.TP = TP
        self.STF = STF
        self.AISC = AISC
        self.NLAS = NLAS
        self.Source = SRC


    def NL_Formator(self,Node_A,Node_B):

        #Don't call it manually!!!
    
        # Amplifier Parameter
        #This parameter affects the link , not the charge of the node
        
    
        Default_Amp = 0.5
    
        if self.Source == 'SV':
            Default_Amp = Default_Amp * (2 * self.STF)
    
        elif self.Source == 'AI':
            Default_Amp = Default_Amp * (2 * self.AISC)
    
        else:
            Default_Amp = Default_Amp * 0.5
        
        
        AFN = False # Activating Faint Node
        #print(self.Node_Base)

        Root_Node = self.Node_Base[f'{Node_A}']
        Sup_Node = self.Node_Base[f'{Node_B}']
        #print(Root_Node[0])
        #print(Sup_Node[0])
    
    
        Extension = False
        Enforcing = False
    
        if Sup_Node[0] < 0.5:
            AFN = True
    
        if Node_A in self.N_Links.keys():
    
            local_link = self.N_Links[f'{Node_A}']
            if Node_B not in local_link.keys():
    
                Extension = True
            else:
                Enforcing = True
        
    
          
            
        if Root_Node[1] == 1 and Enforcing != True:
            #Init Params for link
            self.NLAS += 1
            CNLA = 1 #Current Node link Activations
            if Extension == True:
                
                CNLA += len(local_link.keys()) + 1
            
    
            # First time activation so that's why there is 1
            Conductivity = (CNLA / self.NLAS) * Default_Amp
            Force = 0
    
            OF = 0 # Overflow
            
            
    
            #We taking root node energy to form link to Sup_Node
    
            Consumed_Energy = Root_Node[0] * 0.25
    
    
            if AFN == True:
                Consumed_Energy += (0.50 - Sup_Node[0])
    
            Root_Node[0] -= Consumed_Energy
            #print(Root_Node[0])
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
                        self.N_Links[f'{Node_A}'] = {
                            f"{Node_B}" : [round(Conductivity,3),round(Force,3),CNLA]
                            }
                    else:
                        
                        #print(CNLA)
                        local_link[f'{Node_B}'] = [round(Conductivity,3),round(Force,3),CNLA]
    
                    #print(Sup_Node[0])
                    print(f"Link formed Succesfully")
                else:
                    Sup_Node[0] -= Consumed_Energy
                    Root_Node[0] += round(Consumed_Energy * 0.9,3)
    
                    print('Link forming failed, maybe initial conductivity is not good enough ')
    
    
    
        elif Root_Node[1] == 2:
            print('We met abstraction')
    
        elif Enforcing == True:
            print('We already have that kind of links')
    
        else:
            print("We can't form a link from faint Node")



    def Link_Proc(self):

        for i in range(len(self.TP) - 1):
            if i != len(self.TP) - 1:
                self.NL_Formator(self.TP[i],self.TP[i + 1])

                
                