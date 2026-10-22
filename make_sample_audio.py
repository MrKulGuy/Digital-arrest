"""
Generate a tiny clean 3-second sample WAV file using only the standard library.
"""
import wave
import math
import struct

def generate_sample_wav(filename="sample_call.wav", duration_sec=3, sample_rate=16000):
    num_samples = duration_sec * sample_rate
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1) # mono
        wav_file.setsampwidth(2) # 16-bit
        wav_file.setframerate(sample_rate)
        for i in range(num_samples):
            # 440 Hz tone with gentle envelope
            t = float(i) / sample_rate
            volume = math.sin(math.pi * t / duration_sec)
            val = int(volume * 16000 * math.sin(2.0 * math.pi * 440.0 * t))
            wav_file.writeframes(struct.pack('<h', val))
    print(f"Generated {filename} ({duration_sec}s, {sample_rate}Hz)")

if __name__ == "__main__":
    generate_sample_wav("C:/Users/Acer nitro/.gemini/antigravity/scratch/digital-arrest-shield/sample_call.wav")
