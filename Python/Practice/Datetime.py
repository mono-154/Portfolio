import datetime

year=int(input('西暦を入力してください:'))
month=int(input('月を入力してください:'))
start=(datetime.date(year,month,1).weekday() + 1) % 7
if month == 2:
  if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 !=0)):
    end = 29
  else:
    end=28
if month in [4,6,9,11]:
  end = 30
else:
  end = 31
print('万年カレンダー(%d 年 %d 月)' % (year,month))
print('  Sun  Mon  Tue  Wed  Thr  Fri  Sat')
for i in range(start):
  print('    ',end=' ')
for i in range(1,end+1):
  if i % 7 == (7 - start) % 7:
    print('%4d' % i)
  else:
    print('%4d' % i, end=' ')