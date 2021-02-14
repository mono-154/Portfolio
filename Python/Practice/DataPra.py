print('(1)')
# while文を使ってやると考えられる。
DateList=[]
while True:
  DateMouth=int(input('データ数はいくつですか？:'))
  if DateMouth == 0:
    break
  for i in range(DateMouth):
    
    DateList.append(int(input(f'{i + 1}番目のデータを入力してください:')))
  ave = float(sum(DateList) / len(DateList))
  Sum= sum(DateList)
  print('合計は%d,平均は{:.2f}です。' .format(ave)  %(Sum), end=' ')
  
print('\n(2)')

x=int(input('(x,y)の最大公約数を計算します。但し x>y\nx='))
y=int(input('y='))
while y:
  t=y
  y= x % y
  x=t
  print('最大公約数は %d です。' % x)

print('\n(3)')
dist=int(input('鉄道運賃計算プログラム\n距離＝'))
if dist <= 10:
  fare=200
elif dist <= 30:
  fare=200+(dist-10) * 10
else:
  fare=400+(dist-30) * 5
amari=fare % 10
if amari > 0:
  fare+=(10-amari)
print('運賃は %d 円です。' % fare)

print('\n(4)')

num=int(input('番号を入力してください:'))
num_re=int(str(num).zfill(3))

Math=['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
form=['Spade','Club','Diamond','Heart',]


if 0 < num_re <=413:
  a=(num % 100) - 1
  b=round(num,-2)
  print('This number is %s of %s.' %(Math[a],form[b]),end=' ')
else:
  print('This is Jocker')