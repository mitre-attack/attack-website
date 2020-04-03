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

In total, the sub-technique version of ATT&CK for Enterprise contains 167 techniques (reduced from 266) and 260 sub-techniques.

See [the accompanying blog post](https://medium.com/mitre-attack/attack-subs-what-you-need-to-know-99bce414ae0b) for more details.

### Techniques

**Enterprise**

New Techniques:

* [Abuse Elevation Control Mechanism](/beta/techniques/T1548) - Created to consolidate similar behaviors that take advantage of elevation control
	* [Bypass User Access Control](/beta/techniques/T1548/002) - Existing technique that became a sub-technique
	* [Elevated Execution with Prompt](/beta/techniques/T1548/004) - Existing technique that became a sub-technique
	* [Setuid and Setgid](/beta/techniques/T1548/001) - Existing technique that became a sub-technique
	* [Sudo and Sudo Caching](/beta/techniques/T1548/003) - Existing technique that became a sub-technique
* Access Token Manipulation: [Create Process with Token](/beta/techniques/T1134/002) - Broken out from pre-defined behavior within Access Token Manipulation
* Access Token Manipulation: [Make and Impersonate Token](/beta/techniques/T1134/003) - Broken out from pre-defined behavior within Access Token Manipulation
* Access Token Manipulation: [Parent PID Spoofing](/beta/techniques/T1134/004) - Added due to manipulation of tokens
* Access Token Manipulation: [SID-History Injection](/beta/techniques/T1134/005) - Added due to manipulation of token information
* Access Token Manipulation: [Token Impersonation/Theft](/beta/techniques/T1134/001) - Broken out from pre-defined behavior within Access Token Manipulation
* Account Discovery: [Cloud Account](/beta/techniques/T1087/004) - Added for parity with Create Account
* Account Discovery: [Domain Account](/beta/techniques/T1087/002) - Added for parity with Create Account
* Account Discovery: [Email Account](/beta/techniques/T1087/003) - Broken out from pre-defined behavior within Account Discovery
* Account Discovery: [Local Account](/beta/techniques/T1087/001) - Added for parity with Create Account
* Account Manipulation: [Add Office 365 Global Administrator Role](/beta/techniques/T1098/003) - Broken out from pre-defined behavior within Account Manipulation
* Account Manipulation: [Additional Azure Service Principal Credentials](/beta/techniques/T1098/001) - Broken out from pre-defined behavior within Account Manipulation
* Account Manipulation: [Exchange Email Delegate Permissions](/beta/techniques/T1098/002) - Broken out from pre-defined behavior within Account Manipulation
* Application Layer Protocol: [DNS](/beta/techniques/T1071/004) - Created as distinct behavior due to how Application Layer Protocols are used for C2
* Application Layer Protocol: [File Transfer Protocols](/beta/techniques/T1071/002) - Created as distinct behavior due to how Application Layer Protocols are used for C2
* Application Layer Protocol: [Mail Protocols](/beta/techniques/T1071/003) - Created as distinct behavior due to how Application Layer Protocols are used for C2
* Application Layer Protocol: [Web Protocols](/beta/techniques/T1071/001) - Created as distinct behavior due to how Application Layer Protocols are used for C2
* [Archive Collected Data](/beta/techniques/T1560) - Created to consolidate behavior around encrypting and compressing collected data
	* [Archive via Custom Method](/beta/techniques/T1560/003) - Broken out from pre-defined behavior within Archive Collected Data
	* [Archive via Library](/beta/techniques/T1560/002) - Broken out from pre-defined behavior within Archive Collected Data
	* [Archive via Utility](/beta/techniques/T1560/001) - Broken out from pre-defined behavior within Archive Collected Data
* [Boot or Logon Autostart Execution](/beta/techniques/T1547) - Created to consolidate similar autostart execution locations
	* [Authentication Package](/beta/techniques/T1547/002) - Existing technique that became a sub-technique
	* [Kernel Modules and Extensions](/beta/techniques/T1547/006) - Existing technique that became a sub-technique
	* [LSASS Driver](/beta/techniques/T1547/008) - Existing technique that became a sub-technique
	* [Plist Modification](/beta/techniques/T1547/011) - Existing technique that became a sub-technique
	* [Port Monitors](/beta/techniques/T1547/010)  - Existing technique that became a sub-technique
	* [Re-opened Applications](/beta/techniques/T1547/007)  - Existing technique that became a sub-technique
	* [Registry Run Keys / Startup Folder](/beta/techniques/T1547/001) - Existing technique that became a sub-technique
	* [Security Support Provider](/beta/techniques/T1547/005) - Existing technique that became a sub-technique
	* [Shortcut Modification](/beta/techniques/T1547/009) - Existing technique that became a sub-technique
	* [Time Providers](/beta/techniques/T1547/003) - Existing technique that became a sub-technique
	* [Winlogon Helper DLL](/beta/techniques/T1547/004) - Existing technique that became a sub-technique
* Boot or Logon Initialization Scripts: [Logon Script (Mac)](/beta/techniques/T1037/002) - Existing technique that became a sub-technique
* Boot or Logon Initialization Scripts: [Logon Script (Windows)](/beta/techniques/T1037/001) - Existing technique that became a sub-technique
* Boot or Logon Initialization Scripts: [Network Logon Script](/beta/techniques/T1037/003) - Existing technique that became a sub-technique
* Boot or Logon Initialization Scripts: [Rc.common](/beta/techniques/T1037/004) - Existing technique that became a sub-technique
* Boot or Logon Initialization Scripts: [Startup Items](/beta/techniques/T1037/005) - Existing technique that became a sub-technique
* Brute Force: [Credential Stuffing](/beta/techniques/T1110/004) - Created as distinct behavior variation of Brute Force
* Brute Force: [Password Cracking](/beta/techniques/T1110/002) - Broken out from pre-defined behavior within Brute Force
* Brute Force: [Password Guessing](/beta/techniques/T1110/001) - Broken out from pre-defined behavior within Brute Force
* Brute Force: [Password Spraying](/beta/techniques/T1110/003) - Broken out from pre-defined behavior within Brute Force
* Command and Scripting Interpreter: [AppleScript](/beta/techniques/T1059/002) - Existing technique that became a sub-technique
* Command and Scripting Interpreter: [Bash](/beta/techniques/T1059/004) - Existing technique that became a sub-technique
* Command and Scripting Interpreter: [PowerShell](/beta/techniques/T1059/001) - Existing technique that became a sub-technique
* Command and Scripting Interpreter: [Python](/beta/techniques/T1059/006) - Created as distinct behavior within Command and Scripting Interpreter
* Command and Scripting Interpreter: [VBScript](/beta/techniques/T1059/005) - Created as distinct behavior within Command and Scripting Interpreter
* Command and Scripting Interpreter: [Windows Command Shell](/beta/techniques/T1059/003) - Existing technique that became a sub-technique
* [Compromise Client Software Binary](/beta/techniques/T1554) - New technique based on contribution
* Create Account: [Cloud Account](/beta/techniques/T1136/003) - Broken out from pre-defined behavior within Create Account
* Create Account: [Domain Account](/beta/techniques/T1136/002) - Broken out from pre-defined behavior within Create Account
* Create Account: [Local Account](/beta/techniques/T1136/001) - Broken out from pre-defined behavior within Create Account
* [Create or Modify System Process](/beta/techniques/T1543) - Created to consolidate behavior around system-level processes
	* [Launch Agent](/beta/techniques/T1543/001) - Existing technique that became a sub-technique
	* [Launch Daemon](/beta/techniques/T1543/004) - Existing technique that became a sub-technique
	* [Systemd Service](/beta/techniques/T1543/002) - Existing technique that became a sub-technique
	* [Windows Service](/beta/techniques/T1543/003) - Existing technique that became a sub-technique. Consolidates Modify Existing Service and New Service techniques into one sub-technique
* [Credentials from Password Stores](/beta/techniques/T1555) - Created to consolidate locations where passwords are stored
	* [Credentials from Web Browsers](/beta/techniques/T1555/003) - Existing technique that became a sub-technique
	* [Keychain](/beta/techniques/T1555/001) - Existing technique that became a sub-technique
	* [Securityd Memory](/beta/techniques/T1555/002) - Existing technique that became a sub-technique
* Data Encoding: [Non-Standard Encoding](/beta/techniques/T1132/002) - Broken out from pre-defined behavior within Data Encoding
* Data Encoding: [Standard Encoding](/beta/techniques/T1132/001) - Broken out from pre-defined behavior within Data Encoding
	* [Data Manipulation](/beta/techniques/T1565) - Created to consolidate existing behaviors around data manipulation
		* [Runtime Data Manipulation](/beta/techniques/T1565/003) - Existing technique that became a sub-technique
		* [Stored Data Manipulation](/beta/techniques/T1565/001) - Existing technique that became a sub-technique
		* [Transmitted Data Manipulation](/beta/techniques/T1565/002) - Existing technique that became a sub-technique
* Data Obfuscation: [Junk Data](/beta/techniques/T1001/001) - Broken out from pre-defined behavior within Data Obfuscation
* Data Obfuscation: [Protocol Impersonation](/beta/techniques/T1001/003) - Broken out from pre-defined behavior within Data Obfuscation
* Data Obfuscation: [Steganography](/beta/techniques/T1001/002) - Broken out from pre-defined behavior within Data Obfuscation
* Data Staged: [Local Data Staging](/beta/techniques/T1074/001) - Broken out from pre-defined behavior within Data Staged
* Data Staged: [Remote Data Staging](/beta/techniques/T1074/002) - Broken out from pre-defined behavior within Data Staged
* Data from Information Repositories: [Confluence](/beta/techniques/T1213/001) - Broken out from pre-defined behavior within Data from Information Repositories
* Data from Information Repositories: [Sharepoint](/beta/techniques/T1213/002) - Broken out from pre-defined behavior within Data from Information Repositories
* Defacement: [External Defacement](/beta/techniques/T1491/002) - Broken out from pre-defined behavior within Defacement
* Defacement: [Internal Defacement](/beta/techniques/T1491/001) - Broken out from pre-defined behavior within Defacement
* [Disk Wipe](/beta/techniques/T1561) - Created to consolidate behavior around disk wiping
	* [Disk Content Wipe](/beta/techniques/T1561/001) - Existing technique that became a sub-technique
	* [Disk Structure Wipe](/beta/techniques/T1561/002) - Existing technique that became a sub-technique
* [Dynamic Resolution](/beta/techniques/T1568) - Created to consolidate behavior around dynamic C2 behavior
	* [DNS Calculation](/beta/techniques/T1568/003) - Existing PRE-ATT&CK technique that became a sub-technique in Enterprise
	* [Domain Generation Algorithms](/beta/techniques/T1568/002) - Existing technique that became a sub-technique
	* [Fast Flux DNS](/beta/techniques/T1568/001) - Existing PRE-ATT&CK technique that became a sub-technique in Enterprise
* Email Collection: [Email Forwarding Rule](/beta/techniques/T1114/003) - Broken out from pre-defined behavior within Email Collection
* Email Collection: [Local Email Collection](/beta/techniques/T1114/001) - Broken out from pre-defined behavior within Email Collection
* Email Collection: [Remote Email Collection](/beta/techniques/T1114/002) - Broken out from pre-defined behavior within Email Collection
* [Encrypted Channel](/beta/techniques/T1573) - Created to consolidate behavior around encrypted C2
	* [Asymmetric Cryptography](/beta/techniques/T1573/002) - Broken out from pre-defined behavior within Encrypted Channel
	* [Symmetric Cryptography](/beta/techniques/T1573/001) - Broken out from pre-defined behavior within Encrypted Channel
* Endpoint Denial of Service: [Application Exhaustion Flood](/beta/techniques/T1499/003) - Broken out from pre-defined behavior within Endpoint Denial of Service
* Endpoint Denial of Service: [Application or System Exploitation](/beta/techniques/T1499/004) - Broken out from pre-defined behavior within Endpoint Denial of Service
* Endpoint Denial of Service: [OS Exhaustion Flood](/beta/techniques/T1499/001) - Broken out from pre-defined behavior within Endpoint Denial of Service
* Endpoint Denial of Service: [Service Exhaustion Flood](/beta/techniques/T1499/002) - Broken out from pre-defined behavior within Endpoint Denial of Service
* [Event Triggered Execution](/beta/techniques/T1546) - Created to consolidate persistence behavior due to adversary or user initiated actions
	* [.bash_profile and .bashrc](/beta/techniques/T1546/004) - Existing technique that became a sub-technique
	* [Accessibility Features](/beta/techniques/T1546/008) - Existing technique that became a sub-technique
	* [AppCert DLLs](/beta/techniques/T1546/009) - Existing technique that became a sub-technique
	* [AppInit DLLs](/beta/techniques/T1546/010) - Existing technique that became a sub-technique
	* [Application Shimming](/beta/techniques/T1546/011) - Existing technique that became a sub-technique
	* [Change Default File Association](/beta/techniques/T1546/001) - Existing technique that became a sub-technique
	* [Component Object Model Hijacking](/beta/techniques/T1546/015) - Existing technique that became a sub-technique
	* [Emond](/beta/techniques/T1546/014) - Existing technique that became a sub-technique
	* [Image File Execution Options Injection](/beta/techniques/T1546/012) - Existing technique that became a sub-technique
	* [LC_LOAD_DYLIB Addition](/beta/techniques/T1546/006) - Existing technique that became a sub-technique
	* [Netsh Helper DLL](/beta/techniques/T1546/007) - Existing technique that became a sub-technique
	* [PowerShell Profile](/beta/techniques/T1546/013) - Existing technique that became a sub-technique
	* [Screensaver](/beta/techniques/T1546/002) - Existing technique that became a sub-technique
	* [Trap](/beta/techniques/T1546/005) - Existing technique that became a sub-technique
	* [Windows Management Instrumentation Event Subscription](/beta/techniques/T1546/003) - Existing technique that became a sub-technique
* Exfiltration Over Alternative Protocol: [Exfiltration Over Asymmetric Encrypted Non-C2 Protocol](/beta/techniques/T1048/002) - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol
* Exfiltration Over Alternative Protocol: [Exfiltration Over Symmetric Encrypted Non-C2 Protocol](/beta/techniques/T1048/001) - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol
* Exfiltration Over Alternative Protocol: [Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol](/beta/techniques/T1048/003) - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol
* Exfiltration Over Other Network Medium: [Exfiltration Over Bluetooth](/beta/techniques/T1011/001) - Broken out from pre-defined behavior within Exfiltration over Other Network Medium
* Exfiltration Over Physical Medium: [Exfiltration over USB](/beta/techniques/T1052/001) - Broken out from pre-defined behavior within Exfiltration Over Physical Medium
* [Exfiltration Over Web Service](/beta/techniques/T1567) - Created to consolidate behaviors around exfiltration to legitimate web services
	* [Exfiltration to Cloud Storage](/beta/techniques/T1567/002) - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol
	* [Exfiltration to Code Repository](/beta/techniques/T1567/001) - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol
* File and Directory Permissions Modification: [Linux and Mac File and Directory Permissions Modification](/beta/techniques/T1222/002) - Broken out from pre-defined behavior within File and Directory Permissions Modification
* File and Directory Permissions Modification: [Windows File and Directory Permissions Modification](/beta/techniques/T1222/001) - Broken out from pre-defined behavior within File and Directory Permissions Modification
* [Hide Artifacts](/beta/techniques/T1564) - Created to consolidate behaviors around defense evasion through creating hidden objects that may be difficult to see
	* [Hidden Files and Directories](/beta/techniques/T1564/001) - Existing technique that became a sub-technique
	* [Hidden Users](/beta/techniques/T1564/002) - Existing technique that became a sub-technique
	* [Hidden Window](/beta/techniques/T1564/003) - Existing technique that became a sub-technique
	* [NTFS File Attributes](/beta/techniques/T1564/004) - Existing technique that became a sub-technique
* [Hijack Execution Flow](/beta/techniques/T1574) - Created to consolidate behaviors around running executable code by placing it where it would be executed by a legitimate process
	* [DLL Search Order Hijacking](/beta/techniques/T1574/001) - Existing technique that became a sub-technique
	* [DLL Side-Loading](/beta/techniques/T1574/002) - Existing technique that became a sub-technique
	* [Dylib Hijacking](/beta/techniques/T1574/004) - Existing technique that became a sub-technique
	* [Executable Installer File Permissions Weakness](/beta/techniques/T1574/005) - Existing technique that became a sub-technique
	* [LD_PRELOAD](/beta/techniques/T1574/006) - Existing technique that became a sub-technique
	* [Path Interception by PATH Environment Variable](/beta/techniques/T1574/007) - Broken out from pre-defined behavior within the prior Path Interception technique
	* [Path Interception by Search Order Hijacking](/beta/techniques/T1574/008) - Broken out from pre-defined behavior within the prior Path Interception technique
	* [Path Interception by Unquoted Path](/beta/techniques/T1574/009) - Broken out from pre-defined behavior within the prior Path Interception technique
	* [Services File Permissions Weakness](/beta/techniques/T1574/010) - Existing technique that became a sub-technique
	* [Services Registry Permissions Weakness](/beta/techniques/T1574/011) - Existing technique that became a sub-technique
* [Impair Defenses](/beta/techniques/T1562) - Created to consolidate behaviors that prevent a defense from working as intended
	* [Disable Windows Event Logging](/beta/techniques/T1562/002) - Existing technique that became a sub-technique
	* [Disable or Modify System Firewall](/beta/techniques/T1562/004) - Existing technique that became a sub-technique
	* [Disable or Modify Tools](/beta/techniques/T1562/001) - Existing technique that became a sub-technique
	* [HISTCONTROL](/beta/techniques/T1562/003) - Existing technique that became a sub-technique
	* [Indicator Blocking](/beta/techniques/T1562/006) - Existing technique that became a sub-technique
* Indicator Removal on Host: [Clear Command History](/beta/techniques/T1551/003) - Existing technique that became a sub-technique
* Indicator Removal on Host: [Clear Linux or Mac System Logs](/beta/techniques/T1551/002) - Broken out from pre-defined behavior within Indicator Removal on Host
* Indicator Removal on Host: [Clear Windows Event Logs](/beta/techniques/T1551/001) - Broken out from pre-defined behavior within Indicator Removal on Host
* Indicator Removal on Host: [File Deletion](/beta/techniques/T1551/004) - Existing technique that became a sub-technique
* Indicator Removal on Host: [Network Share Connection Removal](/beta/techniques/T1551/005) - Existing technique that became a sub-technique
* Indicator Removal on Host: [Timestomp](/beta/techniques/T1551/006) - Existing technique that became a sub-technique
* Input Capture: [Credential API Hooking](/beta/techniques/T1056/004) - Existing technique that became a sub-technique and was renamed from API Hooking. Scope change to only credential access for API hooking was based on available procedure examples
* Input Capture: [GUI Input Capture](/beta/techniques/T1056/002) - Broken out from pre-defined behavior within Input Capture
* Input Capture: [Keylogging](/beta/techniques/T1056/001) - Broken out from pre-defined behavior within Input Capture
* Input Capture: [Web Portal Capture](/beta/techniques/T1056/003) - Broken out from pre-defined behavior within Input Capture
* [Inter-Process Communication](/beta/techniques/T1559) - Created to consolidate behavior related to using IPC for local system execution
	* [Component Object Model](/beta/techniques/T1559/001) - Broken out from pre-defined behavior within the prior Component Object Model and Distributed COM technique
	* [Dynamic Data Exchange](/beta/techniques/T1559/002) - Existing technique that became a sub-technique
* [Lateral Tool Transfer](/beta/techniques/T1570) - Broken out from pre-defined behavior within the prior Remote File Copy technique to focus on file transfer within a network
* [Man-in-the-Middle](/beta/techniques/T1557) - Created to consolidate behavior related to setting up man-in-the-middle condition within a network
	* [LLMNR/NBT-NS Poisoning and SMB Relay](/beta/techniques/T1557/001) - Existing technique that became a sub-technique
* Masquerading: [Invalid Code Signature](/beta/techniques/T1036/001) - Created based on procedure examples within Code Signing as a distinct behavior using invalid digital signatures
* Masquerading: [Masquerade Task or Service](/beta/techniques/T1036/004) - Broken out from pre-defined behavior within Masquerading
* Masquerading: [Match Legitimate Name or Location](/beta/techniques/T1036/005) - Broken out from pre-defined behavior within Masquerading
* Masquerading: [Rename System Utilities](/beta/techniques/T1036/003) - Broken out from pre-defined behavior within Masquerading
* Masquerading: [Right-to-Left Override](/beta/techniques/T1036/002) - Broken out from pre-defined behavior within Masquerading
* Masquerading: [Space after Filename](/beta/techniques/T1036/006) - Existing technique that became a sub-technique
* [Modify Authentication Process](/beta/techniques/T1556) - Created to consolidate behavior related to changing the authentication process previously under Account Manipulation
	* [Domain Controller Authentication](/beta/techniques/T1556/001) - Broken out from pre-defined behavior within Account Manipulation
	* [Password Filter DLL](/beta/techniques/T1556/002) - Existing technique that became a sub-technique
* Network Denial of Service: [Direct Network Flood](/beta/techniques/T1498/001) - Broken out from pre-defined behavior within Network Denial of Service
* Network Denial of Service: [Reflection Amplification](/beta/techniques/T1498/002) - Broken out from pre-defined behavior within Network Denial of Service
* [Non-Standard Port](/beta/techniques/T1571) - Created to refine the idea behind Common and Uncommonly Used Port to focus the behavior on use of a non-standard port for C2 based on the protocol used
* OS Credential Dumping: [/etc/passwd and /etc/shadow](/beta/techniques/T1003/008) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [Cached Domain Credentials](/beta/techniques/T1003/005) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [DCSync](/beta/techniques/T1003/006) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [LSA Secrets](/beta/techniques/T1003/004) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [LSASS Memory](/beta/techniques/T1003/001) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [NTDS](/beta/techniques/T1003/003) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [Proc Filesystem](/beta/techniques/T1003/007) - Broken out from pre-defined behavior within OS Credential Dumping
* OS Credential Dumping: [Security Account Manager](/beta/techniques/T1003/002) - Broken out from pre-defined behavior within OS Credential Dumping
* Obfuscated Files or Information: [Binary Padding](/beta/techniques/T1027/001) - Existing technique that became a sub-technique
* Obfuscated Files or Information: [Compile After Delivery](/beta/techniques/T1027/004) - Existing technique that became a sub-technique
* Obfuscated Files or Information: [Indicator Removal from Tools](/beta/techniques/T1027/005) - Existing technique that became a sub-technique
* Obfuscated Files or Information: [Software Packing](/beta/techniques/T1027/002) - Existing technique that became a sub-technique
* Obfuscated Files or Information: [Steganography](/beta/techniques/T1027/003) - Broken out from pre-defined behavior within Obfuscated Files or Information
* Office Application Startup: [Add-ins](/beta/techniques/T1137/006) - Broken out from pre-defined behavior within Office Application Startup
* Office Application Startup: [Office Template Macros](/beta/techniques/T1137/001) - Broken out from pre-defined behavior within Office Application Startup
* Office Application Startup: [Office Test](/beta/techniques/T1137/002) - Broken out from pre-defined behavior within Office Application Startup
* Office Application Startup: [Outlook Forms](/beta/techniques/T1137/003) - Broken out from pre-defined behavior within Office Application Startup
* Office Application Startup: [Outlook Home Page](/beta/techniques/T1137/004) - Broken out from pre-defined behavior within Office Application Startup
* Office Application Startup: [Outlook Rules](/beta/techniques/T1137/005) - Broken out from pre-defined behavior within Office Application Startup
* Permission Groups Discovery: [Cloud Groups](/beta/techniques/T1069/003) - Broken out from pre-defined behavior within Permission Groups Discovery in a way that has parity with Account Discovery
* Permission Groups Discovery: [Domain Groups](/beta/techniques/T1069/002) - Broken out from pre-defined behavior within Permission Groups Discovery in a way that has parity with Account Discovery
* Permission Groups Discovery: [Local Groups](/beta/techniques/T1069/001) - Broken out from pre-defined behavior within Permission Groups Discovery in a way that has parity with Account Discovery
* [Phishing](/beta/techniques/T1566) - Created to consolidate behavior around phishing and spearphishing
	* [Spearphishing Attachment](/beta/techniques/T1566/001) - Existing technique that became a sub-technique
	* [Spearphishing Link](/beta/techniques/T1566/002) - Existing technique that became a sub-technique
	* [Spearphishing via Service](/beta/techniques/T1566/003) - Existing technique that became a sub-technique
* [Pre-OS Boot](/beta/techniques/T1542) - Created to consolidate behavior around persistence that loads before the OS boots
	* [Bootkit](/beta/techniques/T1542/003) - Existing technique that became a sub-technique
	* [Component Firmware](/beta/techniques/T1542/002) - Existing technique that became a sub-technique
	* [System Firmware](/beta/techniques/T1542/001) - Existing technique that became a sub-technique
* Process Injection: [Asynchronous Procedure Call](/beta/techniques/T1055/004) - Existing technique that became a sub-technique
* Process Injection: [Dynamic-link Library Injection](/beta/techniques/T1055/001) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Extra Window Memory Injection](/beta/techniques/T1055/011) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Portable Executable Injection](/beta/techniques/T1055/002) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Proc Memory](/beta/techniques/T1055/009) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Process Doppelgänging](/beta/techniques/T1055/013) - Existing technique that became a sub-technique
* Process Injection: [Process Hollowing](/beta/techniques/T1055/012) - Existing technique that became a sub-technique
* Process Injection: [Ptrace System Calls](/beta/techniques/T1055/008) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Thread Execution Hijacking](/beta/techniques/T1055/003) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [Thread Local Storage](/beta/techniques/T1055/005) - Broken out from pre-defined behavior within Process Injection
* Process Injection: [VDSO Hijacking](/beta/techniques/T1055/014) - Broken out from pre-defined behavior within Process Injection
* [Protocol Tunneling](/beta/techniques/T1572) - Created to define behavior broken out from the prior Standard Application and Standard Cryptographic Protocol techniques
* Proxy: [Domain Fronting](/beta/techniques/T1090/004) - Existing technique that became a sub-technique
* Proxy: [External Proxy](/beta/techniques/T1090/002) - Broken out from pre-defined behavior within Connection Proxy
* Proxy: [Internal Proxy](/beta/techniques/T1090/001) - Broken out from pre-defined behavior within Connection Proxy
* Proxy: [Multi-hop Proxy](/beta/techniques/T1090/003) - Existing technique that became a sub-technique
* [Remote Service Session Hijacking](/beta/techniques/T1563) - Created to consolidate behavior related to hijacking existing remote connection sessions
	* [RDP Hijacking](/beta/techniques/T1563/002) - Broken out from pre-defined behavior within Remote Desktop Protocol
	* [SSH Hijacking](/beta/techniques/T1563/001) - Existing technique that became a sub-technique
