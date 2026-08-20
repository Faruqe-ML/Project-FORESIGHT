import streamlit as st

st.write("MAIN START")

try:
    import api
    st.write("✅ api")
except Exception as e:
    st.error(f"❌ api: {e}")

try:
    from app_pages.category_performance import show_category_performance
    st.write("✅ category_performance")
except Exception as e:
    st.error(f"❌ category_performance: {e}")

try:
    from app_pages.executive_dashboard import show_executive
    st.write("✅ executive")
except Exception as e:
    st.error(f"❌ executive: {e}")