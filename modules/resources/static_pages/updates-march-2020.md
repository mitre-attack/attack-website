Title: Updates - March 2020
Date: March 2020
Category: Cyber Threat Intelligence
Authors: Blake Strom
Template: resources/update-post
url: /resources/updates/updates-march-2020
save_as: resources/updates/updates-march-2020/index.html

The March 2020 update for ATT&CK contains the beta release of sub-techniques for the Enterprise ATT&CK content. The beta site will be
separate from the main (and still official) ATT&CK content for a period of approximately 3 months to allow for feedback and for users to
assess their transition plans to ATT&CK with sub-techniques.

In total, the sub-technique version of ATT&CK for Enterprise contains 156 techniques (reduced from 266) and 260 sub-techniques.

See [the accompanying blog post](https://medium.com/mitre-attack/attack-subs-what-you-need-to-know-99bce414ae0b) for more details.

### Techniques

**Enterprise**

View enterprise technique updates in the ATT&CK Navigator [here](https://mitre-attack.github.io/attack-navigator/beta/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fattack-navigator%2Ffeature%2Fsubtechniques-3.1%2Flayers%2Fdata%2Fupdate_layers%2FMarch_2020_Updates_Enterprise.json).

New Techniques:

* [Abuse Elevation Control Mechanism](/techniques/T1548) - Created to consolidate similar behaviors that take advantage of elevation control
	* [Bypass User Access Control](/techniques/T1548/002) - Existing technique that became a sub-technique
	* [Elevated Execution with Prompt](/techniques/T1548/004) - Existing technique that became a sub-technique
	* [Setuid and Setgid](/techniques/T1548/001) - Existing technique that became a sub-technique
	* [Sudo and Sudo Caching](/techniques/T1548/003) - Existing technique that became a sub-technique
* Access Token Manipulation: [Create Process with Token](/techniques/T1134/002) - Broken out from pre-defined behavior within Access Token Manipulation
* Access Token Manipulation: [Make and Impersonate Token](/techniques/T1134/003) - Broken out from pre-defined behavior within Access Token Manipulation
* Access Token Manipulation: [Parent PID Spoofing](/techniques/T1134/004) - Added due to manipulation of tokens
* Access Token Manipulation: [SID-History Injection](/techniques/T1134/005) - Added due to manipulation of token information
* Access Token Manipulation: [Token Impersonation/Theft](/techniques/T1134/001) - Broken out from pre-defined behavior within Access Token Manipulation
* Account Discovery: [Cloud Account](/techniques/T1087/004) - Added for parity with Create Account
* Account Discovery: [Domain Account](/techniques/T1087/002) - Added for parity with Create Account
* Account Discovery: [Email Account](/techniques/T1087/003) - Broken out from pre-defined behavior within Account Discovery
* Account Discovery: [Local Account](/techniques/T1087/001) - Added for parity with Create Account
* Account Manipulation: [Add Office 365 Global Administrator Role](/techniques/T1098/003) - Broken out from pre-defined behavior within Account Manipulation
* Account Manipulation: [Additional Azure Service Principal Credentials](/techniques/T1098/001) - Broken out from pre-defined behavior within Account Manipulation
* Account Manipulation: [Exchange Email Delegate Permissions](/techniques/T1098/002) - Broken out from pre-defined behavior within Account Manipulation
* Application Layer Protocol: [DNS](/techniques/T1071/004) - Created as distinct behavior due to how Application Layer Protocols are used for C2
* Application Layer Protocol: [File Transfer Protocols](/techniques/T1071/002) - Created as distinct behavior due to how Application Layer Protocols are used for C2
* Application Layer Protocol: [Mail Protocols](/techniques/T1071/003) - Created as distinct behavior due to how Application Layer Protocols are used for C2
* Application Layer Protocol: [Web Protocols](/techniques/T1071/001) - Created as distinct behavior due to how Application Layer Protocols are used for C2
* [Archive Collected Data](/techniques/T1560) - Created to consolidate behavior around encrypting and compressing collected data
	* [Archive via Custom Method](/techniques/T1560/003) - Broken out from pre-defined behavior within Archive Collected Data
	* [Archive via Library](/techniques/T1560/002) - Broken out from pre-defined behavior within Archive Collected Data
	* [Archive via Utility](/techniques/T1560/001) - Broken out from pre-defined behavior within Archive Collected Data
* [Boot or Logon Autostart Execution](/techniques/T1547) - Created to consolidate similar autostart execution locations
	* [Authentication Package](/techniques/T1547/002) - Existing technique that became a sub-technique
	* [Kernel Modules and Extensions](/techniques/T1547/006) - Existing technique that became a sub-technique
	* [LSASS Driver](/techniques/T1547/008) - Existing technique that became a sub-technique
	* [Plist Modification](/techniques/T1547/011) - Existing technique that became a sub-technique
	* [Port Monitors](/techniques/T1547/010)  - Existing technique that became a sub-technique
	* [Re-opened Applications](/techniques/T1547/007)  - Existing technique that became a sub-technique
	* [Registry Run Keys / Startup Folder](/techniques/T1547/001) - Existing technique that became a sub-technique
	* [Security Support Provider](/techniques/T1547/005) - Existing technique that became a sub-technique
	* [Shortcut Modification](/techniques/T1547/009) - Existing technique that became a sub-technique
	* [Time Providers](/techniques/T1547/003) - Existing technique that became a sub-technique
	* [Winlogon Helper DLL](/techniques/T1547/004) - Existing technique that became a sub-technique
* Boot or Logon Initialization Scripts: [Logon Script (Mac)](/techniques/T1037/002) - Existing technique that became a sub-technique
* Boot or Logon Initialization Scripts: [Logon Script (Windows)](/techniques/T1037/001) - Existing technique that became a sub-technique
* Boot or Logon Initialization Scripts: [Network Logon Script](/techniques/T1037/003) - Existing technique that became a sub-technique
* Boot or Logon Initialization Scripts: [Rc.common](/techniques/T1037/004) - Existing technique that became a sub-technique
* Boot or Logon Initialization Scripts: [Startup Items](/techniques/T1037/005) - Existing technique that became a sub-technique
* Brute Force: [Credential Stuffing](/techniques/T1110/004) - Created as distinct behavior variation of Brute Force
* Brute Force: [Password Cracking](/techniques/T1110/002) - Broken out from pre-defined behavior within Brute Force
* Brute Force: [Password Guessing](/techniques/T1110/001) - Broken out from pre-defined behavior within Brute Force
* Brute Force: [Password Spraying](/techniques/T1110/003) - Broken out from pre-defined behavior within Brute Force
* Command and Scripting Interpreter: [AppleScript](/techniques/T1059/002) - Existing technique that became a sub-technique
* Command and Scripting Interpreter: [Bash](/techniques/T1059/004) - Existing technique that became a sub-technique
* Command and Scripting Interpreter: [PowerShell](/techniques/T1059/001) - Existing technique that became a sub-technique
* Command and Scripting Interpreter: [Python](/techniques/T1059/006) - Created as distinct behavior within Command and Scripting Interpreter
* Command and Scripting Interpreter: [VBScript](/techniques/T1059/005) - Created as distinct behavior within Command and Scripting Interpreter
* Command and Scripting Interpreter: [Windows Command Shell](/techniques/T1059/003) - Existing technique that became a sub-technique
* [Compromise Client Software Binary](/techniques/T1554) - New technique based on contribution
* Create Account: [Cloud Account](/techniques/T1136/003) - Broken out from pre-defined behavior within Create Account
* Create Account: [Domain Account](/techniques/T1136/002) - Broken out from pre-defined behavior within Create Account
* Create Account: [Local Account](/techniques/T1136/001) - Broken out from pre-defined behavior within Create Account
* [Create or Modify System Process](/techniques/T1543) - Created to consolidate behavior around system-level processes
	* [Launch Agent](/techniques/T1543/001) - Existing technique that became a sub-technique
	* [Launch Daemon](/techniques/T1543/004) - Existing technique that became a sub-technique
	* [Systemd Service](/techniques/T1543/002) - Existing technique that became a sub-technique
	* [Windows Service](/techniques/T1543/003) - Existing technique that became a sub-technique. Consolidates Modify Existing Service and New Service techniques into one sub-technique
* [Credentials from Password Stores](/techniques/T1555) - Created to consolidate locations where passwords are stored
	* [Credentials from Web Browsers](/techniques/T1555/003) - Existing technique that became a sub-technique
	* [Keychain](/techniques/T1555/001) - Existing technique that became a sub-technique
	* [Securityd Memory](/techniques/T1555/002) - Existing technique that became a sub-technique
* Data Encoding: [Non-Standard Encoding](/techniques/T1132/002) - Broken out from pre-defined behavior within Data Encoding
* Data Encoding: [Standard Encoding](/techniques/T1132/001) - Broken out from pre-defined behavior within Data Encoding
	* [Data Manipulation](/techniques/T1565) - Created to consolidate existing behaviors around data manipulation
		* [Runtime Data Manipulation](/techniques/T1565/003) - Existing technique that became a sub-technique
		* [Stored Data Manipulation](/techniques/T1565/001) - Existing technique that became a sub-technique
		* [Transmitted Data Manipulation](/techniques/T1565/002) - Existing technique that became a sub-technique
* Data Obfuscation: [Junk Data](/techniques/T1001/001) - Broken out from pre-defined behavior within Data Obfuscation
* Data Obfuscation: [Protocol Impersonation](/techniques/T1001/003) - Broken out from pre-defined behavior within Data Obfuscation
* Data Obfuscation: [Steganography](/techniques/T1001/002) - Broken out from pre-defined behavior within Data Obfuscation
* Data Staged: [Local Data Staging](/techniques/T1074/001) - Broken out from pre-defined behavior within Data Staged
* Data Staged: [Remote Data Staging](/techniques/T1074/002) - Broken out from pre-defined behavior within Data Staged
* Data from Information Repositories: [Confluence](/techniques/T1213/001) - Broken out from pre-defined behavior within Data from Information Repositories
* Data from Information Repositories: [Sharepoint](/techniques/T1213/002) - Broken out from pre-defined behavior within Data from Information Repositories
* Defacement: [External Defacement](/techniques/T1491/002) - Broken out from pre-defined behavior within Defacement
* Defacement: [Internal Defacement](/techniques/T1491/001) - Broken out from pre-defined behavior within Defacement
* [Disk Wipe](/techniques/T1561) - Created to consolidate behavior around disk wiping
	* [Disk Content Wipe](/techniques/T1561/001) - Existing technique that became a sub-technique
	* [Disk Structure Wipe](/techniques/T1561/002) - Existing technique that became a sub-technique
* [Dynamic Resolution](/techniques/T1568) - Created to consolidate behavior around dynamic C2 behavior
	* [DNS Calculation](/techniques/T1568/003) - Existing PRE-ATT&CK technique that became a sub-technique in Enterprise
	* [Domain Generation Algorithms](/techniques/T1568/002) - Existing technique that became a sub-technique
	* [Fast Flux DNS](/techniques/T1568/001) - Existing PRE-ATT&CK technique that became a sub-technique in Enterprise
* Email Collection: [Email Forwarding Rule](/techniques/T1114/003) - Broken out from pre-defined behavior within Email Collection
* Email Collection: [Local Email Collection](/techniques/T1114/001) - Broken out from pre-defined behavior within Email Collection
* Email Collection: [Remote Email Collection](/techniques/T1114/002) - Broken out from pre-defined behavior within Email Collection
* [Encrypted Channel](/techniques/T1573) - Created to consolidate behavior around encrypted C2
	* [Asymmetric Cryptography](/techniques/T1573/002) - Broken out from pre-defined behavior within Encrypted Channel
	* [Symmetric Cryptography](/techniques/T1573/001) - Broken out from pre-defined behavior within Encrypted Channel
* Endpoint Denial of Service: [Application Exhaustion Flood](/techniques/T1499/003) - Broken out from pre-defined behavior within Endpoint Denial of Service
* Endpoint Denial of Service: [Application or System Exploitation](/techniques/T1499/004) - Broken out from pre-defined behavior within Endpoint Denial of Service
* Endpoint Denial of Service: [OS Exhaustion Flood](/techniques/T1499/001) - Broken out from pre-defined behavior within Endpoint Denial of Service
* Endpoint Denial of Service: [Service Exhaustion Flood](/techniques/T1499/002) - Broken out from pre-defined behavior within Endpoint Denial of Service
* [Event Triggered Execution](/techniques/T1546) - Created to consolidate persistence behavior due to adversary or user initiated actions
	* [.bash_profile and .bashrc](/techniques/T1546/004) - Existing technique that became a sub-technique
	* [Accessibility Features](/techniques/T1546/008) - Existing technique that became a sub-technique
	* [AppCert DLLs](/techniques/T1546/009) - Existing technique that became a sub-technique
	* [AppInit DLLs](/techniques/T1546/010) - Existing technique that became a sub-technique
	* [Application Shimming](/techniques/T1546/011) - Existing technique that became a sub-technique
	* [Change Default File Association](/techniques/T1546/001) - Existing technique that became a sub-technique
	* [Component Object Model Hijacking](/techniques/T1546/015) - Existing technique that became a sub-technique
	* [Emond](/techniques/T1546/014) - Existing technique that became a sub-technique
	* [Image File Execution Options Injection](/techniques/T1546/012) - Existing technique that became a sub-technique
	* [LC_LOAD_DYLIB Addition](/techniques/T1546/006) - Existing technique that became a sub-technique
	* [Netsh Helper DLL](/techniques/T1546/007) - Existing technique that became a sub-technique
	* [PowerShell Profile](/techniques/T1546/013) - Existing technique that became a sub-technique
	* [Screensaver](/techniques/T1546/002) - Existing technique that became a sub-technique
	* [Trap](/techniques/T1546/005) - Existing technique that became a sub-technique
	* [Windows Management Instrumentation Event Subscription](/techniques/T1546/003) - Existing technique that became a sub-technique
* Exfiltration Over Alternative Protocol: [Exfiltration Over Asymmetric Encrypted Non-C2 Protocol](/techniques/T1048/002) - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol
* Exfiltration Over Alternative Protocol: [Exfiltration Over Symmetric Encrypted Non-C2 Protocol](/techniques/T1048/001) - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol
* Exfiltration Over Alternative Protocol: [Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol](/techniques/T1048/003) - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol
* Exfiltration Over Other Network Medium: [Exfiltration Over Bluetooth](/techniques/T1011/001) - Broken out from pre-defined behavior within Exfiltration over Other Network Medium
* Exfiltration Over Physical Medium: [Exfiltration over USB](/techniques/T1052/001) - Broken out from pre-defined behavior within Exfiltration Over Physical Medium
* [Exfiltration Over Web Service](/techniques/T1567) - Created to consolidate behaviors around exfiltration to legitimate web services
	* [Exfiltration to Cloud Storage](/techniques/T1567/002) - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol
	* [Exfiltration to Code Repository](/techniques/T1567/001) - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol
* File and Directory Permissions Modification: [Linux and Mac File and Directory Permissions Modification](/techniques/T1222/002) - Broken out from pre-defined behavior within File and Directory Permissions Modification
* File and Directory Permissions Modification: [Windows File and Directory Permissions Modification](/techniques/T1222/001) - Broken out from pre-defined behavior within File and Directory Permissions Modification
* [Hide Artifacts](/techniques/T1564) - Created to consolidate behaviors around defense evasion through creating hidden objects that may be difficult to see
	* [Hidden Files and Directories](/techniques/T1564/001) - Existing technique that became a sub-technique
	* [Hidden Users](/techniques/T1564/002) - Existing technique that became a sub-technique
	* [Hidden Window](/techniques/T1564/003) - Existing technique that became a sub-technique
	* [NTFS File Attributes](/techniques/T1564/004) - Existing technique that became a sub-technique
* [Hijack Execution Flow](/techniques/T1574) - Created to consolidate behaviors around running executable code by placing it where it would be executed by a legitimate process
	* [DLL Search Order Hijacking](/techniques/T1574/001) - Existing technique that became a sub-technique
	* [DLL Side-Loading](/techniques/T1574/002) - Existing technique that became a sub-technique
	* [Dylib Hijacking](/techniques/T1574/004) - Existing technique that became a sub-technique
	* [Executable Installer File Permissions Weakness](/techniques/T1574/005) - Existing technique that became a sub-technique
	* [LD_PRELOAD](/techniques/T1574/006) - Existing technique that became a sub-technique
	* [Path Interception by PATH Environment Variable](/techniques/T1574/007) - Broken out from pre-defined behavior within the prior Path Interception technique
	* [Path Interception by Search Order Hijacking](/techniques/T1574/008) - Broken out from pre-defined behavior within the prior Path Interception technique
	* [Path Interception by Unquoted Path](/techniques/T1574/009) - Broken out from pre-defined behavior within the prior Path Interception technique
	* [Services File Permissions Weakness](/techniques/T1574/010) - Existing technique that became a sub-technique
	* [Services Registry Permissions Weakness](/techniques/T1574/011) - Existing technique that became a sub-technique
* [Impair Defenses](/techniques/T1562) - Created to consolidate behaviors that prevent a defense from working as intended
	* [Disable Windows Event Logging](/techniques/T1562/002) - Existing technique that became a sub-technique
	* [Disable or Modify System Firewall](/techniques/T1562/004) - Existing technique that became a sub-technique
	* [Disable or Modify Tools](/techniques/T1562/001) - Existing technique that became a sub-technique
	* [HISTCONTROL](/techniques/T1562/003) - Existing technique that became a sub-technique
	* [Indicator Blocking](/techniques/T1562/006) - Existing technique that became a sub-technique
* Indicator Removal on Host: [Clear Command History](/techniques/T1070/003) - Existing technique that became a sub-technique
* Indicator Removal on Host: [Clear Linux or Mac System Logs](/techniques/T1070/002) - Broken out from pre-defined behavior within Indicator Removal on Host
* Indicator Removal on Host: [Clear Windows Event Logs](/techniques/T1070/001) - Broken out from pre-defined behavior within Indicator Removal on Host
* Indicator Removal on Host: [File Deletion](/techniques/T1070/004) - Existing technique that became a sub-technique
* Indicator Removal on Host: [Network Share Connection Removal](/techniques/T1070/005) - Existing technique that became a sub-technique
* Indicator Removal on Host: [Timestomp](/techniques/T1070/006) - Existing technique that became a sub-technique
* Input Capture: [Credential API Hooking](/techniques/T1056/004) - Existing technique that became a sub-technique and was renamed from API Hooking. Scope change to only credential access for API hooking was based on available procedure examples
* Input Capture: [GUI Input Capture](/techniques/T1056/002) - Broken out from pre-defined behavior within Input Capture
* Input Capture: [Keylogging](/techniques/T1056/001) - Broken out from pre-defined behavior within Input Capture
* Input Capture: [Web Portal Capture](/techniques/T1056/003) - Broken out from pre-defined behavior within Input Capture
* [Inter-Process Communication](/techniques/T1559) - Created to consolidate behavior related to using IPC for local system execution
	* [Component Object Model](/techniques/T1559/001) - Broken out from pre-defined behavior within the prior Component Object Model and Distributed COM technique
	* [Dynamic Data Exchange](/techniques/T1559/002) - Existing technique that became a sub-technique
* [Lateral Tool Transfer](/techniques/T1570) - Broken out from pre-defined behavior within the prior Remote File Copy technique to focus on file transfer within a network
* [Man-in-the-Middle](/techniques/T1557) - Created to consolidate behavior related to setting up man-in-the-middle condition within a network
	* [LLMNR/NBT-NS Poisoning and SMB Relay](/techniques/T1557/001) - Existing technique that became a sub-technique
* Masquerading: [Invalid Code Signature](/techniques/T1036/001) - Created based on procedure examples within Code Signing as a distinct behavior using invalid digital signatures
* Masquerading: [Masquerade Task or Service](/techniques/T1036/004) - Broken out from pre-defined behavior within Masquerading
* Masquerading: [Match Legitimate Name or Location](/techniques/T1036/005) - Broken out from pre-defined behavior within Masquerading
* Masquerading: [Rename System Utilities](/techniques/T1036/003) - Broken out from pre-defined behavior within Masquerading
* Masquerading: [Right-to-Left Override](/techniques/T1036/002) - Broken out from pre-defined behavior within Masquerading
* Masquerading: [Space after Filename](/techniques/T1036/006) - Existing technique that became a sub-technique
* [Modify Authentication Process](/techniques/T1556) - Created to consolidate behavior related to changing the authentication process previously under Account Manipulation
	* [Domain Controller Authentication](/techniques/T1556/001) - Broken out from pre-defined behavior within Account Manipulation
	* [Password Filter DLL](/techniques/T1556/002) - Existing technique that became a sub-technique
* Network Denial of Service: [Direct Network Flood](/techniques/T1498/001) - Broken out from pre-defined behavior within Network Denial of Service
* Network Denial of Service: [Reflection Amplification](/techniques/T1498/002) - Broken out from pre-defined behavior within Network Denial of Service
* [Non-Standard Port](/techniques/T1571) - Created to refine the idea behind Common and Uncommonly Used Port to focus the behavior on use of a non-standard port for C2 based on the protocol used
* OS Credential Dumping: [/etc/passwd and /etc/shadow](/techniques/T1003/008) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [Cached Domain Credentials](/techniques/T1003/005) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [DCSync](/techniques/T1003/006) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [LSA Secrets](/techniques/T1003/004) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [LSASS Memory](/techniques/T1003/001) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [NTDS](/techniques/T1003/003) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [Proc Filesystem](/techniques/T1003/007) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [Security Account Manager](/techniques/T1003/002) - Broken out from pre-defined behavior within OS Credential Dumping
* Obfuscated Files or Information: [Binary Padding](/techniques/T1027/001) - Existing technique that became a sub-technique
* Obfuscated Files or Information: [Compile After Delivery](/techniques/T1027/004) - Existing technique that became a sub-technique
* Obfuscated Files or Information: [Indicator Removal from Tools](/techniques/T1027/005) - Existing technique that became a sub-technique
* Obfuscated Files or Information: [Software Packing](/techniques/T1027/002) - Existing technique that became a sub-technique
* Obfuscated Files or Information: [Steganography](/techniques/T1027/003) - Broken out from pre-defined behavior within Obfuscated Files or Information
* Office Application Startup: [Add-ins](/techniques/T1137/006) - Broken out from pre-defined behavior within Office Application Startup
* Office Application Startup: [Office Template Macros](/techniques/T1137/001) - Broken out from pre-defined behavior within Office Application Startup
* Office Application Startup: [Office Test](/techniques/T1137/002) - Broken out from pre-defined behavior within Office Application Startup
* Office Application Startup: [Outlook Forms](/techniques/T1137/003) - Broken out from pre-defined behavior within Office Application Startup
* Office Application Startup: [Outlook Home Page](/techniques/T1137/004) - Broken out from pre-defined behavior within Office Application Startup
* Office Application Startup: [Outlook Rules](/techniques/T1137/005) - Broken out from pre-defined behavior within Office Application Startup
* Permission Groups Discovery: [Cloud Groups](/techniques/T1069/003) - Broken out from pre-defined behavior within Permission Groups Discovery in a way that has parity with Account Discovery
* Permission Groups Discovery: [Domain Groups](/techniques/T1069/002) - Broken out from pre-defined behavior within Permission Groups Discovery in a way that has parity with Account Discovery
* Permission Groups Discovery: [Local Groups](/techniques/T1069/001) - Broken out from pre-defined behavior within Permission Groups Discovery in a way that has parity with Account Discovery
* [Phishing](/techniques/T1566) - Created to consolidate behavior around phishing and spearphishing
	* [Spearphishing Attachment](/techniques/T1566/001) - Existing technique that became a sub-technique
	* [Spearphishing Link](/techniques/T1566/002) - Existing technique that became a sub-technique
	* [Spearphishing via Service](/techniques/T1566/003) - Existing technique that became a sub-technique
* [Pre-OS Boot](/techniques/T1542) - Created to consolidate behavior around persistence that loads before the OS boots
	* [Bootkit](/techniques/T1542/003) - Existing technique that became a sub-technique
	* [Component Firmware](/techniques/T1542/002) - Existing technique that became a sub-technique
	* [System Firmware](/techniques/T1542/001) - Existing technique that became a sub-technique
* Process Injection: [Asynchronous Procedure Call](/techniques/T1055/004) - Existing technique that became a sub-technique
* Process Injection: [Dynamic-link Library Injection](/techniques/T1055/001) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Extra Window Memory Injection](/techniques/T1055/011) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Portable Executable Injection](/techniques/T1055/002) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Proc Memory](/techniques/T1055/009) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Process Doppelgänging](/techniques/T1055/013) - Existing technique that became a sub-technique
* Process Injection: [Process Hollowing](/techniques/T1055/012) - Existing technique that became a sub-technique
* Process Injection: [Ptrace System Calls](/techniques/T1055/008) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Thread Execution Hijacking](/techniques/T1055/003) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Thread Local Storage](/techniques/T1055/005) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [VDSO Hijacking](/techniques/T1055/014) - Broken out from pre-defined behavior within Process Injection
* [Protocol Tunneling](/techniques/T1572) - Created to define behavior broken out from the prior Standard Application and Standard Cryptographic Protocol techniques
* Proxy: [Domain Fronting](/techniques/T1090/004) - Existing technique that became a sub-technique
* Proxy: [External Proxy](/techniques/T1090/002) - Broken out from pre-defined behavior within Connection Proxy
* Proxy: [Internal Proxy](/techniques/T1090/001) - Broken out from pre-defined behavior within Connection Proxy
* Proxy: [Multi-hop Proxy](/techniques/T1090/003) - Existing technique that became a sub-technique
* [Remote Service Session Hijacking](/techniques/T1563) - Created to consolidate behavior related to hijacking existing remote connection sessions
	* [RDP Hijacking](/techniques/T1563/002) - Broken out from pre-defined behavior within Remote Desktop Protocol
	* [SSH Hijacking](/techniques/T1563/001) - Existing technique that became a sub-technique
