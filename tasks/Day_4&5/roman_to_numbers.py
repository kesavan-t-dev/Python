"""
Write a function that function usage is convert roman_charaters to integer (1 method)
"""

#Method_1
try:
    def roman_to_int(s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        n = len(s)
        # print(s,"S ")
        # print(n,"N LEN OF S")
        while i < n:
            if i+1< n and s[i:i+2] in roman:
                # print(s[i:i+2])
                num += roman[s[i:i+2]]
                # print(num,"IF NUM VALUE")
                i+=2
                # print(i)
            else:
                num += roman[s[i]]
                # print(num,"ELSE NUM VALUE")
                i += 1
        # print(num)
        return num

    s = input("Enter a Roman Letter(XIV):")
    print(roman_to_int(s))
except KeyError as e:
    print("give Roman values - (I V X L C D M) with Correct Combination",e)
