import streamlit as st

# Load modules an toàn
try:
    from apps import app1, app2, app3, app4, app5, app6, app7
except ImportError as e:
    st.error(f"Failed to load app modules: {str(e)}")
    st.stop()

st.set_page_config(page_title="General Engineering Toolkit", layout="centered")

# ---------- Ngôn ngữ ----------
LANG = {
    "en": {
        "title": "📱 General Engineering Toolkit",
        "description": "Select a tool below to perform engineering calculations.",
        "back": "🔙 Back to main menu",
        "apps": {
            "Convert Unit": "Convert Unit",
            "Concrete Strength": "Concrete Strength",
            "Steel Strength": "Steel Strength",
            "Reinforcement Area": "Reinforcement Area",
            "Loading": "Loading",
            "Load Combination": "Load Combination",
            "Section Calculator": "Section Calculator"
        }
    },
    "vi": {
        "title": "📱 Bộ công cụ kỹ thuật xây dựng",
        "description": "Chọn một công cụ bên dưới để tính toán kỹ thuật.",
        "back": "🔙 Quay lại menu chính",
        "apps": {
            "Convert Unit": "Đổi đơn vị",
            "Concrete Strength": "Cường độ Bê tông",
            "Steel Strength": "Cường độ Thép",
            "Reinforcement Area": "Diện tích Cốt thép",
            "Loading": "Tải trọng",
            "Load Combination": "Tổ hợp tải trọng",
            "Section Calculator": "Tính tiết diện"
        }
    }
}

# Chọn ngôn ngữ
if "lang" not in st.session_state:
    st.session_state.lang = "en"

with st.sidebar:
    lang_choice = st.radio("🌐 Language / Ngôn ngữ", options=["en", "vi"], format_func=lambda x: "English" if x == "en" else "Tiếng Việt")
    st.session_state.lang = lang_choice
    current_lang = LANG[st.session_state.lang]

# ---------- Danh sách apps ----------
apps = [
    {"key": "Convert Unit", "icon": "🔁", "func": getattr(app1, "run", None)},
    {"key": "Concrete Strength", "icon": "🏗️", "func": getattr(app2, "run", None)},
    {"key": "Steel Strength", "icon": "🔩", "func": getattr(app3, "run", None)},
    {"key": "Reinforcement Area", "icon": "🧮", "func": getattr(app4, "run", None)},
    {"key": "Loading", "icon": "📦", "func": getattr(app5, "run", None)},
    {"key": "Load Combination", "icon": "📊", "func": getattr(app6, "run", None)},
    {"key": "Section Calculator", "icon": "📐", "func": getattr(app7, "run", None)},
]
apps = [app for app in apps if app["func"] is not None]

# Custom CSS cho button đẹp
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        padding: 12px;
        font-size: 16px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- State điều hướng ----------
if "selected_app" not in st.session_state:
    st.session_state.selected_app = None

# ---------- Giao diện chính ----------
if st.session_state.selected_app is None:
    st.title(current_lang["title"])
    st.write(current_lang["description"])

    num_cols = min(3, len(apps))
    for i in range(0, len(apps), num_cols):
        cols = st.columns(num_cols)
        for j, app in enumerate(apps[i:i + num_cols]):
            with cols[j]:
                app_name = current_lang["apps"].get(app["key"], app["key"])
                if st.button(f"{app['icon']} {app_name}", key=app["key"]):
                    st.session_state.selected_app = app["key"]
                    st.rerun()
        # Fill cột trống nếu số app không chia hết
        for j in range(len(apps[i:i + num_cols]), num_cols):
            with cols[j]:
                st.empty()

# ---------- Giao diện app con ----------
else:
    with st.sidebar:
        if st.button(current_lang["back"]):
            st.session_state.selected_app = None
            st.rerun()
    try:
        selected = next(app for app in apps if app["key"] == st.session_state.selected_app)
        app_name = current_lang["apps"].get(selected["key"], selected["key"])
        st.subheader(f"{selected['icon']} {app_name}")
        selected["func"]()
    except StopIteration:
        st.error("App not found. Returning to main menu.")
        st.session_state.selected_app = None
        st.rerun()
    except Exception as e:
        st.error(f"Error in app '{st.session_state.selected_app}': {str(e)}")
