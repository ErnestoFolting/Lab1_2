
#25.Дані гіпотенуза і катет прямокутного трикутника. Знайти другий катет цього трикутника
import math
c = float(input('Hypotenuse c = '))
a = float(input('Cathetus a = '))
b = math.sqrt(pow(c, 2) - pow(a, 2))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("%3.2f" % b)
else:
    print("Error")