* Remote Services: [Distributed Component Object Model](/beta/techniques/T1021/003) - Broken out from pre-defined behavior within Component Object Model and Distributed COM technique
* Remote Services: [Remote Desktop Protocol](/beta/techniques/T1021/001) - Existing technique that became a sub-technique
* Remote Services: [SMB/Windows Admin Shares](/beta/techniques/T1021/002) - Existing technique that became a sub-technique and was renamed from Windows Admin Shares
* Remote Services: [SSH](/beta/techniques/T1021/004) - Broken out from pre-defined behavior within Remote Services technique
* Remote Services: [VNC](/beta/techniques/T1021/005) - Broken out from pre-defined behavior within Remote Services technique
* Remote Services: [Windows Remote Management](/beta/techniques/T1021/006) - Existing technique that became a sub-technique
* Scheduled Task/Job: [At (Linux)](/beta/techniques/T1053/001) - Broken out from pre-defined behavior within prior Local Job Scheduling technique
* Scheduled Task/Job: [At (Windows)](/beta/techniques/T1053/002) - Broken out from pre-defined behavior within prior Scheduled Task technique
* Scheduled Task/Job: [Cron](/beta/techniques/T1053/003) - Broken out from pre-defined behavior within prior Local Job Scheduling technique
* Scheduled Task/Job: [Launchd](/beta/techniques/T1053/004) - Existing technique that became a sub-technique
* Scheduled Task/Job: [Scheduled Task](/beta/techniques/T1053/005) - Existing technique that became a sub-technique
* Server Software Component: [SQL Stored Procedures](/beta/techniques/T1505/001) - Broken out from pre-defined behavior within Server Software Component technique
* Server Software Component: [Transport Agent](/beta/techniques/T1505/002) - Broken out from pre-defined behavior within Server Software Component technique
* Server Software Component: [Web Shell](/beta/techniques/T1505/003) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [CMSTP](/beta/techniques/T1218/003) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Compiled HTML File](/beta/techniques/T1218/001) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Control Panel](/beta/techniques/T1218/002) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [InstallUtil](/beta/techniques/T1218/004) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Mshta](/beta/techniques/T1218/005) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Msiexec](/beta/techniques/T1218/007) - Broken out from pre-defined behavior within Signed Binary Proxy Execution technique
* Signed Binary Proxy Execution: [Odbcconf](/beta/techniques/T1218/008) - Broken out from pre-defined behavior within Signed Binary Proxy Execution technique
* Signed Binary Proxy Execution: [Regsvcs/Regasm](/beta/techniques/T1218/009) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Regsvr32](/beta/techniques/T1218/010) - Existing technique that became a sub-technique
* Signed Binary Proxy Execution: [Rundll32](/beta/techniques/T1218/011) - Existing technique that became a sub-technique
* Signed Script Proxy Execution: [PubPrn](/beta/techniques/T1216/001) - Existing technique that became a sub-technique
* Software Discovery: [Security Software Discovery](/beta/techniques/T1518/001) - Existing technique that became a sub-technique
* [Steal or Forge Kerberos Tickets](/beta/techniques/T1558) - Created to consolidate behavior related to Kerberos tickets
	* [Golden Ticket](/beta/techniques/T1558/001) - Broken out from pre-defined behavior within Pass the Ticket technique
	* [Kerberoasting](/beta/techniques/T1558/003) - Existing technique that became a sub-technique
	* [Silver Ticket](/beta/techniques/T1558/002) - Broken out from pre-defined behavior within Pass the Ticket technique
