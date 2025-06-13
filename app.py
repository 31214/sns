import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📱 사람당 평균 SNS 이용 시간 분석")

# 데이터 불러오기
df = pd.read_csv("data/sns_usage.csv")
df['daily_minutes'] = df['weekly_minutes'] / 7

# 사용자 필터
ages = st.multiselect("연령대 선택", df['age_group'].unique(), default=df['age_group'].unique())
gender = st.radio("성별 선택", ['전체', '남', '여'])

filtered = df[df['age_group'].isin(ages)]
if gender != '전체':
    filtered = filtered[filtered['gender'] == gender]

# 시각화
st.subheader("📊 연령대별 하루 평균 SNS 이용 시간")

fig, ax = plt.subplots()
sns.barplot(data=filtered, x="age_group", y="daily_minutes", hue="gender", ax=ax)
ax.set_ylabel("일일 평균 SNS 사용 시간 (분)")
st.pyplot(fig)

st.markdown("### 🔍 인사이트 요약")
st.markdown("- 20대가 SNS 사용 시간이 가장 길어요.")
st.markdown("- 여성이 평균적으로 더 많이 사용해요.")
