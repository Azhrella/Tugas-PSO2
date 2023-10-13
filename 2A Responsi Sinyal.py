import numpy as np
import matplotlib.pyplot as plt

# Fungsi FFT 1D sederhana
def fft_1d(x):
    N = len(x)
    if N <= 1:
        return x
    else:
        X_even = fft_1d(x[::2])
        X_odd = fft_1d(x[1::2])
        factor = np.exp(-2j * np.pi / N)
        return [X_even[k] + factor ** k * X_odd[k] for k in range(N // 2)] + \
               [X_even[k] - factor ** k * X_odd[k] for k in range(N // 2)]

# Contoh sinyal 1D
N = 32  # Jumlah sampel
t = np.linspace(0,0.25, N, endpoint=False)  # Interval waktu
frequencies = [4, 8, 16]  # Frekuensi komponen sinyal
signal = np.sum([np.sin(2 * np.pi * freq * t) for freq in frequencies], axis=0)

# Hitung FFT dengan implementasi sendiri
fft_result = fft_1d(signal)

# Hitung FFT dengan NumPy
numpy_fft_result = np.fft.fft(signal)

# Plot sinyal asli
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.plot(t, signal)
plt.title("Sinyal Asli")

# Plot spektrum frekuensi (FFT hasil implementasi sendiri)
plt.subplot(132)
frequencies = np.fft.fftfreq(N, t[1] - t[0])
plt.plot(frequencies, np.abs(fft_result))
plt.title("Spektrum Frekuensi (FFT Implementasi Sendiri)")

# Plot spektrum frekuensi (FFT hasil NumPy)
plt.subplot(133)
plt.plot(frequencies, np.abs(numpy_fft_result))
plt.title("Spektrum Frekuensi (FFT NumPy)")

plt.show()

# Validasi dengan NumPy FFT
if np.allclose(fft_result, numpy_fft_result, atol=1e-10):
    print("Hasil FFT NumPy dan FFT Implementasi Sendiri cocok!")
else:
    print("Hasil FFT NumPy dan FFT Implementasi Sendiri tidak cocok.")

