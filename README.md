
# Mood Beats

## Project Overview

Mood Beats is an emotion-based music prototype developed in TunePad using Python.

The project explores how pitch, rhythm, note duration, repetition and dynamics can express four different emotions: Happy, Calm, Sad and Energetic.

The project contains four musical sections created across five instrument tracks.

## Musical Sections

### 1. Happy
Happy V4 uses short notes, repeated melodic patterns, a rising ending and a high chord to create a bright and playful feeling.

### 2. Calm
Calm V4 uses longer notes, gentle melodic variations, softer note velocities and an open final chord to create a peaceful atmosphere.

### 3. Sad
Sad V1 uses notes from A minor, a descending melody, longer note durations and softer dynamics to create a gradually developing sad feeling.

### 4. Energetic
Energetic combines a piano melody and a programmed drum beat.

The piano uses short rhythmic patterns, repetition and accented notes. The drums use kick, snare and hi-hat patterns to add energy.

## Software and Requirements

- TunePad: https://tunepad.com/
- Python-based TunePad music programming environment
- A web browser with audio enabled

The Python files use TunePad-specific functions such as `playNote()`. They are designed for the TunePad environment and are not standalone Python programs.

No separate Python packages are required to open the shared TunePad project in a browser.

## Project Files

- `happy.py` — Happy V4 piano melody
- `calm.py` — Calm V4 piano melody
- `sad.py` — Sad V1 piano melody
- `energetic_keys.py` — Energetic piano melody
- `energetic_drums.py` — Energetic drum pattern
- `tunepad_project_135214.json` — Exported TunePad project containing the complete arrangement and code
- `README.md` — Project description and instructions

## How to Run the Project

### Option 1: Open the TunePad Project

1. Open the project: https://tunepad.com/project/135214
2. Open the Code tab to view the instrument cells and Python code.
3. Use the individual cell play buttons to listen to the piano melodies.
4. Open the Tracks tab to manage which instruments play together.

### Listening to Each Emotion

In the Tracks tab, use Solo (headphone icon) to select the required track.

- Happy: Solo the Happy track.
- Calm: Solo the Calm track.
- Sad: Solo the Sad track.
- Energetic: Solo both Energetic Keys and Energetic Drums.

Press the main Play button to listen to the selected tracks. Stop playback before switching between emotions, then turn off the previous Solo selections.

### Option 2: Project Source Files

The repository contains the original exported TunePad JSON project and individual Python source files.

The `.py` files are provided for reading and reviewing the code. They should be used within the corresponding TunePad instrument environment.

## Programming Concepts

The project uses:

- Variables to store notes, note durations and volume values
- Lists to organise melodies and drum patterns
- For loops to repeat and play musical sequences
- Functions to organise reusable musical code
- If/else statements to control note accents
- TunePad's `playNote()` function to create music

## Development Process

I developed the music through listening, testing and revising different versions.

Happy V4 and Calm V4 were selected after comparing earlier versions. Sad V1 was retained because its emotional effect developed naturally. Energetic was improved by adding a separate programmed drum track to the piano melody.

## Credits and Acknowledgements

Project concept and musical direction: Qianyu Zheng.

Music programming environment: TunePad.

I used ChatGPT to help me understand the course content and assignment requirements, and to organise my personal listening feedback and project notes. I listened to and compared the different music versions myself before choosing the final versions.
