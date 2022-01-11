#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

sum_leng_songs = 0
sum_leng_songs += violator_songs_list[3][1]
sum_leng_songs += violator_songs_list[5][1]
sum_leng_songs += violator_songs_list[-1][1]
sum_leng_songs = round(sum_leng_songs,3)

print('Summary sound length of 3 songs', sum_leng_songs, 'min')


# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

#Суммирование указанных трех песен в словаре
dict_len = 0
dict_len += violator_songs_dict.get('Sweetest Perfection')
dict_len += violator_songs_dict.get('Policy of Truth')
dict_len += violator_songs_dict.get('Blue Dress')
dict_len = round(dict_len,3)

#Суммирование оставшихся песен в словаре
dict_len_last = 0
dict_len_last += violator_songs_dict.get('World in My Eyes')
dict_len_last += violator_songs_dict.get('Personal Jesus')
dict_len_last += violator_songs_dict.get('Waiting for the Night')
dict_len_last = round(dict_len_last,3)

print('Summ len of 3 songs is ',dict_len,'min.', 'And last 3 is', dict_len_last, 'min.')