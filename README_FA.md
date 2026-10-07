<a id="readme-top"></a>

<div align="center">

[![English Documentation](https://img.shields.io/badge/Documentation-English-blue.svg?style=for-the-badge)](README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![UI: Streamlit / Dash](https://img.shields.io/badge/UI-Streamlit_&_Plotly-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![DSP: SciPy](https://img.shields.io/badge/DSP-SciPy_Signal-8CAAE6.svg?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org/)

<br />

# 📊 داشبورد بصری‌سازی و تحلیل داده‌های مهندسی (Engineering Data Dashboard)
### *تحلیل چندمتغیره در لحظه، طیف‌سنجی فوریه (FFT)، نمودارهای ترمودینامیکی و بصری‌سازی تعاملی در وب*

<p align="center">
  <b>یک داشبورد تحلیلی و مهندسی کامل و ماژولار برای پایش و اعتبارسنجی داده‌های حسگرهای فیزیکی، سیستم‌های ارتعاشی و چرخه‌های مکانیکی. این سیستم امکان دریافت فایل‌های CSV حجیم تله‌متری را فراهم کرده و ابزارهای پیشرفته‌ای نظیر تبدیل فوریه سریع (FFT)، فیلترهای باترورث (Butterworth Filter) و تحلیل‌های آماری توزیع تنش و دما را با بازخورد گرافیکی زنده ارائه می‌دهد.</b>
  <br /><br />
  <a href="#-قابلیت‌های-تحلیلی-داشبورد"><strong>ابزارهای پردازش سیگنال »</strong></a>
  &nbsp;•&nbsp;
  <a href="#-معماری-پردازش-و-نمایش"><strong>معماری داشبورد »</strong></a>
  &nbsp;•&nbsp;
  <a href="#-نحوه-اجرا"><strong>دستورالعمل اجرا »</strong></a>
</p>

</div>

---

<details open>
  <summary><h2 style="display: inline-block;">📑 فهرست مطالب</h2></summary>
  <ol>
    <li><a href="#-چکیده-پروژه">چکیده پروژه</a></li>
    <li><a href="#-قابلیت‌های-تحلیلی-داشبورد">قابلیت‌های تحلیلی داشبورد</a></li>
    <li><a href="#-معماری-پردازش-و-نمایش">معماری پردازش و نمایش</a></li>
    <li><a href="#-فرمولاسیون-ریاضی-پردازش-سیگنال">فرمولاسیون ریاضی پردازش سیگنال</a></li>
    <li><a href="#-پشته-فناوری">پشته فناوری</a></li>
    <li><a href="#-ساختار-فایل‌ها">ساختار فایل‌ها</a></li>
    <li><a href="#-نحوه-اجرا">نحوه اجرا</a></li>
    <li><a href="#-مجوز">مجوز</a></li>
  </ol>
</details>

---

## 📌 چکیده پروژه

در آزمون‌های تجربی مکانیک و تله‌متری خطوط تولید، حسگرها حجم عظیمی از داده‌های ارتعاشی، فشاری و دمایی با نویز محیطی بالا تولید می‌کنند. تحلیل سریع این داده‌ها نیازمند محیطی تعاملی و کاربرپسند است که بدون نیاز به کدنویسی مجدد، ابزارهای پردازش سیگنال و آمار مهندسی را در اختیار متخصصان قرار دهد. این پروژه محیطی یکپارچه جهت مصورسازی و پالایش داده‌های مهندسی به کمک پایتون و وب مدرن مهیا ساخته است.

---

## 🚀 قابلیت‌های تحلیلی داشبورد

- **آنالیز طیفی فرکانسی (FFT Spectrum Analysis):** محاسبه چگالی طیفی توان و تشخیص مؤلفه‌های فرکانسی غالب سیستم‌های نوسانی و دوار.
- **فیلترینگ دیجیتال سیگنال:** فیلترهای پایین‌گذر، بالاگذر و میان‌گذر باترورث (Butterworth Filters) برای حذف نویزهای فرکانس بالای اندازه‌گیری.
- **نمودارهای فاز و چرخه‌های ترمودینامیکی (Phase & State Diagrams):** ترسیم نمودارهای فشار-حجم ($P-V$) و دما-آنتروپی ($T-S$).
- **بصری‌سازی تعاملی با Plotly:** امکان بزرگ‌نمایی بدون افت کیفیت، جابجایی روی نمودار و بررسی داده‌های هر نقطه در میلی‌ثانیه‌های بحرانی.

---

## 🏗 معماری پردازش و نمایش

```
[Raw Engineering CSV / Telemetry Log]
               │
               ▼
     [Pandas Data Pipeline] ─── (Missing Value Imputation / Resampling)
               │
               ▼
    [Signal Processing Core]
         ├─ SciPy Butterworth Filtering (Low-pass / Band-pass)
         ├─ Fast Fourier Transform (FFT) & Power Spectral Density
         └─ Statistical Metrics (Kurtosis, Crest Factor, RMS)
               │
               ▼
[Interactive Dashboard Engine] (Streamlit / Plotly Core)
         ├─ Dynamic Time-Series Waveforms
         ├─ Frequency Spectrum Visualizer
         └─ Data Export (Processed CSV / Summary PDF)
```

---

## 📐 فرمولاسیون ریاضی پردازش سیگنال

### ۱. تبدیل فوریه گسسته (Discrete Fourier Transform - DFT)
تبدیل سیگنال حوزه زمان $x[n]$ به حوزه فرکانس $X[k]$:
$$X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-j \frac{2\pi}{N} k n}, \quad k = 0, 1, \dots, N-1$$

### ۲. فاکتور برآمدگی سیگنال (Crest Factor)
برای تشخیص ضربات مکانیکی اولیه و خرابی زودرس یاتاقان‌ها:
$$CF = \frac{\max |x(t)|}{x_{\text{RMS}}} = \frac{x_{\text{peak}}}{\sqrt{\frac{1}{N}\sum_{n=1}^{N} x[n]^2}}$$

---

## 💻 پشته فناوری

- **رابط کاربری و سرور وب:** `Streamlit` / `Plotly`
- **پردازش عددی و سیگنال:** `NumPy`, `SciPy.signal`
- **مدیریت دیتافریم‌ها:** `Pandas`
- **زبان پیاده‌سازی:** Python 3.10+

---

## 📂 ساختار فایل‌ها

```
04-engineering-data-dashboard/
├── dashboard.py         # اپلیکیشن اصلی داشبورد Streamlit
├── signal_utils.py      # توابع فیلترینگ و تبدیل فوریه
├── sample_data/         # داده‌های نمونه تله‌متری حسگرها
├── requirements.txt     # کتابخانه‌های مورد نیاز
├── README.md            # مستندات انگلیسی
└── README_FA.md         # مستندات فارسی
```

---

## ⚙️ نحوه اجرا

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```
سپس مرورگر را در آدرس `http://localhost:8501` باز کرده و فایل داده مورد نظر را آپلود نمایید.

---

## 📄 مجوز
این پروژه تحت مجوز [MIT](https://opensource.org/licenses/MIT) منتشر شده است.