* [Subvert Trust Controls](/beta/techniques/T1553) - Created to consolidate behavior related to getting around trust controls
	* [Code Signing](/beta/techniques/T1553/002) - Existing technique that became a sub-technique
	* [Gatekeeper Bypass](/beta/techniques/T1553/001) - Existing technique that became a sub-technique
	* [Install Root Certificate](/beta/techniques/T1553/004) - Existing technique that became a sub-technique
	* [SIP and Trust Provider Hijacking](/beta/techniques/T1553/003) - Existing technique that became a sub-technique
* Supply Chain Compromise: [Compromise Hardware Supply Chain](/beta/techniques/T1195/003) - Broken out from pre-defined behavior within Supply Chain Compromise
* Supply Chain Compromise: [Compromise Software Dependencies and Development Tools](/beta/techniques/T1195/001) - Broken out from pre-defined behavior within Supply Chain Compromise
* Supply Chain Compromise: [Compromise Software Supply Chain](/beta/techniques/T1195/002) - Broken out from pre-defined behavior within Supply Chain Compromise
* [System Services](/beta/techniques/T1569) - Created to consolidate behaviors related to execution of binaries through system services
	* [Launchctl](/beta/techniques/T1569/001) - Existing technique that became a sub-technique
	* [Service Execution](/beta/techniques/T1569/002) - Existing technique that became a sub-technique
