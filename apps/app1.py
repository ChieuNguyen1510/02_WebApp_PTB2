import streamlit as st

# ===== Các hàm chuyển đổi đơn vị =====

def convert_unit(value, from_unit, to_unit, factors):
    return value * factors[from_unit] / factors[to_unit]

def run():
    st.title("🧮 Convert Unit")

    tabs = st.tabs(["Force", "Length", "Pressure", "Moment"])

    # ========== Tab Force ==========
    with tabs[0]:
        st.subheader("🔧 Force")
        factors = {
            "N": 1,
            "daN": 10,
            "kN": 1_000,
            "T": 9_806.65,
        }
        unit_list = list(factors.keys())

        value = st.number_input("Value conversion", value=1.0, key="force_val")
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.radio("From:", unit_list, key="force_from")
        with col2:
            to_unit = st.radio("To:", unit_list, key="force_to")

        result = convert_unit(value, from_unit, to_unit, factors)
        st.markdown(f"### ✅ Result: **{value} {from_unit} = {result:.4f} {to_unit}**")

    # ========== Tab Length ==========
    with tabs[1]:
        st.subheader("📏 Length")
        factors = {
            "mm": 1,
            "cm": 10,
            "m": 1000,
            "km": 1_000_000,
            "inch": 25.4,
            "ft": 304.8,
        }
        unit_list = list(factors.keys())

        value = st.number_input("Value conversion", value=1.0, key="len_val")
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.radio("From:", unit_list, key="len_from")
        with col2:
            to_unit = st.radio("To:", unit_list, key="len_to")

        result = convert_unit(value, from_unit, to_unit, factors)
        st.markdown(f"### ✅ Result: **{value} {from_unit} = {result:.4f} {to_unit}**")

    # ========== Tab Pressure ==========
    with tabs[2]:
        st.subheader("💥 Pressure")
        factors = {
            "Pa": 1,
            "kPa": 1_000,
            "MPa": 1_000_000,
            "bar": 100_000,
            "atm": 101_325,
            "psi": 6_894.76,
        }
        unit_list = list(factors.keys())

        value = st.number_input("Value conversion", value=1.0, key="pressure_val")
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.radio("From:", unit_list, key="pressure_from")
        with col2:
            to_unit = st.radio("To:", unit_list, key="pressure_to")

        result = convert_unit(value, from_unit, to_unit, factors)
        st.markdown(f"### ✅ Result: **{value} {from_unit} = {result:.4f} {to_unit}**")

    # ========== Tab Moment ==========
    with tabs[3]:
        st.subheader("🔄 Moment")
        factors = {
            "N.m": 1,
            "kN.m": 1_000,
            "tf.m": 9_806.65,
        }
        unit_list = list(factors.keys())

        value = st.number_input("Value conversion", value=1.0, key="moment_val")
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.radio("From:", unit_list, key="moment_from")
        with col2:
            to_unit = st.radio("To:", unit_list, key="moment_to")

        result = convert_unit(value, from_unit, to_unit, factors)
        st.markdown(f"### ✅ Result: **{value} {from_unit} = {result:.4f} {to_unit}**")
