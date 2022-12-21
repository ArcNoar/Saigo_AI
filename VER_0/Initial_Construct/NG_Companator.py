


def NG_Companator(GN,GNCL,NS,NLS,NGS,Status = 'COMPLETE',Act_Amount=1,Distribution=0,NGX=0.0,NGY=0.0,NGZ=0.0):
    """
    GN = Group Name (Example : Entry - Hello => GN - Hello;) In constant cases
    GNCL = GN Construct list
    Act_Amount = Number of Activations (Default = 1 (Init activation))
    Distribution = Amount of clusters that contain this group (Default = 0 (Initial))
    NGX = Node_group X Cord (By default it's 0)
    NGY = Node_group X Cord (By default it's 0)
    NGZ = Node_group X Cord (By default it's 0)
    """

    if GN.upper() not in NGS.keys():

        NGS[f'{GN.upper()}'] = {}

        Initial_Forming = NGS[f'{GN.upper()}'] # Group Init in storage
        print(GNCL)
        for i in range(len(GNCL)):
            try:
                if i != len(GNCL) - 1:
                    Data_Filling = [
                        
                         NS[f'{GNCL[i]}'],
                         NLS[f'{GNCL[i]}'][f'{GNCL[i + 1]}']
                        ]

                else: # For last element in group
                    #print('We are here')
                    Data_Filling = [
                        
                         NS[f'{GNCL[i]}'],
                         0
                        ]
                        
                    
                if GNCL[i] not in Initial_Forming.keys():
                    Initial_Forming[f'{GNCL[i]}'] = Data_Filling # Filling data in group
                        
                else:
                    Initial_Forming[f'{GNCL[i]}_2'] = Data_Filling #Double Case
            except Exception as _ex:
                print('Link not accessed, or not formed. Creating Broken Group')
                Act_Amount = 0
                Status = 'BROKEN'
                
        #Group Params
        Initial_Forming['GP'] = [Status,Act_Amount,Distribution,[NGX,NGY,NGZ]] 