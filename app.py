import io
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Engineering Mechanics & Market Analytics Suite",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("⚙️ Engineering Mechanics & Market Intelligence Dashboard")
st.markdown("Developed by **Ardavan Ghal-Eh** | Sharif University of Technology")
st.markdown("---")

tab1, tab2 = st.tabs([
    "🏗️ تحلیل تنش و خیز تیر مکانیکی (Beam Stress & Deflection)",
    "📊 هوش تجاری و رصد قیمت‌های بازار (Market Analytics)"
])

# -------------------------------------------------------------
# TAB 1: MECHANICAL BEAM DEFLECTION, STRESS & SAFETY FACTOR
# -------------------------------------------------------------
with tab1:
    st.header("تحلیل استحکام مکانیکی: تنش خمشی، ضریب اطمینان و خیز تیر (Euler-Bernoulli)")
    st.caption("محاسبه دقیق تنش ماکزیمم و ضریب اطمینان طراحی بر اساس تسلیم مواد مهندسی")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("۱. ابعاد و بارگذاری تیر")
        L = st.slider("طول تیر L (متر)", min_value=1.0, max_value=10.0, value=4.0, step=0.5)
        P = st.number_input("بار متمرکز P (نیوتن)", min_value=0.0, max_value=100000.0, value=8000.0, step=500.0)
        a = st.slider("موقعیت اعمال بار a (متر)", min_value=0.0, max_value=float(L), value=float(L / 2), step=0.1)
        w = st.number_input("بار گسترده یکنواخت w (N/m)", min_value=0.0, max_value=20000.0, value=1500.0, step=250.0)
        
        st.subheader("۲. انتخاب پروفیل و جنس مقطع")
        profile_type = st.selectbox(
            "نوع مقطع سازه‌ای:",
            ["تیرآهن IPE 140 (I-Beam)", "قوطی پروفیل مستطیلی 100x60x4", "شافت استوانه‌ای توپر Ø50mm"]
        )

        material_choice = st.selectbox(
            "جنس متریال مهندسی:",
            ["فولاد ساختمانی St37 (Sy = 235 MPa)", "فولاد آلیاژی CK45 (Sy = 370 MPa)", "آلومینیوم مهندسی 6061-T6 (Sy = 276 MPa)"]
        )

        # Profile parameters (SI Units: m, m^4, m)
        if "IPE 140" in profile_type:
            I = 5.41e-6       # m^4
            y_max = 0.070     # m (h/2)
            desc_profile = "h=140mm, b=73mm"
        elif "قوطی" in profile_type:
            I = 1.62e-6       # m^4
            y_max = 0.050     # m
            desc_profile = "100x60mm, t=4mm"
        else: # Round 50mm
            r = 0.025
            I = (np.pi * (r**4)) / 4
            y_max = r
            desc_profile = "قطر 50 میلی‌متر"

        # Material Yield Strength Sy (Pa) and E (Pa)
        if "St37" in material_choice:
            Sy = 235e6
            E = 205e9
        elif "CK45" in material_choice:
            Sy = 370e6
            E = 210e9
        else:
            Sy = 276e6
            E = 70e9

    with col2:
        x = np.linspace(0, L, 500)
        b = L - a
        
        R1 = (P * b / L) + (w * L / 2)
        R2 = (P * a / L) + (w * L / 2)

        V = np.zeros_like(x)
        M = np.zeros_like(x)
        deflection = np.zeros_like(x)

        for idx, xi in enumerate(x):
            v_val = R1 - w * xi
            if xi > a:
                v_val -= P
            V[idx] = v_val

            m_val = R1 * xi - 0.5 * w * (xi ** 2)
            if xi > a:
                m_val -= P * (xi - a)
            M[idx] = m_val

            y_w = (w * xi / (24 * E * I)) * (L**3 - 2 * L * (xi**2) + xi**3)
            if xi <= a:
                y_p = (P * b * xi / (6 * E * I * L)) * (L**2 - b**2 - xi**2)
            else:
                y_p = (P * a * (L - xi) / (6 * E * I * L)) * (2 * L * xi - xi**2 - a**2)
            deflection[idx] = -(y_w + y_p) * 1000  # mm

        max_M = np.max(np.abs(M))
        max_delta = np.max(np.abs(deflection))
        
        # Max Bending Stress: sigma = (M * y) / I  (in MPa)
        sigma_max_pa = (max_M * y_max) / I
        sigma_max_mpa = sigma_max_pa / 1e6
        sy_mpa = Sy / 1e6
        safety_factor = sy_mpa / max(1e-6, sigma_max_mpa)

        # Metrics display
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("حداکثر لنگر خمشی (|M_max|)", f"{max_M:,.0f} N·m")
        m2.metric("حداکثر خیز وسط دهانه (δ)", f"{max_delta:.2f} mm")
        m3.metric("حداکثر تنش خمشی (σ_max)", f"{sigma_max_mpa:.1f} MPa")
        
        sf_label = "✅ طراحی ایمن" if safety_factor >= 1.5 else ("⚠️ لب‌مرز" if safety_factor >= 1.0 else "❌ شکست سازه‌ای")
        m4.metric("ضریب اطمینان (Safety Factor)", f"{safety_factor:.2f}", sf_label)

        # Plotting diagrams
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(9, 7.5), sharex=True)
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
        ax3.set_xlabel("طول تیر x (متر)")
        ax3.grid(True, linestyle="--", alpha=0.6)

        st.pyplot(fig)

