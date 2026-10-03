# 📊 Engineering Mechanics & Market Intelligence Interactive Dashboard

A dual-module interactive engineering and business analytics web application developed with **Streamlit**, **NumPy**, **Matplotlib**, and a high-performance **Rust computational kernel**. Bridges structural beam mechanics (bending stress, deflection, and safety factor validation) with e-commerce market price intelligence.

---

## 🌟 Modules Overview

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│          ⚙️ Engineering Mechanics & Market Intelligence Dashboard           │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
│  Tab 1: Structural Mechanics Engine  │  │  Tab 2: Market Intelligence Engine   │
│  - Euler-Bernoulli Beam Equations    │  │  - E-Commerce Price Monitoring       │
│  - SFD & BMD Interactive Diagrams    │  │  - Dynamic Excel / CSV File Upload   │
│  - Section Modulus (IPE, Tube, Shaft)│  │  - Price Distributions & Metrics     │
│  - Bending Stress & Yield Safety     │  │  - 1-Click Cleaned Excel Export      │
└──────────────────────────────────────┘  └──────────────────────────────────────┘
```

---

## 🏗️ Module 1: Structural Beam Mechanics & Stress Analysis

### 📐 Mathematical Formulation (Euler-Bernoulli Beam Theory)
The governing differential equation for beam deflection $w(x)$:
$$E I \frac{d^4 w}{dx^4} = q(x)$$

For a simply-supported beam of span $L$ subjected to a point load $P$ at distance $a$ and a uniform distributed load $w$:
1. **Support Reactions:**
   $$R_1 = \frac{P (L - a)}{L} + \frac{w L}{2}, \quad R_2 = \frac{P a}{L} + \frac{w L}{2}$$

2. **Shear Force $V(x)$ & Bending Moment $M(x)$:**
   $$V(x) = R_1 - w x - P \cdot \mathcal{H}(x - a)$$
   $$M(x) = R_1 x - \frac{1}{2} w x^2 - P (x - a) \cdot \mathcal{H}(x - a)$$
   *(where $\mathcal{H}$ is the Heaviside step function)*

3. **Maximum Bending Stress ($\sigma_{max}$):**
   $$\sigma_{max} = \frac{|M_{max}| \cdot y_{max}}{I} = \frac{|M_{max}|}{Z}$$

4. **Design Safety Factor ($\text{SF}$):**
   $$\text{SF} = \frac{S_y}{\sigma_{max}}$$
   - $\text{SF} \ge 1.5$: ✅ طراحی ایمن (Safe Structural Design)
   - $1.0 \le \text{SF} < 1.5$: ⚠️ هشدار لب‌مرز (Marginal / Requires Review)
   - $\text{SF} < 1.0$: ❌ شکست سازه‌ای و تسلیم پلاستیک (Plastic Failure)

### 🔩 Cross-Section & Material Database
- **Standard Profiles:**
  - **تیرآهن IPE 140 (I-Beam):** $I_x = 5.41 \times 10^{-6} \text{ m}^4$, $y_{max} = 70\text{ mm}$
  - **قوطی پروفیل مستطیلی 100x60x4mm:** $I_x = 1.62 \times 10^{-6} \text{ m}^4$, $y_{max} = 50\text{ mm}$
  - **شافت استوانه‌ای توپر Ø50mm:** $I = \frac{\pi r^4}{4}$, $y_{max} = 25\text{ mm}$
- **Alloy Materials:**
  - **فولاد ساختمانی St37:** $S_y = 235\text{ MPa}$, $E = 205\text{ GPa}$
  - **فولاد آلیاژی CK45:** $S_y = 370\text{ MPa}$, $E = 210\text{ GPa}$
  - **آلومینیوم هوافضایی 6061-T6:** $S_y = 276\text{ MPa}$, $E = 70\text{ GPa}$

---

## 📊 Module 2: Market Intelligence & Price Analytics
- Interactive drag-and-drop file uploader accepting external `.xlsx` and `.csv` workbooks.
- Real-time calculation of market averages, price spreads (min/max), and discount distributions.
- Built-in data cleaning routine with immediate in-memory Excel export button.

---

## ⚡ High-Performance Rust Kernel (`rust_beam_solver/`)
Includes a companion Rust library that computes beam deflection profiles and safety factors using zero-allocation stack memory, ready for compilation to WebAssembly (WASM) for in-browser client-side execution.

---


---

## 🌊 Module 3: Dynamic Vibration & Structural Resonance Analyzer ()
- **Natural Frequency Modal Analysis:** Solves Euler-Bernoulli beam vibration eigenfrequencies:
  42777f_n = rac{n^2 \pi}{2 L^2} \sqrt{rac{E I}{ho A}} \quad (	ext{Hz})42777
- **Rotational Machinery Resonance Check:** Compares operating motor RPM ({exc} = 	ext{RPM} / 60$) against structural natural frequencies.
- **Resonance Hazard Detection:** Flags a $\pm 15\%$ dangerous excitation proximity band with automated engineering corrective recommendations.
- **Quick Run:**
  

## 🚀 Installation & Local Run

### 1. Clone Repository
```bash
git clone https://github.com/ArdavanGhal-Eh/engineering-data-dashboard.git
cd engineering-data-dashboard
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Application
```bash
streamlit run app.py
```
*The interactive dashboard will automatically open at `http://localhost:8501`.*

### 4. (Optional) Build Rust Computational Kernel
```bash
cd rust_beam_solver
cargo build --release
```

---

## ☁️ 1-Click Cloud Deployment
This project is pre-configured for free instant deployment on **Streamlit Community Cloud**:
1. Push your repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io/).
3. Connect your repository, specify `app.py`, and click **Deploy**!

---

## 🛠️ Tech Stack
- **Web UI & State Management:** `streamlit`
- **Scientific Computing:** `numpy`, `scipy`
- **Plotting & Visuals:** `matplotlib` (Seaborn styles)
- **High-Performance Kernel:** Rust 1.70+
- **Data Engineering:** `pandas`, `openpyxl`

---

## 👨‍💻 Author
**Ardavan Ghal-Eh**  
Mechanical Engineering Student, Sharif University of Technology  
*Focus: Structural Mechanics, Scientific Computing & Interactive Dashboards*
