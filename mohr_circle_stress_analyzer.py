"""
Mohr's Circle & Principal Stress Tensor Analyzer Module
Part of Engineering & Market Analytics Dashboard Suite
Author: Ardavan Ghal-Eh | Sharif University of Technology
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any, Tuple


class MohrCircleStressAnalyzer:
    """
    Computes 2D plane stress transformations, principal normal stresses (sigma_1, sigma_2),
    maximum in-plane shear stress (tau_max), and evaluates Von Mises and Tresca failure criteria.
    """

    def __init__(self):
        pass

    def analyze_plane_stress(
        self,
        sigma_x: float,
        sigma_y: float,
        tau_xy: float,
        yield_strength_mpa: float = 235.0  # St37 Steel default
    ) -> Dict[str, Any]:
        """
        sigma_x, sigma_y, tau_xy: stresses in MPa
        yield_strength_mpa: Material yield strength in MPa
        """
        center = (sigma_x + sigma_y) / 2.0
        radius = np.sqrt(((sigma_x - sigma_y) / 2.0) ** 2 + tau_xy ** 2)

        sigma_1 = center + radius
        sigma_2 = center - radius
        tau_max = radius

        # Principal angle in degrees
        theta_p_rad = 0.5 * np.arctan2(2.0 * tau_xy, (sigma_x - sigma_y))
        theta_p_deg = np.degrees(theta_p_rad)

        # Von Mises Equivalent Stress (Plane Stress)
        sigma_vm = np.sqrt(sigma_1 ** 2 - sigma_1 * sigma_2 + sigma_2 ** 2)

        # Tresca Equivalent Stress (Max shear stress criterion)
        # In plane stress, considering sigma_3 = 0
        s3 = 0.0
        s_vals = sorted([sigma_1, sigma_2, s3])
        sigma_tresca = s_vals[-1] - s_vals[0]

        # Safety Factors
        sf_vm = yield_strength_mpa / sigma_vm if sigma_vm > 0 else 999.0
        sf_tresca = yield_strength_mpa / sigma_tresca if sigma_tresca > 0 else 999.0

        # Safety Status
        if sf_vm >= 1.5:
            verdict = "✅ طراحی ایمن و پایدار (Safe Design)"
        elif sf_vm >= 1.0:
            verdict = "⚠️ لب‌مرز تسلیم الاستیک (Marginal Safety)"
        else:
            verdict = "❌ شکست سازه‌ای و تسلیم پلاستیک (Plastic Failure)"

        return {
            "center_mpa": round(center, 2),
            "radius_mpa": round(radius, 2),
            "sigma_1_mpa": round(sigma_1, 2),
            "sigma_2_mpa": round(sigma_2, 2),
            "tau_max_mpa": round(tau_max, 2),
            "theta_p_degrees": round(theta_p_deg, 2),
            "von_mises_stress_mpa": round(sigma_vm, 2),
            "tresca_stress_mpa": round(sigma_tresca, 2),
            "safety_factor_von_mises": round(sf_vm, 2),
            "safety_factor_tresca": round(sf_tresca, 2),
            "yield_strength_mpa": yield_strength_mpa,
            "status_verdict": verdict
        }

    def plot_mohr_circle(
        self,
        sigma_x: float,
        sigma_y: float,
        tau_xy: float,
        yield_strength_mpa: float = 235.0,
        output_filepath: str = "mohr_circle_plot.png"
    ) -> str:
        """Generates publication-quality Mohr's Circle diagram."""
        data = self.analyze_plane_stress(sigma_x, sigma_y, tau_xy, yield_strength_mpa)
        center = data["center_mpa"]
        radius = data["radius_mpa"]

        fig, ax = plt.subplots(figsize=(8, 7))

        # Circle theta
        angles = np.linspace(0, 2 * np.pi, 200)
        c_x = center + radius * np.cos(angles)
        c_y = radius * np.sin(angles)

        ax.plot(c_x, c_y, 'b-', linewidth=2.0, label="Mohr's Circle")
        ax.plot([center], [0], 'ko', label=f'Center ({center:.1f}, 0)')

        # Principal points
        ax.plot([data["sigma_1_mpa"]], [0], 'ro', label=f'$\\sigma_1$ = {data["sigma_1_mpa"]} MPa')
        ax.plot([data["sigma_2_mpa"]], [0], 'go', label=f'$\\sigma_2$ = {data["sigma_2_mpa"]} MPa')

        # Current state points X (sigma_x, -tau_xy) and Y (sigma_y, tau_xy)
        ax.plot([sigma_x, sigma_y], [-tau_xy, tau_xy], 'k--', linewidth=1.2, label='Diameter Axis X-Y')
        ax.plot([sigma_x], [-tau_xy], 'ms', label=f'Plane X ({sigma_x}, {-tau_xy})')
        ax.plot([sigma_y], [tau_xy], 'cs', label=f'Plane Y ({sigma_y}, {tau_xy})')

        ax.axhline(0, color='gray', linestyle=':', linewidth=0.8)
        ax.axvline(0, color='gray', linestyle=':', linewidth=0.8)

        ax.set_title(f"Mohr's Circle (2D Plane Stress) | {data['status_verdict']}", fontsize=12, fontweight='bold')
        ax.set_xlabel(r"Normal Stress $\sigma$ (MPa)", fontsize=11)
        ax.set_ylabel(r"Shear Stress $\tau$ (MPa)", fontsize=11)
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='upper right', fontsize=9)

        plt.tight_layout()
        plt.savefig(output_filepath, dpi=200)
        return output_filepath


def run_demo_mohr():
    analyzer = MohrCircleStressAnalyzer()
    # Stress state on beam web under bending & shear
    sigma_x = 95.0
    sigma_y = -35.0
    tau_xy = 45.0
    yield_sy = 235.0

    res = analyzer.analyze_plane_stress(sigma_x, sigma_y, tau_xy, yield_sy)
    plot_path = analyzer.plot_mohr_circle(sigma_x, sigma_y, tau_xy, yield_sy, "sample_mohr_circle.png")

    print("=" * 65)
    print("⭕ تحلیل دایره مور و تنش‌های اصلی (Mohr's Circle & Yield Criteria):")
    print("=" * 65)
    print(f"تنش‌های ورودی: σx = {sigma_x} MPa, σy = {sigma_y} MPa, τxy = {tau_xy} MPa")
    print(f"تنش اصلی اول (σ1): {res['sigma_1_mpa']} MPa")
    print(f"تنش اصلی دوم (σ2): {res['sigma_2_mpa']} MPa")
    print(f"حداکثر تنش برشی (τmax): {res['tau_max_mpa']} MPa")
    print(f"زاویه صفحه اصلی (θp): {res['theta_p_degrees']}°")
    print(f"تنش معادل فون‌مایزز (Von Mises): {res['von_mises_stress_mpa']} MPa (SF = {res['safety_factor_von_mises']})")
    print(f"تنش ترسکا (Tresca): {res['tresca_stress_mpa']} MPa (SF = {res['safety_factor_tresca']})")
    print(f"وضعیت پایداری سازه: {res['status_verdict']}")
    print(f"نمودار ذخیره شد: {plot_path}")
    print("=" * 65)


if __name__ == "__main__":
    run_demo_mohr()
