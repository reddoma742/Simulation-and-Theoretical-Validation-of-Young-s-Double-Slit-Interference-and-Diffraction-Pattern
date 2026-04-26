# Title: Numerical Simulation and Theoretical Validation of Youngâ€™s Double-Slit Interference and Diffraction Pattern
# Author: [Ø§ÙƒØªØ¨ Ø§Ø³Ù…Ùƒ Ø§Ù„Ø­Ù‚ÙŠÙ‚ÙŠ Ù‡Ù†Ø§]
# License: MIT License

import numpy as np
import matplotlib.pyplot as plt

# 1. Ø§Ù„Ù…Ø¹Ø·ÙŠØ§Øª (Parameters)
L = 2.0# Ø§Ù„Ù…Ø³Ø§ÙØ© Ù„Ù„Ø´Ø§Ø´Ø© (Ù…ØªØ±)
d = 0.0001# Ø§Ù„Ù…Ø³Ø§ÙØ© Ø¨ÙŠÙ† Ø§Ù„Ø´Ù‚ÙŠÙ† (Ù…ØªØ±)
a = 0.00002# Ø¹Ø±Ø¶ Ø§Ù„Ø´Ù‚ Ø§Ù„ÙˆØ§Ø­Ø¯ (Ù…ØªØ±)
wavelength = 600e-9# Ø§Ù„Ø·ÙˆÙ„ Ø§Ù„Ù…ÙˆØ¬ÙŠ (Ù…ØªØ±)
y = np.linspace(-0.05, 0.05, 2000) # Ù†Ø·Ø§Ù‚ Ø§Ù„Ø±Ø¤ÙŠØ© Ø¹Ù„Ù‰ Ø§Ù„Ø´Ø§Ø´Ø© (Ù…ØªØ±)

# 2. Ø§Ù„Ø­Ø³Ø§Ø¨Ø§Øª (Interference + Diffraction)
# Interference (Ø§Ù„ØªØ¯Ø§Ø®Ù„)
path_diff = (d * y) / L
phi = (2 * np.pi * path_diff) / wavelength
I_interf = np.cos(phi / 2.0)**2

# Diffraction (Ø§Ù„Ø­ÙŠÙˆØ¯)
beta = (np.pi * a * y) / (wavelength * L)
I_diff = (np.sin(beta) / beta)**2

# Full Pattern
I = I_interf * I_diff

# 3. Ø­Ø³Ø§Ø¨ Ù…ÙˆØ§Ù‚Ø¹ Ø§Ù„Ù‚Ù…Ù… "Ø§Ù„Ù†Ø¸Ø±ÙŠØ©" (Theoretical Peaks)
m = np.arange(-20, 21) 
y_theory = (m * wavelength * L) / d
y_theory_mm = y_theory * 1000

# 4. Ø§Ù„Ø±Ø³Ù… Ù…Ø¹ Ø§Ù„ØªØ­Ù‚Ù‚
plt.figure(figsize=(12, 5))
plt.plot(y * 1000, I, label='Real Pattern (Interference + Diffraction)', color='navy')

# Ø¥Ø¶Ø§ÙØ© Ø§Ù„Ø®Ø·ÙˆØ· Ø§Ù„Ù†Ø¸Ø±ÙŠØ©
for i, val in enumerate(y_theory_mm):
if abs(val) <= 50:
        plt.axvline(x=val, color='brown', linestyle='--', alpha=0.4, 
                    label='Theory' if i == 20 else "")

plt.title('Young Double Slit: Numerical with Diffraction Envelope')
plt.xlabel('y (mm)')
plt.ylabel('Intensity')
plt.legend()
plt.grid(True)
plt.show()