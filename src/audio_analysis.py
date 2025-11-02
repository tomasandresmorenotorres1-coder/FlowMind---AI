import librosa
import numpy as np

def analyze_audio(file_path):
    """
    Analiza un archivo de audio y devuelve métricas básicas:
    tempo (BPM), duración, y pitch promedio.
    """
    y, sr = librosa.load(file_path)
    
    # Duración
    duration = librosa.get_duration(y=y, sr=sr)
    
    # Tempo (BPM)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    
    # Pitch (frecuencia fundamental aproximada)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch_mean = np.mean(pitches[pitches > 0])
    

    from src.audio_analysis import analyze_audio
    print(analyze_audio("data/samples/saxo_escala.mp3"))

    return {
        "duracion_seg": round(duration, 2),
        "bpm": round(float(tempo), 2),
        "pitch_promedio_Hz": round(float(pitch_mean), 2)
    }
    
