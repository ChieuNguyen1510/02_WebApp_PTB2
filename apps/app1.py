import streamlit as st

def convert_length(value, from_unit, to_unit):
    factors = {
        "mm": 1,
        "cm": 10,
        "m": 1000,
        "km": 1_000_000,
        "inch": 25.4,
        "ft": 304.8,
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_area(value, from_unit, to_unit):
    factors = {
        "mm²": 1,
        "cm²": 100,
        "m²": 1_000_000,
        "ha": 10_000_000_000,
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_force(value, from_unit, to_unit):
    factors = {
        "N": 1,
        "kN": 1_000,
        "MN": 1_000_000,
        "tf": 9_806.65,  # tấn lực
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_pressure(value, from_unit, to_unit):
    factors = {
        "Pa": 1,
        "kPa": 1_000,
        "MPa": 1_000_000,
        "psi": 6_894.76,
        "atm": 101_325,
    }
    return value * factors[from_unit] / factors[to_unit]

def run():
    st.header("🔁 Đổi Đơn Vị")

    category = st.selectbox("Chọn loại đơn vị:", ["Lực", "Độ dài", "Diện tích", "Áp lực"])

    if category == "Lực":
        units = ["N", "kN", "MN", "tf"]
        convert_fn = convert_force
    elif category == "Độ dài":
        units = ["mm", "cm", "m", "km", "inch", "ft"]
        convert_fn = convert_length
    elif category == "Diện tích":
        units = ["mm²", "cm²", "m²", "ha"]
        convert_fn = convert_area
    else:  # Áp lực
        units = ["Pa", "kPa", "MPa", "psi", "atm"]
        convert_fn = convert_pressure

    value = st.number_input("Giá trị cần đổi", value=0.0)
    from_unit = st.selectbox("Từ đơn vị", options=units, key="from")
    to_unit = st.selectbox("Sang đơn vị", options=units, key="to")

    if st.button("Chuyển đổi"):
        result = convert_fn(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
