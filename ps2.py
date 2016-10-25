import pandas as pd
import pandasql as pdsql


filename = 'weather_underground.csv'

def num_rainy_days(f_name):
    weather_data = pd.read_csv('./data/' + f_name)
    
    q = """
    SELECT count(*)
    FROM weather_data wd
    WHERE wd.rain == 1;
    """
    
    rainy_days = pdsql.sqldf(q.lower(), locals())
    
    return rainy_days

print(num_rainy_days(filename))


def avg_weekend_temperature(f_name):
    weather_data = pd.read_csv('./data/' + f_name)
    
    q = """
    SELECT cast(strftime('%w', date) as integer), AVG(meantempi)
    FROM weather_data
    WHERE cast(strftime('%w', date) as integer) == 0 OR cast(strftime('%w', date) as integer) == 6
    GROUP BY cast(strftime('%w', date) as integer)
    """
    
    mean_temp_weekends = pdsql.sqldf(q.lower(), locals())
    
    return mean_temp_weekends

    
print(avg_weekend_temperature(filename))



