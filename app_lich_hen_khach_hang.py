import streamlit as st
import gspread
import pandas as pd

# Kết nối Google Sheets (cần file service_account.json)
gc = gspread.service_account(filename='credentials.json')
sh = gc.open('Ten_File_Google_Sheets')

# Hàm đăng nhập đơn giản
def check_login(username, password):
    df_nv = pd.DataFrame(sh.worksheet('Nhan_Vien').get_all_records())
    user = df_nv[(df_nv['Ten_NV'] == username) & (df_nv['Mat_khau'] == password)]
    return not user.empty

# Giao diện chính
st.title("CRM Showroom - Quản Lý Khách Hàng")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    user = st.text_input("Tên đăng nhập")
    pw = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if check_login(user, pw):
            st.session_state.logged_in = True
            st.session_state.user = user
            st.rerun()
else:
    st.write(f"Xin chào: {st.session_state.user}")
    # Tại đây bạn hiển thị các Tab (st.tabs) và dữ liệu từ Google Sheets
    # Dùng st.dataframe hoặc st.data_editor để NV cập nhật thông tin
