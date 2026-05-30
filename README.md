# IMU-MIDI
gyrOSC > TouchDesigner > Mainstage ::: sensor for musical generation during dance performance

Using an iPhone strapped to the body to generate live music.

1. Download the gyrOSC app and set the IP address to the computer running the TouchDesigner file, and set the port to the same as in the gyrOSC node in TouchDesigner (currently set to 10,000).
2. In gyrOSC, enable accelerometer and rotational matrix
3. In TouchDesigner, you can enable or disable different data pulled from gyrOSC (button1 to button9 nodes), you can activate or deactivate the whole code (activate1 node), and you can change the instrument (slider1) so long as the program channel aligns with the program channels in MainStage.
4. If you are using MainStage, the current TouchDesigner file takes up to five (5) different instruments. In Mainstage, be sure to enable and set the program of your five instruments (000 to 004). You can add more instruments and change the 'Value Range' maximum number of the slider1 to match.
5. If you are using another DAW, then the program change may not correspond and the iPhone will only play whatever MIDI instrument you have selected.

You can change how frequently a note fires (using the note frequency sliders) and in which octaves they operate (octaves sliders). The volume of each note is procedural and can be changed within the chopexec1 DAT (there is an array of 100 volumes and each note that plays plays one of those volumes, the next note plays the next, etc.).