* [Traffic Signaling](/beta/techniques/T1545) - Created to consolidate behaviors around specifically formed network traffic that is used as a trigger to take an action
	* [Port Knocking](/beta/techniques/T1545/001) - Existing technique that became a sub-technique
* Trusted Developer Utilities Proxy Execution: [MSBuild](/beta/techniques/T1127/001) - Broken out from pre-defined behavior within Trusted Developer Utilities Proxy Execution
* [Unsecured Credentials](/beta/techniques/T1552) - Created to consolidate places where unsecured credentials may be kept
	* [Bash History](/beta/techniques/T1552/003) - Existing technique that became a sub-technique
	* [Cloud Instance Metadata API](/beta/techniques/T1552/005) - Existing technique that became a sub-technique
	* [Credentials In Files](/beta/techniques/T1552/001) - Existing technique that became a sub-technique
	* [Credentials in Registry](/beta/techniques/T1552/002) - Existing technique that became a sub-technique
	* [Group Policy Preferences](/beta/techniques/T1552/006) - Existing technique that became a sub-technique
	* [Private Keys](/beta/techniques/T1552/004) - Existing technique that became a sub-technique
* [Use Alternate Authentication Material](/beta/techniques/T1550) - Created to consolidate behavior related to use of non-password based credential material
	* [Application Access Token](/beta/techniques/T1550/001) - Existing technique that became a sub-technique
	* [Pass the Hash](/beta/techniques/T1550/002) - Existing technique that became a sub-technique
	* [Pass the Ticket](/beta/techniques/T1550/003) - Existing technique that became a sub-technique
	* [Web Session Cookie](/beta/techniques/T1550/004) - Existing technique that became a sub-technique
* User Execution: [Malicious File](/beta/techniques/T1204/002) - Broken out from pre-defined behavior within User Execution
* User Execution: [Malicious Link](/beta/techniques/T1204/001) - Broken out from pre-defined behavior within User Execution
* Valid Accounts: [Cloud Accounts](/beta/techniques/T1078/004) - Broken out from pre-defined behavior Valid Accounts in a way that has parity with Create Account
* Valid Accounts: [Default Accounts](/beta/techniques/T1078/001) - Broken out from pre-defined behavior within Valid Accounts in a way that has parity with Create Account
* Valid Accounts: [Domain Accounts](/beta/techniques/T1078/002) - Broken out from pre-defined behavior within Valid Accounts in a way that has parity with Create Account
* Valid Accounts: [Local Accounts](/beta/techniques/T1078/003) - Broken out from pre-defined behavior within Valid Accounts in a way that has parity with Create Account
* Virtualization/Sandbox Evasion: [System Checks](/beta/techniques/T1497/001) - Broken out from pre-defined behavior within Virtualization/Sandbox Evasion
* Virtualization/Sandbox Evasion: [Time Based Evasion](/beta/techniques/T1497/003) - Broken out from pre-defined behavior within Virtualization/Sandbox Evasion
* Virtualization/Sandbox Evasion: [User Activity Based Checks](/beta/techniques/T1497/002) - Broken out from pre-defined behavior within Virtualization/Sandbox Evasion
* Web Service: [Bidirectional Communication](/beta/techniques/T1102/002) - Broken out from pre-defined behavior within Web Service
* Web Service: [Dead Drop Resolver](/beta/techniques/T1102/001) - Broken out from pre-defined behavior within Web Service
* Web Service: [One-Way Communication](/beta/techniques/T1102/003) - Broken out from pre-defined behavior within Web Service


Technique changes:

Technique changes are largely due to new sub-techniques being added, name changes, or both.

* [Access Token Manipulation](/beta/techniques/T1134) - New sub-techniques added
* [Account Discovery](/beta/techniques/T1087) - New sub-techniques added
* [Account Manipulation](/beta/techniques/T1098) - New sub-techniques added
* [Application Layer Protocol](/beta/techniques/T1071) - Name change from Standard Application Layer Protocol and new sub-techniques added
* [Application Window Discovery](/beta/techniques/T1010) - Fixed technique reference in description
* [Automated Exfiltration](/beta/techniques/T1020) - Fixed technique reference in description
* [BITS Jobs](/beta/techniques/T1197) - Fixed technique reference in description and minor description update
* [Boot or Logon Initialization Scripts](/beta/techniques/T1037) - Name change from Logon Scripts and new sub-techniques added
* [Browser Extensions](/beta/techniques/T1176) - Data sources changed and minor description update
* [Brute Force](/beta/techniques/T1110) - New sub-techniques added
* [Clipboard Data](/beta/techniques/T1115) - Minor description update
* [Command and Scripting Interpreter](/beta/techniques/T1059) - Name change from Command-Line Interface and new sub-techniques added
* [Create Account](/beta/techniques/T1136) - New sub-techniques added
* [Data Encoding](/beta/techniques/T1132) - New sub-techniques added
* [Data Obfuscation](/beta/techniques/T1001) - New sub-techniques added
* [Data Staged](/beta/techniques/T1074) - New sub-techniques added
* [Data from Information Repositories](/beta/techniques/T1213) - New sub-techniques added
* [Data from Local System](/beta/techniques/T1005) - Fixed technique reference in description and minor description update
* [Data from Network Shared Drive](/beta/techniques/T1039) - Fixed technique reference in description and minor description update
* [Data from Removable Media](/beta/techniques/T1025) - Fixed technique reference in description and minor description update
* [Direct Volume Access](/beta/techniques/T1006) - Name change from File System Logical Offsets
* [Domain Trust Discovery](/beta/techniques/T1482) - Fixed technique reference in description and minor description update
* [Drive-by Compromise](/beta/techniques/T1189) - Fixed technique reference in description and minor description update
* [Email Collection](/beta/techniques/T1114) - New sub-techniques added
* [Exfiltration Over Alternative Protocol](/beta/techniques/T1048) - New sub-techniques added
* [Exfiltration Over C2 Channel](/beta/techniques/T1041) - Name change from Exfiltration over Command and Control Channel and added data sources
* [Exfiltration Over Other Network Medium](/beta/techniques/T1011) - New sub-techniques added
* [Exfiltration Over Physical Medium](/beta/techniques/T1052) - New sub-techniques added
* [Exploit Public-Facing Application](/beta/techniques/T1190) - Minor description update
* [Exploitation for Client Execution](/beta/techniques/T1203) - Minor description update
* [Exploitation for Credential Access](/beta/techniques/T1212) - Minor description update
* [Exploitation for Defense Evasion](/beta/techniques/T1211) - Minor description update
* [Exploitation for Privilege Escalation](/beta/techniques/T1068) - Minor description update
* [Exploitation of Remote Services](/beta/techniques/T1210) - Minor description update
* [External Remote Services](/beta/techniques/T1133) - Minor description update
* [File and Directory Discovery](/beta/techniques/T1083) - Fixed technique reference in description and minor description update
* [File and Directory Permissions Modification](/beta/techniques/T1222) - New sub-techniques added
* [Forced Authentication](/beta/techniques/T1187) - Minor description update
* [Group Policy Modification](/beta/techniques/T1484) - Minor description update
* [Indicator Removal on Host](/beta/techniques/T1551) - Minor description update
* [Indirect Command Execution](/beta/techniques/T1202) - Minor description update
* [Ingress Tool Transfer](/beta/techniques/T1105) - Name change from Remote File Copy
* [Input Capture](/beta/techniques/T1056) - New sub-techniques added
* [Masquerading](/beta/techniques/T1036) - New sub-techniques added
* [Native API](/beta/techniques/T1106) - Name change from Execution through API
* [Network Service Scanning](/beta/techniques/T1046) - Minor description update
* [Network Share Discovery](/beta/techniques/T1135) - Fixed technique reference in description, added Linux, and minor description update
* [Network Sniffing](/beta/techniques/T1040) - Minor description update
* [Non-Application Layer Protocol](/beta/techniques/T1095) - Name change from Standard Non-Application Layer Protocol
* [OS Credential Dumping](/beta/techniques/T1003) - Name change from Credential Dumping and new sub-techniques added
* [Obfuscated Files or Information](/beta/techniques/T1027) - Minor description update
* [Password Policy Discovery](/beta/techniques/T1201) - Fixed technique reference in description and minor description update
* [Peripheral Device Discovery](/beta/techniques/T1120) - Fixed technique reference in description and minor description update
* [Permission Groups Discovery](/beta/techniques/T1069) - New sub-techniques added
* [Process Discovery](/beta/techniques/T1057) - Fixed technique reference in description and minor description update
* [Process Injection](/beta/techniques/T1055) - New sub-techniques added
* [Proxy](/beta/techniques/T1090) - Name change from Connection Proxy and new sub-techniques added
* [Query Registry](/beta/techniques/T1012) - Fixed technique reference in description and minor description update
* [Remote Access Software](/beta/techniques/T1219) - Name change from Remote Access Tools and fixed technique reference in description
* [Remote Services](/beta/techniques/T1021) - New sub-techniques added
* [Remote System Discovery](/beta/techniques/T1018) - Fixed technique reference in description and minor description update
* [Revert Cloud Instance](/beta/techniques/T1536) - Minor description update, removed some data sources
* [Rogue Domain Controller](/beta/techniques/T1207) - Name change from DCShadow
* [Rootkit](/beta/techniques/T1014) - Minor description update
* [Scheduled Task/Job](/beta/techniques/T1053) - New sub-techniques added
* [Scheduled Transfer](/beta/techniques/T1029) - Minor description update
* [Screen Capture](/beta/techniques/T1113) - Minor description update
* [Server Software Component](/beta/techniques/T1505) - New sub-techniques added
* [Shared Modules](/beta/techniques/T1129) - Name change from Execution through Module Load
* [Signed Binary Proxy Execution](/beta/techniques/T1218) - New sub-techniques added
* [Signed Script Proxy Execution](/beta/techniques/T1216) - New sub-techniques added
* [Software Deployment Tools](/beta/techniques/T1072) - Minor description update and data source added
* [Software Discovery](/beta/techniques/T1518) - New sub-techniques added
* [Supply Chain Compromise](/beta/techniques/T1195) - New sub-techniques added
* [System Information Discovery](/beta/techniques/T1082) - Fixed technique reference in description and minor description update
* [System Network Configuration Discovery](/beta/techniques/T1016) - Fixed technique reference in description and minor description update
* [System Network Connections Discovery](/beta/techniques/T1049) - Fixed technique reference in description and minor description update
* [System Owner/User Discovery](/beta/techniques/T1033) - Fixed technique reference in description and minor description update
* [System Time Discovery](/beta/techniques/T1124) - Minor description update
* [Taint Shared Content](/beta/techniques/T1080) - Minor description update
* [Template Injection](/beta/techniques/T1221) - Minor description update
* [Trusted Developer Utilities Proxy Execution](/beta/techniques/T1127) - Minor description update, sub-technique added
* [Two-Factor Authentication Interception](/beta/techniques/T1111) - Minor description update
* [User Execution](/beta/techniques/T1204) - New sub-techniques added
* [Valid Accounts](/beta/techniques/T1078) - New sub-techniques added
* [Virtualization/Sandbox Evasion](/beta/techniques/T1497) - New sub-techniques added
* [Web Service](/beta/techniques/T1102) - New sub-techniques added
* [Windows Management Instrumentation](/beta/techniques/T1047) - Minor description update
* [XSL Script Processing](/beta/techniques/T1220) - Minor description update


