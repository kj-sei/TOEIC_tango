import streamlit as st
import random
import tng
import tng_all

st.title('streamlit単語帳')
st.write('項目を入力してください')

option = st.selectbox(
    '項目を選択してください', 
    ['day1','day2','day3','day4','day5','day6','day7','day8','day9','day10','day11','day12','day13','day14','day15','day16','day17','day18','day19','day20']
)
if option=='day1':
    d=tng.day1
elif option=='day2':
    d=tng.day2
elif option=='day3':
    d=tng.day3
elif option=='day4':
    d=tng.day4
elif option=='day5':
    d=tng.day5
elif option=='day6':
    d=tng.day6
elif option=='day7':
    d=tng.day7
elif option=='day8':
    d=tng.day8
elif option=='day9':
    d=tng.day9
elif option=='day10':
    d=tng.day10
elif option=='day11':
    d=tng.day11
elif option=='day12':
    d=tng.day12
elif option=='day13':
    d=tng.day13
elif option=='day14':
    d=tng.day14
elif option=='day15':
    d=tng.day15
elif option=='day16':
    d=tng.day16
elif option=='day17':
    d=tng.day17
elif option=='day18':
    d=tng.day18
elif option=='day19':
    d=tng.day19
elif option=='day20':
    d=tng.day20
elif option=='all':
    d=tng_all.all


    
a={" ":"\b "}

st.session_state.word = random.choice(list(d.keys()))
st.write(st.session_state.word)
if st.button('答え'):
    st.write(d[st.session_state.word])


        
    