* Remote Services: [Distributed Component Object Model](/techniques/T1021/003) - Broken out from pre-defined behavior within Component Object Model and Distributed COM technique
* Remote Services: [Remote Desktop Protocol](/techniques/T1021/001) - Existing technique that became a sub-technique
* Remote Services: [SMB/Windows Admin Shares](/techniques/T1021/002) - Existing technique that became a sub-technique and was renamed from Windows Admin Shares
* Remote Services: [SSH](/techniques/T1021/004) - Broken out from pre-defined behavior within Remote Services technique
* Remote Services: [VNC](/techniques/T1021/005) - Broken out from pre-defined behavior within Remote Services technique
* Remote Services: [Windows Remote Management](/techniques/T1021/006) - Existing technique that became a sub-technique
* Scheduled Task/Job: [At (Linux)](/techniques/T1053/001) - Broken out from pre-defined behavior within prior Local Job Scheduling technique
* Scheduled Task/Job: [At (Windows)](/techniques/T1053/002) - Broken out from pre-defined behavior within prior Scheduled Task technique
* Scheduled Task/Job: [Cron](/techniques/T1053/003) - Broken out from pre-defined behavior within prior Local Job Scheduling technique
* Scheduled Task/Job: [Launchd](/techniques/T1053/004) - Existing technique that became a sub-technique
* Scheduled Task/Job: [Scheduled Task](/techniques/T1053/005) - Existing technique that became a sub-technique
* Server Software Component: [SQL Stored Procedures](/techniques/T1505/001) - Broken out from pre-defined behavior within Server Software Component technique
* Server Software Component: [Transport Agent](/techniques/T1505/002) - Broken out from pre-defined behavior within Server Software Component technique
* Server Software Component: [Web Shell](/techniques/T1505/003) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [CMSTP](/techniques/T1218/003) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Compiled HTML File](/techniques/T1218/001) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Control Panel](/techniques/T1218/002) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [InstallUtil](/techniques/T1218/004) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Mshta](/techniques/T1218/005) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Msiexec](/techniques/T1218/007) - Broken out from pre-defined behavior within Signed Binary Proxy Execution technique
* Signed Binary Proxy Execution: [Odbcconf](/techniques/T1218/008) - Broken out from pre-defined behavior within Signed Binary Proxy Execution technique
* Signed Binary Proxy Execution: [Regsvcs/Regasm](/techniques/T1218/009) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Regsvr32](/techniques/T1218/010) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Rundll32](/techniques/T1218/011) - Existing technique that became a sub-technique
* Signed Script Proxy Execution: [PubPrn](/techniques/T1216/001) - Existing technique that became a sub-technique
* Software Discovery: [Security Software Discovery](/techniques/T1518/001) - Existing technique that became a sub-technique
* [Steal or Forge Kerberos Tickets](/techniques/T1558) - Created to consolidate behavior related to Kerberos tickets
	* [Golden Ticket](/techniques/T1558/001) - Broken out from pre-defined behavior within Pass the Ticket technique
	* [Kerberoasting](/techniques/T1558/003) - Existing technique that became a sub-technique
	* [Silver Ticket](/techniques/T1558/002) - Broken out from pre-defined behavior within Pass the Ticket technique
