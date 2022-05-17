import streamlit as st
import time

st.title('Streamlit nyumon')

st.write('progress bar')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!'

col1, col2 = st.columns(2)

with col1:
    button = col1.button('右カラムに文字を表示')

with col2:
    if button:
        col2.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#text = st.text_input('あなたの趣味を教えて下さい。') 
#condition = st.slider('あなたの今の調子は？', 0, 100, 50)

#'あなたの趣味：', text, 'です。'
#'コンディション:', condition 

#option = st.selectbox(
#    'あなたが好きな数字を教えてください、',
#    list(range(1, 11))
#)
#'あなたの好きな数字は、', option, 'です。'

#if st.checkbox('Show Image'):
#    img = Image.open('/Users/yuki/Pictures/現像/web/yosida/DSC01974.jpg')   
#    st.image(img, caption= 'yoshida', use_column_width=True)


