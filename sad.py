
# Mood Beats - Sad V1
# A gentle and emotional melody in A minor

# Notes from the A minor scale
sad_notes = [69, 67, 64, 60, 62, 64, 60, 57]

# Slow and steady note durations
sad_beats = [2, 2, 2, 3, 2, 2, 2, 4]

# Soft piano volume
sad_volume = 55

# Play the sad melody
def play_sad():
    for i in range(len(sad_notes)):
        playNote(sad_notes[i],
                 beats=sad_beats[i],
                 velocity=sad_volume)

# Play the melody once
play_sad()

# Gentle descending ending
playNote(64, beats=2, velocity=50)
playNote(60, beats=2, velocity=45)
playNote(57, beats=4, velocity=40)

# Final A minor chord
sad_chord = [57, 60, 64]
playNote(sad_chord, beats=4, velocity=40)
