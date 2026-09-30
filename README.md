# 📊 Engineering & Market Analytics Dashboard

An interactive, responsive analytical web application built with **Streamlit**, **NumPy**, and **Matplotlib**. Combines structural engineering simulation with e-commerce market intelligence.

---

## 🌟 Modules & Features

### 1. 🏗️ Mechanical Beam Stress & Deflection Simulator
- Solves classical **Euler-Bernoulli Beam Equations** for simply-supported beams.
- Real-time parametric slider controls:
  - Beam Span $L$
  - Concentrated Point Load $P$ & Load Location $a$
  - Uniformly Distributed Load $w$
  - Material Modulus of Elasticity $E$ & Second Moment of Area $I$
- Interactive engineering plots:
  - **Shear Force Diagram (SFD)**
  - **Bending Moment Diagram (BMD)**
  - **Deflection Curve $\delta(x)$** with calculated maximum deflection (mm) and reaction forces.

### 2. 📊 Market Intelligence & E-Commerce Analytics
- Upload custom `.xlsx` or `.csv` datasets or explore built-in market snapshots.
- Real-time calculation of key commercial metrics:
  - Average, minimum, and maximum market prices.
  - Active vendor distribution and discount percentages.
- One-click export of cleaned and validated Excel reports.

---

## 🚀 Installation & Local Run

1. **Clone repository:**
   ```bash
   git clone https://github.com/your-username/engineering-data-dashboard.git
   cd engineering-data-dashboard
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch application:**
   ```bash
   streamlit run app.py
   ```
   *The application will automatically open in your default browser at `http://localhost:8501`.*

---

## ☁️ 1-Click Free Cloud Deployment
This project is configured for instant deployment on **Streamlit Community Cloud**:
1. Fork or push this repository to your GitHub profile.
2. Sign in to [share.streamlit.io](https://share.streamlit.io/).
3. Select your repository, set the main file path to `app.py`, and click **Deploy**!

---

## 🛠️ Tech Stack
- **Web UI:** `streamlit`
- **Scientific Computing:** `numpy`, `scipy`
- **Visualization:** `matplotlib`
- **Data Manipulation:** `pandas`, `openpyxl`

---

## 👨‍💻 Author
**Ardavan Ghal-Eh**  
Mechanical Engineering Student, Sharif University of Technology  
*Focus: Computational Engineering, Automation & Interactive Data Applications*
