pub struct BeamParams {
    pub length: f64,
    pub load: f64,
    pub i: f64,
    pub e: f64,
}

pub fn solve_max_moment(length: f64, load: f64) -> f64 {
    load * length / 4.0
}

pub fn solve_safety_factor(max_moment: f64, section_modulus: f64, yield_strength: f64) -> f64 {
    let stress = max_moment / section_modulus;
    yield_strength / stress
}
