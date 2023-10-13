# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:42:18 2023

@author: AZHRELLA
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def fft_2d(x):
    M, N = x.shape
    if M <= 1 and N <= 1:
        return x

    X = np.zeros((M, N), dtype=complex)

    for m in range(M):
        for n in range(N):
            X[m, n] = complex(0, 0)
            for u in range(M):
                for v in range(N):
                    angle = 2 * math.pi * (u * m / M + v * n / N)
                    X[m, n] += x[u, v] * (math.cos(angle) - 1j * math.sin(angle))

    return X

# Validasi dengan NumPy FFT
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], dtype=complex)
fft_result = fft_2d(x)
numpy_fft_result = np.fft.fft2(x)

# Plot spektrum frekuensi
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(np.abs(fft_result), cmap='gray', extent=[0, 1, 0, 1])
plt.title("Custom FFT")

plt.subplot(122)
plt.imshow(np.abs(numpy_fft_result), cmap='gray', extent=[0, 1, 0, 1])
plt.title("NumPy FFT")

plt.show()

# Periksa apakah hasilnya cocok (dalam toleransi)
if np.allclose(fft_result, numpy_fft_result, atol=1e-10):
    print("Hasil cocok!")
else:
    print("Hasil tidak cocok.")