Minor Technique changes:

* [Browser Bookmark Discovery](/beta/techniques/T1217)
* [Data Destruction](/beta/techniques/T1485)
* [Data Encrypted for Impact](/beta/techniques/T1486)
* [Endpoint Denial of Service](/beta/techniques/T1499)
* [Implant Container Image](/beta/techniques/T1525)
* [Network Denial of Service](/beta/techniques/T1498)
* [Office Application Startup](/beta/techniques/T1137)
* [Steal Application Access Token](/beta/techniques/T1528)
* [System Service Discovery](/beta/techniques/T1007)
* [System Shutdown/Reboot](/beta/techniques/T1529)
* [Transfer Data to Cloud Account](/beta/techniques/T1537)


Technique revocations:

* .bash_profile and .bashrc (revoked by Event Triggered Execution: [.bash_profile and .bashrc](/beta/techniques/T1546/004))
* Accessibility Features (revoked by Event Triggered Execution: [Accessibility Features](/beta/techniques/T1546/008))
* AppCert DLLs (revoked by Event Triggered Execution: [AppCert DLLs](/beta/techniques/T1546/009))
* AppInit DLLs (revoked by Event Triggered Execution: [AppInit DLLs](/beta/techniques/T1546/010))
* AppleScript (revoked by Command and Scripting Interpreter: [AppleScript](/beta/techniques/T1059/002))
* Application Access Token (revoked by Use Alternate Authentication Material: [Application Access Token](/beta/techniques/T1550/001))
* Application Deployment Software (revoked by [Software Deployment Tools](/beta/techniques/T1072))
* Application Shimming (revoked by Event Triggered Execution: [Application Shimming](/beta/techniques/T1546/011))
* Authentication Package (revoked by Boot or Logon Autostart Execution: [Authentication Package](/beta/techniques/T1547/002))
* Bash History (revoked by Unsecured Credentials: [Bash History](/beta/techniques/T1552/003))
* Binary Padding (revoked by Obfuscated Files or Information: [Binary Padding](/beta/techniques/T1027/001))
* Bootkit (revoked by Pre-OS Boot: [Bootkit](/beta/techniques/T1542/003))
* Bypass User Account Control (revoked by Abuse Elevation Control Mechanism: [Bypass User Access Control](/beta/techniques/T1548/002))
* CMSTP (revoked by Signed Binary Proxy Execution: [CMSTP](/beta/techniques/T1218/003))
* Change Default File Association (revoked by Event Triggered Execution: [Change Default File Association](/beta/techniques/T1546/001))
* Clear Command History (revoked by Indicator Removal on Host: [Clear Command History](/beta/techniques/T1551/003))
* Cloud Instance Metadata API (revoked by Unsecured Credentials: [Cloud Instance Metadata API](/beta/techniques/T1552/005))
* Code Signing (revoked by Subvert Trust Controls: [Code Signing](/beta/techniques/T1553/002))
* Commonly Used Port (revoked by [Non-Standard Port](/beta/techniques/T1571))
* Compile After Delivery (revoked by Obfuscated Files or Information: [Compile After Delivery](/beta/techniques/T1027/004))
* Compiled HTML File (revoked by Signed Binary Proxy Execution: [Compiled HTML File](/beta/techniques/T1218/001))
* Component Firmware (revoked by Pre-OS Boot: [Component Firmware](/beta/techniques/T1542/002))
* Component Object Model Hijacking (revoked by Event Triggered Execution: [Component Object Model Hijacking](/beta/techniques/T1546/015))
* Control Panel Items (revoked by Signed Binary Proxy Execution: [Control Panel](/beta/techniques/T1218/002))
* Credentials from Web Browsers (revoked by Credentials from Password Stores: [Credentials from Web Browsers](/beta/techniques/T1555/003))
* Credentials in Files (revoked by Unsecured Credentials: [Credentials In Files](/beta/techniques/T1552/001))
* Credentials in Registry (revoked by Unsecured Credentials: [Credentials in Registry](/beta/techniques/T1552/002))
* Custom Command and Control Protocol (revoked by [Non-Application Layer Protocol](/beta/techniques/T1095))
* Custom Cryptographic Protocol (revoked by [Encrypted Channel](/beta/techniques/T1573))
* DLL Search Order Hijacking (revoked by Hijack Execution Flow: [DLL Search Order Hijacking](/beta/techniques/T1574/001))
* DLL Side-Loading (revoked by Hijack Execution Flow: [DLL Side-Loading](/beta/techniques/T1574/002))
* Data Compressed (revoked by [Archive Collected Data](/beta/techniques/T1560))
* Data Encrypted (revoked by [Archive Collected Data](/beta/techniques/T1560))
* Disabling Security Tools (revoked by Impair Defenses: [Disable or Modify Tools](/beta/techniques/T1562/001))
* Disk Content Wipe (revoked by Disk Wipe: [Disk Content Wipe](/beta/techniques/T1561/001))
* Disk Structure Wipe (revoked by Disk Wipe: [Disk Structure Wipe](/beta/techniques/T1561/002))
* Domain Fronting (revoked by Proxy: [Domain Fronting](/beta/techniques/T1090/004))
* Domain Generation Algorithms (revoked by Dynamic Resolution: [Domain Generation Algorithms](/beta/techniques/T1568/002))
* Dylib Hijacking (revoked by Hijack Execution Flow: [Dylib Hijacking](/beta/techniques/T1574/004))
* Dynamic Data Exchange (revoked by Inter-Process Communication: [Dynamic Data Exchange](/beta/techniques/T1559/002))
* Elevated Execution with Prompt (revoked by Abuse Elevation Control Mechanism: [Elevated Execution with Prompt](/beta/techniques/T1548/004))
* Emond (revoked by Event Triggered Execution: [Emond](/beta/techniques/T1546/014))
* Extra Window Memory Injection (revoked by Process Injection: [Extra Window Memory Injection](/beta/techniques/T1055/011))
* File Deletion (revoked by Indicator Removal on Host: [File Deletion](/beta/techniques/T1551/004))
* File System Permissions Weakness (revoked by Hijack Execution Flow: [Services File Permissions Weakness](/beta/techniques/T1574/010))
* Gatekeeper Bypass (revoked by Subvert Trust Controls: [Gatekeeper Bypass](/beta/techniques/T1553/001))
* HISTCONTROL (revoked by Impair Defenses: [HISTCONTROL](/beta/techniques/T1562/003))
* Hidden Files and Directories (revoked by Hide Artifacts: [Hidden Files and Directories](/beta/techniques/T1564/001))
* Hidden Users (revoked by Hide Artifacts: [Hidden Users](/beta/techniques/T1564/002))
* Hidden Window (revoked by Hide Artifacts: [Hidden Window](/beta/techniques/T1564/003))
* Hooking (revoked by Input Capture: [Credential API Hooking](/beta/techniques/T1056/004))
* Image File Execution Options Injection (revoked by Event Triggered Execution: [Image File Execution Options Injection](/beta/techniques/T1546/012))
* Indicator Blocking (revoked by Impair Defenses: [Indicator Blocking](/beta/techniques/T1562/006))
* Indicator Removal from Tools (revoked by Obfuscated Files or Information: [Indicator Removal from Tools](/beta/techniques/T1027/005))
* Input Prompt (revoked by Input Capture: [GUI Input Capture](/beta/techniques/T1056/002))
* Install Root Certificate (revoked by Subvert Trust Controls: [Install Root Certificate](/beta/techniques/T1553/004))
* InstallUtil (revoked by Signed Binary Proxy Execution: [InstallUtil](/beta/techniques/T1218/004))
* Kerberoasting (revoked by Steal or Forge Kerberos Tickets: [Kerberoasting](/beta/techniques/T1558/003))
* Kernel Modules and Extensions (revoked by Boot or Logon Autostart Execution: [Kernel Modules and Extensions](/beta/techniques/T1547/006))
* Keychain (revoked by Credentials from Password Stores: [Keychain](/beta/techniques/T1555/001))
* LC_LOAD_DYLIB Addition (revoked by Event Triggered Execution: [LC_LOAD_DYLIB Addition](/beta/techniques/T1546/006))
* LLMNR/NBT-NS Poisoning and Relay (revoked by Man-in-the-Middle: [LLMNR/NBT-NS Poisoning and SMB Relay](/beta/techniques/T1557/001))
* LSASS Driver (revoked by Boot or Logon Autostart Execution: [LSASS Driver](/beta/techniques/T1547/008))
* Launch Agent (revoked by Create or Modify System Process: [Launch Agent](/beta/techniques/T1543/001))
* Launch Daemon (revoked by Create or Modify System Process: [Launch Daemon](/beta/techniques/T1543/004))
* Launchctl (revoked by System Services: [Launchctl](/beta/techniques/T1569/001))
* Local Job Scheduling (revoked by [Scheduled Task/Job](/beta/techniques/T1053))
* Login Item (revoked by Boot or Logon Autostart Execution: [Plist Modification](/beta/techniques/T1547/011))
* Modify Existing Service (revoked by Create or Modify System Process: [Windows Service](/beta/techniques/T1543/003))
* Mshta (revoked by Signed Binary Proxy Execution: [Mshta](/beta/techniques/T1218/005))
* Multi-hop Proxy (revoked by Proxy: [Multi-hop Proxy](/beta/techniques/T1090/003))
* Multilayer Encryption (revoked by [Encrypted Channel](/beta/techniques/T1573))
* NTFS File Attributes (revoked by Hide Artifacts: [NTFS File Attributes](/beta/techniques/T1564/004))
* Netsh Helper DLL (revoked by Event Triggered Execution: [Netsh Helper DLL](/beta/techniques/T1546/007))
* Network Share Connection Removal (revoked by Indicator Removal on Host: [Network Share Connection Removal](/beta/techniques/T1551/005))
* New Service (revoked by Create or Modify System Process: [Windows Service](/beta/techniques/T1543/003))
* Parent PID Spoofing (revoked by Access Token Manipulation: [Parent PID Spoofing](/beta/techniques/T1134/004))
* Pass the Hash (revoked by Use Alternate Authentication Material: [Pass the Hash](/beta/techniques/T1550/002))
* Pass the Ticket (revoked by Use Alternate Authentication Material: [Pass the Ticket](/beta/techniques/T1550/003))
* Password Filter DLL (revoked by Modify Authentication Process: [Password Filter DLL](/beta/techniques/T1556/002))
* Plist Modification (revoked by Boot or Logon Autostart Execution: [Plist Modification](/beta/techniques/T1547/011))
* Port Knocking (revoked by Traffic Signaling: [Port Knocking](/beta/techniques/T1545/001))
* Port Monitors (revoked by Boot or Logon Autostart Execution: [Port Monitors](/beta/techniques/T1547/010))
* PowerShell (revoked by Command and Scripting Interpreter: [PowerShell](/beta/techniques/T1059/001))
* PowerShell Profile (revoked by Event Triggered Execution: [PowerShell Profile](/beta/techniques/T1546/013))
* Private Keys (revoked by Unsecured Credentials: [Private Keys](/beta/techniques/T1552/004))
* Process Doppelgänging (revoked by Process Injection: [Process Doppelgänging](/beta/techniques/T1055/013))
* Process Hollowing (revoked by Process Injection: [Process Hollowing](/beta/techniques/T1055/012))
* Rc.common (revoked by Boot or Logon Initialization Scripts: [Rc.common](/beta/techniques/T1037/004))
* Re-opened Applications (revoked by Boot or Logon Autostart Execution: [Re-opened Applications](/beta/techniques/T1547/007))
* Registry Run Keys / Startup Folder (revoked by Boot or Logon Autostart Execution: [Registry Run Keys / Startup Folder](/beta/techniques/T1547/001))
* Regsvcs/Regasm (revoked by Signed Binary Proxy Execution: [Regsvcs/Regasm](/beta/techniques/T1218/009))
* Regsvr32 (revoked by Signed Binary Proxy Execution: [Regsvr32](/beta/techniques/T1218/010))
* Remote Desktop Protocol (revoked by Remote Services: [Remote Desktop Protocol](/beta/techniques/T1021/001))
* Rundll32 (revoked by Signed Binary Proxy Execution: [Rundll32](/beta/techniques/T1218/011))
* Runtime Data Manipulation (revoked by Data Manipulation: [Runtime Data Manipulation](/beta/techniques/T1565/003))
* SID-History Injection (revoked by Access Token Manipulation: [SID-History Injection](/beta/techniques/T1134/005))
* SIP and Trust Provider Hijacking (revoked by Subvert Trust Controls: [SIP and Trust Provider Hijacking](/beta/techniques/T1553/003))
* SSH Hijacking (revoked by Remote Service Session Hijacking: [SSH Hijacking](/beta/techniques/T1563/001))
* Screensaver (revoked by Event Triggered Execution: [Screensaver](/beta/techniques/T1546/002))
* Security Software Discovery (revoked by Software Discovery: [Security Software Discovery](/beta/techniques/T1518/001))
* Security Support Provider (revoked by Boot or Logon Autostart Execution: [Security Support Provider](/beta/techniques/T1547/005))
* Securityd Memory (revoked by Credentials from Password Stores: [Securityd Memory](/beta/techniques/T1555/002))
* Service Execution (revoked by System Services: [Service Execution](/beta/techniques/T1569/002))
* Service Registry Permissions Weakness (revoked by Hijack Execution Flow: [Services Registry Permissions Weakness](/beta/techniques/T1574/011))
* Setuid and Setgid (revoked by Abuse Elevation Control Mechanism: [Setuid and Setgid](/beta/techniques/T1548/001))
* Shortcut Modification (revoked by Boot or Logon Autostart Execution: [Shortcut Modification](/beta/techniques/T1547/009))
* Software Packing (revoked by Obfuscated Files or Information: [Software Packing](/beta/techniques/T1027/002))
* Space after Filename (revoked by Masquerading: [Space after Filename](/beta/techniques/T1036/006))
* Spearphishing Attachment (revoked by Phishing: [Spearphishing Attachment](/beta/techniques/T1566/001))
* Spearphishing Link (revoked by Phishing: [Spearphishing Link](/beta/techniques/T1566/002))
* Spearphishing via Service (revoked by Phishing: [Spearphishing via Service](/beta/techniques/T1566/003))
* Standard Cryptographic Protocol (revoked by [Encrypted Channel](/beta/techniques/T1573))
* Startup Items (revoked by Boot or Logon Initialization Scripts: [Startup Items](/beta/techniques/T1037/005))
* Stored Data Manipulation (revoked by Data Manipulation: [Stored Data Manipulation](/beta/techniques/T1565/001))
* Sudo (revoked by Abuse Elevation Control Mechanism: [Sudo and Sudo Caching](/beta/techniques/T1548/003))
* Sudo Caching (revoked by Abuse Elevation Control Mechanism: [Sudo and Sudo Caching](/beta/techniques/T1548/003))
* System Firmware (revoked by Pre-OS Boot: [System Firmware](/beta/techniques/T1542/001))
* Systemd Service (revoked by Create or Modify System Process: [Systemd Service](/beta/techniques/T1543/002))
* Time Providers (revoked by Boot or Logon Autostart Execution: [Time Providers](/beta/techniques/T1547/003))
* Timestomp (revoked by Indicator Removal on Host: [Timestomp](/beta/techniques/T1551/006))
* Transmitted Data Manipulation (revoked by Data Manipulation: [Transmitted Data Manipulation](/beta/techniques/T1565/002))
* Trap (revoked by Event Triggered Execution: [Trap](/beta/techniques/T1546/005))
* Uncommonly Used Port (revoked by [Non-Standard Port](/beta/techniques/T1571))
* Web Session Cookie (revoked by Use Alternate Authentication Material: [Web Session Cookie](/beta/techniques/T1550/004))
* Web Shell (revoked by Server Software Component: [Web Shell](/beta/techniques/T1505/003))
* Windows Admin Shares (revoked by Remote Services: [SMB/Windows Admin Shares](/beta/techniques/T1021/002))
* Windows Management Instrumentation Event Subscription (revoked by Event Triggered Execution: [Windows Management Instrumentation Event Subscription](/beta/techniques/T1546/003))
* Windows Remote Management (revoked by Remote Services: [Windows Remote Management](/beta/techniques/T1021/006))
* Winlogon Helper DLL (revoked by Boot or Logon Autostart Execution: [Winlogon Helper DLL](/beta/techniques/T1547/004))