# -------------------------------------------------------------
# TAB 2: MARKET DATA INTELLIGENCE & PRICE ANALYTICS
# -------------------------------------------------------------
with tab2:
    st.header("هوش تجاری و رصد رقبا (Market Intelligence)")
    st.caption("پایش قیمت‌ها، وضعیت تخفیف‌ها و ارزیابی اقتصادی کالاهای بازار")

    uploaded_file = st.file_uploader("بارگذاری فایل اکسل یا CSV داده‌های بازار:", type=["xlsx", "csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(".xlsx") else pd.read_csv(uploaded_file)
            st.success(f"فایل با موفقیت بارگذاری شد ({len(df):,} ردیف).")
        except Exception as e:
            st.error(f"خطا در خواندن فایل: {e}")
            df = None
    else:
        sample_records = [
            {"عنوان کالا": "لپ‌تاپ ایسوس Vivobook 15", "دسته‌بندی": "لپ‌تاپ", "قیمت (تومان)": 38500000, "تخفیف (%)": 10, "فروشنده": "دیجی‌کالا", "ارزش خرید": "🔥 عالی"},
            {"عنوان کالا": "مک‌بوک ایر اپل M2", "دسته‌بندی": "لپ‌تاپ", "قیمت (تومان)": 89000000, "تخفیف (%)": 5, "فروشنده": "تأمین‌کننده پایتخت", "ارزش خرید": "⚖️ منصفانه"},
            {"عنوان کالا": "گوشی سامسونگ S24 Ultra", "دسته‌بندی": "موبایل", "قیمت (تومان)": 72000000, "تخفیف (%)": 15, "فروشنده": "دیجی‌لند", "ارزش خرید": "🔥 عالی"},
            {"عنوان کالا": "مانیتور 27 اینچ شیائومی 165Hz", "دسته‌بندی": "مانیتور", "قیمت (تومان)": 14200000, "تخفیف (%)": 18, "فروشنده": "دیجی‌کالا", "ارزش خرید": "🔥 عالی"},
            {"عنوان کالا": "هدفون بی‌سیم سونی WH-1000XM5", "دسته‌بندی": "صوتی", "قیمت (تومان)": 19500000, "تخفیف (%)": 8, "فروشنده": "فروشگاه مرکزی", "ارزش خرید": "⚖️ منصفانه"},
            {"عنوان کالا": "ماوس لاجیتک MX Master 3S", "دسته‌بندی": "لوازم جانبی", "قیمت (تومان)": 6200000, "تخفیف (%)": 20, "فروشنده": "بازرگانی پارس", "ارزش خرید": "🔥 عالی"}
        ]
        df = pd.DataFrame(sample_records)

    if df is not None and not df.empty:
        col_m1, col_m2, col_m3 = st.columns(3)
        price_col = [c for c in df.columns if "قیمت" in c or "price" in c.lower()]
        
        if price_col:
            p_name = price_col[0]
            col_m1.metric("تعداد محصولات مانیتور شده", f"{len(df)} قلم")
            col_m2.metric("میانگین قیمت بازار", f"{df[p_name].mean():,.0f} تومان")
            col_m3.metric("بیشترین تخفیف فعال", f"{df['تخفیف (%)'].max()}%" if 'تخفیف (%)' in df else "N/A")

        st.dataframe(df, use_container_width=True)

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Cleaned_Data")
        st.download_button(
            label="📥 دانلود فایل اکسل پردازش‌شده",
            data=buffer.getvalue(),
            file_name="market_intelligence_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
