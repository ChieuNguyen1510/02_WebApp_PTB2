
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():
    lang = st.session_state.get("language", "en")
    def _(en, vi): return vi if lang == "vi" else en

    st.subheader(_("🧱 Column PM Interaction Checker", "🧱 Kiểm tra tương tác N-M cột"))

    st.markdown("### " + _("Input Parameters", "Thông số đầu vào"))

    # Vật liệu
    fcd = st.number_input(_("Concrete strength fcd (MPa)", "Cường độ bê tông fcd (MPa)"), value=17.0)
    fyd = st.number_input(_("Steel yield strength fyd (MPa)", "Cường độ chảy thép fyd (MPa)"), value=435.0)

    # Hình học
    b = st.number_input(_("Width b (mm)", "Chiều rộng b (mm)"), value=300.0)
    h = st.number_input(_("Height h (mm)", "Chiều cao h (mm)"), value=500.0)
    cover = st.number_input(_("Concrete cover (mm)", "Lớp bê tông bảo vệ (mm)"), value=25.0)

    # Thép
    n_bars = st.number_input(_("Total rebars (even, both sides)", "Tổng số thép (chia đều 2 cạnh)"), value=4, step=2)
    dia = st.selectbox(_("Bar diameter (mm)", "Đường kính thép (mm)"), [10, 12, 14, 16, 20, 25, 28, 32], index=3)

    # Nội lực
    Ned = st.number_input(_("Axial force Ned (kN)", "Lực dọc Ned (kN)"), value=800.0)
    Med = st.number_input(_("Bending moment Med (kNm)", "Mô men uốn Med (kNm)"), value=60.0)

    # Tính toán
    Ast = n_bars * (np.pi * dia**2 / 4)
    d = h - cover
    dp = cover
    ecu = 0.0035
    Es = 200000  # MPa
    epyd = fyd / Es

    N_list = []
    M_list = []

    e_list = np.linspace(-ecu, epyd*1.5, 200)

    for eps in e_list:
        # Giả sử kéo ở thép đáy, nén ở thép trên
        c = d * ecu / (ecu + eps) if eps > 0 else h  # tránh chia 0
        c = np.clip(c, 1e-3, h)
        x = c
        z = d - dp
        a = 0.8 * x
        Fc = fcd * a * b
        Fs = Ast * fyd if eps > epyd else Ast * Es * eps
        N = Fc + Fs * -1  # Trục N hướng xuống
        M = Fc * (d - a/2) * 1e-3 + Fs * z * 1e-3  # kNm

        N_list.append(N / 1e3)  # kN
        M_list.append(M)  # kNm

    st.markdown("### " + _("Interaction Diagram", "Biểu đồ tương tác"))

    fig, ax = plt.subplots()
    ax.plot(N_list, M_list, label=_("Interaction Curve", "Đường tương tác"))
    ax.plot(Ned, Med, "ro", label=_("Design Point", "Điểm tổ hợp"))
    ax.set_xlabel(_("Axial force N (kN)", "Lực dọc N (kN)"))
    ax.set_ylabel(_("Bending moment M (kNm)", "Mô men M (kNm)"))
    ax.set_title(_("N-M Interaction", "Tương tác N-M"))
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    # Kết luận
    is_safe = False
    for i in range(len(N_list)):
        if Ned <= N_list[i] and Med <= M_list[i]:
            is_safe = True
            break

    st.markdown("### " + _("Result", "Kết quả"))
    if is_safe:
        st.success(_("✅ The column is safe under the given loads.", "✅ Cột đạt với tổ hợp tải đã cho."))
    else:
        st.error(_("❌ The column is NOT safe under the given loads.", "❌ Cột không đạt với tổ hợp tải đã cho."))
