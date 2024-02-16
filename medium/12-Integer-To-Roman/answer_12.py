class Solution:
    def intToRoman(self, num: int) -> str:
        
        rules = {
            1: "I",
            4: "IV",
            5: "V", 
            9: "IX",   
            10: "X",   
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",  
            400: "CD", 
            500: "D",  
            900: "CM",
            1000: "M"
        }

        roman = ''

        numbers = [num for num in rules]

        for n in reversed(numbers):
            while n <= num:
                roman += rules[n]
                num -= n
        
        return roman