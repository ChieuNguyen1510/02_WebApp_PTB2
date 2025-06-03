import streamlit as st
try:
    from apps import app1, app2, app3, app4, app5
except ImportError as e:
    st.error(f"Failed to load app modules: {str(e)}")
    st.stop()

st.set_page_config(page_title="General Engineering Toolkit", layout="centered")

# Danh sách apps
apps = [
    {"name": "Convert Unit", "icon": "🔁", "func": getattr(app1, "run", None)},
    {"name": "Concrete Strength", "icon": "🏗️", "func": getattr(app2, "run", None)},
    {"name": "Steel Strength", "icon": "🔩", "func": getattr(app3, "run", None)},
    {"name": "Reinforcement Area", "icon": "🧮", "func": getattr(app4, "run", None)},
    {"name": "Loading", "icon": "📦", "func": getattr(app5, "run", None)},
]
apps = [app for app in apps if app["func"] is not None]

# Custom CSS for buttons
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

if "selected_app" not in st.session_state:
    st.session_state.selected_app = None

# MAIN MENU
if st.session_state.selected_app is None:
    st.title("📱 General Engineering Toolkit")
    st.write("Select a tool below to perform engineering calculations.")
    num_cols = min(3, len(apps))
    for i in range(0, len(apps), num_cols):
        cols = st.columns(num_cols)
        for j, app in enumerate(apps[i:i + num_cols]):
            with cols[j]:
                if st.button(f"{app['icon']} {app['name']}", key=app["name"]):
                    st.session_state.selected_app = app["name"]
                    st.rerun()
        for j in range(len(apps[i:i + num_cols]), num_cols):
            with cols[j]:
                st.empty()
else:
    with st.sidebar:
        if st.button("🔙 Back to main menu"):
            st.session_state.selected_app = None
            st.rerun()
    try:
        selected = next(app for app in apps if app["name"] == st.session_state.selected_app)
        st.subheader(f"{selected['icon']} {selected['name']}")
        selected["func"]()
    except StopIteration:
        st.error("Selected app not found. Returning to main menu.")
        st.session_state.selected_app = None
        st.rerun()
    except Exception as e:
        st.error(f"Error in {st.session_state.selected_app}: {str(e)}")