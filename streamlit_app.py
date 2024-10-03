import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.title('私の最初のStreamlitアプリ')

st.write('これは、Streamlitで作成したシンプルなアプリです。')

# スライダー
value = st.slider('好きな数字を選んでください', 0, 100, 50)
st.write('あなたの選んだ数字は', value, 'です。')
