import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Báo cáo cuối kỳ môn Xử lý ảnh👋")

st.sidebar.success("Chọn chương trình chạy ở trên ")

st.markdown(
    """
        <h3>Họ tên sinh viên thực hiện:</h2> <br>
        <div>\t 1. Trịnh Hoàng Phúc - MSSV: 20110700 </div>
        <div>\t 2. Nguyễn Bá Phước - MSSV: 20110702 </div> 
    """,
    unsafe_allow_html=True
)

st.image('img_test.png')
