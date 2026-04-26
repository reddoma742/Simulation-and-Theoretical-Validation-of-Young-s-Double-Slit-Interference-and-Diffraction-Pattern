import numpy as np
import matplotlib.pyplot as plt

# 1. المعطيات (Parameters)
L = 2.0                 # المسافة للشاشة (متر)
d = 0.0001              # المسافة بين الشقين (متر)
a = 0.00002             # عرض الشق الواحد (متر)
wavelength = 600e-9      # الطول الموجي (متر)
y = np.linspace(-0.05, 0.05, 2000) 

# 2. الحسابات باستخدام np.sinc (تعديل احترافي)
path_diff = (d * y) / L
phi = (2 * np.pi * path_diff) / wavelength
I_interf = np.cos(phi / 2.0)**2

# استخدام np.sinc (تجنب القسمة على صفر بشكل طبيعي)
beta = (a * y) / (wavelength * L)
I_diff = np.sinc(beta)**2
I = I_interf * I_diff

# 3. التحقق (Theoretical Validation)
m = np.arange(-20, 21) 
y_theory_mm = (m * wavelength * L / d) * 1000

# 4. الرسم
plt.figure(figsize=(12, 5))
plt.plot(y * 1000, I, label='Real Pattern (Interference + Diffraction)', color='navy')
for val in y_theory_mm:
    if abs(val) <= 50:
        plt.axvline(x=val, color='brown', linestyle='--', alpha=0.4)

plt.title('Young Double Slit: Numerical with Diffraction Envelope')
plt.xlabel('y (mm)')
plt.ylabel('Intensity')
plt.legend()
plt.grid(True)
plt.show()