* [Subvert Trust Controls](/techniques/T1553) - Created to consolidate behavior related to getting around trust controls
	* [Code Signing](/techniques/T1553/002) - Existing technique that became a sub-technique
	* [Gatekeeper Bypass](/techniques/T1553/001) - Existing technique that became a sub-technique
	* [Install Root Certificate](/techniques/T1553/004) - Existing technique that became a sub-technique
	* [SIP and Trust Provider Hijacking](/techniques/T1553/003) - Existing technique that became a sub-technique
* Supply Chain Compromise: [Compromise Hardware Supply Chain](/techniques/T1195/003) - Broken out from pre-defined behavior within Supply Chain Compromise
* Supply Chain Compromise: [Compromise Software Dependencies and Development Tools](/techniques/T1195/001) - Broken out from pre-defined behavior within Supply Chain Compromise
* Supply Chain Compromise: [Compromise Software Supply Chain](/techniques/T1195/002) - Broken out from pre-defined behavior within Supply Chain Compromise
* [System Services](/techniques/T1569) - Created to consolidate behaviors related to execution of binaries through system services
	* [Launchctl](/techniques/T1569/001) - Existing technique that became a sub-technique
	* [Service Execution](/techniques/T1569/002) - Existing technique that became a sub-technique
* [Traffic Signaling](/techniques/T1205) - Created to consolidate behaviors around specifically formed network traffic that is used as a trigger to take an action
	* [Port Knocking](/techniques/T1205/001) - Existing technique that became a sub-technique
