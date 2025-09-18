import streamlit as st

st.title("Streamlit 요소 예시")  # 페이지 제목

st.header("헤더 예시")  # 큰 제목
st.subheader("서브헤더 예시")  # 작은 제목

st.text("일반 텍스트입니다.")  # 일반 텍스트
st.markdown("**마크다운 텍스트**")  # 마크다운 지원 텍스트

st.write("write 함수는 다양한 타입의 데이터를 출력할 수 있습니다.")  # write 함수

st.code("print('Hello, Streamlit!')", language='python')  # 코드 블록

st.latex(r"\alpha^2 + \beta^2 = \gamma^2")  # LaTeX 수식

st.divider()  # 구분선

st.image("https://static.streamlit.io/examples/dog.jpg", caption="이미지 예시")  # 이미지

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오

st.video("https://www.youtube.com/watch?v=5qap5aO4i9A")  # 비디오

st.button("버튼")  # 버튼

st.checkbox("체크박스")  # 체크박스

st.radio("라디오 버튼", ["옵션 1", "옵션 2"])  # 라디오 버튼

st.selectbox("셀렉트박스", ["A", "B", "C"])  # 셀렉트박스

st.multiselect("멀티셀렉트", ["X", "Y", "Z"])  # 멀티셀렉트

st.slider("슬라이더", 0, 100, 50)  # 슬라이더

st.number_input("숫자 입력", min_value=0, max_value=10, value=5)  # 숫자 입력

st.text_input("텍스트 입력")  # 텍스트 입력

st.text_area("텍스트 영역")  # 텍스트 영역

st.date_input("날짜 입력")  # 날짜 입력

st.time_input("시간 입력")  # 시간 입력

st.file_uploader("파일 업로더")  # 파일 업로더

st.progress(70)  # 진행률 표시 (0~100)

st.spinner("로딩 중...")  # 스피너(로딩 표시)

st.success("성공 메시지")  # 성공 메시지
st.info("정보 메시지")  # 정보 메시지
st.warning("경고 메시지")  # 경고 메시지
st.error("에러 메시지")  # 에러 메시지

import pandas as pd
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
st.dataframe(df)  # 데이터프레임 표시

st.table(df)  # 테이블 표시

import numpy as np
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)  # 라인 차트
st.bar_chart(chart_data)  # 바 차트
st.area_chart(chart_data)  # 에어리어 차트

# 각 요소별 각주:
# 1. st.title, st.header, st.subheader: 페이지의 제목 및 섹션 구분에 사용
# 2. st.text, st.markdown, st.write: 텍스트 및 다양한 데이터 출력
# 3. st.code, st.latex: 코드 및 수식 표현
# 4. st.divider: 시각적 구분선
# 5. st.image, st.audio, st.video: 미디어 파일 출력
# 6. st.button, st.checkbox, st.radio, st.selectbox, st.multiselect, st.slider, st.number_input, st.text_input, st.text_area, st.date_input, st.time_input, st.file_uploader: 입력 및 인터랙션 요소
# 7. st.progress, st.spinner: 진행률 및 로딩 표시
# 8. st.success, st.info, st.warning, st.error: 상태 메시지
# 9. st.dataframe, st.table: 표 및 데이터프레임 출력
# 10. st.line_chart, st.bar_chart, st.area_chart: 차트 시각화

# 위 코드를 streamlit_app.py에 복사하면 모든 주요 요소를 한 페이지에서 확인할 수 있습니다.