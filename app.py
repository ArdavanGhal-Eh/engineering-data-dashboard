import io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Engineering & Market Analytics Suite",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom header
st.title("⚙️ Engineering & Market Analytics Dashboard")
st.markdown("Developed by **Ardavan Ghal-Eh** | Sharif University of Technology")
st.markdown("---")

tab1, tab2 = st.tabs(["🏗️ تحلیل تیر مکانیکی (Beam Deflection Simulator)", "📊 تحلیل داده‌های بازار و قیمت‌ها (Market Intelligence)"])

# -------------------------------------------------------------
# TAB 1: MECHANICAL BEAM DEFLECTION & STRESS
# -------------------------------------------------------------
with tab1:
    st.header("تحلیل مهندسی: نیروی برشی، گشتاور خمشی و خیز تیر (Euler-Bernoulli Beam)")
    st.caption("محاسبه تحلیلی پارامتریک برای تیر دو سر ساده تحت بار متمرکز و بار گسترده یکنواخت")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("پارامترهای ورودی تیر")
        L = st.slider("طول تیر (m)", min_value=1.0, max_value=10.0, value=5.0, step=0.5)
        P = st.number_input("بار متمرکز P (N)", min_value=0.0, max_value=50000.0, value=5000.0, step=500.0)
        a = st.slider("موقعیت بار متمرکز a (m)", min_value=0.0, max_value=float(L), value=float(L / 2), step=0.1)
        w = st.number_input("بار گسترده یکنواخت w (N/m)", min_value=0.0, max_value=10000.0, value=1000.0, step=200.0)
        
        st.markdown("**مشخصات مقطع و جنس:**")
        E_gpa = st.number_input("مدول یانگ E (GPa) - فولاد: 200", min_value=10.0, max_value=500.0, value=200.0)
        I_cm4 = st.number_input("ممان اینرسی I (cm^4)", min_value=10.0, max_value=10000.0, value=300.0)

        E = E_gpa * 1e9
        I = I_cm4 * 1e-8

    with col2:
        # Analytical Beam Calculation
        x = np.linspace(0, L, 500)
        b = L - a
        
        # Reactions for simply supported beam:
        # Due to P: R1_p = P*b/L, R2_p = P*a/L
        # Due to w: R1_w = w*L/2, R2_w = w*L/2
        R1 = (P * b / L) + (w * L / 2)
        R2 = (P * a / L) + (w * L / 2)

        # Shear force V(x) and Moment M(x)
        V = np.zeros_like(x)
        M = np.zeros_like(x)
        deflection = np.zeros_like(x)

        for idx, xi in enumerate(x):
            # Shear force
            v_val = R1 - w * xi
            if xi > a:
                v_val -= P
            V[idx] = v_val

            # Bending moment
            m_val = R1 * xi - 0.5 * w * (xi ** 2)
            if xi > a:
                m_val -= P * (xi - a)
            M[idx] = m_val

            # Deflection approx for central load + UDL
            y_w = (w * xi / (24 * E * I)) * (L**3 - 2 * L * (xi**2) + xi**3)
            if xi <= a:
                y_p = (P * b * xi / (6 * E * I * L)) * (L**2 - b**2 - xi**2)
            else:
                y_p = (P * a * (L - xi) / (6 * E * I * L)) * (2 * L * xi - xi**2 - a**2)
            deflection[idx] = -(y_w + y_p) * 1000  # in mm (downward is negative)

        max_M = np.max(np.abs(M))
        max_delta = np.max(np.abs(deflection))

        m1, m2, m3 = st.columns(3)
        m1.metric("عکس‌العمل تکیه‌گاه چپ (R1)", f"{R1:,.1f} N")
        m2.metric("حداکثر گشتاور خمشی (|M_max|)", f"{max_M:,.1f} N·m")
        m3.metric("حداکثر خیز تیر (Max Deflection)", f"{max_delta:.2f} mm")

        # Plotting
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(9, 7), sharex=True)
        plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

        ax1.plot(x, V / 1000, color="crimson", lw=2)
        ax1.fill_between(x, 0, V / 1000, alpha=0.15, color="crimson")
        ax1.set_ylabel("نیروی برشی V (kN)")
        ax1.grid(True, linestyle="--", alpha=0.6)

        ax2.plot(x, M / 1000, color="navy", lw=2)
        ax2.fill_between(x, 0, M / 1000, alpha=0.15, color="navy")
        ax2.set_ylabel("گشتاور خمشی M (kN·m)")
        ax2.grid(True, linestyle="--", alpha=0.6)

        ax3.plot(x, deflection, color="forestgreen", lw=2)
        ax3.fill_between(x, 0, deflection, alpha=0.15, color="forestgreen")
        ax3.set_ylabel("خیز تیر δ (mm)")
        ax3.set_xlabel("موقعیت در راستای طول تیر x (m)")
        ax3.grid(True, linestyle="--", alpha=0.6)

        st.pyplot(fig)