* Trusted Developer Utilities Proxy Execution: [MSBuild](/techniques/T1127/001) - Broken out from pre-defined behavior within Trusted Developer Utilities Proxy Execution
* [Unsecured Credentials](/techniques/T1552) - Created to consolidate places where unsecured credentials may be kept
	* [Bash History](/techniques/T1552/003) - Existing technique that became a sub-technique
	* [Cloud Instance Metadata API](/techniques/T1552/005) - Existing technique that became a sub-technique
	* [Credentials In Files](/techniques/T1552/001) - Existing technique that became a sub-technique
	* [Credentials in Registry](/techniques/T1552/002) - Existing technique that became a sub-technique
	* [Group Policy Preferences](/techniques/T1552/006) - Existing technique that became a sub-technique
	* [Private Keys](/techniques/T1552/004) - Existing technique that became a sub-technique
* [Use Alternate Authentication Material](/techniques/T1550) - Created to consolidate behavior related to use of non-password based credential material
	* [Application Access Token](/techniques/T1550/001) - Existing technique that became a sub-technique
	* [Pass the Hash](/techniques/T1550/002) - Existing technique that became a sub-technique
	* [Pass the Ticket](/techniques/T1550/003) - Existing technique that became a sub-technique
	* [Web Session Cookie](/techniques/T1550/004) - Existing technique that became a sub-technique
* User Execution: [Malicious File](/techniques/T1204/002) - Broken out from pre-defined behavior within User Execution
* User Execution: [Malicious Link](/techniques/T1204/001) - Broken out from pre-defined behavior within User Execution
* Valid Accounts: [Cloud Accounts](/techniques/T1078/004) - Broken out from pre-defined behavior Valid Accounts in a way that has parity with Create Account
* Valid Accounts: [Default Accounts](/techniques/T1078/001) - Broken out from pre-defined behavior within Valid Accounts in a way that has parity with Create Account
* Valid Accounts: [Domain Accounts](/techniques/T1078/002) - Broken out from pre-defined behavior within Valid Accounts in a way that has parity with Create Account
* Valid Accounts: [Local Accounts](/techniques/T1078/003) - Broken out from pre-defined behavior within Valid Accounts in a way that has parity with Create Account
* Virtualization/Sandbox Evasion: [System Checks](/techniques/T1497/001) - Broken out from pre-defined behavior within Virtualization/Sandbox Evasion
* Virtualization/Sandbox Evasion: [Time Based Evasion](/techniques/T1497/003) - Broken out from pre-defined behavior within Virtualization/Sandbox Evasion
* Virtualization/Sandbox Evasion: [User Activity Based Checks](/techniques/T1497/002) - Broken out from pre-defined behavior within Virtualization/Sandbox Evasion
* Web Service: [Bidirectional Communication](/techniques/T1102/002) - Broken out from pre-defined behavior within Web Service
* Web Service: [Dead Drop Resolver](/techniques/T1102/001) - Broken out from pre-defined behavior within Web Service
* Web Service: [One-Way Communication](/techniques/T1102/003) - Broken out from pre-defined behavior within Web Service


Technique changes:

Technique changes are largely due to new sub-techniques being added, name changes, or both.

* [Access Token Manipulation](/techniques/T1134) - New sub-techniques added
* [Account Discovery](/techniques/T1087) - New sub-techniques added
* [Account Manipulation](/techniques/T1098) - New sub-techniques added
* [Application Layer Protocol](/techniques/T1071) - Name change from Standard Application Layer Protocol and new sub-techniques added
* [Application Window Discovery](/techniques/T1010) - Fixed technique reference in description
* [Automated Exfiltration](/techniques/T1020) - Fixed technique reference in description
* [BITS Jobs](/techniques/T1197) - Fixed technique reference in description and minor description update
* [Boot or Logon Initialization Scripts](/techniques/T1037) - Name change from Logon Scripts and new sub-techniques added
* [Browser Extensions](/techniques/T1176) - Data sources changed and minor description update
* [Brute Force](/techniques/T1110) - New sub-techniques added
* [Clipboard Data](/techniques/T1115) - Minor description update
* [Command and Scripting Interpreter](/techniques/T1059) - Name change from Command-Line Interface and new sub-techniques added
* [Create Account](/techniques/T1136) - New sub-techniques added
* [Data Encoding](/techniques/T1132) - New sub-techniques added
* [Data Obfuscation](/techniques/T1001) - New sub-techniques added
* [Data Staged](/techniques/T1074) - New sub-techniques added
* [Data from Information Repositories](/techniques/T1213) - New sub-techniques added
* [Data from Local System](/techniques/T1005) - Fixed technique reference in description and minor description update
* [Data from Network Shared Drive](/techniques/T1039) - Fixed technique reference in description and minor description update
* [Data from Removable Media](/techniques/T1025) - Fixed technique reference in description and minor description update
* [Direct Volume Access](/techniques/T1006) - Name change from File System Logical Offsets
* [Domain Trust Discovery](/techniques/T1482) - Fixed technique reference in description and minor description update
* [Drive-by Compromise](/techniques/T1189) - Fixed technique reference in description and minor description update
* [Email Collection](/techniques/T1114) - New sub-techniques added
* [Exfiltration Over Alternative Protocol](/techniques/T1048) - New sub-techniques added
* [Exfiltration Over C2 Channel](/techniques/T1041) - Name change from Exfiltration over Command and Control Channel and added data sources
* [Exfiltration Over Other Network Medium](/techniques/T1011) - New sub-techniques added
* [Exfiltration Over Physical Medium](/techniques/T1052) - New sub-techniques added
* [Exploit Public-Facing Application](/techniques/T1190) - Minor description update
* [Exploitation for Client Execution](/techniques/T1203) - Minor description update
* [Exploitation for Credential Access](/techniques/T1212) - Minor description update
* [Exploitation for Defense Evasion](/techniques/T1211) - Minor description update
* [Exploitation for Privilege Escalation](/techniques/T1068) - Minor description update
* [Exploitation of Remote Services](/techniques/T1210) - Minor description update
* [External Remote Services](/techniques/T1133) - Minor description update
* [File and Directory Discovery](/techniques/T1083) - Fixed technique reference in description and minor description update
* [File and Directory Permissions Modification](/techniques/T1222) - New sub-techniques added
* [Forced Authentication](/techniques/T1187) - Minor description update
* [Group Policy Modification](/techniques/T1484) - Minor description update
* [Indicator Removal on Host](/techniques/T1070) - Minor description update
* [Indirect Command Execution](/techniques/T1202) - Minor description update
* [Ingress Tool Transfer](/techniques/T1105) - Name change from Remote File Copy
* [Input Capture](/techniques/T1056) - New sub-techniques added
* [Masquerading](/techniques/T1036) - New sub-techniques added
* [Native API](/techniques/T1106) - Name change from Execution through API
* [Network Service Scanning](/techniques/T1046) - Minor description update
* [Network Share Discovery](/techniques/T1135) - Fixed technique reference in description, added Linux, and minor description update
* [Network Sniffing](/techniques/T1040) - Minor description update
* [Non-Application Layer Protocol](/techniques/T1095) - Name change from Standard Non-Application Layer Protocol
* [OS Credential Dumping](/techniques/T1003) - Name change from Credential Dumping and new sub-techniques added
* [Obfuscated Files or Information](/techniques/T1027) - Minor description update
* [Password Policy Discovery](/techniques/T1201) - Fixed technique reference in description and minor description update
* [Peripheral Device Discovery](/techniques/T1120) - Fixed technique reference in description and minor description update
* [Permission Groups Discovery](/techniques/T1069) - New sub-techniques added
* [Process Discovery](/techniques/T1057) - Fixed technique reference in description and minor description update
* [Process Injection](/techniques/T1055) - New sub-techniques added
* [Proxy](/techniques/T1090) - Name change from Connection Proxy and new sub-techniques added
* [Query Registry](/techniques/T1012) - Fixed technique reference in description and minor description update
* [Remote Access Software](/techniques/T1219) - Name change from Remote Access Tools and fixed technique reference in description
* [Remote Services](/techniques/T1021) - New sub-techniques added
* [Remote System Discovery](/techniques/T1018) - Fixed technique reference in description and minor description update
* [Revert Cloud Instance](/techniques/T1536) - Minor description update, removed some data sources
* [Rogue Domain Controller](/techniques/T1207) - Name change from DCShadow
* [Rootkit](/techniques/T1014) - Minor description update
* [Scheduled Task/Job](/techniques/T1053) - New sub-techniques added
* [Scheduled Transfer](/techniques/T1029) - Minor description update
* [Screen Capture](/techniques/T1113) - Minor description update
* [Server Software Component](/techniques/T1505) - New sub-techniques added
* [Shared Modules](/techniques/T1129) - Name change from Execution through Module Load
* [Signed Binary Proxy Execution](/techniques/T1218) - New sub-techniques added
* [Signed Script Proxy Execution](/techniques/T1216) - New sub-techniques added
* [Software Deployment Tools](/techniques/T1072) - Minor description update and data source added
* [Software Discovery](/techniques/T1518) - New sub-techniques added
* [Supply Chain Compromise](/techniques/T1195) - New sub-techniques added
* [System Information Discovery](/techniques/T1082) - Fixed technique reference in description and minor description update
* [System Network Configuration Discovery](/techniques/T1016) - Fixed technique reference in description and minor description update
* [System Network Connections Discovery](/techniques/T1049) - Fixed technique reference in description and minor description update
* [System Owner/User Discovery](/techniques/T1033) - Fixed technique reference in description and minor description update
* [System Time Discovery](/techniques/T1124) - Minor description update
* [Taint Shared Content](/techniques/T1080) - Minor description update
* [Template Injection](/techniques/T1221) - Minor description update
* [Trusted Developer Utilities Proxy Execution](/techniques/T1127) - Minor description update, sub-technique added
* [Two-Factor Authentication Interception](/techniques/T1111) - Minor description update
* [User Execution](/techniques/T1204) - New sub-techniques added
* [Valid Accounts](/techniques/T1078) - New sub-techniques added
* [Virtualization/Sandbox Evasion](/techniques/T1497) - New sub-techniques added
* [Web Service](/techniques/T1102) - New sub-techniques added
* [Windows Management Instrumentation](/techniques/T1047) - Minor description update
* [XSL Script Processing](/techniques/T1220) - Minor description update


