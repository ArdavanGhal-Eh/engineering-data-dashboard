"""
Dynamic Vibration & Structural Resonance Analysis Module
Part of Engineering & Market Analytics Dashboard Suite
Author: Ardavan Ghal-Eh | Sharif University of Technology
"""

import numpy as np
from typing import Dict, Any


class BeamVibrationAnalyzer:
    """
    Computes natural frequencies, mode shapes, and resonance safety
    for simply-supported structural beams under rotating machinery excitation.
    """

    def __init__(self):
        pass

    def compute_natural_frequencies(
        self,
        length_m: float,
        elastic_modulus_gpa: float,
        second_moment_m4: float,
        density_kg_m3: float,
        cross_section_area_m2: float
    ) -> Dict[str, float]:
        """
        Calculates the first 3 natural frequencies in Hertz (Hz)
        using classical Euler-Bernoulli beam vibration theory:
        f_n = (n^2 * pi / 2L^2) * sqrt(E*I / (rho*A))
        """
        e_pa = elastic_modulus_gpa * 1e9
        mass_per_unit_length = density_kg_m3 * cross_section_area_m2

        if mass_per_unit_length <= 0 or length_m <= 0:
            return {"f1_hz": 0.0, "f2_hz": 0.0, "f3_hz": 0.0}

        wave_speed_factor = np.sqrt((e_pa * second_moment_m4) / mass_per_unit_length)
        f1 = (np.pi / (2.0 * (length_m ** 2))) * wave_speed_factor
        f2 = 4.0 * f1
        f3 = 9.0 * f1

        return {
            "f1_hz": round(float(f1), 2),
            "f2_hz": round(float(f2), 2),
            "f3_hz": round(float(f3), 2),
            "mass_per_meter_kg": round(float(mass_per_unit_length), 2)
        }

    def evaluate_resonance_risk(
        self,
        f_natural_hz: float,
        motor_rpm: float,
        critical_bandwidth_percent: float = 15.0
    ) -> Dict[str, Any]:
        """
        Checks if motor excitation frequency is within the critical resonance band.
        """
        f_excitation = motor_rpm / 60.0
        diff_percent = abs(f_excitation - f_natural_hz) / f_natural_hz * 100.0 if f_natural_hz > 0 else 100.0

        is_resonance = diff_percent <= critical_bandwidth_percent

        if is_resonance:
            status = "⚠️ خطر تشدید ارتعاشی (Critical Resonance Hazard)"
            advice = f"فرکانس تحریک موتور ({f_excitation:.1f} Hz) در محدوده ۱۵٪ فرکانس طبیعی تیر ({f_natural_hz:.1f} Hz) است. تغییر دور یا صلبیت سازه الزامی است."
            color = "red"
        else:
            status = "✅ پایدار و بدون تشدید (Resonance-Safe)"
            advice = f"فاصله فرکانسی مناسب ({diff_percent:.1f}% اختلاف با فرکانس تشدید)."
            color = "green"

        return {
            "motor_rpm": motor_rpm,
            "excitation_frequency_hz": round(f_excitation, 2),
            "natural_frequency_hz": f_natural_hz,
            "frequency_separation_percent": round(diff_percent, 1),
            "is_resonance_hazard": is_resonance,
            "status": status,
            "advice": advice,
            "indicator_color": color
        }


def run_demo_vibration():
    analyzer = BeamVibrationAnalyzer()
    # St37 IPE 140 beam of 4 meters span
    freqs = analyzer.compute_natural_frequencies(
        length_m=4.0,
        elastic_modulus_gpa=205.0,
        second_moment_m4=5.41e-6,
        density_kg_m3=7850.0,
        cross_section_area_m2=0.00164
    )
    resonance = analyzer.evaluate_resonance_risk(
        f_natural_hz=freqs["f1_hz"],
        motor_rpm=1450.0  # Standard 4-pole AC motor RPM
    )

    print("=" * 65)
    print("🌊 تحلیل دینامیکی فرکانس طبیعی و تشدید ارتعاشی:")
    print("=" * 65)
    print(f"فرکانس مود اول (Mode 1): {freqs['f1_hz']} Hz")
    print(f"فرکانس مود دوم (Mode 2): {freqs['f2_hz']} Hz")
    print(f"جرم واحد طول تیر: {freqs['mass_per_meter_kg']} kg/m")
    print(f"فرکانس تحریک موتور (1450 RPM): {resonance['excitation_frequency_hz']} Hz")
    print(f"وضعیت پایداری: {resonance['status']}")
    print(f"توصیه مهندسی: {resonance['advice']}")
    print("=" * 65)


if __name__ == "__main__":
    run_demo_vibration()
