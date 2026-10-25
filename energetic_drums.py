
# Mood Beats - Energetic V2 Drums
# Strong kick, snare and hi-hat rhythm

# Drum sound numbers in TunePad
kick = 0
snare = 2
hihat = 4

# Repeat a four-beat pattern five times
for repeat in range(5):

    # Beat 1: kick and hi-hat
    playNote([kick, hihat], beats=0.5)
    playNote(hihat, beats=0.5)

    # Beat 2: snare and hi-hat
    playNote([snare, hihat], beats=0.5)
    playNote(hihat, beats=0.5)

    # Beat 3: kick and hi-hat
    playNote([kick, hihat], beats=0.5)
    playNote(hihat, beats=0.5)

    # Beat 4: snare and hi-hat
    playNote([snare, hihat], beats=0.5)
    playNote(hihat, beats=0.5)
