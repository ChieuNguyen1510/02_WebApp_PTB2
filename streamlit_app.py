import streamlit as st
from apps import app1, app2, app3, app4, app5

st.set_page_config(page_title="General Application", layout="centered")

# Danh sách apps và hàm tương ứng
apps = {
    "Convert Unit": app1.run,
    "Concrete Strength": app2.run,
    "Steel Strength": app3.run,
    "Reinforcement Area": app4.run,
    "Loading": app5.run
}

# Giao diện chọn app (grid buttons)
if "selected_app" not in st.session_state:
    st.session_state.selected_app = None

if st.session_state.selected_app is None:
    st.title("📱 General Engineering Toolkit")

    # Hiển thị dạng lưới (2 hàng, 3 cột)
    app_names = list(apps.keys())
    num_per_row = 3
    for i in range(0, len(app_names), num_per_row):
        cols = st.columns(num_per_row)
        for j, name in enumerate(app_names[i:i+num_per_row]):
            with cols[j]:
                if st.button(name):
                    st.session_state.selected_app = name
                    st.rerun()
else:
    # Gọi app tương ứng
    st.button("🔙 Back to main menu", on_click=lambda: st.session_state.update(selected_app=None))
    st.subheader(f"🧩 App: {st.session_state.selected_app}")
    apps[st.session_state.selected_app]()
