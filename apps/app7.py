import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def draw_i_section(h, b, tw, tf):
    fig, ax = plt.subplots(figsize=(2.5, 4))
    ax.set_aspect('equal')
    ax.add_patch(plt.Rectangle((-b/2, h/2 - tf), b, tf, color='lightblue'))
    ax.add_patch(plt.Rectangle((-b/2, -h/2), b, tf, color='lightblue'))
    ax.add_patch(plt.Rectangle((-tw/2, -h/2 + tf), tw, h - 2*tf, color='lightblue'))
    ax.set_xlim(-b, b)
    ax.set_ylim(-h/2 - 10, h/2 + 10)
    ax.axis('off')
    return fig

def run():
    st.subheader("📐 Structural Section Calculator")

    mode = st.radio("Select input mode:", ["Manual Input", "Standard Section (Eurocode)"], horizontal=True)

    if mode == "Manual Input":
        st.markdown("### 🔧 Manual Section Input")
        shape = st.selectbox("Section Type", ["I-beam"])
        col1, col2 = st.columns(2)
        with col1:
            h = st.number_input("Height h (mm)", value=200.0)
            b = st.number_input("Flange width b (mm)", value=100.0)
            tw = st.number_input("Web thickness tw (mm)", value=5.0)
            tf = st.number_input("Flange thickness tf (mm)", value=8.0)
        with col2:
            st.markdown("### 📷 Section Illustration")
            fig = draw_i_section(h, b, tw, tf)
            st.pyplot(fig)

        # Tính toán thuộc tính
        A = 2 * b * tf + (h - 2*tf) * tw
        Ix = (b * h**3 - (b - tw) * (h - 2*tf)**3) / 12
        Iy = 2 * (tf * b**3 / 12 + tf * b * (h/2 - tf/2)**2)
        Wx = Ix / (h/2)
        Wy = Iy / (b/2)

        st.markdown("### 📊 Section Properties")
        st.write(f"- Area A = {A:.2f} mm²")
        st.write(f"- Ix = {Ix:.2f} mm⁴")
        st.write(f"- Iy = {Iy:.2f} mm⁴")
        st.write(f"- Wx = {Wx:.2f} mm³")
        st.write(f"- Wy = {Wy:.2f} mm³")

    else:
        st.markdown("### 📚 Select Standard Section")
        df = pd.read_csv("apps/standard_sections_eurocode.csv")
        section_type = st.selectbox("Section Type", sorted(df['Type'].unique()))
        filtered = df[df['Type'] == section_type]
        section = st.selectbox("Section", filtered['Section'])
        selected = filtered[filtered['Section'] == section].iloc[0]

        st.markdown("### 📊 Section Properties")
        for col in ["A_mm2", "Ix_mm4", "Iy_mm4", "Wx_mm3", "Wy_mm3"]:
            st.write(f"- {col.replace('_', ' ')}: {selected[col]:,.2f}")

        st.markdown("### 📷 Illustration")
        if selected["Type"] == "IPE":
            fig = draw_i_section(
                selected["h_mm"],
                selected["b_mm"],
                selected["tw_mm"],
                selected["tf_mm"]
            )
            st.pyplot(fig)
        else:
            st.info("Illustration not available for this section type.")
