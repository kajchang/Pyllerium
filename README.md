# Pyllurium

Python implementation of chemistry concepts. Built with the idea of trying to implement as many natural rules / laws as possible and hard-code as little behavior as possible. 

Currently supports:

- All Elements
- Ionic Bonds
- Electron Configuration
- Percent Composition

## Installation

Clone this repository and run `python3 setup.py install` or `pip3 install .`.

## Examples

Basic Elemental API:

```python
from Pyllurium.Elements import *

H = Hydrogen()

print(H) # H
print(H.electron_configuration) # 1s¹
print(H.mass) # 1.008


Uue = Ununennium()

print(Uue) # Uue
print(Uue.electron_configuration) # 1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹⁴5d¹⁰6p⁶7s²5f¹⁴6d¹⁰7p⁶8s¹
print(Uue.mass) # 315
```

Creating Custom Elements:

```python
from Pyllurium.Atom import Atom

class MyElement(Atom):
    num_protons = 120
    mass = 1000
    symbol = 'My'
    
    
My = MyElement()

print(My) # My
print(My.electron_configuration) # 1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹⁴5d¹⁰6p⁶7s²5f¹⁴6d¹⁰7p⁶8s²
```

Creating Ionic Compounds and Percent Composition:

```python
from Pyllurium.Elements import *
from Pyllurium import Compound

# Making Lithium Flouride (LiF)

#                           Lithium Cation       Flouride Anion
Lithium_Flouride = Compound(Lithium().ionize(1), Fluorine().ionize(-1))

print(Lithium_Flouride) # LiF
print(Lithium_Flouride.mass) # 25.9384031636
print(Lithium_Flouride.percent_composition) # {Pyllurium.Elements.Lithium: 0.26755694852253176,
                                            #  Pyllurium.Elements.Fluorine: 0.7324430514774682}
```

Shortcut for Making Compounds:

```python
from Pyllurium.Elements import *

# Making Calcium Chloride (CaCl₂)

#                   Calcium Cation        2 Chloride Anions
Calcium_Phosphate = Calcium().ionize(2) + Chlorine().ionize(-1) * 2

print(Calcium_Phosphate) # CaCl₂
print(Calcium_Phosphate.mass) # 110.97840000000001
print(Calcium_Phosphate.percent_composition) # {Pyllurium.Elements.Calcium: 0.3611369419634812,
                                             #  Pyllurium.Elements.Chlorine: 0.6388630580365188}
```
