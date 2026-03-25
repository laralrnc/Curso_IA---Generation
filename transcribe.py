import whisper

# Load the Whisper model (choose: "tiny", "base", "small", "medium", or "large")
model = whisper.load_model("tiny")

# Replace this with your own audio file path (mp3, wav, m4a, etc.)
audio_file = "input.mp3"

# Transcribe the audio
result = model.transcribe(audio_file)

# Print and save the transcript
print("Transcript:\n")
print(result["text"])

# Save to a text file
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
