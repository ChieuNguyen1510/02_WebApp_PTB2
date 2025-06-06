import streamlit as st
import pandas as pd
from io import BytesIO

def run():
    st.subheader("⚙️ Load Combination Generator (Eurocode)")

    st.markdown("Generate ULS and SLS load combinations automatically based on Eurocode.")

    # Step 1 – Load types (No Accidental A)
    st.markdown("### 1. Select load types")
    load_inputs = {
        "G": st.checkbox("🧱 Dead Load (G)", value=True),
        "Q": st.checkbox("👣 Live Load (Q)", value=True),
        "W": st.checkbox("🌬️ Wind Load (W)"),
        "S": st.checkbox("❄️ Snow Load (S)")
    }

    active_loads = [k for k, v in load_inputs.items() if v]
    if not active_loads:
        st.warning("Please select at least one load type.")
        return

    # Step 2 – Select combination type
    st.markdown("### 2. Select combination type")
    comb_types = st.multiselect(
        "Choose combination cases to generate",
        ["ULS (STR/GEO)", "SLS – Characteristic", "SLS – Frequent", "SLS – Quasi-permanent"],
        default=["ULS (STR/GEO)", "SLS – Characteristic"]
    )

    # Step 3 – Generate
    if st.button("⚡ Generate Load Combinations"):
        combinations = []

        # Define Eurocode load factors
        γ = {"G": 1.35, "Q": 1.5, "W": 1.5, "S": 1.5}
        ψ1 = {"Q": 0.5, "W": 0.2, "S": 0.2}
        ψ2 = {"Q": 0.3, "W": 0.0, "S": 0.2}

        # ULS
        if "ULS (STR/GEO)" in comb_types:
            for load in active_loads:
                if load != "G" and load in γ:
                    expr = f"{γ['G']}*G + {γ[load]}*{load}"
                    combinations.append(("ULS", expr))

        # SLS
        for label, psi in [
            ("SLS – Characteristic", {"G": 1.0, "Q": 1.0, "W": 1.0, "S": 1.0}),
            ("SLS – Frequent", {"G": 1.0, "Q": ψ1["Q"], "W": ψ1["W"], "S": ψ1["S"]}),
            ("SLS – Quasi-permanent", {"G": 1.0, "Q": ψ2["Q"], "W": ψ2["W"], "S": ψ2["S"]}),
        ]:
            if label in comb_types:
                expr = " + ".join(f"{psi[l]}*{l}" for l in active_loads if l in psi)
                combinations.append((label, expr))

        # Save result to session
        df = pd.DataFrame(combinations, columns=["Combination", "Expression"])
        st.session_state["combination_df"] = df

    # Step 4 – Display result
    if "combination_df" in st.session_state:
        df = st.session_state["combination_df"]
        st.markdown("### ✅ Load Combinations")
        st.dataframe(df, use_container_width=True)

        def to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name="LoadCombinations")
            return output.getvalue()

        col1, col2 = st.columns([4, 1])
        with col1:
            st.download_button(
                label="📥 Download as Excel",
                data=to_excel(df),
                file_name="load_combinations.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        with col2:
            if st.button("❌ Clear"):
                del st.session_state["combination_df"]
                st.rerun()
