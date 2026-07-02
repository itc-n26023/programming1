#1
#answer = '''◯ ● ● ●
#● ◯ ● ●
#● ● ◯ ●
#● ● ● ◯
#'''
#print(answer)

#2
#w = '◯　'
#b = '●　'
#answer= w + b*3 + '\n' + b + w + b*2 + '\n' + b*2 + w + b + '\n' + b*3 + w
#print(answer)

#3
w = '◯　'
b = '●　'  
answer = ''
# i は「行（タテ）」を 0 から 3 (4個)まで数える
for i in range(4):
    # j は「列（ヨコ）」を 0 から 3 (4個)まで数える
    for j in range(4):
        # タテとヨコの位置が同じ（対角線）なら白丸(w)、違えば黒丸(b)
        if i == j:
            answer += w
        else:
            answer += b
    # 1行分（4個）並べ終わったら、お尻に改行(\n)を足す
    answer += '\n'
print(answer)
