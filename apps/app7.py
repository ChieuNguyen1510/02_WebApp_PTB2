import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def run():
    lang = st.session_state.get("language", "en")
    def _(en, vi): return vi if lang == "vi" else en

    st.subheader(_("📐 Structural Section Calculator", "📐 Tính toán tiết diện"))

    # Radio button để chọn giữa Manual và Use Standard
    mode = st.radio(
        _("Select mode:", "Chọn chế độ:"),
        ["Manual", "Use Standard"],
        format_func=lambda x: _(x, "Nhập thủ công" if x == "Manual" else "Sử dụng tiết diện tiêu chuẩn")
    )

    # Bảng tra tiết diện tiêu chuẩn
    standard_sections = {
        "IPE - I": {
            "IPE 80": {"h": 80, "b": 46, "tw": 3.8, "tf": 5.2, "A": 7.64, "Ix": 80.1, "Iy": 8.49},
            "IPE 100": {"h": 100, "b": 55, "tw": 4.1, "tf": 5.7, "A": 10.3, "Ix": 171.0, "Iy": 15.9},
            "IPE 120": {"h": 120, "b": 64, "tw": 4.4, "tf": 6.3, "A": 13.2, "Ix": 317.8, "Iy": 27.7},
            "IPE 200": {"h": 200, "b": 100, "tw": 5.6, "tf": 8.5, "A": 28.5, "Ix": 1943.0, "Iy": 142.4},
            "IPE 240": {"h": 240, "b": 120, "tw": 6.2, "tf": 9.8, "A": 39.1, "Ix": 3892.0, "Iy": 290.2},
        },
        "SHS - ⬜": {
            "SHS 50x50x2": {"h": 50, "b": 50, "t": 2.0, "A": 3.81, "Ix": 17.0, "Iy": 17.0},
            "SHS 100x100x3": {"h": 100, "b": 100, "t": 3.0, "A": 11.7, "Ix": 166.5, "Iy": 166.5},
            "SHS 150x150x5": {"h": 150, "b": 150, "t": 5.0, "A": 28.3, "Ix": 614.9, "Iy": 614.9},
            "SHS 200x200x6": {"h": 200, "b": 200, "t": 6.0, "A": 45.4, "Ix": 1618.0, "Iy": 1618.0},
            "SHS 250x250x8": {"h": 250, "b": 250, "t": 8.0, "A": 75.4, "Ix": 3538.0, "Iy": 3538.0},
        }
    }

    def draw_rectangle(b, h):
        fig, ax = plt.subplots(figsize=(2, 2))  # Kích thước nhỏ gọn
        ax.add_patch(plt.Rectangle((0, 0), b, h, fill=True, color='#4A90E2'))
        ax.text(b/2, -h*0.05, f'b={b:.1f}mm', ha='center', va='top', fontsize=8)
        ax.text(-b*0.05, h/2, f'h={h:.1f}mm', ha='right', va='center', rotation=90, fontsize=8)
        max_dim = max(b, h)
        ax.set_xlim(-max_dim*0.1, max_dim*1.1)
        ax.set_ylim(-max_dim*0.1, max_dim*1.1)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig

    def draw_hollow_box(B, H, b, h):
        fig, ax = plt.subplots(figsize=(2, 2))  # Kích thước nhỏ gọn
        ax.add_patch(plt.Rectangle((0, 0), B, H, color='#4A90E2'))
        ax.add_patch(plt.Rectangle(((B - b) / 2, (H - h) / 2), b, h, color='white'))
        ax.text(B/2, -H*0.05, f'B={B:.1f}mm', ha='center', va='top', fontsize=8)
        ax.text(-B*0.05, H/2, f'H={H:.1f}mm', ha='right', va='center', rotation=90, fontsize=8)
        max_dim = max(B, H)
        ax.set_xlim(-max_dim*0.1, max_dim*1.1)
        ax.set_ylim(-max_dim*0.1, max_dim*1.1)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig

    def draw_circle(d):
        fig, ax = plt.subplots(figsize=(2, 2))  # Kích thước nhỏ gọn
        ax.add_patch(plt.Circle((0, 0), d/2, color='#4A90E2'))
        ax.text(0, -d*0.55, f'd={d:.1f}mm', ha='center', va='top', fontsize=8)
        max_dim = d
        ax.set_xlim(-max_dim*0.6, max_dim*0.6)
        ax.set_ylim(-max_dim*0.6, max_dim*0.6)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig

    def draw_hollow_circle(D, d):
        fig, ax = plt.subplots(figsize=(2, 2))  # Kích thước nhỏ gọn
        ax.add_patch(plt.Circle((0, 0), D/2, color='#4A90E2'))
        ax.add_patch(plt.Circle((0, 0), d/2, color='white'))
        ax.text(0, -D*0.55, f'D={D:.1f}mm', ha='center', va='top', fontsize=8)
        max_dim = D
        ax.set_xlim(-max_dim*0.6, max_dim*0.6)
        ax.set_ylim(-max_dim*0.6, max_dim*0.6)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig

    def draw_h_section(h, b, tw, tf):
        fig, ax = plt.subplots(figsize=(2, 2))  # Kích thước nhỏ gọn
        ax.add_patch(plt.Rectangle((-b/2, h/2 - tf), b, tf, color='#4A90E2'))
        ax.add_patch(plt.Rectangle((-b/2, -h/2), b, tf, color='#4A90E2'))
        ax.add_patch(plt.Rectangle((-tw/2, -h/2 + tf), tw, h - 2*tf, color='#4A90E2'))
        ax.text(0, h/2 + tf*0.5, f'h={h:.1f}mm', ha='center', va='bottom', fontsize=8)
        ax.text(b/2 + tw*0.5, 0, f'b={b:.1f}mm', ha='left', va='center', fontsize=8)
        max_dim = max(b, h)
        ax.set_xlim(-max_dim*0.6, max_dim*0.6)
        ax.set_ylim(-max_dim*0.6, max_dim*0.6)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig

    A = Ix = Iy = Wx = Wy = None
    fig = None

    if mode == "Manual":
        # Option 1: Nhập thủ công
        col_input, col_fig = st.columns([2, 1])

        with col_input:
            st.markdown("### " + _("Input Parameters", "Thông số đầu vào"))
            section_type = st.selectbox(
                _("Select section type:", "Chọn loại tiết diện:"),
                ["⬜ Rectangle", "🔲 Hollow Box", "⬛ H-Section", "⬤ Circle", "⭕ Hollow Circle"]
            )

            if section_type == "⬜ Rectangle":
                b = st.number_input(_("Width b (mm)", "Rộng b (mm)"), min_value=0.1, value=200.0)
                h = st.number_input(_("Height h (mm)", "Cao h (mm)"), min_value=0.1, value=300.0)
                A = b * h
                Ix = b * h**3 / 12
                Iy = h * b**3 / 12
                Wx = Ix / (h/2)
                Wy = Iy / (b/2)
                fig = draw_rectangle(b, h)

            elif section_type == "🔲 Hollow Box":
                B = st.number_input(_("Outer width B (mm)", "Rộng ngoài B (mm)"), min_value=0.1, value=300.0)
                H = st.number_input(_("Outer height H (mm)", "Cao ngoài H (mm)"), min_value=0.1, value=400.0)
                t = st.number_input(_("Wall thickness t (mm)", "Chiều dày thành t (mm)"), min_value=0.1, value=20.0)
                if B <= 2*t or H <= 2*t:
                    st.error(_("Outer dimensions must be greater than twice the wall thickness!", 
                               "Kích thước ngoài phải lớn hơn 2 lần chiều dày thành!"))
                    return
                b = B - 2*t
                h = H - 2*t
                A = B*H - b*h
                Ix = (B * H**3 - b * h**3) / 12
                Iy = (H * B**3 - h * b**3) / 12
                Wx = Ix / (H/2)
                Wy = Iy / (B/2)
                fig = draw_hollow_box(B, H, b, h)

            elif section_type == "⬛ H-Section":
                h = st.number_input(_("Total height h (mm)", "Chiều cao tổng h (mm)"), min_value=0.1, value=300.0)
                b = st.number_input(_("Flange width b (mm)", "Chiều rộng cánh b (mm)"), min_value=0.1, value=150.0)
                tf = st.number_input(_("Flange thickness tf (mm)", "Bề dày cánh tf (mm)"), min_value=0.1, value=20.0)
                tw = st.number_input(_("Web thickness tw (mm)", "Bề dày bụng tw (mm)"), min_value=0.1, value=10.0)
                if h <= 2*tf:
                    st.error(_("Total height must be greater than twice the flange thickness!", 
                               "Chiều cao tổng phải lớn hơn 2 lần bề dày cánh!"))
                    return
                if b <= tw:
                    st.error(_("Flange width must be greater than web thickness!", 
                               "Chiều rộng cánh phải lớn hơn bề dày bụng!"))
                    return
                A = 2 * b * tf + (h - 2*tf) * tw
                Ix = (b * h**3 - (b - tw) * (h - 2*tf)**3) / 12
                Iy = 2 * (tf * b**3 / 12 + tf * b * (h/2 - tf/2)**2)
                Wx = Ix / (h/2)
                Wy = Iy / (b/2)
                fig = draw_h_section(h, b, tw, tf)

            elif section_type == "⬤ Circle":
                d = st.number_input(_("Diameter d (mm)", "Đường kính d (mm)"), min_value=0.1, value=100.0)
                A = np.pi * (d**2) / 4
                Ix = Iy = (np.pi * d**4) / 64
                Wx = Wy = Ix / (d/4)
                fig = draw_circle(d)

            elif section_type == "⭕ Hollow Circle":
                D = st.number_input(_("Outer diameter D (mm)", "Đường kính ngoài D (mm)"), min_value=0.1, value=120.0)
                d = st.number_input(_("Inner diameter d (mm)", "Đường kính trong d (mm)"), min_value=0.0, value=80.0)
                if D <= d:
                    st.error(_("Outer diameter must be greater than inner diameter!", 
                               "Đường kính ngoài phải lớn hơn đường kính trong!"))
                    return
                A = (np.pi/4) * (D**2 - d**2)
                Ix = Iy = (np.pi/64) * (D**4 - d**4)
                Wx = Wy = Ix / (D/4)
                fig = draw_hollow_circle(D, d)

            # Hiển thị thuộc tính tiết diện
            st.markdown("### " + _("Section Properties", "Thuộc tính tiết diện"))
            if A is not None:
                st.write(f"- A = {A:.2f} mm²")
                st.write(f"- Ix = {Ix:.2f} mm⁴")
                st.write(f"- Iy = {Iy:.2f} mm⁴")
                st.write(f"- Wx = {Wx:.2f} mm³")
                st.write(f"- Wy = {Wy:.2f} mm³")

        with col_fig:
            if fig is not None:
                st.pyplot(fig)

    else:
        # Option 2: Tra cứu tiết diện tiêu chuẩn
        st.markdown("### " + _("Select Standard Section Type", "Chọn loại tiết diện tiêu chuẩn"))
        section_type = st.selectbox(
            _("Section type:", "Loại tiết diện:"),
            ["IPE - I", "SHS - ⬜"]
        )

        # Hiển thị bảng tra
        st.markdown("### " + _("Section Table", "Bảng tra tiết diện"))
        section_data = standard_sections[section_type]
        df = pd.DataFrame.from_dict(section_data, orient='index')
        if section_type == "IPE - I":
            df = df[["h", "b", "tw", "tf", "A", "Ix", "Iy"]]
            df.columns = ["h (mm)", "b (mm)", "tw (mm)", "tf (mm)", "A (cm²)", "Ix (cm⁴)", "Iy (cm⁴)"]
        elif section_type == "SHS - ⬜":
            df = df[["h", "b", "t", "A", "Ix", "Iy"]]
            df.columns = ["h (mm)", "b (mm)", "t (mm)", "A (cm²)", "Ix (cm⁴)", "Iy (cm⁴)"]
        
        # Định dạng bảng với pandas.Styler
        styler = df.style.set_table_styles([
            # In đậm tiêu đề cột
            {'selector': 'th.col_heading', 'props': [('font-weight', 'bold'), ('text-align', 'center')]},
            # In đậm tiêu đề hàng (index)
            {'selector': 'th.row_heading', 'props': [('font-weight', 'bold'), ('min-width', '200px'), ('text-align', 'left')]},
            # Đảm bảo cột đầu tiên rộng hơn
            {'selector': 'td.col0', 'props': [('min-width', '200px'), ('text-align', 'left')]}
        ])
        
        # CSS bổ sung để đảm bảo định dạng
        st.markdown(
            """
            <style>
            /* In đậm tiêu đề cột */
            .stDataFrame thead th {
                font-weight: bold !important;
                text-align: center !important;
            }
            /* In đậm và làm rộng cột đầu tiên (index) */
            .stDataFrame tbody th {
                font-weight: bold !important;
                min-width: 200px !important;
                text-align: left !important;
            }
            /* Đảm bảo độ rộng cột đầu tiên cho dữ liệu */
            .stDataFrame td:first-child {
                min-width: 200px !important;
                text-align: left !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        st.dataframe(styler, use_container_width=True, height=300)