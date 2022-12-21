
#Storage Imports

from VER_0.Data_Proc.Storage_Elements import Node_Base
from VER_0.Data_Proc.Storage_Elements import N_Links
from VER_0.Data_Proc.Storage_Elements import Node_Group

# Count Elements
from VER_0.Data_Proc.Counting_Elements import NAS
from VER_0.Data_Proc.Counting_Elements import NLAS

# Proc Imports

from VER_0.Proc_Modules.Synapsis_Forming import Entry_Reciever


#Start Module


Recent_Memory = [] # Recent Memory

#Parameters
NCV = 1.0 # Energy Amount

STF = 0.9 # SuperVisor Trust Factor (Can we trust supervisor?)
AISC = 0.2 # AI Self Confidence  Can AI create nodes and trust it himself?


# Init Classes

ER = Entry_Reciever(NCV,Recent_Memory,STF,AISC,NLAS,NAS,Node_Base,N_Links,Node_Group)
#print(Recent_Memory)

#PM.Entry_Proc('Hello')

ER.Synapse_Forming('Good Morning!')


"""
Дополнение \ Изменение \ Удаление групп Нодов, в гибернационном режиме

Гибернациооный режим - Симмуляция передачи информации в гиппокамп.

Значит Энтри процесс не трогаем, занимаемся тем чтобы отловить ошибки.

Нужно позволить ей сформировать неполную группу

Об корректности и сути не думай. Параметры просто игнорируй.

Нам нужно только то что касается формы.

Для того чтобы дать суть, должен быть сосуд


Крч, мы все таки откажемся от игнорирования пробелов и разделения, потому что хз.

Не соответствует это как то моему концепту текста.

Хотя нет, пусть будет, мы наверное просто потом таким образом кластеры формировать будем.

Тип будем проверять на наличие одиночных групп, которые содержатся в этой группе, и таким образом
будем делать разделение, и одновременно формировать кластер (Ну или группу групп)

Поскольку эти 2 фигурировали вместе
так и корды менять будем я думаю.

по сути действительно у нас генерируются только ноды, линки и нод группы, все остальное это
составные части из этих компонент.

____________

Предсказывать продолжение? Механизм предсказания?


"""


print(Recent_Memory)
print(Node_Base)
print(N_Links)
print(Node_Group)













    

