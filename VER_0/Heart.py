import pickle

#File to score emotions and feelings

# ���������� ������.
    # ����� :
    """
        1 Horror = ����
        2 Anxiety =  = �������
        3 Concern = ������������
        4 Astonishment =  ���������
        5 Confusion = ��������������
        6 Timidity = �������
        7 Guilt = ����
        8 Embarrassment = ��������
        9 Doubt = ��������
     """
    horror = 0.0
    anxiety = 0.0
    concern = 0.0
    astonishment = 0.0
    confusion = 0.0
    timidity = 0.0
    guilt = 0.0
    embarrassment = 0.0
    doubt = 0.0

    
    #���� :
    """
        1 Rage = ������
        2 Irritation = �����������
        3 Resentment = �����
        4 Disgust = ����������\�������������
        5 Jealousy = ��������
        6 Envy = �������
        7 Indignation = �����������/����������
        8 Nervousness = �����������
        9 Disappointment = �������������
    """
    rage = 0.0
    irritation = 0.0
    resentment = 0.0
    disgust = 0.0
    jealousy = 0.0
    envy = 0.0
    indignation = 0.0
    nervousness = 0.0
    disappointment = 0.0


    #������:
    """
        1 Idleness = ����
        2 Despait = ��������
        3 Compassion = �������
        4 Loneliness = ������������/�����������
        5 Helplessness = �������������
        6 Aloofness = �������������
        7 Regret = ���������
        8 Boredom = �����
        9 Sadness = ������
    """
    idleness = 0.0
    despait = 0.0
    compassion = 0.0
    loneliness = 0.0
    helplessness = 0.0
    aloofness = 0.0
    regret = 0.0
    boredom = 0.0
    sadness = 0.0

    #������� :
    """
        1 Happiness = �������
        2 Delight =  �������
        3 Interest = �������
        4 Excitement = �����������
        5 Curiosity = �����������
        6 Confidence = �����������
        7 Horny = �����������(�����)
        8 Laugh = ����
        9 Satisfaction = ��������������
    """
    happiness = 0.0
    delight = 0.0
    interest = 0.0
    excitement = 0.0
    curiosity = 0.0
    confidence = 0.0
    horny = 0.0
    laugh = 0.0
    satisfaction = 0.0