Minor Technique changes:

* [Browser Bookmark Discovery](/techniques/T1217)
* [Data Destruction](/techniques/T1485)
* [Data Encrypted for Impact](/techniques/T1486)
* [Endpoint Denial of Service](/techniques/T1499)
* [Implant Container Image](/techniques/T1525)
* [Network Denial of Service](/techniques/T1498)
* [Office Application Startup](/techniques/T1137)
* [Steal Application Access Token](/techniques/T1528)
* [System Service Discovery](/techniques/T1007)
* [System Shutdown/Reboot](/techniques/T1529)
* [Transfer Data to Cloud Account](/techniques/T1537)


Technique revocations:

* .bash_profile and .bashrc (revoked by Event Triggered Execution: [.bash_profile and .bashrc](/techniques/T1546/004))
* Accessibility Features (revoked by Event Triggered Execution: [Accessibility Features](/techniques/T1546/008))
* AppCert DLLs (revoked by Event Triggered Execution: [AppCert DLLs](/techniques/T1546/009))
* AppInit DLLs (revoked by Event Triggered Execution: [AppInit DLLs](/techniques/T1546/010))
* AppleScript (revoked by Command and Scripting Interpreter: [AppleScript](/techniques/T1059/002))
* Application Access Token (revoked by Use Alternate Authentication Material: [Application Access Token](/techniques/T1550/001))
* Application Deployment Software (revoked by [Software Deployment Tools](/techniques/T1072))
* Application Shimming (revoked by Event Triggered Execution: [Application Shimming](/techniques/T1546/011))
* Authentication Package (revoked by Boot or Logon Autostart Execution: [Authentication Package](/techniques/T1547/002))
* Bash History (revoked by Unsecured Credentials: [Bash History](/techniques/T1552/003))
* Binary Padding (revoked by Obfuscated Files or Information: [Binary Padding](/techniques/T1027/001))
* Bootkit (revoked by Pre-OS Boot: [Bootkit](/techniques/T1542/003))
* Bypass User Account Control (revoked by Abuse Elevation Control Mechanism: [Bypass User Access Control](/techniques/T1548/002))
* CMSTP (revoked by Signed Binary Proxy Execution: [CMSTP](/techniques/T1218/003))
* Change Default File Association (revoked by Event Triggered Execution: [Change Default File Association](/techniques/T1546/001))
* Clear Command History (revoked by Indicator Removal on Host: [Clear Command History](/techniques/T1070/003))
* Cloud Instance Metadata API (revoked by Unsecured Credentials: [Cloud Instance Metadata API](/techniques/T1552/005))
* Code Signing (revoked by Subvert Trust Controls: [Code Signing](/techniques/T1553/002))
* Commonly Used Port (revoked by [Non-Standard Port](/techniques/T1571))
* Compile After Delivery (revoked by Obfuscated Files or Information: [Compile After Delivery](/techniques/T1027/004))
* Compiled HTML File (revoked by Signed Binary Proxy Execution: [Compiled HTML File](/techniques/T1218/001))
* Component Firmware (revoked by Pre-OS Boot: [Component Firmware](/techniques/T1542/002))
* Component Object Model Hijacking (revoked by Event Triggered Execution: [Component Object Model Hijacking](/techniques/T1546/015))
* Control Panel Items (revoked by Signed Binary Proxy Execution: [Control Panel](/techniques/T1218/002))
* Credentials from Web Browsers (revoked by Credentials from Password Stores: [Credentials from Web Browsers](/techniques/T1555/003))
* Credentials in Files (revoked by Unsecured Credentials: [Credentials In Files](/techniques/T1552/001))
* Credentials in Registry (revoked by Unsecured Credentials: [Credentials in Registry](/techniques/T1552/002))
* Custom Command and Control Protocol (revoked by [Non-Application Layer Protocol](/techniques/T1095))
* Custom Cryptographic Protocol (revoked by [Encrypted Channel](/techniques/T1573))
* DLL Search Order Hijacking (revoked by Hijack Execution Flow: [DLL Search Order Hijacking](/techniques/T1574/001))
* DLL Side-Loading (revoked by Hijack Execution Flow: [DLL Side-Loading](/techniques/T1574/002))
* Data Compressed (revoked by [Archive Collected Data](/techniques/T1560))
* Data Encrypted (revoked by [Archive Collected Data](/techniques/T1560))
* Disabling Security Tools (revoked by Impair Defenses: [Disable or Modify Tools](/techniques/T1562/001))
* Disk Content Wipe (revoked by Disk Wipe: [Disk Content Wipe](/techniques/T1561/001))
* Disk Structure Wipe (revoked by Disk Wipe: [Disk Structure Wipe](/techniques/T1561/002))
* Domain Fronting (revoked by Proxy: [Domain Fronting](/techniques/T1090/004))
* Domain Generation Algorithms (revoked by Dynamic Resolution: [Domain Generation Algorithms](/techniques/T1568/002))
* Dylib Hijacking (revoked by Hijack Execution Flow: [Dylib Hijacking](/techniques/T1574/004))
* Dynamic Data Exchange (revoked by Inter-Process Communication: [Dynamic Data Exchange](/techniques/T1559/002))
* Elevated Execution with Prompt (revoked by Abuse Elevation Control Mechanism: [Elevated Execution with Prompt](/techniques/T1548/004))
* Emond (revoked by Event Triggered Execution: [Emond](/techniques/T1546/014))
* Extra Window Memory Injection (revoked by Process Injection: [Extra Window Memory Injection](/techniques/T1055/011))
* File Deletion (revoked by Indicator Removal on Host: [File Deletion](/techniques/T1070/004))
* File System Permissions Weakness (revoked by Hijack Execution Flow: [Services File Permissions Weakness](/techniques/T1574/010))
* Gatekeeper Bypass (revoked by Subvert Trust Controls: [Gatekeeper Bypass](/techniques/T1553/001))
* HISTCONTROL (revoked by Impair Defenses: [HISTCONTROL](/techniques/T1562/003))
* Hidden Files and Directories (revoked by Hide Artifacts: [Hidden Files and Directories](/techniques/T1564/001))
* Hidden Users (revoked by Hide Artifacts: [Hidden Users](/techniques/T1564/002))
* Hidden Window (revoked by Hide Artifacts: [Hidden Window](/techniques/T1564/003))
* Hooking (revoked by Input Capture: [Credential API Hooking](/techniques/T1056/004))
* Image File Execution Options Injection (revoked by Event Triggered Execution: [Image File Execution Options Injection](/techniques/T1546/012))
* Indicator Blocking (revoked by Impair Defenses: [Indicator Blocking](/techniques/T1562/006))
* Indicator Removal from Tools (revoked by Obfuscated Files or Information: [Indicator Removal from Tools](/techniques/T1027/005))
* Input Prompt (revoked by Input Capture: [GUI Input Capture](/techniques/T1056/002))
* Install Root Certificate (revoked by Subvert Trust Controls: [Install Root Certificate](/techniques/T1553/004))
* InstallUtil (revoked by Signed Binary Proxy Execution: [InstallUtil](/techniques/T1218/004))
* Kerberoasting (revoked by Steal or Forge Kerberos Tickets: [Kerberoasting](/techniques/T1558/003))
* Kernel Modules and Extensions (revoked by Boot or Logon Autostart Execution: [Kernel Modules and Extensions](/techniques/T1547/006))
* Keychain (revoked by Credentials from Password Stores: [Keychain](/techniques/T1555/001))
* LC_LOAD_DYLIB Addition (revoked by Event Triggered Execution: [LC_LOAD_DYLIB Addition](/techniques/T1546/006))
* LLMNR/NBT-NS Poisoning and Relay (revoked by Man-in-the-Middle: [LLMNR/NBT-NS Poisoning and SMB Relay](/techniques/T1557/001))
* LSASS Driver (revoked by Boot or Logon Autostart Execution: [LSASS Driver](/techniques/T1547/008))
* Launch Agent (revoked by Create or Modify System Process: [Launch Agent](/techniques/T1543/001))
* Launch Daemon (revoked by Create or Modify System Process: [Launch Daemon](/techniques/T1543/004))
* Launchctl (revoked by System Services: [Launchctl](/techniques/T1569/001))
* Local Job Scheduling (revoked by [Scheduled Task/Job](/techniques/T1053))
* Login Item (revoked by Boot or Logon Autostart Execution: [Plist Modification](/techniques/T1547/011))
* Modify Existing Service (revoked by Create or Modify System Process: [Windows Service](/techniques/T1543/003))
* Mshta (revoked by Signed Binary Proxy Execution: [Mshta](/techniques/T1218/005))
* Multi-hop Proxy (revoked by Proxy: [Multi-hop Proxy](/techniques/T1090/003))
* Multilayer Encryption (revoked by [Encrypted Channel](/techniques/T1573))
* NTFS File Attributes (revoked by Hide Artifacts: [NTFS File Attributes](/techniques/T1564/004))
* Netsh Helper DLL (revoked by Event Triggered Execution: [Netsh Helper DLL](/techniques/T1546/007))
* Network Share Connection Removal (revoked by Indicator Removal on Host: [Network Share Connection Removal](/techniques/T1070/005))
* New Service (revoked by Create or Modify System Process: [Windows Service](/techniques/T1543/003))
* Parent PID Spoofing (revoked by Access Token Manipulation: [Parent PID Spoofing](/techniques/T1134/004))
* Pass the Hash (revoked by Use Alternate Authentication Material: [Pass the Hash](/techniques/T1550/002))
* Pass the Ticket (revoked by Use Alternate Authentication Material: [Pass the Ticket](/techniques/T1550/003))
* Password Filter DLL (revoked by Modify Authentication Process: [Password Filter DLL](/techniques/T1556/002))
* Plist Modification (revoked by Boot or Logon Autostart Execution: [Plist Modification](/techniques/T1547/011))
* Port Knocking (revoked by Traffic Signaling: [Port Knocking](/techniques/T1205/001))
* Port Monitors (revoked by Boot or Logon Autostart Execution: [Port Monitors](/techniques/T1547/010))
* PowerShell (revoked by Command and Scripting Interpreter: [PowerShell](/techniques/T1059/001))
* PowerShell Profile (revoked by Event Triggered Execution: [PowerShell Profile](/techniques/T1546/013))
* Private Keys (revoked by Unsecured Credentials: [Private Keys](/techniques/T1552/004))
* Process Doppelgänging (revoked by Process Injection: [Process Doppelgänging](/techniques/T1055/013))
* Process Hollowing (revoked by Process Injection: [Process Hollowing](/techniques/T1055/012))
* Rc.common (revoked by Boot or Logon Initialization Scripts: [Rc.common](/techniques/T1037/004))
* Re-opened Applications (revoked by Boot or Logon Autostart Execution: [Re-opened Applications](/techniques/T1547/007))
* Registry Run Keys / Startup Folder (revoked by Boot or Logon Autostart Execution: [Registry Run Keys / Startup Folder](/techniques/T1547/001))
* Regsvcs/Regasm (revoked by Signed Binary Proxy Execution: [Regsvcs/Regasm](/techniques/T1218/009))
* Regsvr32 (revoked by Signed Binary Proxy Execution: [Regsvr32](/techniques/T1218/010))
* Remote Desktop Protocol (revoked by Remote Services: [Remote Desktop Protocol](/techniques/T1021/001))
* Rundll32 (revoked by Signed Binary Proxy Execution: [Rundll32](/techniques/T1218/011))
* Runtime Data Manipulation (revoked by Data Manipulation: [Runtime Data Manipulation](/techniques/T1565/003))
* SID-History Injection (revoked by Access Token Manipulation: [SID-History Injection](/techniques/T1134/005))
* SIP and Trust Provider Hijacking (revoked by Subvert Trust Controls: [SIP and Trust Provider Hijacking](/techniques/T1553/003))
* SSH Hijacking (revoked by Remote Service Session Hijacking: [SSH Hijacking](/techniques/T1563/001))
* Screensaver (revoked by Event Triggered Execution: [Screensaver](/techniques/T1546/002))
* Security Software Discovery (revoked by Software Discovery: [Security Software Discovery](/techniques/T1518/001))
* Security Support Provider (revoked by Boot or Logon Autostart Execution: [Security Support Provider](/techniques/T1547/005))
* Securityd Memory (revoked by Credentials from Password Stores: [Securityd Memory](/techniques/T1555/002))
* Service Execution (revoked by System Services: [Service Execution](/techniques/T1569/002))
* Service Registry Permissions Weakness (revoked by Hijack Execution Flow: [Services Registry Permissions Weakness](/techniques/T1574/011))
* Setuid and Setgid (revoked by Abuse Elevation Control Mechanism: [Setuid and Setgid](/techniques/T1548/001))
* Shortcut Modification (revoked by Boot or Logon Autostart Execution: [Shortcut Modification](/techniques/T1547/009))
* Software Packing (revoked by Obfuscated Files or Information: [Software Packing](/techniques/T1027/002))
* Space after Filename (revoked by Masquerading: [Space after Filename](/techniques/T1036/006))
* Spearphishing Attachment (revoked by Phishing: [Spearphishing Attachment](/techniques/T1566/001))
* Spearphishing Link (revoked by Phishing: [Spearphishing Link](/techniques/T1566/002))
* Spearphishing via Service (revoked by Phishing: [Spearphishing via Service](/techniques/T1566/003))
* Standard Cryptographic Protocol (revoked by [Encrypted Channel](/techniques/T1573))
* Startup Items (revoked by Boot or Logon Initialization Scripts: [Startup Items](/techniques/T1037/005))
* Stored Data Manipulation (revoked by Data Manipulation: [Stored Data Manipulation](/techniques/T1565/001))
* Sudo (revoked by Abuse Elevation Control Mechanism: [Sudo and Sudo Caching](/techniques/T1548/003))
* Sudo Caching (revoked by Abuse Elevation Control Mechanism: [Sudo and Sudo Caching](/techniques/T1548/003))
* System Firmware (revoked by Pre-OS Boot: [System Firmware](/techniques/T1542/001))
* Systemd Service (revoked by Create or Modify System Process: [Systemd Service](/techniques/T1543/002))
* Time Providers (revoked by Boot or Logon Autostart Execution: [Time Providers](/techniques/T1547/003))
* Timestomp (revoked by Indicator Removal on Host: [Timestomp](/techniques/T1070/006))
* Transmitted Data Manipulation (revoked by Data Manipulation: [Transmitted Data Manipulation](/techniques/T1565/002))
* Trap (revoked by Event Triggered Execution: [Trap](/techniques/T1546/005))
* Uncommonly Used Port (revoked by [Non-Standard Port](/techniques/T1571))
* Web Session Cookie (revoked by Use Alternate Authentication Material: [Web Session Cookie](/techniques/T1550/004))
* Web Shell (revoked by Server Software Component: [Web Shell](/techniques/T1505/003))
* Windows Admin Shares (revoked by Remote Services: [SMB/Windows Admin Shares](/techniques/T1021/002))
* Windows Management Instrumentation Event Subscription (revoked by Event Triggered Execution: [Windows Management Instrumentation Event Subscription](/techniques/T1546/003))
* Windows Remote Management (revoked by Remote Services: [Windows Remote Management](/techniques/T1021/006))
* Winlogon Helper DLL (revoked by Boot or Logon Autostart Execution: [Winlogon Helper DLL](/techniques/T1547/004))


