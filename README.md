# Pyllurium

Python implementation of chemistry concepts. Built with the idea of trying to implement as many natural rules / laws as possible and hard-code as little behavior as possible. 

Currently supports:

- All Elements
- Electron Configuration

To Do:
- Bonding (Covalent & Ionic)

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