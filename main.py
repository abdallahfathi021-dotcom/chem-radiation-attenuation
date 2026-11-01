import re

# Sample atomic data: Atomic Mass (g/mol) and Mass Attenuation Coefficient (cm^2/g) at 1 MeV
ATOMIC_DATA = {
    'H': {'mass': 1.008, 'mu_rho': 0.1263},
    'O': {'mass': 15.999, 'mu_rho': 0.0636},
    'Pb': {'mass': 207.2, 'mu_rho': 0.0710},
    'Ba': {'mass': 137.327, 'mu_rho': 0.0600},
    'S': {'mass': 32.065, 'mu_rho': 0.0632}
}

def parse_chemical_formula(formula: str) -> dict:
    """Parses a chemical formula into a dictionary of element counts."""
    pattern = r'([A-Z][a-z]*)(\d*)'
    matches = re.findall(pattern, formula)
    
    parsed = {}
    for element, count in matches:
        count = int(count) if count else 1
        parsed[element] = parsed.get(element, 0) + count
    return parsed

def calculate_compound_attenuation(formula: str) -> float:
    """Calculates the total mass attenuation coefficient of a compound."""
    elements = parse_chemical_formula(formula)
    
    total_molar_mass = 0.0
    for element, count in elements.items():
        if element not in ATOMIC_DATA:
            raise ValueError(f"Element {element} not found in database.")
        total_molar_mass += ATOMIC_DATA[element]['mass'] * count
        
    compound_mu_rho = 0.0
    for element, count in elements.items():
        weight_fraction = (ATOMIC_DATA[element]['mass'] * count) / total_molar_mass
        compound_mu_rho += weight_fraction * ATOMIC_DATA[element]['mu_rho']
        
    return round(compound_mu_rho, 5)

if __name__ == "__main__":
    # Example usage for Water and Barium Sulfate
    print(f"Water (H2O) mu/rho: {calculate_compound_attenuation('H2O')} cm^2/g")
    print(f"Barium Sulfate (BaSO4) mu/rho: {calculate_compound_attenuation('BaSO4')} cm^2/g")
