from datetime import datetime, timedelta

def diferenca_entre_datas(data_inicial, data_final, unidade):
    delta = data_final - data_inicial
    
    if unidade == "dias":
        return delta.days
    elif unidade == "horas":
        return delta.days * 24 + delta.seconds // 3600
    elif unidade == "minutos":
        return delta.days * 24 * 60 + delta.seconds // 60
    elif unidade == "segundos":
        return delta.days * 24 * 60 * 60 + delta.seconds
    elif unidade == "meses":
        return delta.days // 30  
    elif unidade == "anos":
        return delta.days // 365  
    else:
        raise ValueError("A unidade não esta sendo reconhecida.")
