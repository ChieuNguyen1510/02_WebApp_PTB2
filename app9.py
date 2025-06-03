
import streamlit as st
import numpy as np

def run():
    lang = st.session_state.get("language", "en")
    def _(en, vi): return vi if lang == "vi" else en

    st.subheader(_("🔩 Anchor Bolt Capacity Checker", "🔩 Kiểm tra khả năng chịu lực bu lông neo"))

    st.markdown("### " + _("Input Parameters", "Thông số đầu vào"))

    # Bulong
    d = st.selectbox(_("Bolt diameter (mm)", "Đường kính bu lông (mm)"), [12, 16, 20, 24, 30, 36], index=2)
    hef = st.number_input(_("Embedment depth hef (mm)", "Chiều sâu cắm hef (mm)"), value=120.0)
    fuk = st.number_input(_("Steel tensile strength fuk (MPa)", "Cường độ kéo thép fuk (MPa)"), value=600.0)
    fyk = st.number_input(_("Steel yield strength fyk (MPa)", "Giới hạn chảy thép fyk (MPa)"), value=500.0)

    # Bê tông
    fck = st.selectbox(_("Concrete strength class", "Cấp độ bền bê tông"), ["C20/25", "C25/30", "C30/37", "C35/45", "C40/50"], index=1)
    fck_val = int(fck.split("/")[0][1:])

    # Tải tác dụng
    N_ed = st.number_input(_("Axial tension N (kN)", "Lực kéo N (kN)"), value=20.0)
    V_ed = st.number_input(_("Shear force V (kN)", "Lực cắt V (kN)"), value=10.0)

    # Tính toán sức chịu tải đơn giản theo Eurocode EN 1992-4

    # 1. Sức chịu kéo của thép
    A_bolt = np.pi * (d/2)**2
    N_Rk_steel = A_bolt * fuk / 1e3  # kN

    # 2. Sức chịu kéo breakout bê tông (Eurocode công thức đơn giản)
    f_ctk = 0.3 * fck_val ** (2/3)
    N_Rk_concrete = 7.2 * f_ctk * hef**1.5 / 1e3  # kN, giả sử không gần mép

    # 3. Sức chịu cắt của thép
    V_Rk_steel = 0.6 * A_bolt * fyk / 1e3  # kN

    st.markdown("### " + _("Design Capacities", "Khả năng chịu lực thiết kế"))

    st.write(f"🧵 **Tensile capacity (steel):** {N_Rk_steel:.1f} kN")
    st.write(f"🧱 **Tensile capacity (concrete breakout):** {N_Rk_concrete:.1f} kN")
    st.write(f"↔️ **Shear capacity (steel):** {V_Rk_steel:.1f} kN")

    st.markdown("### " + _("Check Result", "Kết quả kiểm tra"))

    result_tension = N_ed < min(N_Rk_steel, N_Rk_concrete)
    result_shear = V_ed < V_Rk_steel

    if result_tension:
        st.success(_("✅ Tension check passed", "✅ Lực kéo đạt"))
    else:
        st.error(_("❌ Tension check failed", "❌ Lực kéo không đạt"))

    if result_shear:
        st.success(_("✅ Shear check passed", "✅ Lực cắt đạt"))
    else:
        st.error(_("❌ Shear check failed", "❌ Lực cắt không đạt"))
