# Main
Identifying and Replacing Given Objects in an Image

## Dependencies

1. Some Kind of Android Simulator, we use [Genymotion](https://www.genymotion.com/)
  * Note: On macOS, you must install [Virtualbox](http://virtualbox.org)
2. [Android Studio](https://developer.android.com/studio/index.html) (Or at least just the ADK)
3. Ability to use [Google Cloud Vision API](https://cloud.google.com/vision/). They offer a free trial and have a free option for personal use, but you have to have a mail address and there are a bunch of other restrictions :disappointed_relieved:

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
8. The simulation should launch

### Install and Set Up Android Studio

1. Download [Android Stuidio](https://developer.android.com/studio/index.html)
2. Complete the install process for your platform
3. On Genymotion, go to `Settings -> ADB` and check `Use custom Android SDK tools`
4. Then provide in the box below the location of the `ADK` / `Android SDK`
  * On macOS/Linux the path should look something like `/Users/user_name/Library/Android/sdk`

### Install the Snapseed APK on the VM

1. The APK is located in the repo under `apk/Snapseed-VX.X.X.apk`
2. On Genymotion, this can be done by dragging the `apk/Snapseed-VX.X.X.apk` file into the open VM
3. This will take a little while, depending on the specs of your machine, but the app will install.
  * Note: you may have to reboot your VM 

### Set up ADB
1. Go into the settings on the VM
2. Scroll down to the `about phone`
3. Scroll down to `build number`
4. Tab build number about 10
5. There will be a message saying that you have enabled developer options
5. Go back to the settings page and you will see the developeroptions menu
6. Open the developer options, and enable `USB debugging`
7. Install adb and fastboot into the `scripts` folder

Run in terminal on macOS and Linux

    sudo apt-get install unzip
    unzip Android.zip -d /PATH/TO/main/scripts/

On macOS

    ./PATH/TO/main/scripts/ADB-Install-Linux.sh
    mv /PATH/TO/main/scripts/Android/Mac/* /PATH/TO/main/scripts/

On Linux

    ./PATH/TO/main/scripts/ADB-Install-Mac.sh
    mv /PATH/TO/main/scripts/Android/Mac/* /PATH/TO/main/scripts/


### Setup Google Cloud Vision API with you account

Still working on how to get this to work for people other than me

### Selecting image and Sub-image

When selecting your image and sub-image, there are a few things to keep in mind:
 1. You should pick an image where the subimage is clearly visiable and is not obscured
 2. The subimage should be somthing that is able to be recognized by Google Cloud Vision


### **Note that this is not yet finished**



