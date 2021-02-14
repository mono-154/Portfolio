mouth=int(input('月を入力してください:'))
seasons=['冬','春','夏','秋',]
season=int((mouth % 12) / 3 )
print('季節は %s ですね。' % (seasons[season]))