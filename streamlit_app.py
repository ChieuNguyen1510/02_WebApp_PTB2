import streamlit as st
from apps import app1, app2, app3, app4, app5

st.set_page_config(page_title="General Application", layout="centered")

# Danh sách ứng dụng
apps = [
    {"name": "Convert Unit", "icon": "🔁", "func": app1.run},
    {"name": "Concrete Strength", "icon": "🏗️", "func": app2.run},
    {"name": "Steel Strength", "icon": "🔩", "func": app3.run},
    {"name": "Reinforcement Area", "icon": "🧮", "func": app4.run},
    {"name": "Loading", "icon": "📦", "func": app5.run},
]

# State điều hướng
if "selected_app" not in st.session_state:
    st.session_state.selected_app = None

# Giao diện chọn app
if st.session_state.selected_app is None:
    st.title("📱 General Engineering Toolkit")
    num_cols = 3
    for i in range(0, len(apps), num_cols):
        cols = st.columns(num_cols)
        for j, app in enumerate(apps[i:i + num_cols]):
            with cols[j]:
                if st.button(f"{app['icon']} {app['name']}", key=app["name"]):
                    st.session_state.selected_app = app["name"]
                    st.rerun()
else:
    st.button("🔙 Back to main menu", on_click=lambda: st.session_state.update(selected_app=None))
    selected = next(app for app in apps if app["name"] == st.session_state.selected_app)
    st.subheader(f"{selected['icon']} {selected['name']}")
    selected["func"]()
