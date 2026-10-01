# 📊 Polyglot Engineering Dashboard (Python + Rust WASM)

An interactive structural mechanics suite combining a **high-performance Rust computational kernel** with a **Python Streamlit analytical web interface**.

## 🌟 Polyglot Architecture
- **Rust Computational Kernel (`rust_beam_solver/`):** High-speed Euler-Bernoulli beam stress and safety factor calculations.
- **Python Web UI (`app.py`):** Interactive sliders, live Plotly diagrams, and material selectors.

## 🎯 Real-World Applications & Cross-Industry Impact
### ⚙️ Structural & Mechanical Engineering
- Instant sizing of I-beams and hollow profiles against yield stress ($S_y$).
### 🌐 Cross-Industry & Software Applications
- In-browser WebAssembly engineering simulations with near-native execution speed.
- Real-time physics engine structural mechanics for simulation and gaming.

## 🚀 Execution
```bash
# Rust Kernel:
cd rust_beam_solver && cargo build --release

# Streamlit App:
pip install -r requirements.txt && streamlit run app.py
```

## 👨‍💻 Author
**Ardavan Ghal-Eh** | Sharif University of Technology
