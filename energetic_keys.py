
# Mood Beats - Energetic V1
# Strong rhythm and powerful repeated melody

# Main energetic melody
energy_notes = [60, 60, 67, 67, 69, 67, 64, 67]
energy_beats = [0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5, 1]

# Loud and strong playing
strong_volume = 105

# Play one energetic phrase
def play_energy():
    for i in range(len(energy_notes)):
        if i == 0 or i == 4:
            note_volume = 115
        else:
            note_volume = strong_volume

        playNote(energy_notes[i],
                 beats=energy_beats[i],
                 velocity=note_volume)

# Repeat the main phrase four times
for repeat in range(4):
    play_energy()

# Rising ending
ending_notes = [67, 69, 72, 76]

for note in ending_notes:
    playNote(note, beats=0.25, velocity=115)

# Strong final chord
energy_chord = [60, 67, 72, 76]
playNote(energy_chord, beats=2, velocity=110)
