import sys
import random as r

# 数字が重複しないように
def has_not_duplicates(seq):
  return len(seq) == len(set(seq))

# ヒットとブローの判定
def judgement(yin, ans):
  h=0
  b=0
  for i in range(len(yin)):
    if yin[i]==ans[i]:
      h += 1
    else:
      if yin[i] in ans:
        b += 1
  return ([h,b])

# 出題　4桁のランダムな並びの重複しない数列
def make_question():
  nums=list(range(10))
  return (r.sample(nums, 4))

# プレイヤーの入力と何ターン目か又、判定結果の表示
def main():
  turn =1
  ans = make_question()
  print(ans)
  print("Hit&Blowゲーム!")
# ヒットが4になるまで繰り返す
  while True:
    print("第%02d手目" % turn)
    print("4桁の重複しない数字を入力してください")
    print("->", end=" ")
    hit=0
    blow=0
    tmp=input()
    your_input=[]
    for i in tmp:
      your_input.append(int(i))
    if has_not_duplicates(your_input):
      hit,blow = judgement(your_input, ans)
      print("hit =" +str(hit)+", blow ="+str(blow))
      if hit ==4:
        print("おめでとう！ %02d手目で正解です：" % turn)
        break
      elif hit < 4:
        turn+=1
        if 5 < turn < 7:
          print("残念でした。正解は"+ str(ans) +"でした。")
          break


if __name__ == "__main__":
  main()