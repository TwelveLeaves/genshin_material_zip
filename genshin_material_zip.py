# coding: UTF-8
import sys
# 原神の「これ前部圧縮したらいくつになるんだっけ？」を計算するスクリプト
# 半角スペース区切りで入力を受け付けて、配列0番目に圧縮した結果を表示する
# 途中の計算経過を表示すれば途中のレアリティの圧縮結果もわかるから表示してある

try:
    sozai_list = list(map(int, input().split()))
except:
    print("ミスってる")
    sys.exit

for i in range(len(sozai_list)-1, 0, -1):
    tmp = sozai_list[i] // 3
    sozai_list[i] = sozai_list[i] % 3
    sozai_list[i-1] += tmp
    print(sozai_list)

print("result:")
print(sozai_list)
