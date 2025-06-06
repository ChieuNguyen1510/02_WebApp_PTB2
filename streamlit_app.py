import streamlit as st
from apps import app1, app2, app3, app4, app5, app6, app7, app8, app9, app10

st.set_page_config(page_title="General Engineering Toolkit", layout="centered")

# Ngôn ngữ
LANG = {
    "en": {
        "title": "📱 General Engineering Toolkit",
        "description": "Select a tool below to perform engineering calculations.",
        "back": "🔙 Back to main menu",
        "groups": {
            "lookup": "📖 Table & Material Lookup",
            "loads": "📦 Loads & Combinations",
            "concrete": "🧱 Concrete Member Tools",
            "steel": "🔩 Steel Member Tools"
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
            "Base Plate Checker": "Base Plate Checker"
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
            "Column PM Interaction": "Tương tác N-M Cột",
            "Anchor Bolt Capacity": "Khả năng chịu lực Bu lông",
            "Base Plate Checker": "Kiểm tra bản đế"
        }
    }
}

# Ngôn ngữ & hàm dịch
language = st.session_state.get("language", "en")
T = LANG[language]
def _(key): return T["apps"].get(key, key)

# Danh sách app theo nhóm
GROUPED_APPS = {
    "lookup": [
        {"key": "Convert Unit", "icon": "🔁", "func": getattr(app1, "run", None)},
        {"key": "Concrete Strength", "icon": "🧱", "func": getattr(app2, "run", None)},
        {"key": "Steel Strength", "icon": "🔩", "func": getattr(app3, "run", None)},
        {"key": "Reinforcement Area", "icon": "📐", "func": getattr(app4, "run", None)},
    ],
    "loads": [
        {"key": "Loading", "icon": "📦", "func": getattr(app5, "run", None)},
        {"key": "Load Combination", "icon": "📊", "func": getattr(app6, "run", None)},
    ],
    "concrete": [
        {"key": "Section Calculator", "icon": "📏", "func": getattr(app7, "run", None)},
        {"key": "Column PM Interaction", "icon": "📉", "func": getattr(app8, "run", None)},
    ],
    "steel": [
        {"key": "Anchor Bolt Capacity", "icon": "🔧", "func": getattr(app9, "run", None)},
        {"key": "Base Plate Checker", "icon": "🪛", "func": getattr(app10, "run", None)},
    ]
}

# Trang chính
if "selected_app" not in st.session_state:
    st.session_state.selected_app = None

if st.session_state.selected_app is None:
    st.title(T["title"])
    st.write(T["description"])

    for group_key, apps in GROUPED_APPS.items():
        st.markdown(f"### {T['groups'][group_key]}")
        cols = st.columns(3)
        for i, app in enumerate(apps):
            with cols[i % 3]:
                if st.button(f"{app['icon']} {_(app['key'])}", key=app["key"]):
                    st.session_state.selected_app = app["key"]
                    st.rerun()

else:
    with st.sidebar:
        if st.button(T["back"]):
            st.session_state.selected_app = None
            st.rerun()

    for group in GROUPED_APPS.values():
        for app in group:
            if app["key"] == st.session_state.selected_app:
                st.subheader(f"{app['icon']} {_(app['key'])}")
                app["func"]()
