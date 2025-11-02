import sys
import os

# Asegura que el sistema encuentre la carpeta src
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.audio_analysis import analyze_audio

def main():
    print("🎧 FlowMind-AI - Análisis de audio básico")
    ruta = input("Introduce la ruta del archivo de audio: ")

    try:
        resultado = analyze_audio(ruta)
        print("\n✅ Análisis completado:")
        for clave, valor in resultado.items():
            print(f"{clave}: {valor}")
    except Exception as e:
        print(f"❌ Error al analizar el audio: {e}")

if __name__ == "__main__":
    main()
