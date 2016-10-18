import pandas as pd
import pandasql as pdsql


filename = 'weather_underground.csv'

def num_rainy_days(f_name):
    weather_data = pd.read_csv('./data/' + f_name)
    
    q = """
    SELECT count(*)
    FROM weather_data wd
    WHERE wd.rain == 1
    """
    
    rainy_days = pdsql.sqldf(q.lower(), locals())
    
    return rainy_days

print(num_rainy_days(filename))




