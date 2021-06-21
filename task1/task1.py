import re


def sep_str(org_str, method):
    if method == 0:
        int_str = re.findall(r'\d+', org_str)
        int_str = [int(i) for i in int_str]
        return int_str
    elif method == 1:
        str_str = re.findall(r'\D', org_str)
        str_str = [str(i) for i in str_str]
        str_str = ''.join(str_str)
        return str_str
    else:
        return "unknown method"


# at first I did this, and then i remembered that it was not C
# def sep_str(org_str, method):
#     i, k = 0, 0
#     int_str = []
#     str_str = ""
#     if method == 0:
#         while i in range(len(org_str)):
#             smbl = ''
#             a = org_str[i]
#             while '0' <= a <= '9':
#                 smbl += a
#                 i += 1
#                 if i < len(org_str):
#                     a = org_str[i]
#                 else:
#                     break
#             i += 1
#             if smbl != '':
#                 int_str.append(int(smbl))
#         return int_str
#     elif method == 1:
#         while i in range(len(org_str)):
#             smbl = ''
#             a = org_str[i]
#             while not '0' <= a <= '9':
#                 smbl += a
#                 i += 1
#                 if i < len(org_str):
#                     a = org_str[i]
#                 else:
#                     break
#             i += 1
#             if smbl != '':
#                 str_str += smbl
#         str_str = ' '.join(str_str.split())
#         return str_str
#     else:
#         return "incorrect method"


def ainA(str_str):
    res = ""
    k = 0
    spl = str(str_str).split()
    for i in spl:
        for i in spl[k].split():
            a = ''.join(spl[k])
            if len(a) == 1:
                res += a[0].upper()+' '
            else:
                res += a[0].upper()+a[1:-1]+a[-1].upper() + ' '
            k += 1
    return res


def degreedList(int_list):
    maxi = max(int_list)
    res = []
    for i in range(len(int_list)):
        if int_list[i] != maxi:
            res.append(int_list[i]**(i+1))
        else:
            res.append(int_list[i])
    return res


org_str = input("Input string > ")

int_list = sep_str(org_str, 0)
print("only numbers : ", int_list)

str_str = sep_str(org_str, 1)
print("only letters : ", str_str)

print("the first and last letters of each word in uppercase : ", ainA(str_str))

print("list of numbers ascended to the power of their index (except for the maximum) : ",
      degreedList(int_list))