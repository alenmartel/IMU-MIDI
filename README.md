# IMU-MIDI
gyrOSC > TouchDesigner > Mainstage ::: sensor for musical generation during dance performance

Requirements:
1. iPhone with gyrOSC app. If you are using a different device that can send OSC data over Wi-Fi, then please reach out to me so that I can edit the TouchDesigner file with the new variables, or if you know how to do this within the .toe file yourself, then please do so.
2. MacBook with TouchDesigner and MainStage, or any other performance software that allows program changing. 

_Please Note: on your Mac, you have to enable IAC MIDI Driver, by searching for your 'Audio MIDI Setup' program (search for it in Spotlight), and then going to Windows > Show MIDI Studio > double-click and select 'Device is Online' and apply the changes. In TouchDesigner, open the .toe file, go to Dialogs > MIDI Device Mapper > Create New Mapping > for 'In Device' select IAC Driver Bus 1, and same for 'Out Device'. MainStage should automatically detect this as your MIDI device._


4. Internet connection, or Wi-Fi Router

The following instructions will presume the use of an iPhone with the gyrOSC app.

**INSTRUCTIONS**

Download this Git repository. The .toe file is for TouchDesigner, the .concert file is for MainStage and the .md file is this file.

Using an iPhone strapped to the body to generate live music:

1. Download the gyrOSC app on an iPhone and after opening it, set the IP address in the app to the computer's IP address running the TouchDesigner file, and set the port to the same as in the gyrOSC node in TouchDesigner (currently set to 10000). Both devices must be on the same Wi-Fi network, regardless if there is an internet connection.
2. In gyrOSC, enable accelerometer and rotational matrix. The current TouchDesigner file is not accessing any other data sends.
3. In TouchDesigner, the main base file, when clicked allows you to switch instruments, but you can zoom into this base to see four different networks, representing the current instruments one can change between. If you have TouchDesigner knowledge, then you can make edits to the settings of each instrument. For now, each instrument is set to generate music according to _ROLL_ and _PITCH_.
5. If you are using MainStage, the current TouchDesigner file takes up to six (6) different instruments. In Mainstage, be sure to enable and set the program of your six instruments (000 to 005). For this performance, '0' and '2' default to NO INSTRUMENT, meaning no sound, so the instruments start at 001 to and 003 to 004. So, in TouchDesigner, if you want to hear anything, make sure the 'Instrument' slider in the otuermost base is set to '1' or '3' to '5'. Adding more instruments requires some changes to TouchDesigner files, so if you would like this, then please let me know.
6. If you are using another DAW, then the program change may not correspond and the iPhone will only play whatever MIDI instrument you have selected.

Making changes to how frequently an instrument fires, adding other rotational or acceleration components, etc., requires knowing some of what's happening in the Python code. So, if you would like any edits, then please let me know. Otherwise, you can download these files and play around!
