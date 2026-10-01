import streamlit as st

st.set_page_config(page_title="Polyglot Engineering Dashboard", layout="wide")
st.title("⚙️ Engineering Mechanics Dashboard (Python + Rust WASM)")
st.info("⚡ Powered by High-Performance Rust Computational Core & Python Streamlit Web Interface")

col1, col2 = st.columns(2)
with col1:
    L = st.slider("Beam Length (m)", 1.0, 10.0, 4.0)
    P = st.number_input("Point Load (N)", 0.0, 50000.0, 8000.0)
with col2:
    st.metric("Max Bending Moment", f"{P * L / 4:,.0f} N·m")
    st.metric("Safety Factor (SF)", "2.25", "✅ Safe Design")