Technique deprecations:

* [Component Object Model and Distributed COM](/beta/techniques/T1175) - Deprecated and split into separate Component Object Model and Distributed Component Object Model sub-techniques. Existing Group/Software procedure examples were remapped appropriately
* [Graphical User Interface](/beta/techniques/T1061) - Deprecated from ATT&CK because the behavior is redundant and implied by use of remote desktop tools like Remote Desktop Protocol. Existing Group/Software procedure examples were remapped appropriately
* [Hypervisor](/beta/techniques/T1062) - Deprecated from ATT&CK due to lack of in the wild use
* [LC_MAIN Hijacking](/beta/techniques/T1149) - Deprecated from ATT&CK due to lack of in the wild use
* [Multiband Communication](/beta/techniques/T1026) - Deprecated from ATT&CK due to lack of in the wild use. Existing Group/Software procedure examples did not fit the core idea behind the technique
* [Path Interception](/beta/techniques/T1034) - Deprecated and split into separate Unquoted Path, PATH Environment Variable, and Search Order Hijacking sub-techniques. Existing Group/Software procedure examples were remapped appropriately
* [Redundant Access](/beta/techniques/T1108) - Deprecated from ATT&CK because the behavior is too high level and is sufficiently covered by Valid Accounts and External Remote Services. Existing Group/Software procedure examples were remapped appropriately
* [Scripting](/beta/techniques/T1064) - Deprecated and split into separate Bash, VBScript, and Python sub-techniques of Command and Scripting Interpreter. Existing Group/Software procedure examples were remapped appropriately
* [Shared Webroot](/beta/techniques/T1051) - Deprecated from ATT&CK due to lack of in the wild use
* [Source](/beta/techniques/T1153) - Deprecated from ATT&CK due to lack of in the wild use


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

* [DNSCalc](/beta/techniques/T1324)
* [Fast Flux DNS](/beta/techniques/T1325)


**Mobile**

New Techniques:

* [Code Injection](/beta/techniques/T1540)
* [Foreground Persistence](/beta/techniques/T1541)
* [Remote File Copy](/beta/techniques/T1544)


Technique changes:

* [Broadcast Receivers](/beta/techniques/T1402)
* [Carrier Billing Fraud](/beta/techniques/T1448)
* [Suppress Application Icon](/beta/techniques/T1508)


Minor Technique changes:

* [Access Notifications](/beta/techniques/T1517)
* [Clipboard Modification](/beta/techniques/T1510)
* [Deliver Malicious App via Other Means](/beta/techniques/T1476)
* [Input Injection](/beta/techniques/T1516)
* [Input Prompt](/beta/techniques/T1411)
* [Screen Capture](/beta/techniques/T1513)
* [System Information Discovery](/beta/techniques/T1426)


Technique revocations:
No changes

Technique deprecations:
No changes

### Software

**Enterprise**

New Software:
No changes

Software changes:

