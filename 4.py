from datetime import *

try:
    print('Введите дату отправления в виде ДД/ММ/ГГ')
    data = datetime.strptime(input(), '%d/%m/%Y')
except:
    exit()
data_days = data + timedelta(10000, 0)
data_mins = data + timedelta(seconds=60000000)
data_secs = data + timedelta(seconds=1000000000)
print(data_days)
print(data_mins)
print(data_secs)
