import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import numpy as np
from mohr_circle_stress_analyzer import MohrCircleStressAnalyzer
from vibration_resonance_analyzer import BeamVibrationAnalyzer


def test_mohr_circle_pure_shear():
    analyzer = MohrCircleStressAnalyzer()
    res = analyzer.analyze_plane_stress(sigma_x=0.0, sigma_y=0.0, tau_xy=50.0, yield_strength_mpa=235.0)

    assert res["center_mpa"] == pytest.approx(0.0)
    assert res["radius_mpa"] == pytest.approx(50.0)
    assert res["sigma_1_mpa"] == pytest.approx(50.0)
    assert res["sigma_2_mpa"] == pytest.approx(-50.0)
    assert res["tau_max_mpa"] == pytest.approx(50.0)
    # Von Mises in pure shear = sqrt(3) * tau = 1.732 * 50 = 86.6 MPa
    assert res["von_mises_stress_mpa"] == pytest.approx(50.0 * np.sqrt(3.0), rel=1e-2)
    # Tresca in pure shear = sigma1 - sigma2 = 100 MPa
    assert res["tresca_stress_mpa"] == pytest.approx(100.0, rel=1e-2)
    assert res["safety_factor_von_mises"] > 1.5


def test_mohr_circle_uniaxial_tension():
    analyzer = MohrCircleStressAnalyzer()
    res = analyzer.analyze_plane_stress(sigma_x=120.0, sigma_y=0.0, tau_xy=0.0, yield_strength_mpa=235.0)

    assert res["sigma_1_mpa"] == pytest.approx(120.0)
    assert res["sigma_2_mpa"] == pytest.approx(0.0)
    assert res["tau_max_mpa"] == pytest.approx(60.0)
    assert res["von_mises_stress_mpa"] == pytest.approx(120.0)
    assert res["tresca_stress_mpa"] == pytest.approx(120.0)
    assert res["safety_factor_von_mises"] == pytest.approx(235.0 / 120.0, rel=1e-2)


def test_beam_natural_frequencies():
    analyzer = BeamVibrationAnalyzer()
    freqs = analyzer.compute_natural_frequencies(
        length_m=4.0,
        elastic_modulus_gpa=205.0,
        second_moment_m4=5.41e-6,
        density_kg_m3=7850.0,
        cross_section_area_m2=0.00164
    )

    assert freqs["f1_hz"] > 0
    # Mode 2 is 4x Mode 1, Mode 3 is 9x Mode 1
    assert freqs["f2_hz"] == pytest.approx(4.0 * freqs["f1_hz"], rel=1e-2)
    assert freqs["f3_hz"] == pytest.approx(9.0 * freqs["f1_hz"], rel=1e-2)


def test_resonance_risk_evaluation():
    analyzer = BeamVibrationAnalyzer()
    # At 1500 RPM, excitation freq = 25 Hz.
    # If natural freq is 25 Hz, it should trigger critical resonance hazard.
    danger = analyzer.evaluate_resonance_risk(f_natural_hz=25.0, motor_rpm=1500.0)
    assert danger["is_resonance_hazard"] is True
    assert "خطر تشدید" in danger["status"]

    # If natural freq is 60 Hz, diff is large -> resonance-safe
    safe = analyzer.evaluate_resonance_risk(f_natural_hz=60.0, motor_rpm=1500.0)
    assert safe["is_resonance_hazard"] is False
    assert "پایدار" in safe["status"]
