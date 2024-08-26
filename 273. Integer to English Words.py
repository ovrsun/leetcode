# https://leetcode.com/problems/integer-to-english-words


class Solution:
    def numberToWords(self, num):
        nums_to_words = {
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen",
            "20": "Twenty",
            "30": "Thirty",
            "40": "Forty",
            "50": "Fifty",
            "60": "Sixty",
            "70": "Seventy",
            "80": "Eighty",
            "90": "Ninety",
        }

        str_num = str(num).rjust(12, "0")
        # print(str_num)
        # for rank in str_num[0::3]:
        digits = {
            "Billion": "",
            "Million": "",
            "Thousand": "",
            "Hundred": "",
        }

        i = 0
        for k in digits:
            digits[k] = str_num[i : i + 3]
            # print(i)
            i += 3
        # print(digits)
        # digits['Hundred'] = str(num).rjust(3, '0')
        res = ""
        for k, v in digits.items():
            if v != "000":

                if v[0] == "0":
                    ...
                else:
                    res += f"{nums_to_words[v[0]]} Hundred "
                if v[1:].lstrip("0") in nums_to_words:
                    res += nums_to_words[v[1:].lstrip("0")] + " "
                elif v[1:] == "00":
                    ...
                else:
                    res += f'{nums_to_words[v[1]+"0"]} {nums_to_words[v[2]]} '
                if k != "Hundred":
                    res += k + " "

        return res.strip()


sln = Solution()
assert (res := sln.numberToWords(123)) == "Thirteen", res
# assert (res := sln.numberToWords(13)) == 'Thirteen', res
# assert (res := sln.numberToWords(25)) == 'Twenty Five', res
# assert (res := sln.numberToWords(52)) == 'Fifty Two', res
# assert (res := sln.numberToWords(152)) == 'One Hundred Fifty Two', res
# assert (res := sln.numberToWords(101)) == 'One Hundred One', res
# assert (res := sln.numberToWords(201)) == 'Two Hundred One', res
# assert (res := sln.numberToWords(990)) == 'Nine Hundred Ninety', res
# assert (res := sln.numberToWords(999)) == 'Nine Hundred Ninety Nine', res
# assert (res := sln.numberToWords(900)) == 'Nine Hundred', res
# assert (res := sln.numberToWords(800)) == 'Eight Hundred', res
# assert (res := sln.numberToWords(1800)) == 'One Thousand Eight Hundred', res
# assert ((res := sln.numberToWords(100800)) == "Oƒne Hundred Thousand Eight Hundred", res)
# assert (res := sln.numberToWords(1000000)) == 'One Hundred Thousand Eight Hundred', res

print("end")