Technique deprecations:

* [Component Object Model and Distributed COM](/techniques/T1175) - Deprecated and split into separate Component Object Model and Distributed Component Object Model sub-techniques. Existing Group/Software procedure examples were remapped appropriately
* [Graphical User Interface](/techniques/T1061) - Deprecated from ATT&CK because the behavior is redundant and implied by use of remote desktop tools like Remote Desktop Protocol. Existing Group/Software procedure examples were remapped appropriately
* [Hypervisor](/techniques/T1062) - Deprecated from ATT&CK due to lack of in the wild use
* [LC_MAIN Hijacking](/techniques/T1149) - Deprecated from ATT&CK due to lack of in the wild use
* [Multiband Communication](/techniques/T1026) - Deprecated from ATT&CK due to lack of in the wild use. Existing Group/Software procedure examples did not fit the core idea behind the technique
* [Path Interception](/techniques/T1034) - Deprecated and split into separate Unquoted Path, PATH Environment Variable, and Search Order Hijacking sub-techniques. Existing Group/Software procedure examples were remapped appropriately
* [Redundant Access](/techniques/T1108) - Deprecated from ATT&CK because the behavior is too high level and is sufficiently covered by Valid Accounts and External Remote Services. Existing Group/Software procedure examples were remapped appropriately
* [Scripting](/techniques/T1064) - Deprecated and split into separate Bash, VBScript, and Python sub-techniques of Command and Scripting Interpreter. Existing Group/Software procedure examples were remapped appropriately
* [Shared Webroot](/techniques/T1051) - Deprecated from ATT&CK due to lack of in the wild use
* [Source](/techniques/T1153) - Deprecated from ATT&CK due to lack of in the wild use


**PRE-ATT&CK**

New Techniques:
No changes

Technique changes:
No changes

Minor Technique changes:
No changes

Technique revocations:
No changes

Technique deprecations:

* DNSCalc
* Fast Flux DNS


**Mobile**

