import pandas as pd
import numpy as np
""" читаем табличный файл формата csv с помощью pandas"""
data = pd.read_csv('train.csv',  index_col='PassengerId')

"""
Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
"""


def get_number(sex, data = None):

    sexratio= data.value_counts()

    if (sex == 'male'):
        return sexratio['male']
    else:
        return sexratio['female']


def percentage(perc, whole):
    return (perc * 100) / whole

male = get_number('male', data['Sex'])
female = get_number('female', data['Sex'])
total_num = male + female

#print (round(percentage(male, total)), round(percentage(female, total)) )

"""
Посчитайте долю погибших на параходе (число и процент)?
"""
def get_nubmer_of_survived(data = None):
    survived = data.value_counts()
    died_int = survived[0]
    surv_int = survived[1]
    return percentage(surv_int, surv_int+died_int)

data = pd.read_csv('titanic.csv', index_col='PassengerId')

surv_int = get_nubmer_of_survived(data['Survived'])
dead  = total_num - surv_int
print(dead)


"""
#Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
"""

sibsp_arr = data['SibSp']
parch_arr = data['Parch']

pearson_int = np.corrcoef(sibsp_arr, parch_arr)

ages_lst = data['Age'].value_counts().index.tolist()
# print (type(age.value_counts().index.tolist()))
# print(age)

print(np.average(ages_lst))

#print(data.corr())
print((pearson_int[0, 1]))


"""
    Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
"""


"""
  Какие доли составляли пассажиры первого, второго, третьего класса?
"""

classes = data['Pclass'].value_counts()
thirdClass = classes[3]
secondClass = classes[2]
firstClass = classes[1]
totalCount = total_num
def partof(smth, total):
    return smth/total
firstClassPart = firstClass/total_num
secondClassPart = secondClass/total_num
thirdClassPart = partof(thirdClass,totalCount)
#print(classes)
print(pd.DataFrame([{'1st class':firstClass, '2nd class':secondClass, '3rd class':thirdClass},{'1st class':firstClassPart, '2nd class':secondClassPart, '3rd class':thirdClassPart}]))

""" """
""" """
""" """