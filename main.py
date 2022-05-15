import streamlit as st
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.03)

a_column, b_column = st.columns(2)

button = a_column.button('右カラムにテキストを表示させる')
if button:
    b_column.write('ここは右カラムです')

text = st.text_input('あなたの趣味を教えてください。')
condition = st.slider('あなたの今のモチベは？',-100,100,0)

'あなたの趣味は、',text,'です。'
'コンディション：', condition

expander = st.expander('問い合わせ')
expander.write('問い合わせの回答')

# if st.checkbox('Show Image'):
#     img = Image.open('sample01.png')
#     st.image(img,caption='マスター記念', use_column_width = True)