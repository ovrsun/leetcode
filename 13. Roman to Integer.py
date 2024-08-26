class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        if s in roman_to_int:
            return roman_to_int[s]
        
        res = 0
        # идея 1: сделать массив из чисел и потом пройти по нему суммируя по правилам
        # II = [1, 1]
        # IV = [1, 5], IX = [1, 9]
        # VI = [5, 1] XI = []
        
        # идея 2: в зависимости от размера римского числа сделать массив
        # (по условию на входе – римское число [1; 4000) (включительно по 3999)
        # starts with I, V -> это числа от 1 до 9
        # starts with X or L -> 10, 20, 30, 40 (XL), 50 (L), 60, 70, 80, 90 (XC)
        # starts with C or D -> 100 (C), 400 (CD), 500 (D), CM (900)
        # starts with M -> 1000 (M)
        # то есть возможна размерность массива от 1 до 4
        # для каждого из этих разрядов можно попробовать посчитать по отдельности
        # MCMXCIV: начинается с M, значит тысячи
        # [1000] [1000, 100] [100, 10] [5, 1]
        # LVIII: начинается с L, значит десятки
        # [50] [1, 1, 1, 5]
        # [1, 1, 1, 5, 50] -> 3+5+50 -> 58
        # кажется, что если заполнять разрядные массивы с конца, то потом
        # можно посчитать разряд: если первое число больше, чем последующие
        # то вычитаем, если меньше - суммируем
        # можно ли то же самое сделать с одним массивом?
        # MCMXCIV [5, 1, 100, 10, 1000, 100, 1000] -> 5 - 1 + 100 - 10 + 1000 - 100 + 1000
        # кажется да: если следующее число меньше текущего, то вычитаем его, иначе - суммируем
        # 
        # 3888. Оно записывается как MMMDCCCLXXXVIII и состоит из 15 символов. - самое длинное
        # это нужно чтобы сразу создать массив и не аппендить потом к нему новые числа
        # идем пока не закончится или пока значение не ноль

        # arr = [0] * len('MMMDCCCLXXXVIII')
        # n = len(s) - 1
        # i = 0
        # while n - i >= 0:
        #     arr[i] = roman_to_int[s[n-i]]
        #     i += 1
        # res = arr[0]
        # i = 1
        # while i < len(arr) and arr[i] != 0:
        #     if arr[i] < arr[i-1]:
        #         res -= arr[i]
        #     else:
        #         res += arr[i]
        #     i += 1
        # return res

        # попробуем оптимизировать без использования доп массива
        i = len(s) - 2
        res = roman_to_int[s[-1]]
        while i >= 0:
            if roman_to_int[s[i+1]] > roman_to_int[s[i]]:
                res -= roman_to_int[s[i]]
            else:
                res += roman_to_int[s[i]]
            i -= 1
        return res

        
# sln = Solution()
# print(sln.romanToInt('IX'))

sln = Solution()
assert sln.romanToInt('I') == 1
assert sln.romanToInt('V') == 5
assert sln.romanToInt('X') == 10
assert sln.romanToInt('L') == 50
assert sln.romanToInt('C') == 100
assert sln.romanToInt('D') == 500
assert sln.romanToInt('M') == 1000

assert sln.romanToInt('II') == 2
assert sln.romanToInt('III') == 3
assert sln.romanToInt('IV') == 4
assert sln.romanToInt('VI') == 6
assert sln.romanToInt('IX') == 9
assert sln.romanToInt('LVIII') == 58
