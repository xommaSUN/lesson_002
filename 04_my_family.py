#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mom','dad','brother']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Natasha',164], ['Yura',180], ['Sasha',185]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print('Height:', my_family[1],'-',my_family_height[1][1],'cm')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

sum_family_height = 0
sum_family_height += my_family_height[0][1]
sum_family_height += my_family_height[1][1]
sum_family_height += my_family_height[2][1]

print('Summary height of my family is -', sum_family_height,' cm')