# -------------------------------------------------------------
# TAB 2: MARKET DATA INTELLIGENCE & PRICE ANALYTICS
# -------------------------------------------------------------
with tab2:
    st.header("هوش تجاری و رصد قیمت‌های بازار (E-Commerce Market Analytics)")
    st.caption("تجزیه و تحلیل داده‌های استخراج‌شده از مارکت‌پلیس‌ها و مقایسه قیمت تأمین‌کنندگان")

    # Generate or upload dataset
    uploaded_file = st.file_uploader("بارگذاری فایل داده اکسل یا CSV سفارشی (اختیاری):", type=["xlsx", "csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(".xlsx") else pd.read_csv(uploaded_file)
            st.success(f"فایل با موفقیت بارگذاری شد ({len(df)} ردیف).")
        except Exception as e:
            st.error(f"خطا در خواندن فایل: {e}")
            df = None
    else:
        # Built-in synthetic market sample
        sample_records = [
            {"عنوان کالا": "لپ‌تاپ ایسوس Vivobook 15", "دسته‌بندی": "لپ‌تاپ", "قیمت (تومان)": 38500000, "تخفیف (%)": 10, "فروشنده": "دیجی‌کالا", "امتیاز": 4.6},
            {"عنوان کالا": "مک‌بوک ایر اپل M2", "دسته‌بندی": "لپ‌تاپ", "قیمت (تومان)": 89000000, "تخفیف (%)": 5, "فروشنده": "تأمین‌کننده پایتخت", "امتیاز": 4.9},
            {"عنوان کالا": "گوشی سامسونگ S24 Ultra", "دسته‌بندی": "موبایل", "قیمت (تومان)": 72000000, "تخفیف (%)": 12, "فروشنده": "دیجی‌لند", "امتیاز": 4.8},
            {"عنوان کالا": "مانیتور گیمینگ 27 اینچ شیائومی", "دسته‌بندی": "مانیتور", "قیمت (تومان)": 14200000, "تخفیف (%)": 15, "فروشنده": "دیجی‌کالا", "امتیاز": 4.4},
            {"عنوان کالا": "هدفون بی‌سیم سونی WH-1000XM5", "دسته‌بندی": "صوتی", "قیمت (تومان)": 19500000, "تخفیف (%)": 8, "فروشنده": "فروشگاه مرکزی", "امتیاز": 4.7},
            {"عنوان کالا": "اس‌اس‌دی 1 ترابایت سامسونگ T7", "دسته‌بندی": "ذخیره‌سازی", "قیمت (تومان)": 6800000, "تخفیف (%)": 0, "فروشنده": "دیجی‌کالا", "امتیاز": 4.5},
            {"عنوان کالا": "ماوس لاجیتک MX Master 3S", "دسته‌بندی": "لوازم جانبی", "قیمت (تومان)": 6200000, "تخفیف (%)": 20, "فروشنده": "بازرگانی پارس تک", "امتیاز": 4.9},
            {"عنوان کالا": "کیبورد مکانیکی تسکو GK-8128", "دسته‌بندی": "لوازم جانبی", "قیمت (تومان)": 2800000, "تخفیف (%)": 10, "فروشنده": "دیجی‌کالا", "امتیاز": 4.2}
        ]
        df = pd.DataFrame(sample_records)

    if df is not None and not df.empty:
        # High level metrics
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        price_col = [c for c in df.columns if "قیمت" in c or "price" in c.lower()]
        
        if price_col:
            p_name = price_col[0]
            col_m1.metric("تعداد محصولات مانیتور شده", f"{len(df)} قلم")
            col_m2.metric("میانگین قیمت بازار", f"{df[p_name].mean():,.0f} تومان")
            col_m3.metric("کمترین قیمت", f"{df[p_name].min():,.0f} تومان")
            col_m4.metric("بیشترین قیمت", f"{df[p_name].max():,.0f} تومان")

        st.subheader("جدول جامع اقلام استخراج شده")
        st.dataframe(df, use_container_width=True)

        # Download button
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Data")
        st.download_button(
            label="📥 دانلود فایل اکسل تمیزشده",
            data=buffer.getvalue(),
            file_name="market_cleaned_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
