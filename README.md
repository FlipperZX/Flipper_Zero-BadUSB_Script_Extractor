<h1>BadUSB Script Extraction Guide</h1>

<h2>Install required software</h2>

**REQUIRED:**

1. <p>Wireshark (with USBPcap)</p>
2. <p>duckhunt (GitHub)</p>
3. <p>FlipperZero-BadUSB-Wireshark (GitHub)</p>
4. <p>Python</p>

<h3>1. Wireshark install</h3>

<p>Download from official website: https://www.wireshark.org/</p>
<p>Check USBPcap like so:</p>

![wireshark_wizard](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/wireshark_wizard.png)

<br>

<h3>2. FlipperZero-BadUSB-Wireshark install</h3>
<p>Follow installation process of the following repository: https://github.com/agentzex/FlipperZero-BadUSB-Wireshark/tree/main</p>

**<p>Be sure to replace the restructor.py with the provided restructor.py from THIS repository</p>**

<br>

<h3>3. duckhunt install</h3>
<p>Navigate to this repository: https://github.com/agentzex/FlipperZero-BadUSB-Wireshark/tree/main</p>

**Shortened setup process:**
1. <p>Clone repository: 'git clone https://github.com/pmsosa/duckhunt.git'</p>
2. Install [this](https://github.com/pmsosa/duckhunt/raw/master/builds/duckhunt.0.9.blacklist.exe) script (duckhunt.0.9.blacklist)
3. <p>Press WINDOWS + R and type 'shell:startup'</p>
4. <p>Paste duckhunt.0.9.blacklist.exe + duckhunt_script_killer.py in directory</p>
5. <p>(Optional) Modify duckhunt.conf to match use case</p>

<br>

**(Optional) Run all of this in a Windows 10 VM for better security**
<br>
<br>
**!!! REBOOT IS REQUIRED AFTER ALL OF THESE STEPS !!!**

<br>

<h2>Virtual Machine Note</h2>

It's important to know which device or port you are going to connect to your VM. Below you can find the best method for safely connecting a BadUSB to your virtual machine.

<br>

**<h3>1. Use my script to analyze USB</h3>**

Click [here](https://github.com/larsje99/usbscanner_for_ParrotOS) to find my official USB analyzer and follow the steps from the README.

<br>

**<h3>2. Save USB idVendor and idProduct for later use</h3>**

The analyzer will return some important information about the device, save the idVendor and idProduct for later use!

![output_example](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/output_example.PNG)

<br>

**<h3>3. Add saved information to virtual machine</h3>**

Now we can whitelist a specific USB device in our virtual machine with the idVendor and idProduct.

![whitelist_usb](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/whitelist_usb.PNG)

**<p>NOW WHEN LAUNCHING YOUR WINDOWS 10 VIRTUAL MACHINE THE DEVICE WILL AUTOMATICALLY BE CONNECTED TO THE VM!</p>**

<br>

<h2>Usage</h2>

**<h3>1. Navigate to Start-up folder with WINDOWS + R and 'shell:startup'</h3>**

<p>Run duckhunt.0.9.blacklist</p>

![start-up-screen](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/start-up-screen.png)

<p>Executable is now running</p>

![task-manager](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/task-manager.png)

<br>

**<h3>2. Open Wireshark and capture USBPcap</h3>**
![wireshark](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/wireshark.PNG)
![wireshark_capturing](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/wireshark_capturing.PNG)

<br>

**<h3>3. Open terminal window</h3>**

<p>The duckhunt executable will now block and log all input given</p>

**RECOMMENDED SETUP EXAMPLE BELOW**
![wireshark-cmd](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/wireshark_cmd.PNG)

<p>Log file is present in the Start-up directory</p>

**THIS IS NOT IDEAL AND NOT REALLY PLEASENT TO READ -> SOLVED BELOW**
![log_startup](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/log_startup.PNG)
![log_example](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/log_example.PNG)

<br>

**<h3>4. Plug in BadUSB</h3>**
<p>Wireshark will now capture all of the input</p>

**!!! IMPORTANT: ALWAYS BE FOCUSSED ON THE TERMINAL WINDOW !!!**
**<p>-> In case of input running past the terminal window, duckhunt.exe will stop the attack</p>**
![capturing_badusb](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/capturing_badusb.PNG)

<br>

**<h3>5. Save Wireshark report as JSON</h3>**
<p>Save file to the reconstructor directory (C:\Users\\%USER%\FlipperZero-BadUSB-Wireshark\reconstructor)</p>

![saving_packet](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/saving_packet.png)
![folder_save](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/wireshark_save.PNG)

<br>

**<h3>6. Run reconstructor.py</h3>**

<p>After saving the file you can close Wireshark and end duckhunt.0.9.blacklist in task manager</p>

<p>Open terminal, navigate to reconstructor folder and run 'python reconstructor.py FILENAME.json</p>

![cmd_python](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/cmd_python.PNG)

<p>If all goes well you will find reconstructed_ducky_script.txt in the reconstructor directory</p>

![reconstructor](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/reconstructor.PNG)

![final_output](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/final_output.PNG)

**YOU HAVE SUCCESFULLY CAUGHT THE DUCKY SCRIPT!**

<br>

**<h3>Credits</h3>**
<p>@agentzex https://github.com/agentzex</p>
<p>@pmsosa https://github.com/pmsosa</p>