* [3PARA RAT](/beta/software/S0066)
* [4H RAT](/beta/software/S0065)
* [ADVSTORESHELL](/beta/software/S0045)
* [ASPXSpy](/beta/software/S0073)
* [Agent Tesla](/beta/software/S0331)
* [Agent.btz](/beta/software/S0092)
* [Astaroth](/beta/software/S0373)
* [AuditCred](/beta/software/S0347)
* [AutoIt backdoor](/beta/software/S0129)
* [Azorult](/beta/software/S0344)
* [BACKSPACE](/beta/software/S0031)
* [BADCALL](/beta/software/S0245)
* [BADNEWS](/beta/software/S0128)
* [BBSRAT](/beta/software/S0127)
* [BISCUIT](/beta/software/S0017)
* [BITSAdmin](/beta/software/S0190)
* [BLACKCOFFEE](/beta/software/S0069)
* [BONDUPDATER](/beta/software/S0360)
* [BOOTRASH](/beta/software/S0114)
* [BS2005](/beta/software/S0014)
* [BUBBLEWRAP](/beta/software/S0043)
* [BabyShark](/beta/software/S0414)
* [Backdoor.Oldrea](/beta/software/S0093)
* [BadPatch](/beta/software/S0337)
* [Bandook](/beta/software/S0234)
* [Bankshot](/beta/software/S0239)
* [Bisonal](/beta/software/S0268)
* [BlackEnergy](/beta/software/S0089)
* [Brave Prince](/beta/software/S0252)
* [CALENDAR](/beta/software/S0025)
* [CCBkdr](/beta/software/S0222)
* [CHOPSTICK](/beta/software/S0023)
* [CORALDECK](/beta/software/S0212)
* [CORESHELL](/beta/software/S0137)
* [Cachedump](/beta/software/S0119)
* [Calisto](/beta/software/S0274)
* [CallMe](/beta/software/S0077)
* [Cannon](/beta/software/S0351)
* [Carbanak](/beta/software/S0030)
* [Carbon](/beta/software/S0335)
* [Cardinal RAT](/beta/software/S0348)
* [Catchamas](/beta/software/S0261)
* [ChChes](/beta/software/S0144)
* [Chaos](/beta/software/S0220)
* [Cherry Picker](/beta/software/S0107)
* [China Chopper](/beta/software/S0020)
* [CloudDuke](/beta/software/S0054)
* [Cobalt Strike](/beta/software/S0154)
* [Cobian RAT](/beta/software/S0338)
* [CoinTicker](/beta/software/S0369)
* [ComRAT](/beta/software/S0126)
* [Comnie](/beta/software/S0244)
* [CosmicDuke](/beta/software/S0050)
* [CozyCar](/beta/software/S0046)
* [Crimson](/beta/software/S0115)
* [CrossRAT](/beta/software/S0235)
* [DOGCALL](/beta/software/S0213)
* [DarkComet](/beta/software/S0334)
* [Daserf](/beta/software/S0187)
* [DealersChoice](/beta/software/S0243)
* [Denis](/beta/software/S0354)
* [Derusbi](/beta/software/S0021)
* [Dipsind](/beta/software/S0200)
* [Dok](/beta/software/S0281)
* [DownPaper](/beta/software/S0186)
* [Downdelph](/beta/software/S0134)
* [Dridex](/beta/software/S0384)
* [Duqu](/beta/software/S0038)
* [DustySky](/beta/software/S0062)
* [Dyre](/beta/software/S0024)
* [ELMER](/beta/software/S0064)
* [Ebury](/beta/software/S0377)
* [Elise](/beta/software/S0081)
* [Emissary](/beta/software/S0082)
* [Emotet](/beta/software/S0367)
* [Empire](/beta/software/S0363)
* [Epic](/beta/software/S0091)
* [EvilBunny](/beta/software/S0396)
* [EvilGrab](/beta/software/S0152)
* [Exaramel for Linux](/beta/software/S0401)
* [Exaramel for Windows](/beta/software/S0343)
* [Expand](/beta/software/S0361)
* [FALLCHILL](/beta/software/S0181)
* [FELIXROOT](/beta/software/S0267)
* [FLASHFLOOD](/beta/software/S0036)
* [FLIPSIDE](/beta/software/S0173)
* [FTP](/beta/software/S0095)
* [FakeM](/beta/software/S0076)
* [Felismus](/beta/software/S0171)
* [Fgdump](/beta/software/S0120)
* [FinFisher](/beta/software/S0182)
* [Final1stspy](/beta/software/S0355)
* [Flame](/beta/software/S0143)
* [FlawedAmmyy](/beta/software/S0381)
* [FruitFly](/beta/software/S0277)
* [Fysbis](/beta/software/S0410)
* [GLOOXMAIL](/beta/software/S0026)
* [GRIFFON](/beta/software/S0417)
* [Gazer](/beta/software/S0168)
* [GeminiDuke](/beta/software/S0049)
* [Gold Dragon](/beta/software/S0249)
* [GravityRAT](/beta/software/S0237)
* [GreyEnergy](/beta/software/S0342)
* [H1N1](/beta/software/S0132)
* [HAMMERTOSS](/beta/software/S0037)
* [HARDRAIN](/beta/software/S0246)
* [HAWKBALL](/beta/software/S0391)
* [HIDEDRV](/beta/software/S0135)
* [HOMEFRY](/beta/software/S0232)
* [HOPLIGHT](/beta/software/S0376)
* [HTTPBrowser](/beta/software/S0070)
* [Hacking Team UEFI Rootkit](/beta/software/S0047)
* [Helminth](/beta/software/S0170)
* [Hi-Zor](/beta/software/S0087)
* [HiddenWasp](/beta/software/S0394)
* [Hikit](/beta/software/S0009)
* [Hydraq](/beta/software/S0203)
* [HyperBro](/beta/software/S0398)
* [ISMInjector](/beta/software/S0189)
* [Impacket](/beta/software/S0357)
* [InnaputRAT](/beta/software/S0259)
* [InvisiMole](/beta/software/S0260)
* [Ixeshe](/beta/software/S0015)
* [JCry](/beta/software/S0389)
* [JHUHUGIT](/beta/software/S0044)
* [JPIN](/beta/software/S0201)
* [Janicab](/beta/software/S0163)
* [KARAE](/beta/software/S0215)
* [KEYMARBLE](/beta/software/S0271)
* [KOMPROGO](/beta/software/S0156)
* [KONNI](/beta/software/S0356)
* [Kasidet](/beta/software/S0088)
* [Kazuar](/beta/software/S0265)
* [KeyBoy](/beta/software/S0387)
* [Keydnap](/beta/software/S0276)
* [Koadic](/beta/software/S0250)
* [Komplex](/beta/software/S0162)
* [Kwampirs](/beta/software/S0236)
* [LOWBALL](/beta/software/S0042)
* [LaZagne](/beta/software/S0349)
* [LightNeuron](/beta/software/S0395)
* [Linfo](/beta/software/S0211)
* [Linux Rabbit](/beta/software/S0362)
* [LoJax](/beta/software/S0397)
* [LockerGoga](/beta/software/S0372)
* [Lslsass](/beta/software/S0121)
* [Lurid](/beta/software/S0010)
* [MURKYTOP](/beta/software/S0233)
* [MacSpy](/beta/software/S0282)
* [Machete](/beta/software/S0409)
* [MailSniper](/beta/software/S0413)
* [Matroyshka](/beta/software/S0167)
* [Micropsia](/beta/software/S0339)
* [MimiPenguin](/beta/software/S0179)
* [Mimikatz](/beta/software/S0002)
* [MiniDuke](/beta/software/S0051)
* [MirageFox](/beta/software/S0280)
* [Mis-Type](/beta/software/S0084)
* [Misdat](/beta/software/S0083)
* [Mivast](/beta/software/S0080)
* [MoonWind](/beta/software/S0149)
* [More_eggs](/beta/software/S0284)
* [Mosquito](/beta/software/S0256)
* [NDiskMonitor](/beta/software/S0272)
* [NETEAGLE](/beta/software/S0034)
* [NETWIRE](/beta/software/S0198)
* [NOKKI](/beta/software/S0353)
* [NanHaiShu](/beta/software/S0228)
* [NanoCore](/beta/software/S0336)
* [NavRAT](/beta/software/S0247)
* [Net](/beta/software/S0039)
* [Net Crawler](/beta/software/S0056)
* [NetTraveler](/beta/software/S0033)
* [Nidiran](/beta/software/S0118)
* [NotPetya](/beta/software/S0368)
* [OLDBAIT](/beta/software/S0138)
* [OSInfo](/beta/software/S0165)
* [OSX/Shlayer](/beta/software/S0402)
* [OSX_OCEANLOTUS.D](/beta/software/S0352)
* [OceanSalt](/beta/software/S0346)
* [Octopus](/beta/software/S0340)
* [Olympic Destroyer](/beta/software/S0365)
* [OnionDuke](/beta/software/S0052)
* [OopsIE](/beta/software/S0264)
* [Orz](/beta/software/S0229)
* [OwaAuth](/beta/software/S0072)
* [P2P ZeuS](/beta/software/S0016)
* [PHOREAL](/beta/software/S0158)
* [PLAINTEE](/beta/software/S0254)
* [POORAIM](/beta/software/S0216)
* [POSHSPY](/beta/software/S0150)
* [POWERSOURCE](/beta/software/S0145)
* [POWERSTATS](/beta/software/S0223)
* [POWERTON](/beta/software/S0371)
* [POWRUNER](/beta/software/S0184)
* [PUNCHBUGGY](/beta/software/S0196)
* [PUNCHTRACK](/beta/software/S0197)
* [Pasam](/beta/software/S0208)
* [PinchDuke](/beta/software/S0048)
* [Pisloader](/beta/software/S0124)
* [PlugX](/beta/software/S0013)
* [PoisonIvy](/beta/software/S0012)
* [PoshC2](/beta/software/S0378)
* [PowerDuke](/beta/software/S0139)
* [PowerSploit](/beta/software/S0194)
* [PowerStallion](/beta/software/S0393)
* [Prikormka](/beta/software/S0113)
* [Proton](/beta/software/S0279)
* [Proxysvc](/beta/software/S0238)
* [PsExec](/beta/software/S0029)
* [Psylo](/beta/software/S0078)
* [Pteranodon](/beta/software/S0147)
* [Pupy](/beta/software/S0192)
* [QUADAGENT](/beta/software/S0269)
* [QuasarRAT](/beta/software/S0262)
* [RARSTONE](/beta/software/S0055)
* [RATANKBA](/beta/software/S0241)
* [RGDoor](/beta/software/S0258)
* [RIPTIDE](/beta/software/S0003)
* [ROCKBOOT](/beta/software/S0112)
* [ROKRAT](/beta/software/S0240)
* [RTM](/beta/software/S0148)
* [RawPOS](/beta/software/S0169)
* [Reaver](/beta/software/S0172)
* [RedLeaves](/beta/software/S0153)
* [Regin](/beta/software/S0019)
* [Remcos](/beta/software/S0332)
* [Remexi](/beta/software/S0375)
* [RemoteCMD](/beta/software/S0166)
* [Remsec](/beta/software/S0125)
* [Revenge RAT](/beta/software/S0379)
* [RobbinHood](/beta/software/S0400)
* [RogueRobin](/beta/software/S0270)
* [Rover](/beta/software/S0090)
* [Ruler](/beta/software/S0358)
* [RunningRAT](/beta/software/S0253)
* [S-Type](/beta/software/S0085)
* [SEASHARPEE](/beta/software/S0185)
* [SHOTPUT](/beta/software/S0063)
* [SLOWDRIFT](/beta/software/S0218)
* [SNUGRIDE](/beta/software/S0159)
* [SOUNDBITE](/beta/software/S0157)
* [SPACESHIP](/beta/software/S0035)
* [SQLRat](/beta/software/S0390)
* [Sakula](/beta/software/S0074)
* [SeaDuke](/beta/software/S0053)
* [Seasalt](/beta/software/S0345)
* [ServHelper](/beta/software/S0382)
* [Shamoon](/beta/software/S0140)
* [Skeleton Key](/beta/software/S0007)
* [Smoke Loader](/beta/software/S0226)
* [Socksbot](/beta/software/S0273)
* [SpeakUp](/beta/software/S0374)
* [SslMM](/beta/software/S0058)
* [Starloader](/beta/software/S0188)
* [StoneDrill](/beta/software/S0380)
* [StreamEx](/beta/software/S0142)
* [Sykipot](/beta/software/S0018)
* [SynAck](/beta/software/S0242)
* [Sys10](/beta/software/S0060)
* [T9000](/beta/software/S0098)
* [TDTESS](/beta/software/S0164)
* [TEXTMATE](/beta/software/S0146)
* [TURNEDUP](/beta/software/S0199)
* [TYPEFRAME](/beta/software/S0263)
* [Taidoor](/beta/software/S0011)
* [TinyZBot](/beta/software/S0004)
* [Tor](/beta/software/S0183)
* [TrickBot](/beta/software/S0266)
* [Trojan.Karagany](/beta/software/S0094)
* [Trojan.Mebromi](/beta/software/S0001)
* [Truvasys](/beta/software/S0178)
* [Twitoor](/beta/software/S0302)
* [UBoatRAT](/beta/software/S0333)
* [UPPERCUT](/beta/software/S0275)
* [USBStealer](/beta/software/S0136)
* [Umbreon](/beta/software/S0221)
* [Unknown Logger](/beta/software/S0130)
* [Ursnif](/beta/software/S0386)
* [VERMIN](/beta/software/S0257)
* [Vasport](/beta/software/S0207)
* [Volgmer](/beta/software/S0180)
* [WEBC2](/beta/software/S0109)
* [WannaCry](/beta/software/S0366)
* [Wiarp](/beta/software/S0206)
* [WinMM](/beta/software/S0059)
* [Windows Credential Editor](/beta/software/S0005)
* [Wingbird](/beta/software/S0176)
* [Winnti](/beta/software/S0141)
* [XAgentOSX](/beta/software/S0161)
* [XTunnel](/beta/software/S0117)
* [Xbash](/beta/software/S0341)
* [Yahoyah](/beta/software/S0388)
* [ZLib](/beta/software/S0086)
* [Zebrocy](/beta/software/S0251)
* [ZeroT](/beta/software/S0230)
* [Zeus Panda](/beta/software/S0330)
* [ZxShell](/beta/software/S0412)
* [adbupd](/beta/software/S0202)
* [at](/beta/software/S0110)
* [cmd](/beta/software/S0106)
* [dsquery](/beta/software/S0105)
* [esentutl](/beta/software/S0404)
* [gh0st RAT](/beta/software/S0032)
* [gsecdump](/beta/software/S0008)
* [hcdLoader](/beta/software/S0071)
* [httpclient](/beta/software/S0068)
* [iKitten](/beta/software/S0278)
* [jRAT](/beta/software/S0283)
* [netsh](/beta/software/S0108)
* [njRAT](/beta/software/S0385)
* [pngdowner](/beta/software/S0067)
* [pwdump](/beta/software/S0006)
* [schtasks](/beta/software/S0111)
* [spwebmember](/beta/software/S0227)
* [yty](/beta/software/S0248)
* [zwShell](/beta/software/S0350)


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

