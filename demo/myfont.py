'''
@Author: kingw
@Date: 2020-03-09 15:01:31
@Description: file content
'''
def myfont():
    name = input("输入你的名字:(only English words) \t")
    length = len(name)

    for x in range(0, length):
        c = name[x]
        c = c.upper()

        if c == 'A':
            print('''-----A-----
---A---A---
--A-A-A-A--
-A-------A-''', '\n')

        elif c == 'B':
            print('''---B-B-B---
---B--B----
---B--B----
---B-B-B---''', '\n')

        elif c == 'C':
            print('''---C-C-C---
--C--------
--C--------
---C-C-C---''', '\n')

        elif c == 'D':
            print('''---D-D-D---
---D----D--
---D----D--
---D-D-D---''', '\n')

        elif c == 'E':
            print('''---E-E-E---
---EEE-----
---EEE-----
---E-E-E---''', '\n')

        elif c == 'F':
            print('''---F-F-F---
---F-------
---F-F-F---
---F-------''', '\n')

        elif c == 'G':
            print('''---G--GG---
--G--------
--G---GG---
---G--GG---''', '\n')

        elif c == 'H':
            print('''--H-----H--
--H--H--H--
--H--H--H--
--H-----H--''', '\n')

        elif c == 'I':
            print('''--II-I-II--
-----I-----
-----I-----
--II-I-II--''', '\n')

        elif c == 'J':
            print('''-----J-----
-----J-----
--J--J-----
---J-J-----''', '\n')

        elif c == 'K':
            print('''---K---K---
---K-K-----
---K-K-----
---K---K---''', '\n')

        elif c == 'L':
            print('''--L--------
--L--------
--L--------
--L-L-L-L--''', '\n')

        elif c == 'M':
            print('''--M-----M--
--M-M-M-M--
--M--M--M--
--M-----M--''', '\n')

        elif c == 'N':
            print('''--N-----N--
--N-N---N--
--N--N--N--
--N---N-N--''', '\n')

        elif c == 'O':
            print('''----OOO----
--OO---OO--
--OO---OO--
----OOO----''', '\n')

        elif c == 'P':
            print('''---P-P-P---
---P----P---
---P-P-P----
---P--------''', '\n')

        elif c == 'Q':
            print('''----QQQ----
--QQ---QQ--
--QQ-Q-QQ--
----QQQ--Q-''', '\n')

        elif c == 'R':
            print('''--R-RR-----
--R---R----
--R-RR-----
--R---R----''', '\n')

        elif c == 'S':
            print('''----SS-----
--SS---SS--
-SS---SS---
----SS-----''', '\n')

        elif c == 'T':
            print('''--TT-T-TT--
-----T-----
-----T-----
-----T-----''', '\n')

        elif c == 'U':
            print('''--U-----U--
--U-----U--
--U-----U--
---U-U-U---''', '\n')

        elif c == 'V':
            print('''--V-----V--
---V---V---
----V-V----
-----V-----''', '\n')

        elif c == 'W':
            print('''-W---W---W-
--W--W--W--
---W---W---
----W-W----''', '\n')

        elif c == 'X':
            print('''--X-----X--
----X-X----
----X-X----
--X-----X--''', '\n')

        elif c == 'Y':
            print('''--Y-----Y--
---Y---Y---
-----Y-----
-----Y-----''', '\n')

        elif c == 'Z':
            print('''--Z--Z--Z--
-------Z---
----Z------
--Z--Z--Z--''', '\n')

        elif c == ' ':
            print('''-----------
-----------
-----------
-----------''', '\n')

        elif c == '.':
            print('''----..-----
---..-..---
---..-..---
----..-----''', '\n')

if __name__ == '__main__':
    myfont()