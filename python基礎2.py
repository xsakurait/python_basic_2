集合内包表記(集合はシーケンスオブジェクトではない。つまり
       生成したとき毎回ランダムで決まるので作成するごとに結果が違う可能性あり)

num=(1,2,3,5,4)
nums={i**2 for i in num}
print(i)#{9,4,1,25,16}

辞書内包表記
keys= ['a','b','c']
values=[1,2,3]
dicts = {for key,value in zip(keys,values)}
       dicts[key] = value
print(dicts)#{'b':2,'a':1,'c':3}

ジェネレータ内包表記
words=['Python','css','HTML','Javascript']

words_gen=(word.lower for word in words if len(word)<7)

for text in words_gen:
       print(text)

freeWIFIに接続して何かを検索したり、個人情報入力したりすると
ログデータとしてWIFIに送られるので、IPアドレスや検索したURLなどの閲覧履歴バレル
(URLが管理者が検索すれば管理者もＵRLみれる)

ルーター再起動したときに自宅のWIFIのログなくなる

リスト内包表記などで実行処理速度上がる理由
リストを普通に書いた時、appendメソッドを毎回forの中で
呼び出す必要があり、若干のロスが重なる24%の速度差ある

プログラム実行速度図る方法
from time import time
start=time()
proc_time=time()-start

generator リストの違い
generatornoyieldは返してもまだ続けることができるが、
リストのreturn はfor分から抜けてしまう。
なので、リストを返したいときは、リストに返したい要素リストにまとめて
返さなければいけない

三項演算子「条件式Trueの時の返り値」[if条件式]「Falseのとき」
x='奇数' if x%2!=0 else x='偶数'

