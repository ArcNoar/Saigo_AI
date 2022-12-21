

from VER_0.Initial_Construct.Node_Generator import Node_Manager
from VER_0.Initial_Construct.NLink_Former import NL_Manager
from VER_0.Initial_Construct.NG_Companator import NG_Companator


class Entry_Reciever():
    """
    NCV - Node Charge Val
    RM - Recent Memory
    STF - SuperVisor Trust Factor
    AISC - AI Self Confidence

    NLAS - Node Link Activation Counter
    NAS - Node Activation Counter
    NS - Node Storage
    NLS - Node Link Storage
    NGS - Node Group Storage
    """


    def __init__(self, NCV ,RM,STF,AISC, NLAS , NAS, NS,NLS,NGS):


        self.NCV = NCV 
        self.RM = RM
        self.STF = STF
        self.AISC = AISC

        self.NLAS = NLAS
        self.NAS = NAS 
        self.NS = NS
        self.NLS = NLS
        self.NGS = NGS



    def Synapse_Forming(self,Entry):
        
        if Entry not in self.RM: # Check for recent cases

            Temporal_Proc = list(Entry) # Local temporal proc memory
            print(f'TP : {Temporal_Proc}')

            NM = Node_Manager(self.NS,self.NCV,Temporal_Proc)
            NM.Node_Proc()


            print(self.NS)
            NLM = NL_Manager(Temporal_Proc,self.NS,self.NLS,self.STF,self.AISC,self.NLAS,SRC='SV')
            NLM.Link_Proc()

            print(self.NLS)
            
            NG_Companator(Entry,Temporal_Proc,self.NS,self.NLS,self.NGS)

           

            self.RM.append(Entry)

        else:
            pass

            