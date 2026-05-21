import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Hàm kết nối dùng Secrets
def get_gspread_client():
    # Lấy từ Secrets
    creds_dict = dict(st.secrets["gcp_service_account"])
    # Xử lý ký tự xuống dòng
    creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n")
    
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    return gspread.authorize(creds)

# Kết nối
gc = get_gspread_client()
sh = gc.open('DSNV') 

st.title("CRM Showroom - Vinken")
st.write("Kết nối thành công!")
