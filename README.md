# Pyllurium

Python implementation of chemistry concepts. Built with the idea of trying to implement as many natural rules / laws as possible and hard-code as little behavior as possible. 

Currently supports:

- First Two Periods of Elements
- Electron Configuration
- Ions

To Do:
- Differences between Ionic and Convalent Bonds

## Installation

Clone this repository and run `python3 setup.py install` or `pip3 install .`.

## Examples

Basic Elemental API and Ionization:

```python
from Pyllurium.Elements import *

N = Nitrogen()

print(N) # N

print(N.Z) # 7 Protons
print(N.E) # 7 Electrons

print(N.electron_configuration) # 1s²2s²2p³
print(N.optimal_ionization) # -3

# Ionizing Nitrogen to Nitride

N.ionize(N.optimal_ionization) # Add 3 Electrons

print(N) # N³⁻

print(N.electron_configuration) # 1s²2s²2p⁶
print(N.is_ion) # True
print(N.charge) # -3
```

Compounds:

```python
from Pyllurium.Elements import *

O = Oxygen()

# Bonding 3 Oxygens into Ozone

Ozone = O * 3

print(Ozone) # O₃
```
