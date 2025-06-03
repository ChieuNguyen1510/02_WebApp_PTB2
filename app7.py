
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def run():
    lang = st.session_state.get("language", "en")
    def _(en, vi): return vi if lang == "vi" else en

    st.subheader(_("📐 Structural Section Calculator", "📐 Tính toán tiết diện"))

    section_type = st.selectbox(
        _("Select section type:", "Chọn loại tiết diện:"),
        ["⬜ Rectangle", "🔲 Hollow Box", "⬛ H-Section", "⬤ Circle", "⭕ Hollow Circle"]
    )

    def draw_rectangle(b, h):
        fig, ax = plt.subplots()
        ax.add_patch(plt.Rectangle((0, 0), b, h, fill=True, color='lightblue'))
        ax.set_xlim(-b*0.1, b*1.1)
        ax.set_ylim(-h*0.1, h*1.1)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig

    def draw_hollow_box(B, H, b, h):
        fig, ax = plt.subplots()
        ax.add_patch(plt.Rectangle((0, 0), B, H, color='lightblue'))
        ax.add_patch(plt.Rectangle(((B - b) / 2, (H - h) / 2), b, h, color='white'))
        ax.set_xlim(-B*0.1, B*1.1)
        ax.set_ylim(-H*0.1, H*1.1)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig

    def draw_circle(d):
        fig, ax = plt.subplots()
        ax.add_patch(plt.Circle((0, 0), d/2, color='lightblue'))
        ax.set_xlim(-d*0.6, d*0.6)
        ax.set_ylim(-d*0.6, d*0.6)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig

    def draw_hollow_circle(D, d):
        fig, ax = plt.subplots()
        ax.add_patch(plt.Circle((0, 0), D/2, color='lightblue'))
        ax.add_patch(plt.Circle((0, 0), d/2, color='white'))
        ax.set_xlim(-D*0.6, D*0.6)
        ax.set_ylim(-D*0.6, D*0.6)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig

    def draw_h_section(h, b, tw, tf):
        fig, ax = plt.subplots(figsize=(2.5, 4))
        ax.set_aspect('equal')
        ax.add_patch(plt.Rectangle((-b/2, h/2 - tf), b, tf, color='lightblue'))
        ax.add_patch(plt.Rectangle((-b/2, -h/2), b, tf, color='lightblue'))
        ax.add_patch(plt.Rectangle((-tw/2, -h/2 + tf), tw, h - 2*tf, color='lightblue'))
        ax.set_xlim(-b, b)
        ax.set_ylim(-h/2 - 10, h/2 + 10)
        ax.axis('off')
        return fig

    st.markdown("### " + _("Input Parameters", "Thông số đầu vào"))
    if section_type == "⬜ Rectangle":
        b = st.number_input(_("Width b (mm)", "Rộng b (mm)"), value=200.0)
        h = st.number_input(_("Height h (mm)", "Cao h (mm)"), value=300.0)
        A = b * h
        Ix = b * h**3 / 12
        Iy = h * b**3 / 12
        fig = draw_rectangle(b, h)
    elif section_type == "🔲 Hollow Box":
        B = st.number_input(_("Outer width B (mm)", "Rộng ngoài B (mm)"), value=300.0)
        H = st.number_input(_("Outer height H (mm)", "Cao ngoài H (mm)"), value=400.0)
        t = st.number_input(_("Wall thickness t (mm)", "Chiều dày thành t (mm)"), value=20.0)
        b = B - 2*t
        h = H - 2*t
        A = B*H - b*h
        Ix = (B * H**3 - b * h**3) / 12
        Iy = (H * B**3 - h * b**3) / 12
        fig = draw_hollow_box(B, H, b, h)
    elif section_type == "⬛ H-Section":
        h = st.number_input(_("Total height h (mm)", "Chiều cao tổng h (mm)"), value=300.0)
        b = st.number_input(_("Flange width b (mm)", "Chiều rộng cánh b (mm)"), value=150.0)
        tf = st.number_input(_("Flange thickness tf (mm)", "Bề dày cánh tf (mm)"), value=20.0)
        tw = st.number_input(_("Web thickness tw (mm)", "Bề dày bụng tw (mm)"), value=10.0)
        A = 2 * b * tf + (h - 2*tf) * tw
        Ix = (b * h**3 - (b - tw) * (h - 2*tf)**3) / 12
        Iy = 2 * (tf * b**3 / 12 + tf * b * (h/2 - tf/2)**2)
        fig = draw_h_section(h, b, tw, tf)
    elif section_type == "⬤ Circle":
        d = st.number_input(_("Diameter d (mm)", "Đường kính d (mm)"), value=100.0)
        A = np.pi * (d**2) / 4
        Ix = Iy = (np.pi * d**4) / 64
        fig = draw_circle(d)
    elif section_type == "⭕ Hollow Circle":
        D = st.number_input(_("Outer diameter D (mm)", "Đường kính ngoài D (mm)"), value=120.0)
        d = st.number_input(_("Inner diameter d (mm)", "Đường kính trong d (mm)"), value=80.0)
        A = (np.pi/4) * (D**2 - d**2)
        Ix = Iy = (np.pi/64) * (D**4 - d**4)
        fig = draw_hollow_circle(D, d)

    Wx = Ix / (h/2) if 'h' in locals() and h != 0 else "-"
    Wy = Iy / (b/2) if 'b' in locals() and b != 0 else "-"

    st.markdown("### " + _("Section Properties", "Thuộc tính tiết diện"))
    st.write(f"- A = {A:.2f} mm²")
    st.write(f"- Ix = {Ix:.2f} mm⁴")
    st.write(f"- Iy = {Iy:.2f} mm⁴")
    st.write(f"- Wx = {Wx if Wx == '-' else f'{Wx:.2f}'} mm³")
    st.write(f"- Wy = {Wy if Wy == '-' else f'{Wy:.2f}'} mm³")

    col_input, col_fig = st.columns([2, 1])
    with col_fig:
        st.markdown("### " + _("Illustration", "Hình minh họa"))
        st.pyplot(fig)
