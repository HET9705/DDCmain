# Save as ai_modulation_app.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

Fs = 1000  # Sampling frequency

def ask_modulate(data, bit_duration, carrier_freq=5):
    ask_signal = np.array([])
    for bit in data:
        t_bit = np.arange(0, bit_duration, 1/Fs)
        if bit == 1:
            ask_signal = np.concatenate((ask_signal, np.sin(2 * np.pi * carrier_freq * t_bit)))
        else:
            ask_signal = np.concatenate((ask_signal, np.zeros_like(t_bit)))
    return ask_signal

def fsk_modulate(data, bit_duration, f1=5, f0=2):
    fsk_signal = np.array([])
    for bit in data:
        t_bit = np.arange(0, bit_duration, 1/Fs)
        if bit == 1:
            fsk_signal = np.concatenate((fsk_signal, np.sin(2 * np.pi * f1 * t_bit)))
        else:
            fsk_signal = np.concatenate((fsk_signal, np.sin(2 * np.pi * f0 * t_bit)))
    return fsk_signal

def psk_modulate(data, bit_duration, phase_shift=np.pi):
    psk_signal = np.array([])
    for bit in data:
        t_bit = np.arange(0, bit_duration, 1/Fs)
        if bit == 1:
            psk_signal = np.concatenate((psk_signal, np.sin(2 * np.pi * 5 * t_bit)))
        else:
            psk_signal = np.concatenate((psk_signal, np.sin(2 * np.pi * 5 * t_bit + phase_shift)))
    return psk_signal

def main():
    st.title("📡 AI Modulation Visualizer")
    st.write("Choose modulation scheme and input binary data")

    # Input data
    binary_input = st.text_input("Enter Binary Data (e.g. 10101101):", value="10101011")
    data = [int(bit) for bit in binary_input if bit in ['0', '1']]

    modulation_type = st.selectbox("Select Modulation Type", ["ASK", "FSK", "PSK"])
    bit_duration = st.slider("Bit Duration (seconds)", 0.01, 0.5, 0.1)

    if st.button("🔁 Generate Modulated Signal"):
        if modulation_type == "ASK":
            signal = ask_modulate(data, bit_duration)
        elif modulation_type == "FSK":
            signal = fsk_modulate(data, bit_duration)
        else:
            signal = psk_modulate(data, bit_duration)

        t = np.arange(0, len(signal)) / Fs
        fig, ax = plt.subplots()
        ax.plot(t, signal)
        ax.set_title(f"{modulation_type} Modulated Signal")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
