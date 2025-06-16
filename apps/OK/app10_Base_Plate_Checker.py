import streamlit as st
import numpy as np

def run():
    lang = st.session_state.get("language", "en")
    def _(en, vi): return vi if lang == "vi" else en

    st.subheader(_("📏 Base Plate Checker", "📏 Kiểm tra bản đế cột"))

    st.markdown("### " + _("Input Parameters", "Thông số đầu vào"))

    # Tải trọng
    N = st.number_input(_("Axial force N (kN)", "Lực dọc N (kN)"), value=1000.0)
    M = st.number_input(_("Moment M (kNm)", "Mô men M (kNm)"), value=50.0)

    # Bản đế
    a = st.number_input(_("Plate width a (mm)", "Chiều rộng bản đế a (mm)"), value=300.0)
    b = st.number_input(_("Plate height b (mm)", "Chiều dài bản đế b (mm)"), value=300.0)
    t = st.number_input(_("Plate thickness t (mm)", "Chiều dày bản đế t (mm)"), value=20.0)
    fy = st.number_input(_("Steel yield strength fy (MPa)", "Cường độ chảy thép fy (MPa)"), value=250.0)

    st.markdown("### " + _("Calculation", "Tính toán"))

    A = a * b / 1e6  # m²
    e = M * 1e6 / (N * 1e3) if N != 0 else 0  # mm, eccentricity

    if abs(e) < b / 2:
        sigma_max = (N / A) * (1 + (6 * e / b))  # kN/m²
        sigma_min = (N / A) * (1 - (6 * e / b))  # kN/m²
    else:
        sigma_max = (2 * N) / (a * b / 1e3)  # tam giác áp lực
        sigma_min = 0

    # Uốn bản đế
    m = b / 2  # mm
    q = sigma_max * 1e3  # N/m² → Pa
    M_max = q * m**2 / 8  # Nm/m
    W = (a * 1e-3) * (t * 1e-3)**2 / 6  # m³/m
    sigma_b = M_max / W / 1e6  # MPa

    st.write(f"🧮 " + _("Max pressure under plate", "Ứng suất nén lớn nhất dưới bản đế") + f": {sigma_max:.2f} kN/m²")
    st.write(f"📐 " + _("Bending stress in plate", "Ứng suất uốn trong bản đế") + f": {sigma_b:.2f} MPa")

    st.markdown("### " + _("Result", "Kết quả"))

    if sigma_b <= fy:
        st.success(_("✅ Plate thickness OK", "✅ Chiều dày bản đế đạt"))
    else:
        st.error(_("❌ Plate too thin, increase thickness", "❌ Bản đế quá mỏng, cần tăng chiều dày"))
