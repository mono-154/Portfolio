#うるう年判定のプログラム
#4で割り切れて、100で割り切れない　もしくは400で割り切れる
year_str=input("西暦何年？：")
year=int(year_str)

if  year % 400 == 0:
  print("うるう年です")
elif year % 4 == 0 and year % 100 == 0:
  print('うるう年ではありません')
elif year % 4 ==0:
  print("うるう年です")
else:
  print("うるう年ではありません")