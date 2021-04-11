from datetime import date

band = {
    'members':{
        'Elton':{
            'role': 'singer',
            'date': date(1994, 6, 3)
        },
        'Omar':{
            'role': 'singer',
            'date': date(1986, 7, 12)
        },
        'Kali':{
            'role': 'hip-hop singer',
            'date': date(1992, 5, 25)
        }
    },
    'concerts':{
        'Moscow':{
            'concert_date': date(2021, 5, 28),
            'income': 50000,
            'expenses': [5000, 10000, 2000]
        },
        'SPB':{
            'concert_date': date(2021, 5, 28),
            'income': 50000,
            'expenses': [1000, 5000, 7000]
        },
        'Sweden':{
            'concert_date': date(2021, 7, 28),
            'income': 80000,
            'expenses': [6000, 20000, 7000]
        },
        'Kanada':{
            'concert_date': date(2021, 8, 28),
            'income': 50000,
            'expenses': [7000, 40000, 8000]
        },
        'Chicago':{
            'concert_date': date(2021, 9, 28),
            'income': 90000,
            'expenses': [9000, 30000, 7000]
        }
    }
}


# def func_add(band, **kwargs):
#     band['members'].update(kwargs)
#     return band
# new_member = {'Rita Ora': {'role': 'singer', 'date': date(1985, 3, 12)}}
# print(func_add(band, **new_member))




# def func_del(band, name):
#     band['members'].pop(name)
#     return band
# func_del(band, 'Omar')
# print(band)




# def func_add_conc(band, **kwargs):
#     band['concerts'].update(kwargs)
#     return band
# func_add_conc(band, **{'London':{
#             'concert_date': date(2021, 9, 28),
#             'income': 90000,
#             'expenses': [9000, 30000, 7000]
#         }})    
# print(band)





# def func_expenses(exp):
#     c = 0
#     for i in exp:
#         i += i
#     return i
# print(func_expenses(band['concerts']['SPB']['expenses']))        




# def func_calculate(*args):
#     return sum(args)

# def func_conc(band, concert_name):
#     income = band['concerts'][concert_name]['income']
#     return income - func_calculate(*band['concerts'][concert_name]['expenses'])
# print(func_conc(band, 'SPB'))    





# total_sum = 0
# for concert in band['concerts']:
#     x = band['concerts'][concert]['expenses']
#     total_sum += sum(x)
# print(total_sum)