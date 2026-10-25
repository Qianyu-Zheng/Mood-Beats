
# Mood Beats - Happy V4
# Bright melody, repetition and a high chord ending

# Notes from V1 and V3
happy_notes = [60, 64, 67, 72, 67, 69, 67, 72]

# Short and playful rhythm
happy_beats = [0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 1]

# Play one happy musical phrase
def play_happy():
    for i in range(len(happy_notes)):
        playNote(happy_notes[i], beats=happy_beats[i])

# Repeat the main phrase three times
for repeat in range(3):
    play_happy()

# Create a rising ending
playNote(67, beats=0.25)
playNote(69, beats=0.25)
playNote(72, beats=0.25)
playNote(76, beats=0.25)

# Layer three high notes at the same time
happy_chord = [72, 76, 79]
playNote(happy_chord, beats=1.5)
