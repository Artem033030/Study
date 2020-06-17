# ae = ("В Україні зафіксовано 2203 випадків коронавірусноїхвороби Covid-19 ")
# ar = ("У медічніз закладах наразі перебуває 923 особи (з них 42 дитини)")
# art = ("На апараті штучної вентиляцї легень - 83 особи")
# arte = ("За добу одужало 16 осіб (з них 3 дитини та 1 медсестра померло 12 осіб)")
# artem = ("В місти києві (548)")
# print("Hello, this is Coronavirus Ukraine bot")
# print("----------------------------")
# print("Здраствуйте вас приветствует украиский коронавирус бот Covid-19")
# print("----------------------------")
# print("Если вы хотите посмотреть зафиксирывание случаи напишыте : 1  если в киеве то : 2 если на апарате вентиляцыи легких то: 3")
# a = input("Введите запрос: ")
# if a == '1':
#     print(a)
# if a == '2':
#     print(artem)
# if a == '3':
#     print(art)
# print("-----------------------------------------------")
import urllib.request
import json         

# url = 'https://api.covid19api.com/summary' 
# with urllib.request.urlopen(url) as respouns:
#     data = respouns.read()
#     dict_data = json.loads(data)
# countries = dict_data["Countries"]
# ukraine = countries[234] 
# amerika = countries[235]
# awer = countries[130]
# print("если хотите посмотреть статистику  украины напишыте:3 если арабскіе емірати то:2")
# a = input("Введитете число: ")
# if a == '3':
#     print(ukraine)
# elif a == '2':
#     print(amerika)
# elif a == '1':
#     print(awer)
# else:
#     print("нечем немогу помочь")
# # print(dict_data)
# # print(dict_data)



# url = 'https://api.covid19api.com/country/ukraine'
# with urllib.request.urlopen(url) as respouns:
#     data = respouns.read()
#     dict_data = json.loads(data)
# # for country in dict_data['Countries']:
# #     if country['CountryCode'] == 'UA':
# #        print(country)
# print(dict_data['Countries'])
# last_data = dict_data[-1]
# print(a)
# confirmed = str(last_data['Confirmed'])
# deaths = str(last_data['Deaths'])
# print("------------------------------")
# print('Заболевшых: '+confirmed)
# print("------------------------------")
# print("Смертей: "+confirmed)
# print("------------------------------")
# print(dict_data)
import urllib.request
import json

url = 'https://api.covid19api.com/country/ukraine'

with urllib.request.urlopen(url) as respouns:
    data = respouns.read()
    dict_data = json.loads(data)
cite = dict_data['CityCode'['Kyiv']]
print(cite)

# import urllib.request
# import json

# url = 'https://api.covid19api.com/summary' 

# with urllib.request.urlopen(url) as response:
#     data = response.read()
#     corona = json.loads(data)
# global1 = corona['Global']
# world_confirmed = str(ert['TotalConfirmed'])
# b22 = str(ert['TotalDeaths'])
# print('В мире')
# print('Заболевшых: '+a11)
# print("Смертей: "+b22)






