import streamlit as st
import os

# Load modules an toàn
try:
    from apps import *
except ImportError as e:
    st.error(f"Lỗi khi tải module ứng dụng: {str(e)}")
    st.stop()

st.set_page_config(page_title="General Engineering Toolkit", layout="centered")

# ----------------- CSS style -----------------
st.markdown("""
    <style>
        /* Ẩn toolbar nhưng không ảnh hưởng sidebar */
        [data-testid="stToolbar"] { display: none !important; }
        [data-testid="manage-app-button"] { display: none !important; }

        div.stButton > button {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            border-radius: 8px;
            transition: 0.3s;
            border: 1px solid #bbb;
        }
        div.stButton > button:hover {
            background-color: #f0f0f0 !important;
            border-color: #999;
        }

        .section-title {
            font-weight: 600;
            font-size: 16px;
            margin-top: 1.5em;
            border-bottom: 2px solid #DDD;
            padding-bottom: 4px;
        }

        .group-lookup > div,
        .group-loads > div,
        .group-concrete > div,
        .group-steel > div {
            background-color: #fafafa;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }
        .group-lookup > div { background-color: #eef6ff; }
        .group-loads > div { background-color: #fff7e6; }
        .group-concrete > div { background-color: #f2fff0; }
        .group-steel > div { background-color: #fff0f6; }

        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 150px;
            margin-bottom: 0.5em;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #666;
            margin-top: 1em;
        }
        /* Đảm bảo sidebar hiển thị */
        [data-testid="stSidebar"] {
            display: block !important;
            visibility: visible !important;
            width: 250px !important;
            min-width: 250px !important;
            z-index: 1000 !important;
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
        }
        .stSidebar > div {
            display: block !important;
            visibility: visible !important;
        }
        /* Đảm bảo nội dung chính không bị đè */
        .stApp {
            margin-left: 250px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------- Từ điển ngôn ngữ -----------------
LANG = {
    "en": {
        "title": "General Engineering Toolkit",
        "description": "Select a tool below to perform engineering calculations.",
        "back": "🔙 Back to main menu",
        "groups": {
            "lookup": "📖 Table & Material Lookup",
            "loads": "📦 Loads & Combinations",
            "concrete": "🧱 Concrete Members",
            "steel": "🔩 Steel Members"
        },
        "apps": {
            "Convert Unit": "Convert Unit",
            "Concrete Strength": "Concrete Strength",
            "Steel Strength": "Steel Strength",
            "Reinforcement Area": "Reinforcement Area",
            "Loading": "Loading",
            "Load Combination": "Load Combination",
            "Section Calculator": "Section Calculator",
            "Column PM Interaction": "Column PM Interaction",
            "Anchor Bolt Capacity": "Anchor Bolt Capacity",
            "Base Plate Checker": "Base Plate Checker",
            "Shear Stud Design": "Shear Stud Design"
        }
    },
    "vi": {
        "title": "📱 Bộ công cụ kỹ thuật xây dựng",
        "description": "Chọn một công cụ bên dưới để tính toán kỹ thuật.",
        "back": "🔙 Quay lại menu chính",
        "groups": {
            "lookup": "📖 Tra bảng & vật liệu",
            "loads": "📦 Tải trọng & tổ hợp",
            "concrete": "🧱 Cấu kiện bê tông",
            "steel": "🔩 Cấu kiện thép"
        },
        "apps": {
            "Convert Unit": "Đổi đơn vị",
            "Concrete Strength": "Cường độ Bê tông",
            "Steel Strength": "Cường độ Thép",
            "Reinforcement Area": "Diện tích Cốt thép",
            "Loading": "Tải trọng",
            "Load Combination": "Tổ hợp tải trọng",
            "Section Calculator": "Tính tiết diện",
            "Column PM Interaction": "Kiểm tra cột",
            "Anchor Bolt Capacity": "Kiểm tra bulong",
            "Base Plate Checker": "Kiểm tra bản đế",
            "Shear Stud Design": "Kiểm tra cắt bulong"
        }
    }
}

# ----------------- Chọn ngôn ngữ -----------------
if "lang" not in st.session_state:
    st.session_state.lang = "en"  # Mặc định tiếng Anh
with st.sidebar:
    st.subheader("🌐 Language / Ngôn ngữ")
    lang_choice = st.radio("", ["en", "vi"], format_func=lambda x: "English" if x == "en" else "Tiếng Việt", key="lang_select")
    if lang_choice != st.session_state.lang:
        st.session_state.lang = lang_choice
        st.session_state.selected_app = None  # Reset app khi đổi ngôn ngữ
        st.rerun()
    current_lang = LANG[st.session_state.lang]
    st.write("Debug: Sidebar is rendering")
    st.write(f"Debug: Current language: {st.session_state.lang}")

def _(key): 
    return current_lang["apps"].get(key, key)

# ----------------- Danh sách nhóm app -----------------
GROUPED_APPS = {
    "lookup": [
        {"key": "Convert Unit", "icon": "🔁", "func": getattr(app1_Convert_Unit, "run", None)},
        {"key": "Concrete Strength", "icon": "🧊", "func": getattr(app2_Concrete_Strength_Table, "run", None)},
        {"key": "Steel Strength", "icon": "⛓️", "func": getattr(app3_Steel_Strength_Lookup, "run", None)},
        {"key": "Reinforcement Area", "icon": "🧮", "func": getattr(app4_Steel_Reinforcement_Area, "run", None)},
    ],
    "loads": [
        {"key": "Loading", "icon": "📦", "func": getattr(app5_Load_Reference, "run", None)},
        {"key": "Load Combination", "icon": "📊", "func": getattr(app6_Load_Combination_Generator, "run", None)},
    ],
    "concrete": [
        {"key": "Section Calculator", "icon": "📐", "func": getattr(app7_Structural_Section_Calculator, "run", None)},
        {"key": "Column PM Interaction", "icon": "📉", "func": getattr(app8_Column_PMM_Interaction, "run