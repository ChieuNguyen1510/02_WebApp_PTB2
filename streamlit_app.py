import streamlit as st
from apps import app1, app2, app3, app4, app5

st.set_page_config(page_title="General Application", layout="centered")

# Khai báo danh sách app với tên, icon, hàm
apps = [
    {"name": "Convert Unit", "icon": "🔁", "func": app1.run},
    {"name": "Concrete Strength", "icon": "🏗️", "func": app2.run},
    {"name": "Steel Strength", "icon": "🔩", "func": app3.run},
    {"name": "Reinforcement Area", "icon": "🧮", "func": app4.run},
    {"name": "Loading", "icon": "📦", "func": app5.run},
]

# Quản lý trạng thái app
if "selected_app" not in st.session_state:
    st.session_state.selected_app = None

# ========== Giao diện chính ==========
if st.session_state.selected_app is None:
    st.title("📱 General Engineering Toolkit")

    # Sắp xếp dạng grid (3 app mỗi hàng)
    num_cols = 3
    for i in range(0, len(apps), num_cols):
        cols = st.columns(num_cols)
        for j, app in enumerate(apps[i:i+num_cols]):
            with cols[j]:
                button_label = f"{app['icon']}  \n**{app['name']}**"
                st.markdown(
                    f"""
                    <div style="border:1px solid #ccc; padding:20px; border-radius:10px; text-align:center; height:120px; display:flex; flex-direction:column; justify-content:center;">
                        <form action="" method="post">
                            <button style="all:unset; cursor:pointer;" type="submit" name="app" value="{app['name']}">
                                <div style="font-size:36px;">{app['icon']}</div>
                                <div style="font-weight:bold; font-size:14px;">{app['name']}</div>
                            </button>
                        </form>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if "app" in st.session_state and st.session_state.app == app["name"]:
                    st.session_state.selected_app = app["name"]
                    st.rerun()
else:
    st.button("🔙 Back to main menu", on_click=lambda: st.session_state.update(selected_app=None))
    app = next(a for a in apps if a["name"] == st.session_state.selected_app)
    st.subheader(f"{app['icon']} {app['name']}")
    app["func"]()
