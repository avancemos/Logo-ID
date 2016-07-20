# Main
Identifying and Replacing Given Objects in an Image

## Dependencies

1. Some Kind of Android Simulator, we use [Genymotion](https://www.genymotion.com/)
  * Note: On macOS, you must install [Virtualbox](http://virtualbox.org)
2. Ability to use [Google Cloud Vision API](https://cloud.google.com/vision/). They offer a free trial, but you have to have a mail address and there are a bunch of other restrictions :disappointed_relieved:

## Getting started

### Clone our repo

    git clone git@github.com:avancemos/main.git

### Download and setup an android emulator for your platform

Since we used Genymotion, well show you how to set it up

1. Go to https://www.genymotion.com/download/ and follow the instructions on their site to download the package
  * As of the writing of this README, installing the emulator entails creating an account
2. Launch the application
3. Click the `add` button with the :heavy_plus_sign: sign
4. You will see a sign in prompt at the bottom of the window that pops up. Sign in and select a device.
  * Note: we selected the Nexus 5x running Android 6.0.0 Marshmallow. However, any device with Android 4.1+ Jelly Bean should work fine.
5. Select the device and hit `next`. Read over all the information on the screen, name the device, and hit next. 
6. Genymotion will download all the require files. Depending on your internet speed this might take a while
7. Once done, select the new device from the menu and hit `run` or `ctrl+l`
8. The simulation should launch and you should be all set.

### Install the Snapseed APK on the VM

1. The APK is located in the repo under `apk/Snapseed-VX.X.X.apk`
2. On Genymotion, this can be done by dragging the `apk/Snapseed-VX.X.X.apk` file into the open VM
3. This will take a little while, depending on the specs of your machine, but the app will install.
  * Note: you may have to reboot your VM 


### **Note that this is not yet finished**



