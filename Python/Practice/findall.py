# 文字列の中に入っている文字を出す
# パターン１

import re

Str = str(input('文字列を入力してください:'))
match=re.findall('a',Str,re.IGNORECASE)
print(Str,'の中に','aは',len(match),'文字あります。')



# パターン２
A=str(input('文字列を入力してください'))
String='a'
String2=A.count(String)
print(A,'の中に','aは',String2,'文字あります。')
