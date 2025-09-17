import streamlit as st

st.set_page_config(page_title="BMI 계산기", page_icon="⚖️", layout="centered")

st.title("⚖️ BMI 계산기")

# 사용자 입력
st.subheader("1) 키와 몸무게 입력")
height = st.number_input("키 (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
weight = st.number_input("몸무게 (kg)", min_value=10.0, max_value=200.0, value=65.0, step=0.1)

# BMI 계산
if height > 0:
    bmi = weight / ((height / 100) ** 2)
else:
    bmi = 0

# BMI 판정 함수
def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "저체중 🟦"
    elif bmi < 23:
        return "정상 🟩"
    elif bmi < 25:
        return "과체중 🟨"
    else:
        return "비만 🟥"

# 결과 출력
st.subheader("2) 결과")
st.metric("BMI 지수", f"{bmi:.2f}")
st.write("판정:", bmi_category(bmi))
