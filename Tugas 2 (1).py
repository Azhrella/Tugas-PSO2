# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 08:07:50 2023

@author: AZHRELLA
"""

print("Nama: Azhrella Naradiyanti")
print("NRP: 5009211009")

def convolution(x, h):
    M = len(x)
    N = len(h)
    y = [0] * (M + N - 1)

    for n in range(M + N - 1):
        y[n] = 0
        for k in range(M):
            if n - k >= 0 and n - k < N:
                y[n] += x[k] * h[n - k]

    return y

# Contoh penggunaan:
x = [1, 2, 3]
h = [1, 2, 3, 4]

hasil_konvolusi = convolution(x, h)
print("Hasil Konvolusi:", hasil_konvolusi)
