import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Cấu hình trang web
st.set_page_config(page_title="CRM Showroom", layout="wide")

# Hàm kết nối (có thêm cache để app chạy mượt hơn)
@st.cache_resource
def get_gspread_client():
    creds_dict = dict(st.secrets["gcp_service_account"])
    creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n")
    
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    return gspread.authorize(creds)

# Thực thi
try:
    gc = get_gspread_client()
    sh = gc.open('DSNV') # Đảm bảo file tên là DSNV
    
    st.title("CRM Showroom - Vinken")
    st.success("Kết nối thành công tới Google Sheets!")
    
    # Hiển thị dữ liệu thử nghiệm
    worksheet = sh.sheet1
    data = worksheet.get_all_records()
    st.write("Dữ liệu từ Google Sheets:")
    st.dataframe(data)

except Exception as e:
    st.error(f"Lỗi kết nối: {e}")
    st.write("Hãy kiểm tra lại quyền truy cập của Service Account đối với file Google Sheets 'DSNV'.")
