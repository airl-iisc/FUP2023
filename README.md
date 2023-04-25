# FUP2023
## Section 1 Setting Up Raspberry Pi

1. Setup a WiFi hotspot on your mobile phone with the following details:

    ```
    SSID: airl
    Password: admin_cps280
    ```
2. Power the Raspberry Pi using the provided high current adapter
3. Download the application 'Fing' from the Android Play Store or 'Network Analyzer' on the apple store
4. Download the VNC Application from [here](https://www.tightvnc.com/download.php) and install with an appropriate password
5. Start the VNC Client from your system, it should prompt you to fill in an IP address
6. Use the IP Address you find in Step 3 and add the port number `5901`

        For example:
        If the IP address is 192.168.1.113 then you must enter
        192.168.1.113::5901
7. Login with the password `cps280`

8. [Optional] Optionally use [Putty] `(https://www.putty.org/)` to SSH into the system

## Section 2: Installing ROS

Once you are within the Raspberry Pi System your username is `airl` and password will be `admin`

1.Install git and curl
```
sudo apt install curl git
```

2. Setup your sources.list
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
3. Setup your keys
```
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

4. To be sure that your Ubuntu Mate package index is up to date, type the following command
```
sudo apt-get update
```

5. If you get a message saying the following
```
E: Release file for http://ports.ubuntu.com/ubuntu-ports/dists/focal-updates/InRelease is not valid yet (invalid for another 7h 23min 13s). Updates for this repository will not be applied.
```
6. It probably means that your system time is wrong, update the system time using this one line command:
```
sudo date -s "$(wget --method=HEAD -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f4-10)"
```

7. Install ROS
```
sudo apt install ros-noetic-desktop
```

8. To setup the ROS environment we use the following script
```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
## Section 3: Camera Calibration

Steps to calibrate the camera:
1. Clone the following git repository in your raspberry pi
```
git clone https://github.com/Mnzs1701/camera_calib_python/
```
2. Using the camera calibration checkerboard, record a video covering the entire camera frame

3. Follow the instructions in the GitHub Repository to verify your calibration matrix


### For libboost error:

Download the deb file using:
```
curl -k -O -L http://ports.ubuntu.com/ubuntu-ports/pool/main/b/boost1.71/libboost1.71-dev_1.71.0-6ubuntu6_armhf.deb
```
Install the deb file using:
```
sudo dpkg -i libboost1.71-dev_1.71.0-6ubuntu6_armhf.deb
```
