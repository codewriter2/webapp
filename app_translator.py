import streamlit as st
from googletrans import Translator

st.set_page_config(page_title="한중 번역기", page_icon="🌐", layout="centered")

st.title("🌐 간단 번역기 (한국어 ↔ 중국어)")

# 번역기 초기화
translator = Translator()

# 입력
st.subheader("1) 텍스트 입력")
text = st.text_area("번역할 문장을 입력하세요:", height=100)

# 언어 선택
st.subheader("2) 번역 방향 선택")
direction = st.radio("번역 방향", ["한국어 ➝ 중국어", "중국어 ➝ 한국어"])

# 번역 버튼
if st.button("번역하기"):
    if text.strip() == "":
        st.warning("번역할 문장을 입력하세요!")
    else:
        if direction == "한국어 ➝ 중국어":
            result = translator.translate(text, src="ko", dest="zh-cn")
        else:
            result = translator.translate(text, src="zh-cn", dest="ko")

        # 결과 출력
        st.subheader("3) 번역 결과")
        st.success(result.text)
