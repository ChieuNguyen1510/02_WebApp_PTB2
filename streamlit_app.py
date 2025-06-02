import streamlit as st
from apps import app1, app2, app3, app4, app5

st.set_page_config(page_title="General Application", layout="centered")

# Danh sách apps (tên, icon, hàm)
apps = [
    {"name": "Convert Unit", "icon": "🔁", "func": app1.run},
    {"name": "Concrete Strength", "icon": "🏗️", "func": app2.run},
    {"name": "Steel Strength", "icon": "🔩", "func": app3.run},
    {"name": "Reinforcement Area", "icon": "🧮", "func": app4.run},
    {"name": "Loading", "icon": "📦", "func": app5.run},
]

# State để chuyển app
if "selected_app" not in st.session_state:
    st.session_state.selected_app = None

# Giao diện chính
if st.session_state.selected_app is None:
    st.title("📱 General Engineering Toolkit")

    num_cols = 3
    for i in range(0, len(apps), num_cols):
        cols = st.columns(num_cols)
        for j, app in enumerate(apps[i:i+num_cols]):
            with cols[j]:
                st.markdown(
                    f"""
                    <div style='text-align:center; border:1px solid #ccc; border-radius:12px; padding:20px; height:150px;'>
                        <div style='font-size:36px;'>{app['icon']}</div>
                        <div style='font-weight:bold; margin:10px 0;'>{app['name']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button(f"Open {app['name']}", key=app["name"]):
                    st.session_state.selected_app = app["name"]
                    st.rerun()
else:
    st.button("🔙 Back to main menu", on_click=lambda: st.session_state.update(selected_app=None))
    selected = next(app for app in apps if app["name"] == st.session_state.selected_app)
    st.subheader(f"{selected['icon']} {selected['name']}")
    selected["func"]()
