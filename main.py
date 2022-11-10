
#Storage Imports

from VER_0.Data_Proc.Storage_Elements import Node_Base
from VER_0.Data_Proc.Storage_Elements import N_Links
from VER_0.Data_Proc.Storage_Elements import Node_Group

# Count Elements
from VER_0.Data_Proc.Counting_Elements import NAS
from VER_0.Data_Proc.Counting_Elements import NLAS

# Proc Imports

from VER_0.Proc_Modules.Entry_Proc import Proc_Manager

#Start Module



Recent_Memory = [] # Recent Memory

#Parameters
NCV = 1.0 # Energy Amount

STF = 0.9 # SuperVisor Trust Factor (Can we trust supervisor?)
AISC = 0.2 # AI Self Confidence  Can AI create nodes and trust it himself?


# Init Classes

PM = Proc_Manager(NCV,Recent_Memory,STF,AISC,NLAS,NAS,Node_Base,N_Links,Node_Group)
print(Recent_Memory)

PM.Entry_Proc('Hello')

print(Recent_Memory)
print(Node_Base)
print(N_Links)
print(Node_Group)













    

