import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# 1. Cấu hình kết nối từ Secrets
def get_gspread_client():
    # Lấy thông tin từ mục Secrets
    creds_dict = st.secrets["gcp_service_account"]
    
    # Định nghĩa các quyền cần thiết
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    
    # Tạo xác thực
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    return gspread.authorize(creds)

# 2. Kết nối
gc = get_gspread_client()
sh = gc.open('DS NV') # NHỚ THAY TÊN FILE GOOGLE SHEETS VÀO ĐÂY

# 3. Code giao diện ví dụ
st.title("Chào mừng Vinken!")
st.write("Đã kết nối thành công với Google Sheets.")
