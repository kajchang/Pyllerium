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
    _num_protons = 120
    _mass = 1000
    _symbol = 'My'
    
    
My = MyElement()

print(My) # My
print(My.electron_configuration) # 1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹⁴5d¹⁰6p⁶7s²5f¹⁴6d¹⁰7p⁶8s²
```

Creating Compounds and Percent Composition

```python
from Pyllurium.Elements import *
Heroin = Carbon() * 21 + Hydrogen() * 23 + Nitrogen() + Oxygen() * 5

print(Heroin) # C₂₁H₂₃NO₅
print(Heroin.mass) # 369.41699999999963
print(Heroin.percent_composition) # {Pyllurium.Elements.Oxygen: 0.21654390566757914,
                                  #  Pyllurium.Elements.Hydrogen: 0.06275834625910563,
                                  #  Pyllurium.Elements.Carbon: 0.6827812472084399,
                                  #  Pyllurium.Elements.Nitrogen: 0.037916500864876315}
```