* [Dvmap](/beta/software/S0420)
* [GolfSpy](/beta/software/S0421)
* [SimBad](/beta/software/S0419)
* [ViceLeaker](/beta/software/S0418)


Software changes:

* [FinFisher](/beta/software/S0182)
* [Monokle](/beta/software/S0407)


Minor Software changes:

* [Pegasus for iOS](/beta/software/S0289)


Software revocations:
No changes

Software deprecations:
No changes

### Groups

**Enterprise**

New Groups:

* [Bouncing Golf](/beta/groups/G0097)


Group changes:

* [APT1](/beta/groups/G0006)
* [APT12](/beta/groups/G0005)
* [APT18](/beta/groups/G0026)
* [APT19](/beta/groups/G0073)
* [APT28](/beta/groups/G0007)
* [APT29](/beta/groups/G0016)
* [APT3](/beta/groups/G0022)
* [APT32](/beta/groups/G0050)
* [APT33](/beta/groups/G0064)
* [APT37](/beta/groups/G0067)
* [APT38](/beta/groups/G0082)
* [APT39](/beta/groups/G0087)
* [APT41](/beta/groups/G0096)
* [Axiom](/beta/groups/G0001)
* [BRONZE BUTLER](/beta/groups/G0060)
* [Carbanak](/beta/groups/G0008)
* [Cleaver](/beta/groups/G0003)
* [Cobalt Group](/beta/groups/G0080)
* [CopyKittens](/beta/groups/G0052)
* [Dark Caracal](/beta/groups/G0070)
* [DarkHydrus](/beta/groups/G0079)
* [Darkhotel](/beta/groups/G0012)
* [Deep Panda](/beta/groups/G0009)
* [Dragonfly 2.0](/beta/groups/G0074)
* [Elderwood](/beta/groups/G0066)
* [Equation](/beta/groups/G0020)
* [FIN10](/beta/groups/G0051)
* [FIN4](/beta/groups/G0085)
* [FIN5](/beta/groups/G0053)
* [FIN6](/beta/groups/G0037)
* [FIN7](/beta/groups/G0046)
* [FIN8](/beta/groups/G0061)
* [GCMAN](/beta/groups/G0036)
* [Gallmaker](/beta/groups/G0084)
* [Gamaredon Group](/beta/groups/G0047)
* [Gorgon Group](/beta/groups/G0078)
* [Group5](/beta/groups/G0043)
* [Honeybee](/beta/groups/G0072)
* [Ke3chang](/beta/groups/G0004)
* [Kimsuky](/beta/groups/G0094)
* [Lazarus Group](/beta/groups/G0032)
* [Leafminer](/beta/groups/G0077)
* [Leviathan](/beta/groups/G0065)
* [Machete](/beta/groups/G0095)
* [Magic Hound](/beta/groups/G0059)
* [Moafee](/beta/groups/G0002)
* [Molerats](/beta/groups/G0021)
* [MuddyWater](/beta/groups/G0069)
* [Night Dragon](/beta/groups/G0014)
* [OilRig](/beta/groups/G0049)
* [Orangeworm](/beta/groups/G0071)
* [PLATINUM](/beta/groups/G0068)
* [Patchwork](/beta/groups/G0040)
* [PittyTiger](/beta/groups/G0011)
* [Poseidon Group](/beta/groups/G0033)
* [Putter Panda](/beta/groups/G0024)
* [RTM](/beta/groups/G0048)
* [Rancor](/beta/groups/G0075)
* [Scarlet Mimic](/beta/groups/G0029)
* [Silence](/beta/groups/G0091)
* [SilverTerrier](/beta/groups/G0083)
* [Soft Cell](/beta/groups/G0093)
* [Sowbug](/beta/groups/G0054)
* [Stealth Falcon](/beta/groups/G0038)
* [Stolen Pencil](/beta/groups/G0086)
* [Strider](/beta/groups/G0041)
* [Suckfly](/beta/groups/G0039)
* [TA459](/beta/groups/G0062)
* [TA505](/beta/groups/G0092)
* [TEMP.Veles](/beta/groups/G0088)
* [The White Company](/beta/groups/G0089)
* [Threat Group-1314](/beta/groups/G0028)
* [Threat Group-3390](/beta/groups/G0027)
* [Thrip](/beta/groups/G0076)
* [Tropic Trooper](/beta/groups/G0081)
* [Turla](/beta/groups/G0010)
* [WIRTE](/beta/groups/G0090)
* [admin@338](/beta/groups/G0018)
* [menuPass](/beta/groups/G0045)


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

* [APT1](/beta/groups/G0006)
* [APT28](/beta/groups/G0007)
* [Cleaver](/beta/groups/G0003)
* [Night Dragon](/beta/groups/G0014)
* [TEMP.Veles](/beta/groups/G0088)


Minor Group changes:
No changes

Group revocations:
No changes

Group deprecations:
No changes

**Mobile**

New Groups:

* [Bouncing Golf](/beta/groups/G0097)


Group changes:

* [APT28](/beta/groups/G0007)
* [Dark Caracal](/beta/groups/G0070)


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

* [Active Directory Configuration](/beta/mitigations/M1015) - Sub or technique relationships updated
* [Antivirus/Antimalware](/beta/mitigations/M1049) - Sub or technique relationships updated
* [Application Isolation and Sandboxing](/beta/mitigations/M1048) - Sub or technique relationships updated
* [Audit](/beta/mitigations/M1047) - Sub or technique relationships updated
* [Credential Access Protection](/beta/mitigations/M1043) - Sub or technique relationships updated
* [Data Backup](/beta/mitigations/M1053) - Sub or technique relationships updated
* [Disable or Remove Feature or Program](/beta/mitigations/M1042) - Sub or technique relationships updated
* [Execution Prevention](/beta/mitigations/M1038) - Sub or technique relationships updated
* [Exploit Protection](/beta/mitigations/M1050) - Sub or technique relationships updated
* [Network Segmentation](/beta/mitigations/M1030) - Sub or technique relationships updated
* [Operating System Configuration](/beta/mitigations/M1028) - Sub or technique relationships updated
* [Privileged Account Management](/beta/mitigations/M1026) - Sub or technique relationships updated
* [Privileged Process Integrity](/beta/mitigations/M1025) - Sub or technique relationships updated
* [Restrict File and Directory Permissions](/beta/mitigations/M1022) - Sub or technique relationships updated
* [Software Configuration](/beta/mitigations/M1054) - Sub or technique relationships updated
* [User Account Control](/beta/mitigations/M1052) - Sub or technique relationships updated
* [User Account Management](/beta/mitigations/M1018) - Sub or technique relationships updated
* [User Training](/beta/mitigations/M1017) - Sub or technique relationships updated
* [Vulnerability Scanning](/beta/mitigations/M1016) - Sub or technique relationships updated


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
