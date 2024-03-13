<h1>BadUSB Script Extraction Guide</h1>

<h2>Install required software</h2>

**REQUIRED:**

1. <p>Wireshark (with USBPcap)</p>
2. <p>duckhunt (GitHub)</p>
3. <p>FlipperZero-BadUSB-Wireshark (GitHub)</p>
4. <p>VirtualBox (optional)</p>

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
3. <p>Press Windows + R and type 'shell:startup'</p>
4. <p>Paste duckhunt.0.9.blacklist.exe + duckhunt_script_killer.py in directory</p>
5. <p>(Optional) Modify duckhunt.conf to match use case</p>

<br>

<h3>(Optional) 4. Run all of this in a Windows 10 VM</h3>
