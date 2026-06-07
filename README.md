# IMU-MIDI
gyrOSC > TouchDesigner > Mainstage ::: sensor for musical generation during dance performance

Requirements:
1. iPhone with gyrOSC app
2. MacBook with TouchDesigner and MainStage, or any other performance software that allows program changing. 

_Please Note: on your Mac, you have to enable IAC MIDI Driver, by searching for your 'Audio MIDI Setup' program (search for it in Spotlight), and then going to Windows > Show MIDI Studio > double-click and select 'Device is Online'. In TouchDesigner, open the .toe file, go to Dialogs > MIDI Device Mapper > Create New Mapping > for 'In Device' select IAC Driver Bus 1, and same for 'Out Device'. MainStage should automatically detect this as your MIDI device._


4. Internet connection, or Wi-Fi Router

Using an iPhone strapped to the body to generate live music.

1. Download the gyrOSC app on an iPhone and set the IP address to the computer running the TouchDesigner file, and set the port to the same as in the gyrOSC node in TouchDesigner (currently set to 10000). Both devices must be on the same Wi-Fi network.
2. In gyrOSC, enable accelerometer and rotational matrix
3. In TouchDesigner, the main base file, when clicked allows you to switch instruments, but you can zoom into this base to see four different networks, representing the current four instruments one can change between. If you have TouchDesigner knowledge, then you can make edits to the settings of each instrument. For now, each instrument is set to generate music according to _ROLL_ and _PITCH_. The first instrument is set to produce a static number of musical notes over time when rolled or pitched, whereas the others produce more notes the faster the phone rolls and pitches. The pitch of the musical notes correlates to the range of motion when pitched or rolled.
5. If you are using MainStage, the current TouchDesigner file takes up to five (5) different instruments. In Mainstage, be sure to enable and set the program of your five instruments (000 to 004). For this performance, '0' defaults to NO INSTRUMENT, so the instruments start at 001 to 004. So, in TouchDesigner, if you want to hear anything, make sure the 'Instrument' slider in the otuermost base is set to '1'. Adding more instruments requires some changes to TouchDesigner files, so if you would like this, then please let me know.
6. If you are using another DAW, then the program change may not correspond and the iPhone will only play whatever MIDI instrument you have selected.

Making changes to how frequently an instrument fires, adding other rotational or acceleration components, etc., requires knowing some of what's happening in the Python code. So, if you would like any edits, then please let me know. Otherwise, you can download these files and play around!
