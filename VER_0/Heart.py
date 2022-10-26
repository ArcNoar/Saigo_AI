import pickle

#File to score emotions and feelings

# Компоненты Чувств.
    # СТРАХ :
    """
        1 Horror = Ужас
        2 Anxiety =  = Тревога
        3 Concern = Беспокойство
        4 Astonishment =  Удивление
        5 Confusion = Замешательство
        6 Timidity = Робость
        7 Guilt = Вина
        8 Embarrassment = Смущение
        9 Doubt = Сомнение
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

    
    #ГНЕВ :
    """
        1 Rage = Ярость
        2 Irritation = Раздражение
        3 Resentment = Обида
        4 Disgust = Отвращение\Презрительное
        5 Jealousy = Ревность
        6 Envy = Зависть
        7 Indignation = Негодование/Возмущение
        8 Nervousness = Нервозность
        9 Disappointment = Разочарование
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


    #ГРУСТЬ:
    """
        1 Idleness = Лень
        2 Despait = Отчаяние
        3 Compassion = Жалость
        4 Loneliness = Отрешенность/Одиночество
        5 Helplessness = Беспомощность
        6 Aloofness = Отчужденность
        7 Regret = Сожаление
        8 Boredom = Скука
        9 Sadness = Печаль
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

    #РАДОСТЬ :
    """
        1 Happiness = Счастье
        2 Delight =  Восторг
        3 Interest = Интерес
        4 Excitement = Возбуждение
        5 Curiosity = Любопытство
        6 Confidence = Уверенность
        7 Horny = Возбуждение(хорни)
        8 Laugh = Смех
        9 Satisfaction = Удовлетворение
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