View mobile technique updates in the ATT&CK Navigator [here](https://mitre-attack.github.io/attack-navigator/beta/mobile/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fattack-navigator%2Ffeature%2Fsubtechniques-3.1%2Flayers%2Fdata%2Fupdate_layers%2FMarch_2020_Updates_Mobile.json).

New Techniques:

* [Code Injection](/techniques/T1540)
* [Foreground Persistence](/techniques/T1541)
* [Remote File Copy](/techniques/T1544)


Technique changes:

* [Broadcast Receivers](/techniques/T1402)
* [Carrier Billing Fraud](/techniques/T1448)
* [Suppress Application Icon](/techniques/T1508)


Minor Technique changes:

* [Access Notifications](/techniques/T1517)
* [Clipboard Modification](/techniques/T1510)
* [Deliver Malicious App via Other Means](/techniques/T1476)
* [Input Injection](/techniques/T1516)
* [Input Prompt](/techniques/T1411)
* [Screen Capture](/techniques/T1513)
* [System Information Discovery](/techniques/T1426)


Technique revocations:
No changes

Technique deprecations:
No changes

### Software

**Enterprise**

New Software:
No changes

Software changes:

* [3PARA RAT](/software/S0066)
* [4H RAT](/software/S0065)
* [ADVSTORESHELL](/software/S0045)
* [ASPXSpy](/software/S0073)
* [Agent Tesla](/software/S0331)
* [Agent.btz](/software/S0092)
* [Astaroth](/software/S0373)
* [AuditCred](/software/S0347)
* [AutoIt backdoor](/software/S0129)
* [Azorult](/software/S0344)
* [BACKSPACE](/software/S0031)
* [BADCALL](/software/S0245)
* [BADNEWS](/software/S0128)
* [BBSRAT](/software/S0127)
* [BISCUIT](/software/S0017)
* [BITSAdmin](/software/S0190)
* [BLACKCOFFEE](/software/S0069)
* [BONDUPDATER](/software/S0360)
* [BOOTRASH](/software/S0114)
* [BS2005](/software/S0014)
* [BUBBLEWRAP](/software/S0043)
* [BabyShark](/software/S0414)
* [Backdoor.Oldrea](/software/S0093)
* [BadPatch](/software/S0337)
* [Bandook](/software/S0234)
* [Bankshot](/software/S0239)
* [Bisonal](/software/S0268)
* [BlackEnergy](/software/S0089)
* [Brave Prince](/software/S0252)
* [CALENDAR](/software/S0025)
* [CCBkdr](/software/S0222)
* [CHOPSTICK](/software/S0023)
* [CORALDECK](/software/S0212)
* [CORESHELL](/software/S0137)
* [Cachedump](/software/S0119)
* [Calisto](/software/S0274)
* [CallMe](/software/S0077)
* [Cannon](/software/S0351)
* [Carbanak](/software/S0030)
* [Carbon](/software/S0335)
* [Cardinal RAT](/software/S0348)
* [Catchamas](/software/S0261)
* [ChChes](/software/S0144)
* [Chaos](/software/S0220)
* [Cherry Picker](/software/S0107)
* [China Chopper](/software/S0020)
* [CloudDuke](/software/S0054)
* [Cobalt Strike](/software/S0154)
* [Cobian RAT](/software/S0338)
* [CoinTicker](/software/S0369)
* [ComRAT](/software/S0126)
* [Comnie](/software/S0244)
* [CosmicDuke](/software/S0050)
* [CozyCar](/software/S0046)
* [Crimson](/software/S0115)
* [CrossRAT](/software/S0235)
* [DOGCALL](/software/S0213)
* [DarkComet](/software/S0334)
* [Daserf](/software/S0187)
* [DealersChoice](/software/S0243)
* [Denis](/software/S0354)
* [Derusbi](/software/S0021)
* [Dipsind](/software/S0200)
* [Dok](/software/S0281)
* [DownPaper](/software/S0186)
* [Downdelph](/software/S0134)
* [Dridex](/software/S0384)
* [Duqu](/software/S0038)
* [DustySky](/software/S0062)
* [Dyre](/software/S0024)
* [ELMER](/software/S0064)
* [Ebury](/software/S0377)
* [Elise](/software/S0081)
* [Emissary](/software/S0082)
* [Emotet](/software/S0367)
* [Empire](/software/S0363)
* [Epic](/software/S0091)
* [EvilBunny](/software/S0396)
* [EvilGrab](/software/S0152)
* [Exaramel for Linux](/software/S0401)
* [Exaramel for Windows](/software/S0343)
* [Expand](/software/S0361)
* [FALLCHILL](/software/S0181)
* [FELIXROOT](/software/S0267)
* [FLASHFLOOD](/software/S0036)
* [FLIPSIDE](/software/S0173)
* [FTP](/software/S0095)
* [FakeM](/software/S0076)
* [Felismus](/software/S0171)
* [Fgdump](/software/S0120)
* [FinFisher](/software/S0182)
* [Final1stspy](/software/S0355)
* [Flame](/software/S0143)
* [FlawedAmmyy](/software/S0381)
* [FruitFly](/software/S0277)
* [Fysbis](/software/S0410)
* [GLOOXMAIL](/software/S0026)
* [GRIFFON](/software/S0417)
* [Gazer](/software/S0168)
* [GeminiDuke](/software/S0049)
* [Gold Dragon](/software/S0249)
* [GravityRAT](/software/S0237)
* [GreyEnergy](/software/S0342)
* [H1N1](/software/S0132)
* [HAMMERTOSS](/software/S0037)
* [HARDRAIN](/software/S0246)
* [HAWKBALL](/software/S0391)
* [HIDEDRV](/software/S0135)
* [HOMEFRY](/software/S0232)
* [HOPLIGHT](/software/S0376)
* [HTTPBrowser](/software/S0070)
* [Hacking Team UEFI Rootkit](/software/S0047)
* [Helminth](/software/S0170)
* [Hi-Zor](/software/S0087)
* [HiddenWasp](/software/S0394)
* [Hikit](/software/S0009)
* [Hydraq](/software/S0203)
* [HyperBro](/software/S0398)
* [ISMInjector](/software/S0189)
* [Impacket](/software/S0357)
* [InnaputRAT](/software/S0259)
* [InvisiMole](/software/S0260)
* [Ixeshe](/software/S0015)
* [JCry](/software/S0389)
* [JHUHUGIT](/software/S0044)
* [JPIN](/software/S0201)
* [Janicab](/software/S0163)
* [KARAE](/software/S0215)
* [KEYMARBLE](/software/S0271)
* [KOMPROGO](/software/S0156)
* [KONNI](/software/S0356)
* [Kasidet](/software/S0088)
* [Kazuar](/software/S0265)
* [KeyBoy](/software/S0387)
* [Keydnap](/software/S0276)
* [Koadic](/software/S0250)
* [Komplex](/software/S0162)
* [Kwampirs](/software/S0236)
* [LOWBALL](/software/S0042)
* [LaZagne](/software/S0349)
* [LightNeuron](/software/S0395)
* [Linfo](/software/S0211)
* [Linux Rabbit](/software/S0362)
* [LoJax](/software/S0397)
* [LockerGoga](/software/S0372)
* [Lslsass](/software/S0121)
* [Lurid](/software/S0010)
* [MURKYTOP](/software/S0233)
* [MacSpy](/software/S0282)
* [Machete](/software/S0409)
* [MailSniper](/software/S0413)
* [Matroyshka](/software/S0167)
* [Micropsia](/software/S0339)
* [MimiPenguin](/software/S0179)
* [Mimikatz](/software/S0002)
* [MiniDuke](/software/S0051)
* [MirageFox](/software/S0280)
* [Mis-Type](/software/S0084)
* [Misdat](/software/S0083)
* [Mivast](/software/S0080)
* [MoonWind](/software/S0149)
* [More_eggs](/software/S0284)
* [Mosquito](/software/S0256)
* [NDiskMonitor](/software/S0272)
* [NETEAGLE](/software/S0034)
* [NETWIRE](/software/S0198)
* [NOKKI](/software/S0353)
* [NanHaiShu](/software/S0228)
* [NanoCore](/software/S0336)
* [NavRAT](/software/S0247)
* [Net](/software/S0039)
* [Net Crawler](/software/S0056)
* [NetTraveler](/software/S0033)
* [Nidiran](/software/S0118)
* [NotPetya](/software/S0368)
* [OLDBAIT](/software/S0138)
* [OSInfo](/software/S0165)
* [OSX/Shlayer](/software/S0402)
* [OSX_OCEANLOTUS.D](/software/S0352)
* [OceanSalt](/software/S0346)
* [Octopus](/software/S0340)
* [Olympic Destroyer](/software/S0365)
* [OnionDuke](/software/S0052)
* [OopsIE](/software/S0264)
* [Orz](/software/S0229)
* [OwaAuth](/software/S0072)
* [P2P ZeuS](/software/S0016)
* [PHOREAL](/software/S0158)
* [PLAINTEE](/software/S0254)
* [POORAIM](/software/S0216)
* [POSHSPY](/software/S0150)
* [POWERSOURCE](/software/S0145)
* [POWERSTATS](/software/S0223)
* [POWERTON](/software/S0371)
* [POWRUNER](/software/S0184)
* [PUNCHBUGGY](/software/S0196)
* [PUNCHTRACK](/software/S0197)
* [Pasam](/software/S0208)
* [PinchDuke](/software/S0048)
* [Pisloader](/software/S0124)
* [PlugX](/software/S0013)
* [PoisonIvy](/software/S0012)
* [PoshC2](/software/S0378)
* [PowerDuke](/software/S0139)
* [PowerSploit](/software/S0194)
* [PowerStallion](/software/S0393)
* [Prikormka](/software/S0113)
* [Proton](/software/S0279)
* [Proxysvc](/software/S0238)
* [PsExec](/software/S0029)
* [Psylo](/software/S0078)
* [Pteranodon](/software/S0147)
* [Pupy](/software/S0192)
* [QUADAGENT](/software/S0269)
* [QuasarRAT](/software/S0262)
* [RARSTONE](/software/S0055)
* [RATANKBA](/software/S0241)
* [RGDoor](/software/S0258)
* [RIPTIDE](/software/S0003)
* [ROCKBOOT](/software/S0112)
* [ROKRAT](/software/S0240)
* [RTM](/software/S0148)
* [RawPOS](/software/S0169)
* [Reaver](/software/S0172)
* [RedLeaves](/software/S0153)
* [Regin](/software/S0019)
* [Remcos](/software/S0332)
* [Remexi](/software/S0375)
* [RemoteCMD](/software/S0166)
* [Remsec](/software/S0125)
* [Revenge RAT](/software/S0379)
* [RobbinHood](/software/S0400)
* [RogueRobin](/software/S0270)
* [Rover](/software/S0090)
* [Ruler](/software/S0358)
* [RunningRAT](/software/S0253)
* [S-Type](/software/S0085)
* [SEASHARPEE](/software/S0185)
* [SHOTPUT](/software/S0063)
* [SLOWDRIFT](/software/S0218)
* [SNUGRIDE](/software/S0159)
* [SOUNDBITE](/software/S0157)
* [SPACESHIP](/software/S0035)
* [SQLRat](/software/S0390)
* [Sakula](/software/S0074)
* [SeaDuke](/software/S0053)
* [Seasalt](/software/S0345)
* [ServHelper](/software/S0382)
* [Shamoon](/software/S0140)
* [Skeleton Key](/software/S0007)
* [Smoke Loader](/software/S0226)
* [Socksbot](/software/S0273)
* [SpeakUp](/software/S0374)
* [SslMM](/software/S0058)
* [Starloader](/software/S0188)
* [StoneDrill](/software/S0380)
* [StreamEx](/software/S0142)
* [Sykipot](/software/S0018)
* [SynAck](/software/S0242)
* [Sys10](/software/S0060)
* [T9000](/software/S0098)
* [TDTESS](/software/S0164)
* [TEXTMATE](/software/S0146)
* [TURNEDUP](/software/S0199)
* [TYPEFRAME](/software/S0263)
* [Taidoor](/software/S0011)
* [TinyZBot](/software/S0004)
* [Tor](/software/S0183)
* [TrickBot](/software/S0266)
* [Trojan.Karagany](/software/S0094)
* [Trojan.Mebromi](/software/S0001)
* [Truvasys](/software/S0178)
* [Twitoor](/software/S0302)
* [UBoatRAT](/software/S0333)
* [UPPERCUT](/software/S0275)
* [USBStealer](/software/S0136)
* [Umbreon](/software/S0221)
* [Unknown Logger](/software/S0130)
* [Ursnif](/software/S0386)
* [VERMIN](/software/S0257)
* [Vasport](/software/S0207)
* [Volgmer](/software/S0180)
* [WEBC2](/software/S0109)
* [WannaCry](/software/S0366)
* [Wiarp](/software/S0206)
* [WinMM](/software/S0059)
* [Windows Credential Editor](/software/S0005)
* [Wingbird](/software/S0176)
* [Winnti](/software/S0141)
* [XAgentOSX](/software/S0161)
* [XTunnel](/software/S0117)
* [Xbash](/software/S0341)
* [Yahoyah](/software/S0388)
* [ZLib](/software/S0086)
* [Zebrocy](/software/S0251)
* [ZeroT](/software/S0230)
* [Zeus Panda](/software/S0330)
* [ZxShell](/software/S0412)
* [adbupd](/software/S0202)
* [at](/software/S0110)
* [cmd](/software/S0106)
* [dsquery](/software/S0105)
* [esentutl](/software/S0404)
* [gh0st RAT](/software/S0032)
* [gsecdump](/software/S0008)
* [hcdLoader](/software/S0071)
* [httpclient](/software/S0068)
* [iKitten](/software/S0278)
* [jRAT](/software/S0283)
* [netsh](/software/S0108)
* [njRAT](/software/S0385)
* [pngdowner](/software/S0067)
* [pwdump](/software/S0006)
* [schtasks](/software/S0111)
* [spwebmember](/software/S0227)
* [yty](/software/S0248)
* [zwShell](/software/S0350)


Minor Software changes:
No changes

Software revocations:
No changes

Software deprecations:
No changes

**PRE-ATT&CK**

New Software:
No changes

Software changes:
No changes

Minor Software changes:
No changes

Software revocations:
No changes

Software deprecations:
No changes

**Mobile**

New Software:

* [Dvmap](/software/S0420)
* [GolfSpy](/software/S0421)
* [SimBad](/software/S0419)
* [ViceLeaker](/software/S0418)


Software changes:

* [FinFisher](/software/S0182)
* [Monokle](/software/S0407)


Minor Software changes:

* [Pegasus for iOS](/software/S0289)


Software revocations:
No changes

Software deprecations:
No changes

### Groups

**Enterprise**

New Groups:

* [Bouncing Golf](/groups/G0097)


Group changes:

* [APT1](/groups/G0006)
* [APT12](/groups/G0005)
* [APT18](/groups/G0026)
* [APT19](/groups/G0073)
* [APT28](/groups/G0007)
* [APT29](/groups/G0016)
* [APT3](/groups/G0022)
* [APT32](/groups/G0050)
* [APT33](/groups/G0064)
* [APT37](/groups/G0067)
* [APT38](/groups/G0082)
* [APT39](/groups/G0087)
* [APT41](/groups/G0096)
* [Axiom](/groups/G0001)
* [BRONZE BUTLER](/groups/G0060)
* [Carbanak](/groups/G0008)
* [Cleaver](/groups/G0003)
* [Cobalt Group](/groups/G0080)
* [CopyKittens](/groups/G0052)
* [Dark Caracal](/groups/G0070)
* [DarkHydrus](/groups/G0079)
* [Darkhotel](/groups/G0012)
* [Deep Panda](/groups/G0009)
* [Dragonfly 2.0](/groups/G0074)
* [Elderwood](/groups/G0066)
* [Equation](/groups/G0020)
* [FIN10](/groups/G0051)
* [FIN4](/groups/G0085)
* [FIN5](/groups/G0053)
* [FIN6](/groups/G0037)
* [FIN7](/groups/G0046)
* [FIN8](/groups/G0061)
* [GCMAN](/groups/G0036)
* [Gallmaker](/groups/G0084)
* [Gamaredon Group](/groups/G0047)
* [Gorgon Group](/groups/G0078)
* [Group5](/groups/G0043)
* [Honeybee](/groups/G0072)
* [Ke3chang](/groups/G0004)
* [Kimsuky](/groups/G0094)
* [Lazarus Group](/groups/G0032)
* [Leafminer](/groups/G0077)
* [Leviathan](/groups/G0065)
* [Machete](/groups/G0095)
* [Magic Hound](/groups/G0059)
* [Moafee](/groups/G0002)
* [Molerats](/groups/G0021)
* [MuddyWater](/groups/G0069)
* [Night Dragon](/groups/G0014)
* [OilRig](/groups/G0049)
* [Orangeworm](/groups/G0071)
* [PLATINUM](/groups/G0068)
* [Patchwork](/groups/G0040)
* [PittyTiger](/groups/G0011)
* [Poseidon Group](/groups/G0033)
* [Putter Panda](/groups/G0024)
* [RTM](/groups/G0048)
* [Rancor](/groups/G0075)
* [Scarlet Mimic](/groups/G0029)
* [Silence](/groups/G0091)
* [SilverTerrier](/groups/G0083)
* [Soft Cell](/groups/G0093)
* [Sowbug](/groups/G0054)
* [Stealth Falcon](/groups/G0038)
* [Stolen Pencil](/groups/G0086)
* [Strider](/groups/G0041)
* [Suckfly](/groups/G0039)
* [TA459](/groups/G0062)
* [TA505](/groups/G0092)
* [TEMP.Veles](/groups/G0088)
* [The White Company](/groups/G0089)
* [Threat Group-1314](/groups/G0028)
* [Threat Group-3390](/groups/G0027)
* [Thrip](/groups/G0076)
* [Tropic Trooper](/groups/G0081)
* [Turla](/groups/G0010)
* [WIRTE](/groups/G0090)
* [admin@338](/groups/G0018)
* [menuPass](/groups/G0045)


Minor Group changes:
No changes

Group revocations:
No changes

Group deprecations:
No changes

**PRE-ATT&CK**

New Groups:
No changes

Group changes:

* [APT1](/groups/G0006)
* [APT28](/groups/G0007)
* [Cleaver](/groups/G0003)
* [Night Dragon](/groups/G0014)
* [TEMP.Veles](/groups/G0088)


Minor Group changes:
No changes

Group revocations:
No changes

Group deprecations:
No changes

**Mobile**

New Groups:

* [Bouncing Golf](/groups/G0097)


Group changes:

* [APT28](/groups/G0007)
* [Dark Caracal](/groups/G0070)


Minor Group changes:
No changes

Group revocations:
No changes

Group deprecations:
No changes

### Mitigations

**Enterprise**

New Mitigations:
No changes

Mitigation changes:

* [Active Directory Configuration](/mitigations/M1015) - Sub or technique relationships updated
* [Antivirus/Antimalware](/mitigations/M1049) - Sub or technique relationships updated
* [Application Isolation and Sandboxing](/mitigations/M1048) - Sub or technique relationships updated
* [Audit](/mitigations/M1047) - Sub or technique relationships updated
* [Credential Access Protection](/mitigations/M1043) - Sub or technique relationships updated
* [Data Backup](/mitigations/M1053) - Sub or technique relationships updated
* [Disable or Remove Feature or Program](/mitigations/M1042) - Sub or technique relationships updated
* [Execution Prevention](/mitigations/M1038) - Sub or technique relationships updated
* [Exploit Protection](/mitigations/M1050) - Sub or technique relationships updated
* [Network Segmentation](/mitigations/M1030) - Sub or technique relationships updated
* [Operating System Configuration](/mitigations/M1028) - Sub or technique relationships updated
* [Privileged Account Management](/mitigations/M1026) - Sub or technique relationships updated
* [Privileged Process Integrity](/mitigations/M1025) - Sub or technique relationships updated
* [Restrict File and Directory Permissions](/mitigations/M1022) - Sub or technique relationships updated
* [Software Configuration](/mitigations/M1054) - Sub or technique relationships updated
* [User Account Control](/mitigations/M1052) - Sub or technique relationships updated
* [User Account Management](/mitigations/M1018) - Sub or technique relationships updated
* [User Training](/mitigations/M1017) - Sub or technique relationships updated
* [Vulnerability Scanning](/mitigations/M1016) - Sub or technique relationships updated


Minor Mitigation changes:
No changes

Mitigation revocations:
No changes

Mitigation deprecations:
No changes

Mitigation deletions:

These are old mitigations that are no longer in use.

* Account Manipulation Mitigation
* Command-Line Interface Mitigation
* Connection Proxy Mitigation
* Execution through API Mitigation
* Exfiltration Over Alternative Protocol Mitigation
* File Permissions Modification Mitigation
* Input Capture Mitigation
* Obfuscated Files or Information Mitigation
* Office Application Startup Mitigation
* Process Injection Mitigation
* Remote Services Mitigation
* Signed Binary Proxy Execution Mitigation
* Standard Application Layer Protocol Mitigation
* Trusted Developer Utilities Mitigation
* Virtualization/Sandbox Evasion Mitigation
* Windows Management Instrumentation Mitigation


**PRE-ATT&CK**

New Mitigations:
No changes

Mitigation changes:
No changes

Minor Mitigation changes:
No changes

Mitigation revocations:
No changes

Mitigation deprecations:
No changes

**Mobile**

New Mitigations:
No changes

Mitigation changes:
No changes

Minor Mitigation changes:
No changes

Mitigation revocations:
No changes

Mitigation deprecations:
No changes
