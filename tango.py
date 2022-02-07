import random
import tng
import tng_all

print('項目を入力してください')
z=input()
if z=='day1':
    d=tng.day1
elif z=='day2':
    d=tng.day2
elif z=='day3':
    d=tng.day3
elif z=='day4':
    d=tng.day4
elif z=='day5':
    d=tng.day5
elif z=='day6':
    d=tng.day6
elif z=='day7':
    d=tng.day7
elif z=='day8':
    d=tng.day8
elif z=='day9':
    d=tng.day9
elif z=='day10':
    d=tng.day10
elif z=='day11':
    d=tng.day11
elif z=='day12':
    d=tng.day12
elif z=='day13':
    d=tng.day13
elif z=='day14':
    d=tng.day14
elif z=='day15':
    d=tng.day15
elif z=='day16':
    d=tng.day16
elif z=='day17':
    d=tng.day17
elif z=='day18':
    d=tng.day18
elif z=='day19':
    d=tng.day19
elif z=='day20':
    d=tng.day20
elif z=='all':
    d=tng_all.all
    
print("\n")
a={" ":"\b "}
while True:    
    try:
        word = random.choice(list(d.keys()))
        print(word )
        try:
            print(u'エンターで答えを表示する（CTRL+Cで終了）')
            input()
        except KeyboardInterrupt:
            break
        else:
            print(u'答え: ' +d[word] + '    [cでチェック]')
            x=input()
            if x=='c':
                a[word]=d[word]
            d.pop(word) 
            print('\n\n')
    except IndexError:
        print("\n")
        print('わからなかった単語の表示')
        for k,v in a.items():
            print(k+':'+v)
        break
        
    


