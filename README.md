<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<div align="center">

[![Persian Documentation](https://img.shields.io/badge/مستندات-فارسی-green.svg?style=for-the-badge)](#persian-documentation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Rust Kernel](https://img.shields.io/badge/Kernel-Rust_Zero--Allocation-DEA584.svg?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg?style=for-the-badge)](https://github.com/ArdavanGhal-Eh/engineering-data-dashboard)
[![Stars](https://img.shields.io/github/stars/ArdavanGhal-Eh/engineering-data-dashboard?style=for-the-badge&color=gold)](https://github.com/ArdavanGhal-Eh/engineering-data-dashboard/stargazers)
[![Issues](https://img.shields.io/github/issues/ArdavanGhal-Eh/engineering-data-dashboard?style=for-the-badge&color=red)](https://github.com/ArdavanGhal-Eh/engineering-data-dashboard/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/ArdavanGhal-Eh/engineering-data-dashboard/pulls)

<br />

# 📊 Engineering Mechanics & Structural Dynamics Analytics Dashboard
### *Euler-Bernoulli Beam Solvers, 3D Mohr's Circle Stress Tensors & Vibration Campbell Resonance in Streamlit & Rust*

<p align="center">
  <b>A comprehensive engineering mechanics and structural dynamics web dashboard built with Streamlit, NumPy, Matplotlib, and an ultra-fast Rust computational kernel. Features interactive Euler-Bernoulli beam deflection and Shear Force / Bending Moment Diagrams (SFD/BMD), 2D/3D Mohr's Circle principal stress and Von Mises yield evaluation, and dynamic modal resonance tracking with Campbell diagrams for industrial motor RPM safety.</b>
  <br /><br />
  <a href="#-system-architecture--dashboard-modules"><strong>Explore Modules »</strong></a>
  &nbsp;•&nbsp;
  <a href="#-engineering-mechanics-formulation"><strong>Mechanics Formulation »</strong></a>
  &nbsp;•&nbsp;
  <a href="#-quickstart--installation"><strong>Quickstart Guide »</strong></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/ArdavanGhal-Eh/engineering-data-dashboard/issues"><strong>Report Issue</strong></a>
</p>

</div>

---

<!-- TABLE OF CONTENTS -->
<details open>
  <summary><h2 style="display: inline-block;">📑 Table of Contents</h2></summary>
  <ol>
    <li><a href="#-executive-summary--engineering-problem">Executive Summary & Engineering Problem</a></li>
    <li><a href="#-key-features--capabilities">Key Features & Capabilities</a></li>
    <li><a href="#-system-architecture--dashboard-modules">System Architecture & Dashboard Modules</a></li>
    <li><a href="#-engineering-mechanics-formulation">Engineering Mechanics Formulation</a></li>
    <li><a href="#-technology-stack">Technology Stack</a></li>
    <li><a href="#-repository-structure">Repository Structure</a></li>
    <li><a href="#-quickstart--installation">Quickstart & Installation</a></li>
    <li><a href="#-module-walkthrough--user-guide">Module Walkthrough & User Guide</a></li>
    <li><a href="#-roadmap--future-enhancements">Roadmap & Future Enhancements</a></li>
    <li><a href="#-contributing--license">Contributing & License</a></li>
    <li><a href="#-author--contact">Author & Contact</a></li>
    <li><a href="#persian-documentation"><b>🇮🇷 مستندات جامع مهندسی به زبان فارسی (Persian Documentation)</b></a></li>
  </ol>
</details>

---

## 📌 Executive Summary & Engineering Problem

In structural design, mechanical machinery sizing, and plant engineering:
1. **Disjointed Analysis Tools:** Mechanical engineers waste hours juggling disconnected spreadsheets, textbook charts, and heavy desktop FEA tools just to calculate fundamental beam deflections and Mohr's stress circles.
2. **Resonance Disaster Prevention:** Rotating industrial shafts, pumps, and turbine rotors operating near structural natural frequencies experience catastrophic resonance failure. Engineers need immediate Campbell diagram visualization showing safe operating RPM corridors.
3. **Interactive Visual Intuition:** Real-time design verification requires instant parameter sweeps (e.g., dynamically adjusting beam length, cross-section geometry, or material yield strength) with immediate interactive plot updates.

This project delivers a unified **Streamlit web application** accelerated by a **Rust computational kernel**, providing instantaneous mechanics evaluations in your browser.

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---

## ✨ Key Features & Capabilities

- 🏗️ **Euler-Bernoulli Beam Mechanics (`rust_beam_solver` & `app.py`):** Calculates internal shear forces, bending moments, slope, and deflection curves for simply-supported, cantilever, and overhanging beams with point and distributed loads.
- ⭕ **Interactive 2D & 3D Mohr's Circle (`mohr_circle_stress_analyzer.py`):** Visualizes transformation of plane stress tensors, resolves principal stresses ($\sigma_1, \sigma_2$), maximum in-plane shear ($\tau_{\max}$), and calculates Von Mises & Tresca safety factors.
- ⚡ **Campbell Resonance Diagram (`vibration_resonance_analyzer.py`):** Evaluates beam modal frequencies ($\omega_1, \omega_2, \omega_3$) and plots Campbell diagrams with motor operating speed lines and $\pm 15\%$ critical resonance exclusion corridors.
- 🦀 **High-Speed Rust Computational Kernel:** Offloads heavy numerical discretization loops to compiled Rust code for zero-latency slider updates.
- 📐 **Standard Structural Section Database:** Built-in section properties for European IPE beams, rectangular structural tubes, circular hollow sections, and solid shafts.

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---

## 🏗️ System Architecture & Dashboard Modules

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   Streamlit Interactive Web Interface                  │
│             (Sliders: Span L, Load P, Cross-Section, RPM, Stress)      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐
│   Module 1:      │       │   Module 2:      │       │   Module 3:      │
│ Beam Mechanics   │       │ Mohr's Circle    │       │ Modal Resonance  │
│ - SFD & BMD      │       │ - Stress Tensor  │       │ - Euler-Bernoulli│
│ - Deflection w(x)│       │ - Von Mises SF   │       │ - Campbell Chart │
└────────┬─────────┘       └────────┬─────────┘       └────────┬─────────┘
         │                          │                          │
         ▼                          ▼                          ▼
┌────────────────────────────────────────────────────────────────────────┐
│         Rust Accelerated Computational Core (rust_beam_solver)         │
│          Zero-allocation analytical solvers and Matplotlib plots       │
└────────────────────────────────────────────────────────────────────────┘
```

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---

## 📐 Engineering Mechanics Formulation

### 1. Euler-Bernoulli Beam Governing Equation
$$E I \frac{d^4 w(x)}{dx^4} = q(x)$$

Internal reactions:
- Bending Moment: $M(x) = -E I \frac{d^2 w}{dx^2}$
- Shear Force: $V(x) = \frac{d M}{dx} = -E I \frac{d^3 w}{dx^3}$
- Maximum Normal Stress: $\sigma_{\max} = \frac{|M_{\max}| \cdot c}{I}$

### 2. Plane Stress Transformation & Mohr's Circle
Given stress state $(\sigma_x, \sigma_y, \tau_{xy})$:

$$\text{Center: } \sigma_{\text{avg}} = \frac{\sigma_x + \sigma_y}{2}, \quad \text{Radius: } R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

$$\text{Principal Stresses: } \sigma_{1,2} = \sigma_{\text{avg}} \pm R, \quad \tau_{\max} = R$$

$$\text{Von Mises Equivalent Stress: } \sigma_v = \sqrt{\sigma_1^2 - \sigma_1 \sigma_2 + \sigma_2^2}$$

### 3. Continuous Beam Modal Frequencies & Campbell Resonance
The $n$-th natural frequency of an Euler-Bernoulli beam:

$$\omega_n = \beta_n^2 \sqrt{\frac{E I}{\rho A}} \quad (\text{rad/s}), \quad f_n = \frac{\omega_n}{2\pi} \quad (\text{Hz})$$

*The Campbell diagram maps excitation harmonic orders ($1\times, 2\times, 4\times\text{ RPM}$) against natural frequencies to pinpoint intersection resonance hazards.*

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---

## 🛠️ Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Web Interface** | [Streamlit](https://streamlit.io/) | Interactive dashboard layout and real-time reactive sliders |
| **Numerics** | NumPy & SciPy | Matrix operations, polynomial interpolation, and roots |
| **Plotting Engine**| Matplotlib | Scientific engineering graphs (SFD, BMD, Mohr, Campbell) |
| **Rust Kernel** | Rust (2021 Edition) | High-speed zero-allocation numerical beam solver |

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---

## 📂 Repository Structure

```text
engineering-data-dashboard/
├── app.py                      # Master Streamlit multi-tab web application
├── market_data_sample.xlsx     # Companion market intelligence sample
├── mohr_circle_stress_analyzer.py # 2D/3D Mohr's circle & tensor transformation
├── README.md                   # Comprehensive technical documentation
├── requirements.txt            # Python dependencies
├── vibration_resonance_analyzer.py # Campbell diagram & modal frequency analyzer
└── rust_beam_solver/
    ├── Cargo.toml              # Rust crate manifest
    └── src/
        └── lib.rs              # Zero-allocation compiled beam mechanics solver
```

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---

## 🚀 Quickstart & Installation

### Prerequisites
- Python `3.10+`
- Rust toolchain (`cargo`, optional for compiling the native kernel)

### Setup Instructions
```bash
# 1. Clone repository
git clone https://github.com/ArdavanGhal-Eh/engineering-data-dashboard.git
cd engineering-data-dashboard

# 2. Setup virtual environment & dependencies
python -m venv venv
source venv/bin/activate   # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt

# 3. Launch the interactive web dashboard
streamlit run app.py
```

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---

## 💻 Module Walkthrough & User Guide

1. **Beam Analysis Tab:**
   - Select beam support condition (Simply Supported / Cantilever / Fixed-Fixed).
   - Define point loads $P$ and distributed loads $q$.
   - View real-time Shear Force Diagram (SFD), Bending Moment Diagram (BMD), and elastic deflection curve $w(x)$.
2. **Mohr's Stress Circle Tab:**
   - Input normal stresses $\sigma_x, \sigma_y$ and shear stress $\tau_{xy}$.
   - Inspect interactive circle graph with principal stress markers $\sigma_1, \sigma_2$ and angle $\theta_p$.
   - Evaluate Von Mises safety factor relative to material yield strength.
3. **Resonance & Campbell Tab:**
   - Configure beam geometry and material density.
   - Enter machine operating RPM range.
   - Inspect Campbell diagram highlighting critical speeds and dangerous operating bands.

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---

## 🗺️ Roadmap & Future Enhancements

- [x] Multi-tab Streamlit dashboard architecture
- [x] Euler-Bernoulli SFD/BMD and deflection solver
- [x] 2D & 3D Mohr's circle stress tensor transformation
- [x] Campbell diagram & vibration resonance hazard indicator
- [x] Rust computational acceleration kernel
- [ ] Timoshenko beam theory (shear deformation for stocky beams)
- [ ] Direct export of generated engineering calculation reports to PDF

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---

## 🤝 Contributing & License

Contributions, bug reports, and optimizations are welcome! Feel free to open an issue or submit a Pull Request.

Distributed under the **MIT License**. See `LICENSE` for details.

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---

## 👤 Author & Contact

**Ardavan Ghal-Eh**  
*Department of Mechanical Engineering, Sharif University of Technology*  
- **GitHub:** [@ArdavanGhal-Eh](https://github.com/ArdavanGhal-Eh)
- **Profile:** [github.com/ArdavanGhal-Eh](https://github.com/ArdavanGhal-Eh)

<p align="right">(<a href="#readme-top">Back to top ↑</a>)</p>

---
---

<a id="persian-documentation"></a>

# 🇮🇷 بخش ۲: مستندات جامع مهندسی به زبان فارسی (Persian Documentation)

<div align="center">
  <a href="#readme-top"><strong>بازگشت به ابتدای مستندات انگلیسی (Back to Top / English) ↑</strong></a>
</div>

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

<br />

<div align="center">
  <a href="#readme-top"><strong>بازگشت به ابتدای صفحه (Back to Top) ↑</strong></a>
</div>
