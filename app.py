# app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="성적 계산기 (초간단)", page_icon="🧮", layout="centered")

st.title("🧮 성적 계산기 (초간단)")
st.caption("과목명과 점수(0~100)만 입력하면 총점과 평균을 바로 계산합니다. 행은 자유롭게 추가/삭제하세요.")

# 기본 3행 예시
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        {"과목": ["국어", "영어", "수학"], "점수": [0, 0, 0]}
    )

df = st.data_editor(
    st.session_state.df,
    num_rows="dynamic",              # 행 추가/삭제 허용
    use_container_width=True,
    hide_index=True,
    column_config={
        "과목": st.column_config.TextColumn("과목"),
        "점수": st.column_config.NumberColumn("점수", min_value=0, max_value=100, step=1),
    },
    key="grades_editor",
)

# 계산 (빈칸/NaN은 제외)
scores = pd.to_numeric(df["점수"], errors="coerce").dropna()
count = int(scores.shape[0])
total = float(scores.sum()) if count else 0.0
avg = float(scores.mean()) if count else 0.0

st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("과목 수", f"{count}")
c2.metric("총점", f"{total:.1f}")
c3.metric("평균", f"{avg:.2f}")

st.caption("Tip) 점수는 0~100 사이 값만 허용됩니다. 필요 없으면 행을 삭제하세요.")
