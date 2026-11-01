# Chemical Compound Attenuation Calculator

This repository contains a computational chemistry script designed to calculate the mass attenuation coefficient ($\mu/\rho$) of chemical compounds for ionizing radiation (gamma rays at 1 MeV).

## Computation Description
In radiation physics and chemistry, the shielding effectiveness of a composite material depends on its chemical composition. This tool parses molecular formulas (e.g., `BaSO4`, `H2O`) using regular expressions, calculates the weight fractions of each constituent element based on their atomic masses, and computes the total mass attenuation coefficient using the mixture rule:

$$ (\mu/\rho)_{compound} = \sum w_i (\mu/\rho)_i $$

## Files
- `main.py`: Contains the formula parser and the attenuation calculation algorithm.
- `test_main.py`: Pytest unit tests validating the parsing logic and mathematical outputs against known reference values.

## How to Run
```bash
pip install pytest
pytest test_main.py
