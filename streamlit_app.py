import streamlit as st

# 계산기 페이지
st.title("계산기")
num1 = st.number_input("첫 번째 숫자 입력", value=0.0, format="%f")
num2 = st.number_input("두 번째 숫자 입력", value=0.0, format="%f")
operation = st.radio("연산 선택", ("덧셈", "뺄셈", "곱셈", "나눗셈"))

if st.button("계산하기"):
	if operation == "덧셈":
		result = num1 + num2
		st.success(f"결과: {num1} + {num2} = {result}")
	elif operation == "뺄셈":
		result = num1 - num2
		st.success(f"결과: {num1} - {num2} = {result}")
	elif operation == "곱셈":
		result = num1 * num2
		st.success(f"결과: {num1} × {num2} = {result}")
	elif operation == "나눗셈":
		if num2 != 0:
			result = num1 / num2
			st.success(f"결과: {num1} ÷ {num2} = {result}")
		else:
			st.error("0으로 나눌 수 없습니다.")

