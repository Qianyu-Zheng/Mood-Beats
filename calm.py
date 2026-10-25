
# Mood Beats - Calm V4
# Soft piano melody with gentle harmony

# Main melody based on Calm V1
calm_notes = [60, 64, 67, 64, 62, 60, 62, 60]

# Natural, slow rhythm from V1
calm_beats = [2, 2, 3, 2, 2, 3, 2, 4]

# Soft playing volume
soft_volume = 58

# Play the main calm melody
def play_calm(notes, beats_list):
    for i in range(len(notes)):
        playNote(notes[i], beats=beats_list[i],
                 velocity=soft_volume)

# First phrase: familiar and peaceful
play_calm(calm_notes, calm_beats)

# Second phrase: a small melodic variation
calm_variation = [60, 64, 67, 69, 67, 64, 62, 60]
variation_beats = [2, 2, 3, 2, 2, 2, 2, 4]

play_calm(calm_variation, variation_beats)

# Gentle rising notes before the ending
playNote(64, beats=2, velocity=52)
playNote(67, beats=2, velocity=48)

# Open and airy final chord
calm_chord = [60, 67, 72, 76]
playNote(calm_chord, beats=5, velocity=42)
