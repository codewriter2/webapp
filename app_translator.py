import streamlit as st

st.set_page_config(page_title="한-중 단어 사전", page_icon="📖", layout="centered")

st.title("📖 한-중 단어 사전")

# 간단한 한–중 사전
dict_ko2zh = {
    "안녕하세요": "你好",
    "사랑": "爱",
    "학교": "学校",
    "선생님": "老师",
    "학생": "学生",
    "책": "书",
    "물": "水",
    "밥": "饭"
}

# 역방향 사전
dict_zh2ko = {v: k for k, v in dict_ko2zh.items()}

# 입력
text = st.text_input("번역할 단어/문장을 입력하세요:")

direction = st.radio("번역 방향", ["한국어 ➝ 중국어", "중국어 ➝ 한국어"])

# 번역 처리
if st.button("번역하기"):
    if text.strip() == "":
        st.warning("단어를 입력하세요!")
    else:
        if direction == "한국어 ➝ 중국어":
            result = dict_ko2zh.get(text, "❌ 사전에 없음")
        else:
            result = dict_zh2ko.get(text, "❌ 사전에 없음")

        st.success(result)

