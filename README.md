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

<h2>Usage</h2>

**<h3>1. Navigate to Start-up folder with WINDOWS + R and 'shell:startup'</h3>**

**<p>Run duckhunt.0.9.blacklist</p>**
![start-up-screen](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/start-up-screen.png)

**<p>Executable is now running</p>**
![task-manager](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/task-manager.png)

<br>

**<h3>2. Open Wireshark and capture USBPcap</h3>**
![wireshark](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/wireshark.PNG)
![wireshark_capturing](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/wireshark_capturing.PNG)

<br>

**<h3>3. Open terminal window</h3>**

**<p>The duckhunt executable will now block and log all input given</p>**
**RECOMMENDED SETUP EXAMPLE BELOW**
![wireshark-cmd](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/wireshark_cmd.PNG)

**<p>Log file is present in the Startup directory</p>**
**THIS IS NOT IDEAL AND NOT REALLY PLEASENT TO READ -> SOLVED BELOW**
![log_startup](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/log_startup.PNG)
![log_example](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/log_example.PNG)

<br>

**<h3>4. Plug in BadUSB</h3>**
**<p>Wireshark will now capture all of the input</p>**
**!!! IMPORTANT: ALWAYS BE FOCUSSED ON THE TERMINAL WINDOW !!!**
**<p>-> In case of input running past the terminal window, duckhunt.exe will stop the attack</p>**
![capturing_badusb](https://raw.githubusercontent.com/larsje99/BadUSB_Script_Extractor/master/screenshots/capturing_badusb.PNG)
