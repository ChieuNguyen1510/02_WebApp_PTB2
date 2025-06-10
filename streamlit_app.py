import streamlit as st

# Load modules an toàn
try:
    from apps import app1, app2, app3, app4, app5, app6, app7, app8, app9, app10, app11
except ImportError as e:
    st.error(f"Failed to load app modules: {str(e)}")
    st.stop()

st.set_page_config(page_title="General Engineering Toolkit", layout="centered")

# ----------------- CSS style -----------------
st.markdown("""
    <style>
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
            font-weight: 700;
            font-size: 20px;
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
    </style>
""", unsafe_allow_html=True)

# ----------------- Ngôn ngữ -----------------
LANG = {
    "en": {
        "title": "📱 General Engineering Toolkit",
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
            "Shear Stud Design Calculation": "Shear Stud Design Calculation"
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
            "Shear Stud Design Calculation": "Kiểm tra cắt bulong"
        }
    }
}

# ----------------- Chọn ngôn ngữ -----------------
if "lang" not in st.session_state:
    st.session_state.lang = "en"
with st.sidebar:
    lang_choice = st.radio("🌐 Language / Ngôn ngữ", ["en", "vi"], format_func=lambda x: "English" if x == "en" else "Tiếng Việt")
    st.session_state.lang = lang_choice
    current_lang = LANG[lang_choice]

def _(key): return current_lang["apps"].get(key, key)

# ----------------- Danh sách nhóm app -----------------
GROUPED_APPS = {
    "lookup": [
        {"key": "Convert Unit", "icon": "🔁", "func": getattr(app1, "run", None)},
        {"key": "Concrete Strength", "icon": "🏗️", "func": getattr(app2, "run", None)},
        {"key": "Steel Strength", "icon": "🔩", "func": getattr(app3, "run", None)},
        {"key": "Reinforcement Area", "icon": "🧮", "func": getattr(app4, "run", None)},
    ],
    "loads": [
        {"key": "Loading", "icon": "📦", "func": getattr(app5, "run", None)},
        {"key": "Load Combination", "icon": "📊", "func": getattr(app6, "run", None)},
    ],
    "concrete": [
        {"key": "Section Calculator", "icon": "📐", "func": getattr(app7, "run", None)},
        {"key": "Column PM Interaction", "icon": "📉", "func": getattr(app8, "run", None)},
    ],
    "steel": [
        {"key": "Anchor Bolt Capacity", "icon": "🔧", "func": getattr(app9, "run", None)},
        {"key": "Base Plate Checker", "icon": "🪛", "func": getattr(app10, "run", None)},
        {"key": "Shear Stud Design Calculation", "icon": "🪛", "func": getattr(app11, "run", None)},
    ]
}

# ----------------- State điều hướng -----------------
if "selected_app" not in st.session_state:
    st.session_state.selected_app = None

# ----------------- Giao diện chính -----------------
if st.session_state.selected_app is None:
    st.title(current_lang["title"])
    st.write(current_lang["description"])

    for group_key, app_list in GROUPED_APPS.items():
        st.markdown(f"<div class='section-title'>{current_lang['groups'][group_key]}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='group-{group_key}'>", unsafe_allow_html=True)
        cols = st.columns(3)
        for i, app in enumerate(app_list):
            with cols[i % 3]:
                if st.button(f"{app['icon']} {_(app['key'])}", key=app["key"]):
                    st.session_state.selected_app = app["key"]
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ----------------- App con -----------------
else:
    with st.sidebar:
        if st.button(current_lang["back"]):
            st.session_state.selected_app = None
            st.rerun()

    for group in GROUPED_APPS.values():
        for app in group:
            if app["key"] == st.session_state.selected_app:
                st.subheader(f"{app['icon']} {_(app['key'])}")
                app["func"]()
