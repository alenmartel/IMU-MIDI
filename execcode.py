num_voices = 10

limit_names = [f'limit{i}' for i in range(1, num_voices + 1)]
last_notes = [-1] * num_voices
last_frames = [-999] * num_voices

velocity_pattern = [
    31, 7, 48, 22, 55, 13, 39, 4, 46, 27,
    18, 62, 9, 34, 50, 16, 43, 2, 29, 74,
    11, 37, 24, 52, 6, 41, 19, 33, 85, 14,
    47, 8, 26, 58, 35, 3, 44, 21, 49, 12,
    30, 66, 17, 40, 5, 53, 28, 36, 10, 45,
    23, 79, 15, 32, 1, 42, 25, 51, 20, 38,
    7, 56, 46, 13, 34, 68, 9, 27, 48, 16,
    41, 4, 31, 54, 22, 37, 11, 60, 29, 43,
    6, 35, 50, 18, 76, 24, 39, 8, 47, 14,
    33, 57, 19, 45, 3, 28, 64, 12, 40, 21
]

velocity_step = 0

root = 40

scales = [
    [0, 2, 3, 7, 8],
    [0, 2, 3, 5, 7, 8, 10],
    [0, 2, 3, 5, 7, 8, 11],
    [0, 2, 3, 5, 7, 9, 10],
    [0, 1, 3, 5, 7, 8, 10],
    [0, 1, 3, 5, 7, 8, 11],
    [0, 2, 3, 6, 7, 8, 11],
    [0, 2, 3, 5, 6, 8, 9, 11],
    [0, 3, 5, 7, 10],
    [0, 2, 3, 7, 10],
    [0, 1, 5, 7, 8],
    [0, 1, 5, 7, 10],
    [0, 2, 4, 6, 7, 9, 11],
    [0,1,2,3,4,5,6,7,8,9,10,11],
]

scale_names = [
    'hirajoshi',
    'natural minor',
    'harmonic minor',
    'dorian minor',
    'phrygian',
    'phrygian dominant dark',
    'hungarian minor',
    'diminished octatonic',
    'minor pentatonic',
    'kumoi',
    'balinese pelog-ish',
    'insen',
    'interstellar',
    'chromatic',
]

scale_steps_offset = 11


def get_slider_value():
    slider_op = op('null13')

    if slider_op is None or slider_op.numChans < 1:
        return 0

    try:
        return slider_op[0].eval()
    except:
        return 0


def get_current_scale_index():
    slider_value = get_slider_value()

    scale_index = int(round(slider_value))
    scale_index = max(0, min(scale_index, len(scales) - 1))

    return scale_index


def get_current_scale():
	
    return scales[get_current_scale_index()]


def get_current_scale_name():
    
    return scale_names[get_current_scale_index()]


def get_frame_gap(index):
    gap_op = op(f'framegap{index + 1}')

    if gap_op is None or gap_op.numChans < 1:
        return 1

    try:
        return gap_op[0].eval()
    except:
        return 1


def get_octave_count(index):
    octave_op = op(f'octave{index + 1}')

    if octave_op is None or octave_op.numChans < 1:
        return 4

    try:
        value = int(octave_op[0].eval())
    except:
        return 4

    return max(1, min(value, 10))


def get_scale_notes(index):
    notes = []
    scale = get_current_scale()
    octave_count = get_octave_count(index)

    for octave in range(octave_count):
        for scale_note in scale:
            notes.append(root + scale_note + (octave * 12))

    return notes


def normalize_raw_note(raw_note):
    normalized = (raw_note - 48) / 36
    normalized = max(0, min(1, normalized))

    return normalized


def quantize_to_scale(raw_note, index):
    normalized = normalize_raw_note(raw_note)

    scale_notes = get_scale_notes(index)
    degree = int(normalized * (len(scale_notes) - 1))

    return scale_notes[degree]


def clamp_midi(note):
    return max(0, min(127, note))


def clamp_velocity(velocity):
    return max(0, min(127, velocity))


def get_next_velocity():
    global velocity_step

    velocity = velocity_pattern[velocity_step % len(velocity_pattern)]
    velocity_step += 1

    return clamp_velocity(velocity)


def fix_duplicate(note, existing_notes, index):
    scale_notes = get_scale_notes(index)

    if note not in scale_notes:
        return clamp_midi(note)

    note_index = scale_notes.index(note)

    attempts = 0
    max_attempts = len(scale_notes)

    while note in existing_notes and attempts < max_attempts:
        note_index = (note_index + scale_steps_offset) % len(scale_notes)
        note = scale_notes[note_index]
        attempts += 1

    return clamp_midi(note)


def get_limit_value(op_name):
    limit_op = op(op_name)

    if limit_op is None or limit_op.numChans < 1:
        return None

    try:
        return limit_op[0].eval()
    except:
        return None


def note_off(note):
    if 0 <= note <= 127:
        op('midiout1').send(0x80, note, 0)


def note_on(note, velocity):
    op('midiout1').send(0x90, note, clamp_velocity(velocity))


def play_voice(index):
    raw_note = get_limit_value(limit_names[index])

    if raw_note is None:
        note_off(last_notes[index])
        last_notes[index] = -1
        return

    note = quantize_to_scale(raw_note, index)

    existing_notes = []

    for i in range(len(last_notes)):
        if i != index:
            existing_notes.append(last_notes[i])

    note = fix_duplicate(note, existing_notes, index)

    if note == last_notes[index]:
        return

    velocity = get_next_velocity()

    note_off(last_notes[index])
    note_on(note, velocity)

    last_notes[index] = note

def onValueChange(channel, sampleIndex, val, prev):
    current_frame = absTime.frame

    for i in range(len(limit_names)):
        frame_gap = get_frame_gap(i)

        if current_frame - last_frames[i] >= frame_gap:
            last_frames[i] = current_frame
            play_voice(i)

    return
