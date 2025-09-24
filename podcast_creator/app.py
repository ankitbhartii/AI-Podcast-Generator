"""
Main Podcast Creator API using VibeVoice
"""

import subprocess
import os

def create_podcast(script_text, voice="microsoft/VibeVoice-1.5B", output_path="output.wav", inference_steps=10):
    # Write input text to a temporary file
    tmp_script_path = "tmp_podcast_script.txt"
    with open(tmp_script_path, "w") as f:
        f.write(script_text)

    # Build command to run VibeVoice colab.py
    command = [
        "python", "VibeVoice/demo/colab.py",   # Adjust path if needed
        "--model_path", voice,
        "--input_script", tmp_script_path,      # You may need to adapt colab.py to accept --input_script and --output_path
        "--output_path", output_path,
        "--inference_steps", str(inference_steps),
        "--debug"
    ]

    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Clean up temp file
    os.remove(tmp_script_path)

    # Return output audio file path if successful
    if os.path.exists(output_path):
        return output_path
    else:
        raise Exception(f"Podcast generation failed: {result.stderr}")
