geelkaas = input('is de kaas geel? : ')

if geelkaas == 'ja':
    gaten = input('zitten gaten in? : ')
    if gaten == 'ja':
        duur = input('is de kaas belachelijk duur?? : ')
        if duur == 'ja':
            print('de kaas die jij in je gedachten hebt is Emmenthaller!! ')
        else:
            print('de kaas die jij in je gedachten hebt is Leerdammer!!! ')
    else:
        hard = input('Is de kaas hard als een steen? : ')
        if hard == 'ja':
            print('Pammigiano Reggiano')
        else:
            print('Goudse Kaas')
else:
    schimmel = input('heeft de kaas schimmels? : ') 
    if schimmel == 'ja':
        korst = input('heeft de kaas een korst? : ')
        if korst == 'ja':
            print('de kaas die jij in je gedachten hebt is blue de rochbaron!!! : ') 
        else: 
            print("de kaas die jij in je gedachten hebt is founme d'Ambert")
    else: 
        korst2 = input('heeft de kaas een korst? : ')
        if korst2 == 'ja':
            print(' de kaas die jij in je gedachten hebt is Chamembert!!!')
        else:
            print('de kaas die jij in je gedachten hebt is mozzarella')
