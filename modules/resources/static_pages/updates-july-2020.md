Title: Updates - July 2020
Date: July 2020
Category: Cyber Threat Intelligence
Authors: Adam Pennington
Template: resources/update-post
url: /resources/updates/updates-july-2020
save_as: resources/updates/updates-july-2020/index.html

| Version | Start Date | End Date | Data |
|:--------|:-----------|:---------|:-----|
| [ATT&CK v7](/versions/v7) | July 8, 2020 | October 26, 2020 | [v7.0 on MITRE/CTI](https://github.com/mitre/cti/releases/tag/ATT%26CK-v7.0) |

<ul class="nav nav-tabs" role="tablist">
    <li class="nav-item">
        <a class="nav-link active" role="tab" href="#v6-pane" id="v6-tab" data-toggle="tab" aria-controls="v6-pane" aria-selected="false">Compared to v6.3</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" role="tab" href="#v7-pane" id="v7-tab" data-toggle="tab" aria-controls="v7-pane" aria-selected="true">Compared to v7.0-beta</a>
    </li>
</ul>

<div class="tab-content border border-top-0 p-3">
    
    <div class="tab-pane active" role="tabpanel" id="v6-pane" aria-labelledby="v6-tab">

        <p>The July 2020 (v7) ATT&amp;CK release  updates Techniques, Groups, and Software for both Enterprise and Mobile. This is the first non-beta release of Enterprise ATT&amp;CK represented with sub-techniques. The pre sub-technique version of ATT&amp;CK has been preserved <a href="https://attack.mitre.org/versions/v6/">here</a>. Most of this content was released as a beta in March 2020, and changes between the beta release and this release are documented separately.</p>
        <p>In total, the sub-technique version of ATT&amp;CK for Enterprise contains 156 techniques (reduced from 266) and 272 sub-techniques.</p>
        <p>See <a href="https://medium.com/mitre-attack/attack-with-sub-techniques-is-now-just-attack-8fc20997d8de">the accompanying blog post</a> for more details.</p>
        <p>In this same release we have deprecated white/blacklist language in ATT&amp;CK. Techniques and mitigations previously containing this language have either been reworded or the language has been replaced with allow/denylist. In line with industry terminology changes, application whitelisting and process whitelisting have both been replaced with application control.</p>
        <h3>Techniques</h3>
        <p><strong>Enterprise</strong></p>
        <p>
            View enterprise technique updates in the ATT&CK Navigator <a href="https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fattack-navigator%2Fmaster%2Flayers%2Fdata%2Fupdate_layers%2FJuly_2020%2FJuly_2020_enterprise_attack.json" target="_blank">here</a>.
        </p>
        <p>New Techniques:</p>
        <ul>
        <li><a href="/techniques/T1548">Abuse Elevation Control Mechanism</a> - Created to consolidate similar behaviors that take advantage of elevation control<ul>
        <li><a href="/techniques/T1548/002">Bypass User Access Control</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1548/004">Elevated Execution with Prompt</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1548/001">Setuid and Setgid</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1548/003">Sudo and Sudo Caching</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Access Token Manipulation: <a href="/techniques/T1134/002">Create Process with Token</a> - Broken out from pre-defined behavior within Access Token Manipulation</li>
        <li>Access Token Manipulation: <a href="/techniques/T1134/003">Make and Impersonate Token</a> - Broken out from pre-defined behavior within Access Token Manipulation</li>
        <li>Access Token Manipulation: <a href="/techniques/T1134/004">Parent PID Spoofing</a> - Added due to manipulation of tokens</li>
        <li>Access Token Manipulation: <a href="/techniques/T1134/005">SID-History Injection</a> - Added due to manipulation of token information</li>
        <li>Access Token Manipulation: <a href="/techniques/T1134/001">Token Impersonation/Theft</a> - Broken out from pre-defined behavior within Access Token Manipulation</li>
        <li>Account Discovery: <a href="/techniques/T1087/004">Cloud Account</a> - Added for parity with Create Account</li>
        <li>Account Discovery: <a href="/techniques/T1087/002">Domain Account</a> - Added for parity with Create Account</li>
        <li>Account Discovery: <a href="/techniques/T1087/003">Email Account</a> - Broken out from pre-defined behavior within Account Discovery</li>
        <li>Account Discovery: <a href="/techniques/T1087/001">Local Account</a> - Added for parity with Create Account</li>
        <li>Account Manipulation: <a href="/techniques/T1098/003">Add Office 365 Global Administrator Role</a> - Broken out from pre-defined behavior within Account Manipulation</li>
        <li>Account Manipulation: <a href="/techniques/T1098/001">Additional Azure Service Principal Credentials</a> - Broken out from pre-defined behavior within Account Manipulation</li>
        <li>Account Manipulation: <a href="/techniques/T1098/002">Exchange Email Delegate Permissions</a> - Broken out from pre-defined behavior within Account Manipulation</li>
        <li>Account Manipulation: <a href="/techniques/T1098/004">SSH Authorized Keys</a> - Created as distinct behavior within Account Manipulation</li>
        <li>Application Layer Protocol: <a href="/techniques/T1071/004">DNS</a> - Created as distinct behavior due to how Application Layer Protocols are used for C2</li>
        <li>Application Layer Protocol: <a href="/techniques/T1071/002">File Transfer Protocols</a> - Created as distinct behavior due to how Application Layer Protocols are used for C2</li>
        <li>Application Layer Protocol: <a href="/techniques/T1071/003">Mail Protocols</a> - Created as distinct behavior due to how Application Layer Protocols are used for C2</li>
        <li>Application Layer Protocol: <a href="/techniques/T1071/001">Web Protocols</a> - Created as distinct behavior due to how Application Layer Protocols are used for C2</li>
        <li><a href="/techniques/T1560">Archive Collected Data</a> - Created to consolidate behavior around encrypting and compressing collected data</li>
        <li><a href="/techniques/T1560/003">Archive via Custom Method</a> - Broken out from pre-defined behavior within Archive Collected Data</li>
        <li><a href="/techniques/T1560/002">Archive via Library</a> - Broken out from pre-defined behavior within Archive Collected Data</li>
        <li><a href="/techniques/T1560/001">Archive via Utility</a> - Broken out from pre-defined behavior within Archive Collected Data</li>
        <li><a href="/techniques/T1547">Boot or Logon Autostart Execution</a> - Created to consolidate similar autostart execution locations<ul>
        <li><a href="/techniques/T1547/002">Authentication Package</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1547/006">Kernel Modules and Extensions</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1547/008">LSASS Driver</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1547/011">Plist Modification</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1547/010">Port Monitors</a>  - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1547/007">Re-opened Applications</a>  - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1547/001">Registry Run Keys / Startup Folder</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1547/005">Security Support Provider</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1547/009">Shortcut Modification</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1547/003">Time Providers</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1547/004">Winlogon Helper DLL</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Boot or Logon Initialization Scripts: <a href="/techniques/T1037/002">Logon Script (Mac)</a> - Existing technique that became a sub-technique</li>
        <li>Boot or Logon Initialization Scripts: <a href="/techniques/T1037/001">Logon Script (Windows)</a> - Existing technique that became a sub-technique</li>
        <li>Boot or Logon Initialization Scripts: <a href="/techniques/T1037/003">Network Logon Script</a> - Existing technique that became a sub-technique</li>
        <li>Boot or Logon Initialization Scripts: <a href="/techniques/T1037/004">Rc.common</a> - Existing technique that became a sub-technique</li>
        <li>Boot or Logon Initialization Scripts: <a href="/techniques/T1037/005">Startup Items</a> - Existing technique that became a sub-technique</li>
        <li>Brute Force: <a href="/techniques/T1110/004">Credential Stuffing</a> - Created as distinct behavior variation of Brute Force</li>
        <li>Brute Force: <a href="/techniques/T1110/002">Password Cracking</a> - Broken out from pre-defined behavior within Brute Force</li>
        <li>Brute Force: <a href="/techniques/T1110/001">Password Guessing</a> - Broken out from pre-defined behavior within Brute Force</li>
        <li>Brute Force: <a href="/techniques/T1110/003">Password Spraying</a> - Broken out from pre-defined behavior within Brute Force</li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/002">AppleScript</a> - Existing technique that became a sub-technique</li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/007">JavaScript/JScript</a> - Created as distinct behavior within Command and Scripting Interpreter</li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/001">PowerShell</a> - Existing technique that became a sub-technique</li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/006">Python</a> - Created as distinct behavior within Command and Scripting Interpreter</li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/004">Unix Shell</a> - Existing technique that became a sub-technique</li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/005">Visual Basic</a> - Created as distinct behavior within Command and Scripting Interpreter</li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/003">Windows Command Shell</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1554">Compromise Client Software Binary</a> - New technique based on contribution</li>
        <li>Create Account: <a href="/techniques/T1136/003">Cloud Account</a> - Broken out from pre-defined behavior within Create Account</li>
        <li>Create Account: <a href="/techniques/T1136/002">Domain Account</a> - Broken out from pre-defined behavior within Create Account</li>
        <li>Create Account: <a href="/techniques/T1136/001">Local Account</a> - Broken out from pre-defined behavior within Create Account</li>
        <li><a href="/techniques/T1543">Create or Modify System Process</a> - Created to consolidate behavior around system-level processes<ul>
        <li><a href="/techniques/T1543/001">Launch Agent</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1543/004">Launch Daemon</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1543/002">Systemd Service</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1543/003">Windows Service</a> - Existing technique that became a sub-technique. Consolidates Modify Existing Service and New Service techniques into one sub-technique</li>
        </ul>
        </li>
        <li><a href="/techniques/T1555">Credentials from Password Stores</a> - Created to consolidate locations where passwords are stored<ul>
        <li><a href="/techniques/T1555/003">Credentials from Web Browsers</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1555/001">Keychain</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1555/002">Securityd Memory</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Data Encoding: <a href="/techniques/T1132/002">Non-Standard Encoding</a> - Broken out from pre-defined behavior within Data Encoding</li>
        <li>Data Encoding: <a href="/techniques/T1132/001">Standard Encoding</a> - Broken out from pre-defined behavior within Data Encoding<ul>
        <li><a href="/techniques/T1565">Data Manipulation</a> - Created to consolidate existing behaviors around data manipulation</li>
        <li><a href="/techniques/T1565/003">Runtime Data Manipulation</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1565/001">Stored Data Manipulation</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1565/002">Transmitted Data Manipulation</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Data Obfuscation: <a href="/techniques/T1001/001">Junk Data</a> - Broken out from pre-defined behavior within Data Obfuscation</li>
        <li>Data Obfuscation: <a href="/techniques/T1001/003">Protocol Impersonation</a> - Broken out from pre-defined behavior within Data Obfuscation</li>
        <li>Data Obfuscation: <a href="/techniques/T1001/002">Steganography</a> - Broken out from pre-defined behavior within Data Obfuscation</li>
        <li>Data Staged: <a href="/techniques/T1074/001">Local Data Staging</a> - Broken out from pre-defined behavior within Data Staged</li>
        <li>Data Staged: <a href="/techniques/T1074/002">Remote Data Staging</a> - Broken out from pre-defined behavior within Data Staged</li>
        <li>Data from Information Repositories: <a href="/techniques/T1213/001">Confluence</a> - Broken out from pre-defined behavior within Data from Information Repositories</li>
        <li>Data from Information Repositories: <a href="/techniques/T1213/002">Sharepoint</a> - Broken out from pre-defined behavior within Data from Information Repositories</li>
        <li>Defacement: <a href="/techniques/T1491/002">External Defacement</a> - Broken out from pre-defined behavior within Defacement</li>
        <li>Defacement: <a href="/techniques/T1491/001">Internal Defacement</a> - Broken out from pre-defined behavior within Defacement</li>
        <li><a href="/techniques/T1561">Disk Wipe</a> - Created to consolidate behavior around disk wiping<ul>
        <li><a href="/techniques/T1561/001">Disk Content Wipe</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1561/002">Disk Structure Wipe</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li><a href="/techniques/T1568">Dynamic Resolution</a> - Created to consolidate behavior around dynamic C2 behavior<ul>
        <li><a href="/techniques/T1568/003">DNS Calculation</a> - Existing PRE-ATT&amp;CK technique that became a sub-technique in Enterprise</li>
        <li><a href="/techniques/T1568/002">Domain Generation Algorithms</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1568/001">Fast Flux DNS</a> - Existing PRE-ATT&amp;CK technique that became a sub-technique in Enterprise</li>
        </ul>
        </li>
        <li>Email Collection: <a href="/techniques/T1114/003">Email Forwarding Rule</a> - Broken out from pre-defined behavior within Email Collection</li>
        <li>Email Collection: <a href="/techniques/T1114/001">Local Email Collection</a> - Broken out from pre-defined behavior within Email Collection</li>
        <li>Email Collection: <a href="/techniques/T1114/002">Remote Email Collection</a> - Broken out from pre-defined behavior within Email Collection</li>
        <li><a href="/techniques/T1573">Encrypted Channel</a> - Created to consolidate behavior around encrypted C2<ul>
        <li><a href="/techniques/T1573/002">Asymmetric Cryptography</a> - Broken out from pre-defined behavior within Encrypted Channel</li>
        <li><a href="/techniques/T1573/001">Symmetric Cryptography</a> - Broken out from pre-defined behavior within Encrypted Channel</li>
        </ul>
        </li>
        <li>Endpoint Denial of Service: <a href="/techniques/T1499/003">Application Exhaustion Flood</a> - Broken out from pre-defined behavior within Endpoint Denial of Service</li>
        <li>Endpoint Denial of Service: <a href="/techniques/T1499/004">Application or System Exploitation</a> - Broken out from pre-defined behavior within Endpoint Denial of Service</li>
        <li>Endpoint Denial of Service: <a href="/techniques/T1499/001">OS Exhaustion Flood</a> - Broken out from pre-defined behavior within Endpoint Denial of Service</li>
        <li>Endpoint Denial of Service: <a href="/techniques/T1499/002">Service Exhaustion Flood</a> - Broken out from pre-defined behavior within Endpoint Denial of Service</li>
        <li><a href="/techniques/T1546">Event Triggered Execution</a> - Created to consolidate persistence behavior due to adversary or user initiated actions<ul>
        <li><a href="/techniques/T1546/004">.bash_profile and .bashrc</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/008">Accessibility Features</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/009">AppCert DLLs</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/010">AppInit DLLs</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/011">Application Shimming</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/001">Change Default File Association</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/015">Component Object Model Hijacking</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/014">Emond</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/012">Image File Execution Options Injection</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/006">LC_LOAD_DYLIB Addition</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/007">Netsh Helper DLL</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/013">PowerShell Profile</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/002">Screensaver</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/005">Trap</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1546/003">Windows Management Instrumentation Event Subscription</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Execution Guardrails: <a href="/techniques/T1480/001">Environmental Keying</a> - Broken out from pre-defined behavior within Execution Guardrails</li>
        <li>Exfiltration Over Alternative Protocol: <a href="/techniques/T1048/002">Exfiltration Over Asymmetric Encrypted Non-C2 Protocol</a> - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol</li>
        <li>Exfiltration Over Alternative Protocol: <a href="/techniques/T1048/001">Exfiltration Over Symmetric Encrypted Non-C2 Protocol</a> - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol</li>
        <li>Exfiltration Over Alternative Protocol: <a href="/techniques/T1048/003">Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol</a> - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol</li>
        <li>Exfiltration Over Other Network Medium: <a href="/techniques/T1011/001">Exfiltration Over Bluetooth</a> - Broken out from pre-defined behavior within Exfiltration over Other Network Medium</li>
        <li>Exfiltration Over Physical Medium: <a href="/techniques/T1052/001">Exfiltration over USB</a> - Broken out from pre-defined behavior within Exfiltration Over Physical Medium</li>
        <li><a href="/techniques/T1567">Exfiltration Over Web Service</a> - Created to consolidate behaviors around exfiltration to legitimate web services<ul>
        <li><a href="/techniques/T1567/002">Exfiltration to Cloud Storage</a> - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol</li>
        <li><a href="/techniques/T1567/001">Exfiltration to Code Repository</a> - Broken out from pre-defined behavior within Exfiltration Over Alternative Protocol</li>
        </ul>
        </li>
        <li>File and Directory Permissions Modification: <a href="/techniques/T1222/002">Linux and Mac File and Directory Permissions Modification</a> - Broken out from pre-defined behavior within File and Directory Permissions Modification</li>
        <li>File and Directory Permissions Modification: <a href="/techniques/T1222/001">Windows File and Directory Permissions Modification</a> - Broken out from pre-defined behavior within File and Directory Permissions Modification</li>
        <li><a href="/techniques/T1564">Hide Artifacts</a> - Created to consolidate behaviors around defense evasion through creating hidden objects that may be difficult to see<ul>
        <li><a href="/techniques/T1564/005">Hidden File System</a> - Created as distinct behavior within Hide Artifacts</li>
        <li><a href="/techniques/T1564/001">Hidden Files and Directories</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1564/002">Hidden Users</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1564/003">Hidden Window</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1564/004">NTFS File Attributes</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1564/006">Run Virtual Instance</a> - Created as distinct behavior within Hide Artifacts</li>
        </ul>
        </li>
        <li><a href="/techniques/T1574">Hijack Execution Flow</a> - Created to consolidate behaviors around running executable code by placing it where it would be executed by a legitimate process<ul>
        <li><a href="/techniques/T1574/012">COR_PROFILER</a> - Created as distinct behavior within Hijack Execution Flow</li>
        <li><a href="/techniques/T1574/001">DLL Search Order Hijacking</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1574/002">DLL Side-Loading</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1574/004">Dylib Hijacking</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1574/005">Executable Installer File Permissions Weakness</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1574/006">LD_PRELOAD</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1574/007">Path Interception by PATH Environment Variable</a> - Broken out from pre-defined behavior within the prior Path Interception technique</li>
        <li><a href="/techniques/T1574/008">Path Interception by Search Order Hijacking</a> - Broken out from pre-defined behavior within the prior Path Interception technique</li>
        <li><a href="/techniques/T1574/009">Path Interception by Unquoted Path</a> - Broken out from pre-defined behavior within the prior Path Interception technique</li>
        <li><a href="/techniques/T1574/010">Services File Permissions Weakness</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1574/011">Services Registry Permissions Weakness</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li><a href="/techniques/T1562">Impair Defenses</a> - Created to consolidate behaviors that prevent a defense from working as intended<ul>
        <li><a href="/techniques/T1562/002">Disable Windows Event Logging</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1562/007">Disable or Modify Cloud Firewall</a> - Created as distinct behavior within Impair Defenses</li>
        <li><a href="/techniques/T1562/004">Disable or Modify System Firewall</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1562/001">Disable or Modify Tools</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1562/003">HISTCONTROL</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1562/006">Indicator Blocking</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Indicator Removal on Host: <a href="/techniques/T1070/003">Clear Command History</a> - Existing technique that became a sub-technique</li>
        <li>Indicator Removal on Host: <a href="/techniques/T1070/002">Clear Linux or Mac System Logs</a> - Broken out from pre-defined behavior within Indicator Removal on Host</li>
        <li>Indicator Removal on Host: <a href="/techniques/T1070/001">Clear Windows Event Logs</a> - Broken out from pre-defined behavior within Indicator Removal on Host</li>
        <li>Indicator Removal on Host: <a href="/techniques/T1070/004">File Deletion</a> - Existing technique that became a sub-technique</li>
        <li>Indicator Removal on Host: <a href="/techniques/T1070/005">Network Share Connection Removal</a> - Existing technique that became a sub-technique</li>
        <li>Indicator Removal on Host: <a href="/techniques/T1070/006">Timestomp</a> - Existing technique that became a sub-technique</li>
        <li>Input Capture: <a href="/techniques/T1056/004">Credential API Hooking</a> - Existing technique that became a sub-technique and was renamed from API Hooking. Scope change to only credential access for API hooking was based on available procedure examples</li>
        <li>Input Capture: <a href="/techniques/T1056/002">GUI Input Capture</a> - Broken out from pre-defined behavior within Input Capture</li>
        <li>Input Capture: <a href="/techniques/T1056/001">Keylogging</a> - Broken out from pre-defined behavior within Input Capture</li>
        <li>Input Capture: <a href="/techniques/T1056/003">Web Portal Capture</a> - Broken out from pre-defined behavior within Input Capture</li>
        <li><a href="/techniques/T1559">Inter-Process Communication</a> - Created to consolidate behavior related to using IPC for local system execution<ul>
        <li><a href="/techniques/T1559/001">Component Object Model</a> - Broken out from pre-defined behavior within the prior Component Object Model and Distributed COM technique</li>
        <li><a href="/techniques/T1559/002">Dynamic Data Exchange</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li><a href="/techniques/T1570">Lateral Tool Transfer</a> - Broken out from pre-defined behavior within the prior Remote File Copy technique to focus on file transfer within a network</li>
        <li><a href="/techniques/T1557">Man-in-the-Middle</a> - Created to consolidate behavior related to setting up man-in-the-middle condition within a network<ul>
        <li><a href="/techniques/T1557/001">LLMNR/NBT-NS Poisoning and SMB Relay</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Masquerading: <a href="/techniques/T1036/001">Invalid Code Signature</a> - Created based on procedure examples within Code Signing as a distinct behavior using invalid digital signatures</li>
        <li>Masquerading: <a href="/techniques/T1036/004">Masquerade Task or Service</a> - Broken out from pre-defined behavior within Masquerading</li>
        <li>Masquerading: <a href="/techniques/T1036/005">Match Legitimate Name or Location</a> - Broken out from pre-defined behavior within Masquerading</li>
        <li>Masquerading: <a href="/techniques/T1036/003">Rename System Utilities</a> - Broken out from pre-defined behavior within Masquerading</li>
        <li>Masquerading: <a href="/techniques/T1036/002">Right-to-Left Override</a> - Broken out from pre-defined behavior within Masquerading</li>
        <li>Masquerading: <a href="/techniques/T1036/006">Space after Filename</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1556">Modify Authentication Process</a> - Created to consolidate behavior related to changing the authentication process previously under Account Manipulation<ul>
        <li><a href="/techniques/T1556/001">Domain Controller Authentication</a> - Broken out from pre-defined behavior within Account Manipulation</li>
        <li><a href="/techniques/T1556/002">Password Filter DLL</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1556/003">Pluggable Authentication Modules</a> - Created as distinct behavior within Modify Authentication Process</li>
        </ul>
        </li>
        <li><a href="/techniques/T1578">Modify Cloud Compute Infrastructure</a> - Created to consolidate behaviors around defense evasion through the cloud compute service<ul>
        <li><a href="/techniques/T1578/002">Create Cloud Instance</a> - Created as distinct behavior within Modify Cloud Compute Infrastructure</li>
        <li><a href="/techniques/T1578/001">Create Snapshot</a> - Created as distinct behavior within Modify Cloud Compute Infrastructure</li>
        <li><a href="/techniques/T1578/003">Delete Cloud Instance</a> - Created as distinct behavior within Modify Cloud Compute Infrastructure</li>
        <li><a href="/techniques/T1578/004">Revert Cloud Instance</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Network Denial of Service: <a href="/techniques/T1498/001">Direct Network Flood</a> - Broken out from pre-defined behavior within Network Denial of Service</li>
        <li>Network Denial of Service: <a href="/techniques/T1498/002">Reflection Amplification</a> - Broken out from pre-defined behavior within Network Denial of Service</li>
        <li><a href="/techniques/T1571">Non-Standard Port</a> - Created to refine the idea behind Common and Uncommonly Used Port to focus the behavior on use of a non-standard port for C2 based on the protocol used</li>
        <li>OS Credential Dumping: <a href="/techniques/T1003/008">/etc/passwd and /etc/shadow</a> - Broken out from pre-defined behavior within OS Credential Dumping</li>
        <li>OS Credential Dumping: <a href="/techniques/T1003/005">Cached Domain Credentials</a> - Broken out from pre-defined behavior within OS Credential Dumping</li>
        <li>OS Credential Dumping: <a href="/techniques/T1003/006">DCSync</a> - Broken out from pre-defined behavior within OS Credential Dumping</li>
        <li>OS Credential Dumping: <a href="/techniques/T1003/004">LSA Secrets</a> - Broken out from pre-defined behavior within OS Credential Dumping</li>
        <li>OS Credential Dumping: <a href="/techniques/T1003/001">LSASS Memory</a> - Broken out from pre-defined behavior within OS Credential Dumping</li>
        <li>OS Credential Dumping: <a href="/techniques/T1003/003">NTDS</a> - Broken out from pre-defined behavior within OS Credential Dumping</li>
        <li>OS Credential Dumping: <a href="/techniques/T1003/007">Proc Filesystem</a> - Broken out from pre-defined behavior within OS Credential Dumping</li>
        <li>OS Credential Dumping: <a href="/techniques/T1003/002">Security Account Manager</a> - Broken out from pre-defined behavior within OS Credential Dumping</li>
        <li>Obfuscated Files or Information: <a href="/techniques/T1027/001">Binary Padding</a> - Existing technique that became a sub-technique</li>
        <li>Obfuscated Files or Information: <a href="/techniques/T1027/004">Compile After Delivery</a> - Existing technique that became a sub-technique</li>
        <li>Obfuscated Files or Information: <a href="/techniques/T1027/005">Indicator Removal from Tools</a> - Existing technique that became a sub-technique</li>
        <li>Obfuscated Files or Information: <a href="/techniques/T1027/002">Software Packing</a> - Existing technique that became a sub-technique</li>
        <li>Obfuscated Files or Information: <a href="/techniques/T1027/003">Steganography</a> - Broken out from pre-defined behavior within Obfuscated Files or Information</li>
        <li>Office Application Startup: <a href="/techniques/T1137/006">Add-ins</a> - Broken out from pre-defined behavior within Office Application Startup</li>
        <li>Office Application Startup: <a href="/techniques/T1137/001">Office Template Macros</a> - Broken out from pre-defined behavior within Office Application Startup</li>
        <li>Office Application Startup: <a href="/techniques/T1137/002">Office Test</a> - Broken out from pre-defined behavior within Office Application Startup</li>
        <li>Office Application Startup: <a href="/techniques/T1137/003">Outlook Forms</a> - Broken out from pre-defined behavior within Office Application Startup</li>
        <li>Office Application Startup: <a href="/techniques/T1137/004">Outlook Home Page</a> - Broken out from pre-defined behavior within Office Application Startup</li>
        <li>Office Application Startup: <a href="/techniques/T1137/005">Outlook Rules</a> - Broken out from pre-defined behavior within Office Application Startup</li>
        <li>Permission Groups Discovery: <a href="/techniques/T1069/003">Cloud Groups</a> - Broken out from pre-defined behavior within Permission Groups Discovery in a way that has parity with Account Discovery</li>
        <li>Permission Groups Discovery: <a href="/techniques/T1069/002">Domain Groups</a> - Broken out from pre-defined behavior within Permission Groups Discovery in a way that has parity with Account Discovery</li>
        <li>Permission Groups Discovery: <a href="/techniques/T1069/001">Local Groups</a> - Broken out from pre-defined behavior within Permission Groups Discovery in a way that has parity with Account Discovery</li>
        <li><a href="/techniques/T1566">Phishing</a> - Created to consolidate behavior around phishing and spearphishing<ul>
        <li><a href="/techniques/T1566/001">Spearphishing Attachment</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1566/002">Spearphishing Link</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1566/003">Spearphishing via Service</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li><a href="/techniques/T1542">Pre-OS Boot</a> - Created to consolidate behavior around persistence that loads before the OS boots<ul>
        <li><a href="/techniques/T1542/003">Bootkit</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1542/002">Component Firmware</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1542/001">System Firmware</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Process Injection: <a href="/techniques/T1055/004">Asynchronous Procedure Call</a> - Existing technique that became a sub-technique</li>
        <li>Process Injection: <a href="/techniques/T1055/001">Dynamic-link Library Injection</a> - Broken out from pre-defined behavior within Process Injection</li>
        <li>Process Injection: <a href="/techniques/T1055/011">Extra Window Memory Injection</a> - Broken out from pre-defined behavior within Process Injection</li>
        <li>Process Injection: <a href="/techniques/T1055/002">Portable Executable Injection</a> - Broken out from pre-defined behavior within Process Injection</li>
        <li>Process Injection: <a href="/techniques/T1055/009">Proc Memory</a> - Broken out from pre-defined behavior within Process Injection</li>
        <li>Process Injection: <a href="/techniques/T1055/013">Process DoppelgÃ€nging</a> - Existing technique that became a sub-technique</li>
        <li>Process Injection: <a href="/techniques/T1055/012">Process Hollowing</a> - Existing technique that became a sub-technique</li>
        <li>Process Injection: <a href="/techniques/T1055/008">Ptrace System Calls</a> - Broken out from pre-defined behavior within Process Injection</li>
        <li>Process Injection: <a href="/techniques/T1055/003">Thread Execution Hijacking</a> - Broken out from pre-defined behavior within Process Injection</li>
        <li>Process Injection: <a href="/techniques/T1055/005">Thread Local Storage</a> - Broken out from pre-defined behavior within Process Injection</li>
        <li>Process Injection: <a href="/techniques/T1055/014">VDSO Hijacking</a> - Broken out from pre-defined behavior within Process Injection</li>
        <li><a href="/techniques/T1572">Protocol Tunneling</a> - Created to define behavior broken out from the prior Standard Application and Standard Cryptographic Protocol techniques</li>
        <li>Proxy: <a href="/techniques/T1090/004">Domain Fronting</a> - Existing technique that became a sub-technique</li>
        <li>Proxy: <a href="/techniques/T1090/002">External Proxy</a> - Broken out from pre-defined behavior within Connection Proxy</li>
        <li>Proxy: <a href="/techniques/T1090/001">Internal Proxy</a> - Broken out from pre-defined behavior within Connection Proxy</li>
        <li>Proxy: <a href="/techniques/T1090/003">Multi-hop Proxy</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1563">Remote Service Session Hijacking</a> - Created to consolidate behavior related to hijacking existing remote connection sessions<ul>
        <li><a href="/techniques/T1563/002">RDP Hijacking</a> - Broken out from pre-defined behavior within Remote Desktop Protocol</li>
        <li><a href="/techniques/T1563/001">SSH Hijacking</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Remote Services: <a href="/techniques/T1021/003">Distributed Component Object Model</a> - Broken out from pre-defined behavior within Component Object Model and Distributed COM technique</li>
        <li>Remote Services: <a href="/techniques/T1021/001">Remote Desktop Protocol</a> - Existing technique that became a sub-technique</li>
        <li>Remote Services: <a href="/techniques/T1021/002">SMB/Windows Admin Shares</a> - Existing technique that became a sub-technique and was renamed from Windows Admin Shares</li>
        <li>Remote Services: <a href="/techniques/T1021/004">SSH</a> - Broken out from pre-defined behavior within Remote Services technique</li>
        <li>Remote Services: <a href="/techniques/T1021/005">VNC</a> - Broken out from pre-defined behavior within Remote Services technique</li>
        <li>Remote Services: <a href="/techniques/T1021/006">Windows Remote Management</a> - Existing technique that became a sub-technique</li>
        <li>Scheduled Task/Job: <a href="/techniques/T1053/001">At (Linux)</a> - Broken out from pre-defined behavior within prior Local Job Scheduling technique</li>
        <li>Scheduled Task/Job: <a href="/techniques/T1053/002">At (Windows)</a> - Broken out from pre-defined behavior within prior Scheduled Task technique</li>
        <li>Scheduled Task/Job: <a href="/techniques/T1053/003">Cron</a> - Broken out from pre-defined behavior within prior Local Job Scheduling technique</li>
        <li>Scheduled Task/Job: <a href="/techniques/T1053/004">Launchd</a> - Existing technique that became a sub-technique</li>
        <li>Scheduled Task/Job: <a href="/techniques/T1053/005">Scheduled Task</a> - Existing technique that became a sub-technique</li>
        <li>Server Software Component: <a href="/techniques/T1505/001">SQL Stored Procedures</a> - Broken out from pre-defined behavior within Server Software Component technique</li>
        <li>Server Software Component: <a href="/techniques/T1505/002">Transport Agent</a> - Broken out from pre-defined behavior within Server Software Component technique</li>
        <li>Server Software Component: <a href="/techniques/T1505/003">Web Shell</a> - Existing technique that became a sub-technique</li>
        <li>Signed Binary Proxy Execution: <a href="/techniques/T1218/003">CMSTP</a> - Existing technique that became a sub-technique</li>
        <li>Signed Binary Proxy Execution: <a href="/techniques/T1218/001">Compiled HTML File</a> - Existing technique that became a sub-technique</li>
        <li>Signed Binary Proxy Execution: <a href="/techniques/T1218/002">Control Panel</a> - Existing technique that became a sub-technique</li>
        <li>Signed Binary Proxy Execution: <a href="/techniques/T1218/004">InstallUtil</a> - Existing technique that became a sub-technique</li>
        <li>Signed Binary Proxy Execution: <a href="/techniques/T1218/005">Mshta</a> - Existing technique that became a sub-technique</li>
        <li>Signed Binary Proxy Execution: <a href="/techniques/T1218/007">Msiexec</a> - Broken out from pre-defined behavior within Signed Binary Proxy Execution technique</li>
        <li>Signed Binary Proxy Execution: <a href="/techniques/T1218/008">Odbcconf</a> - Broken out from pre-defined behavior within Signed Binary Proxy Execution technique</li>
        <li>Signed Binary Proxy Execution: <a href="/techniques/T1218/009">Regsvcs/Regasm</a> - Existing technique that became a sub-technique</li>
        <li>Signed Binary Proxy Execution: <a href="/techniques/T1218/010">Regsvr32</a> - Existing technique that became a sub-technique</li>
        <li>Signed Binary Proxy Execution: <a href="/techniques/T1218/011">Rundll32</a> - Existing technique that became a sub-technique</li>
        <li>Signed Script Proxy Execution: <a href="/techniques/T1216/001">PubPrn</a> - Existing technique that became a sub-technique</li>
        <li>Software Discovery: <a href="/techniques/T1518/001">Security Software Discovery</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1558">Steal or Forge Kerberos Tickets</a> - Created to consolidate behavior related to Kerberos tickets<ul>
        <li><a href="/techniques/T1558/001">Golden Ticket</a> - Broken out from pre-defined behavior within Pass the Ticket technique</li>
        <li><a href="/techniques/T1558/003">Kerberoasting</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1558/002">Silver Ticket</a> - Broken out from pre-defined behavior within Pass the Ticket technique</li>
        </ul>
        </li>
        <li><a href="/techniques/T1553">Subvert Trust Controls</a> - Created to consolidate behavior related to getting around trust controls<ul>
        <li><a href="/techniques/T1553/002">Code Signing</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1553/001">Gatekeeper Bypass</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1553/004">Install Root Certificate</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1553/003">SIP and Trust Provider Hijacking</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Supply Chain Compromise: <a href="/techniques/T1195/003">Compromise Hardware Supply Chain</a> - Broken out from pre-defined behavior within Supply Chain Compromise</li>
        <li>Supply Chain Compromise: <a href="/techniques/T1195/001">Compromise Software Dependencies and Development Tools</a> - Broken out from pre-defined behavior within Supply Chain Compromise</li>
        <li>Supply Chain Compromise: <a href="/techniques/T1195/002">Compromise Software Supply Chain</a> - Broken out from pre-defined behavior within Supply Chain Compromise</li>
        <li><a href="/techniques/T1569">System Services</a> - Created to consolidate behaviors related to execution of binaries through system services<ul>
        <li><a href="/techniques/T1569/001">Launchctl</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1569/002">Service Execution</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>Traffic Signaling: <a href="/techniques/T1205/001">Port Knocking</a> - Broken out from pre-defined behavior within Traffic Signaling</li>
        <li>Trusted Developer Utilities Proxy Execution: <a href="/techniques/T1127/001">MSBuild</a> - Broken out from pre-defined behavior within Trusted Developer Utilities Proxy Execution</li>
        <li><a href="/techniques/T1552">Unsecured Credentials</a> - Created to consolidate places where unsecured credentials may be kept<ul>
        <li><a href="/techniques/T1552/003">Bash History</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1552/005">Cloud Instance Metadata API</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1552/001">Credentials In Files</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1552/002">Credentials in Registry</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1552/006">Group Policy Preferences</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1552/004">Private Keys</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li><a href="/techniques/T1550">Use Alternate Authentication Material</a> - Created to consolidate behavior related to use of non-password based credential material<ul>
        <li><a href="/techniques/T1550/001">Application Access Token</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1550/002">Pass the Hash</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1550/003">Pass the Ticket</a> - Existing technique that became a sub-technique</li>
        <li><a href="/techniques/T1550/004">Web Session Cookie</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        <li>User Execution: <a href="/techniques/T1204/002">Malicious File</a> - Broken out from pre-defined behavior within User Execution</li>
        <li>User Execution: <a href="/techniques/T1204/001">Malicious Link</a> - Broken out from pre-defined behavior within User Execution</li>
        <li>Valid Accounts: <a href="/techniques/T1078/004">Cloud Accounts</a> - Broken out from pre-defined behavior Valid Accounts in a way that has parity with Create Account</li>
        <li>Valid Accounts: <a href="/techniques/T1078/001">Default Accounts</a> - Broken out from pre-defined behavior within Valid Accounts in a way that has parity with Create Account</li>
        <li>Valid Accounts: <a href="/techniques/T1078/002">Domain Accounts</a> - Broken out from pre-defined behavior within Valid Accounts in a way that has parity with Create Account</li>
        <li>Valid Accounts: <a href="/techniques/T1078/003">Local Accounts</a> - Broken out from pre-defined behavior within Valid Accounts in a way that has parity with Create Account</li>
        <li>Virtualization/Sandbox Evasion: <a href="/techniques/T1497/001">System Checks</a> - Broken out from pre-defined behavior within Virtualization/Sandbox Evasion</li>
        <li>Virtualization/Sandbox Evasion: <a href="/techniques/T1497/003">Time Based Evasion</a> - Broken out from pre-defined behavior within Virtualization/Sandbox Evasion</li>
        <li>Virtualization/Sandbox Evasion: <a href="/techniques/T1497/002">User Activity Based Checks</a> - Broken out from pre-defined behavior within Virtualization/Sandbox Evasion</li>
        <li>Web Service: <a href="/techniques/T1102/002">Bidirectional Communication</a> - Broken out from pre-defined behavior within Web Service</li>
        <li>Web Service: <a href="/techniques/T1102/001">Dead Drop Resolver</a> - Broken out from pre-defined behavior within Web Service</li>
        <li>Web Service: <a href="/techniques/T1102/003">One-Way Communication</a> - Broken out from pre-defined behavior within Web Service</li>
        </ul>
        <p>Technique changes:</p>
        <p>Technique changes are largely due to new sub-techniques being added, name changes, or both.</p>
        <ul>
        <li><a href="/techniques/T1134">Access Token Manipulation</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1087">Account Discovery</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1098">Account Manipulation</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1071">Application Layer Protocol</a> - Name change from Standard Application Layer Protocol and new sub-techniques added</li>
        <li><a href="/techniques/T1010">Application Window Discovery</a> - Fixed technique reference in description</li>
        <li><a href="/techniques/T1020">Automated Exfiltration</a> - Fixed technique reference in description</li>
        <li><a href="/techniques/T1197">BITS Jobs</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1037">Boot or Logon Initialization Scripts</a> - Name change from Logon Scripts and new sub-techniques added</li>
        <li><a href="/techniques/T1176">Browser Extensions</a> - Data sources changed and minor description update</li>
        <li><a href="/techniques/T1110">Brute Force</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1115">Clipboard Data</a> - Minor description update</li>
        <li><a href="/techniques/T1526">Cloud Service Discovery</a> - Minor description update</li>
        <li><a href="/techniques/T1059">Command and Scripting Interpreter</a> - Name change from Command-Line Interface and new sub-techniques added</li>
        <li><a href="/techniques/T1136">Create Account</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1132">Data Encoding</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1001">Data Obfuscation</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1074">Data Staged</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1213">Data from Information Repositories</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1005">Data from Local System</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1039">Data from Network Shared Drive</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1025">Data from Removable Media</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1006">Direct Volume Access</a> - Name change from File System Logical Offsets</li>
        <li><a href="/techniques/T1482">Domain Trust Discovery</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1189">Drive-by Compromise</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1114">Email Collection</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1480">Execution Guardrails</a> - New sub-technique added</li>
        <li><a href="/techniques/T1048">Exfiltration Over Alternative Protocol</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1041">Exfiltration Over C2 Channel</a> - Name change from Exfiltration over Command and Control Channel and added data sources</li>
        <li><a href="/techniques/T1011">Exfiltration Over Other Network Medium</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1052">Exfiltration Over Physical Medium</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1190">Exploit Public-Facing Application</a> - Minor description update</li>
        <li><a href="/techniques/T1203">Exploitation for Client Execution</a> - Minor description update</li>
        <li><a href="/techniques/T1212">Exploitation for Credential Access</a> - Minor description update</li>
        <li><a href="/techniques/T1211">Exploitation for Defense Evasion</a> - Minor description update</li>
        <li><a href="/techniques/T1068">Exploitation for Privilege Escalation</a> - Minor description update</li>
        <li><a href="/techniques/T1210">Exploitation of Remote Services</a> - Minor description update</li>
        <li><a href="/techniques/T1133">External Remote Services</a> - Minor description update</li>
        <li><a href="/techniques/T1083">File and Directory Discovery</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1222">File and Directory Permissions Modification</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1187">Forced Authentication</a> - Minor description update</li>
        <li><a href="/techniques/T1484">Group Policy Modification</a> - Minor description update</li>
        <li><a href="/techniques/T1070">Indicator Removal on Host</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1202">Indirect Command Execution</a> - Minor description update</li>
        <li><a href="/techniques/T1105">Ingress Tool Transfer</a> - Name change from Remote File Copy</li>
        <li><a href="/techniques/T1056">Input Capture</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1036">Masquerading</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1106">Native API</a> - Name change from Execution through API</li>
        <li><a href="/techniques/T1046">Network Service Scanning</a> - Minor description update</li>
        <li><a href="/techniques/T1135">Network Share Discovery</a> - Fixed technique reference in description, added Linux, and minor description update</li>
        <li><a href="/techniques/T1040">Network Sniffing</a> - Minor description update</li>
        <li><a href="/techniques/T1095">Non-Application Layer Protocol</a> - Name change from Standard Non-Application Layer Protocol</li>
        <li><a href="/techniques/T1003">OS Credential Dumping</a> - Name change from Credential Dumping and new sub-techniques added</li>
        <li><a href="/techniques/T1027">Obfuscated Files or Information</a> - Minor description update</li>
        <li><a href="/techniques/T1201">Password Policy Discovery</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1120">Peripheral Device Discovery</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1069">Permission Groups Discovery</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1057">Process Discovery</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1055">Process Injection</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1090">Proxy</a> - Name change from Connection Proxy and new sub-techniques added</li>
        <li><a href="/techniques/T1012">Query Registry</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1219">Remote Access Software</a> - Name change from Remote Access Tools and fixed technique reference in description</li>
        <li><a href="/techniques/T1021">Remote Services</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1018">Remote System Discovery</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1207">Rogue Domain Controller</a> - Name change from DCShadow</li>
        <li><a href="/techniques/T1014">Rootkit</a> - Minor description update</li>
        <li><a href="/techniques/T1053">Scheduled Task/Job</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1029">Scheduled Transfer</a> - Minor description update</li>
        <li><a href="/techniques/T1113">Screen Capture</a> - Minor description update</li>
        <li><a href="/techniques/T1505">Server Software Component</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1129">Shared Modules</a> - Name change from Execution through Module Load</li>
        <li><a href="/techniques/T1218">Signed Binary Proxy Execution</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1216">Signed Script Proxy Execution</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1072">Software Deployment Tools</a> - Minor description update and data source added</li>
        <li><a href="/techniques/T1518">Software Discovery</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1195">Supply Chain Compromise</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1082">System Information Discovery</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1016">System Network Configuration Discovery</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1049">System Network Connections Discovery</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1033">System Owner/User Discovery</a> - Fixed technique reference in description and minor description update</li>
        <li><a href="/techniques/T1124">System Time Discovery</a> - Minor description update</li>
        <li><a href="/techniques/T1080">Taint Shared Content</a> - Minor description update</li>
        <li><a href="/techniques/T1221">Template Injection</a> - Minor description update</li>
        <li><a href="/techniques/T1205">Traffic Signaling</a> - Technique renamed and sub-technique added</li>
        <li><a href="/techniques/T1127">Trusted Developer Utilities Proxy Execution</a> - Minor description update, sub-technique added</li>
        <li><a href="/techniques/T1111">Two-Factor Authentication Interception</a> - Minor description update</li>
        <li><a href="/techniques/T1204">User Execution</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1078">Valid Accounts</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1497">Virtualization/Sandbox Evasion</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1102">Web Service</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1047">Windows Management Instrumentation</a> - Minor description update</li>
        <li><a href="/techniques/T1220">XSL Script Processing</a> - Minor description update</li>
        </ul>
        <p>Minor Technique changes:</p>
        <ul>
        <li><a href="/techniques/T1119">Automated Collection</a></li>
        <li><a href="/techniques/T1217">Browser Bookmark Discovery</a></li>
        <li><a href="/techniques/T1485">Data Destruction</a></li>
        <li><a href="/techniques/T1486">Data Encrypted for Impact</a></li>
        <li><a href="/techniques/T1499">Endpoint Denial of Service</a></li>
        <li><a href="/techniques/T1525">Implant Container Image</a></li>
        <li><a href="/techniques/T1534">Internal Spearphishing</a></li>
        <li><a href="/techniques/T1498">Network Denial of Service</a></li>
        <li><a href="/techniques/T1137">Office Application Startup</a></li>
        <li><a href="/techniques/T1528">Steal Application Access Token</a></li>
        <li><a href="/techniques/T1539">Steal Web Session Cookie</a></li>
        <li><a href="/techniques/T1007">System Service Discovery</a></li>
        <li><a href="/techniques/T1529">System Shutdown/Reboot</a></li>
        <li><a href="/techniques/T1537">Transfer Data to Cloud Account</a></li>
        </ul>
        <p>Technique revocations:</p>
        <ul>
        <li>.bash_profile and .bashrc (revoked by Event Triggered Execution: <a href="/techniques/T1546/004">.bash_profile and .bashrc</a>)</li>
        <li>Accessibility Features (revoked by Event Triggered Execution: <a href="/techniques/T1546/008">Accessibility Features</a>)</li>
        <li>AppCert DLLs (revoked by Event Triggered Execution: <a href="/techniques/T1546/009">AppCert DLLs</a>)</li>
        <li>AppInit DLLs (revoked by Event Triggered Execution: <a href="/techniques/T1546/010">AppInit DLLs</a>)</li>
        <li>AppleScript (revoked by Command and Scripting Interpreter: <a href="/techniques/T1059/002">AppleScript</a>)</li>
        <li>Application Access Token (revoked by Use Alternate Authentication Material: <a href="/techniques/T1550/001">Application Access Token</a>)</li>
        <li>Application Deployment Software (revoked by <a href="/techniques/T1072">Software Deployment Tools</a>)</li>
        <li>Application Shimming (revoked by Event Triggered Execution: <a href="/techniques/T1546/011">Application Shimming</a>)</li>
        <li>Authentication Package (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/002">Authentication Package</a>)</li>
        <li>Bash History (revoked by Unsecured Credentials: <a href="/techniques/T1552/003">Bash History</a>)</li>
        <li>Binary Padding (revoked by Obfuscated Files or Information: <a href="/techniques/T1027/001">Binary Padding</a>)</li>
        <li>Bootkit (revoked by Pre-OS Boot: <a href="/techniques/T1542/003">Bootkit</a>)</li>
        <li>Bypass User Account Control (revoked by Abuse Elevation Control Mechanism: <a href="/techniques/T1548/002">Bypass User Access Control</a>)</li>
        <li>CMSTP (revoked by Signed Binary Proxy Execution: <a href="/techniques/T1218/003">CMSTP</a>)</li>
        <li>Change Default File Association (revoked by Event Triggered Execution: <a href="/techniques/T1546/001">Change Default File Association</a>)</li>
        <li>Clear Command History (revoked by Indicator Removal on Host: <a href="/techniques/T1070/003">Clear Command History</a>)</li>
        <li>Cloud Instance Metadata API (revoked by Unsecured Credentials: <a href="/techniques/T1552/005">Cloud Instance Metadata API</a>)</li>
        <li>Code Signing (revoked by Subvert Trust Controls: <a href="/techniques/T1553/002">Code Signing</a>)</li>
        <li>Compile After Delivery (revoked by Obfuscated Files or Information: <a href="/techniques/T1027/004">Compile After Delivery</a>)</li>
        <li>Compiled HTML File (revoked by Signed Binary Proxy Execution: <a href="/techniques/T1218/001">Compiled HTML File</a>)</li>
        <li>Component Firmware (revoked by Pre-OS Boot: <a href="/techniques/T1542/002/">Component Firmware</a>)</li>
        <li>Component Object Model Hijacking (revoked by Event Triggered Execution: <a href="/techniques/T1546/015">Component Object Model Hijacking</a>)</li>
        <li>Control Panel Items (revoked by Signed Binary Proxy Execution: <a href="/techniques/T1218/002">Control Panel</a>)</li>
        <li>Credentials from Web Browsers (revoked by Credentials from Password Stores: <a href="/techniques/T1555/003">Credentials from Web Browsers</a>)</li>
        <li>Credentials in Files (revoked by Unsecured Credentials: <a href="/techniques/T1552/001">Credentials In Files</a>)</li>
        <li>Credentials in Registry (revoked by Unsecured Credentials: <a href="/techniques/T1552/002">Credentials in Registry</a>)</li>
        <li>Custom Command and Control Protocol (revoked by <a href="/techniques/T1095">Non-Application Layer Protocol</a>)</li>
        <li>Custom Cryptographic Protocol (revoked by <a href="/techniques/T1573">Encrypted Channel</a>)</li>
        <li>DLL Search Order Hijacking (revoked by Hijack Execution Flow: <a href="/techniques/T1574/001">DLL Search Order Hijacking</a>)</li>
        <li>DLL Side-Loading (revoked by Hijack Execution Flow: <a href="/techniques/T1574/002">DLL Side-Loading</a>)</li>
        <li>Data Compressed (revoked by <a href="/techniques/T1560">Archive Collected Data</a>)</li>
        <li>Data Encrypted (revoked by <a href="/techniques/T1560">Archive Collected Data</a>)</li>
        <li>Disabling Security Tools (revoked by Impair Defenses: <a href="/techniques/T1562/001">Disable or Modify Tools</a>)</li>
        <li>Disk Content Wipe (revoked by Disk Wipe: <a href="/techniques/T1561/001">Disk Content Wipe</a>)</li>
        <li>Disk Structure Wipe (revoked by Disk Wipe: <a href="/techniques/T1561/002">Disk Structure Wipe</a>)</li>
        <li>Domain Fronting (revoked by Proxy: <a href="/techniques/T1090/004">Domain Fronting</a>)</li>
        <li>Domain Generation Algorithms (revoked by Dynamic Resolution: <a href="/techniques/T1568/002">Domain Generation Algorithms</a>)</li>
        <li>Dylib Hijacking (revoked by Hijack Execution Flow: <a href="/techniques/T1574/004">Dylib Hijacking</a>)</li>
        <li>Dynamic Data Exchange (revoked by Inter-Process Communication: <a href="/techniques/T1559/002">Dynamic Data Exchange</a>)</li>
        <li>Elevated Execution with Prompt (revoked by Abuse Elevation Control Mechanism: <a href="/techniques/T1548/004">Elevated Execution with Prompt</a>)</li>
        <li>Emond (revoked by Event Triggered Execution: <a href="/techniques/T1546/014">Emond</a>)</li>
        <li>Extra Window Memory Injection (revoked by Process Injection: <a href="/techniques/T1055/011">Extra Window Memory Injection</a>)</li>
        <li>File Deletion (revoked by Indicator Removal on Host: <a href="/techniques/T1070/004">File Deletion</a>)</li>
        <li>File System Permissions Weakness (revoked by Hijack Execution Flow: <a href="/techniques/T1574/010">Services File Permissions Weakness</a>)</li>
        <li>Gatekeeper Bypass (revoked by Subvert Trust Controls: <a href="/techniques/T1553/001">Gatekeeper Bypass</a>)</li>
        <li>HISTCONTROL (revoked by Impair Defenses: <a href="/techniques/T1562/003">HISTCONTROL</a>)</li>
        <li>Hidden Files and Directories (revoked by Hide Artifacts: <a href="/techniques/T1564/001">Hidden Files and Directories</a>)</li>
        <li>Hidden Users (revoked by Hide Artifacts: <a href="/techniques/T1564/002">Hidden Users</a>)</li>
        <li>Hidden Window (revoked by Hide Artifacts: <a href="/techniques/T1564/003">Hidden Window</a>)</li>
        <li>Hooking (revoked by Input Capture: <a href="/techniques/T1056/004">Credential API Hooking</a>)</li>
        <li>Image File Execution Options Injection (revoked by Event Triggered Execution: <a href="/techniques/T1546/012">Image File Execution Options Injection</a>)</li>
        <li>Indicator Blocking (revoked by Impair Defenses: <a href="/techniques/T1562/006">Indicator Blocking</a>)</li>
        <li>Indicator Removal from Tools (revoked by Obfuscated Files or Information: <a href="/techniques/T1027/005">Indicator Removal from Tools</a>)</li>
        <li>Input Prompt (revoked by Input Capture: <a href="/techniques/T1056/002">GUI Input Capture</a>)</li>
        <li>Install Root Certificate (revoked by Subvert Trust Controls: <a href="/techniques/T1553/004">Install Root Certificate</a>)</li>
        <li>InstallUtil (revoked by Signed Binary Proxy Execution: <a href="/techniques/T1218/004">InstallUtil</a>)</li>
        <li>Kerberoasting (revoked by Steal or Forge Kerberos Tickets: <a href="/techniques/T1558/003">Kerberoasting</a>)</li>
        <li>Kernel Modules and Extensions (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/006">Kernel Modules and Extensions</a>)</li>
        <li>Keychain (revoked by Credentials from Password Stores: <a href="/techniques/T1555/001">Keychain</a>)</li>
        <li>LC_LOAD_DYLIB Addition (revoked by Event Triggered Execution: <a href="/techniques/T1546/006">LC_LOAD_DYLIB Addition</a>)</li>
        <li>LLMNR/NBT-NS Poisoning and Relay (revoked by Man-in-the-Middle: <a href="/techniques/T1557/001">LLMNR/NBT-NS Poisoning and SMB Relay</a>)</li>
        <li>LSASS Driver (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/008">LSASS Driver</a>)</li>
        <li>Launch Agent (revoked by Create or Modify System Process: <a href="/techniques/T1543/001">Launch Agent</a>)</li>
        <li>Launch Daemon (revoked by Create or Modify System Process: <a href="/techniques/T1543/004">Launch Daemon</a>)</li>
        <li>Launchctl (revoked by System Services: <a href="/techniques/T1569/001">Launchctl</a>)</li>
        <li>Local Job Scheduling (revoked by <a href="/techniques/T1053">Scheduled Task/Job</a>)</li>
        <li>Login Item (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/011">Plist Modification</a>)</li>
        <li>Modify Existing Service (revoked by Create or Modify System Process: <a href="/techniques/T1543/003">Windows Service</a>)</li>
        <li>Mshta (revoked by Signed Binary Proxy Execution: <a href="/techniques/T1218/005">Mshta</a>)</li>
        <li>Multi-hop Proxy (revoked by Proxy: <a href="/techniques/T1090/003">Multi-hop Proxy</a>)</li>
        <li>Multilayer Encryption (revoked by <a href="/techniques/T1573">Encrypted Channel</a>)</li>
        <li>NTFS File Attributes (revoked by Hide Artifacts: <a href="/techniques/T1564/004">NTFS File Attributes</a>)</li>
        <li>Netsh Helper DLL (revoked by Event Triggered Execution: <a href="/techniques/T1546/007">Netsh Helper DLL</a>)</li>
        <li>Network Share Connection Removal (revoked by Indicator Removal on Host: <a href="/techniques/T1070/005">Network Share Connection Removal</a>)</li>
        <li>New Service (revoked by Create or Modify System Process: <a href="/techniques/T1543/003">Windows Service</a>)</li>
        <li>Parent PID Spoofing (revoked by Access Token Manipulation: <a href="/techniques/T1134/004">Parent PID Spoofing</a>)</li>
        <li>Pass the Hash (revoked by Use Alternate Authentication Material: <a href="/techniques/T1550/002">Pass the Hash</a>)</li>
        <li>Pass the Ticket (revoked by Use Alternate Authentication Material: <a href="/techniques/T1550/003">Pass the Ticket</a>)</li>
        <li>Password Filter DLL (revoked by Modify Authentication Process: <a href="/techniques/T1556/002">Password Filter DLL</a>)</li>
        <li>Plist Modification (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/011">Plist Modification</a>)</li>
        <li>Port Monitors (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/010">Port Monitors</a>)</li>
        <li>PowerShell (revoked by Command and Scripting Interpreter: <a href="/techniques/T1059/001">PowerShell</a>)</li>
        <li>PowerShell Profile (revoked by Event Triggered Execution: <a href="/techniques/T1546/013">PowerShell Profile</a>)</li>
        <li>Private Keys (revoked by Unsecured Credentials: <a href="/techniques/T1552/004">Private Keys</a>)</li>
        <li>Process DoppelgÃ€nging (revoked by Process Injection: <a href="/techniques/T1055/013">Process DoppelgÃ€nging</a>)</li>
        <li>Process Hollowing (revoked by Process Injection: <a href="/techniques/T1055/012">Process Hollowing</a>)</li>
        <li>Rc.common (revoked by Boot or Logon Initialization Scripts: <a href="/techniques/T1037/004">Rc.common</a>)</li>
        <li>Re-opened Applications (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/007">Re-opened Applications</a>)</li>
        <li>Registry Run Keys / Startup Folder (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/001">Registry Run Keys / Startup Folder</a>)</li>
        <li>Regsvcs/Regasm (revoked by Signed Binary Proxy Execution: <a href="/techniques/T1218/009">Regsvcs/Regasm</a>)</li>
        <li>Regsvr32 (revoked by Signed Binary Proxy Execution: <a href="/techniques/T1218/010">Regsvr32</a>)</li>
        <li>Remote Desktop Protocol (revoked by Remote Services: <a href="/techniques/T1021/001">Remote Desktop Protocol</a>)</li>
        <li>Revert Cloud Instance (revoked by Modify Cloud Compute Infrastructure: <a href="/techniques/T1578/004">Revert Cloud Instance</a>)</li>
        <li>Rundll32 (revoked by Signed Binary Proxy Execution: <a href="/techniques/T1218/011">Rundll32</a>)</li>
        <li>Runtime Data Manipulation (revoked by Data Manipulation: <a href="/techniques/T1565/003">Runtime Data Manipulation</a>)</li>
        <li>SID-History Injection (revoked by Access Token Manipulation: <a href="/techniques/T1134/005">SID-History Injection</a>)</li>
        <li>SIP and Trust Provider Hijacking (revoked by Subvert Trust Controls: <a href="/techniques/T1553/003">SIP and Trust Provider Hijacking</a>)</li>
        <li>SSH Hijacking (revoked by Remote Service Session Hijacking: <a href="/techniques/T1563/001">SSH Hijacking</a>)</li>
        <li>Screensaver (revoked by Event Triggered Execution: <a href="/techniques/T1546/002">Screensaver</a>)</li>
        <li>Security Software Discovery (revoked by Software Discovery: <a href="/techniques/T1518/001">Security Software Discovery</a>)</li>
        <li>Security Support Provider (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/005">Security Support Provider</a>)</li>
        <li>Securityd Memory (revoked by Credentials from Password Stores: <a href="/techniques/T1555/002">Securityd Memory</a>)</li>
        <li>Service Execution (revoked by System Services: <a href="/techniques/T1569/002">Service Execution</a>)</li>
        <li>Service Registry Permissions Weakness (revoked by Hijack Execution Flow: <a href="/techniques/T1574/011">Services Registry Permissions Weakness</a>)</li>
        <li>Setuid and Setgid (revoked by Abuse Elevation Control Mechanism: <a href="/techniques/T1548/001">Setuid and Setgid</a>)</li>
        <li>Shortcut Modification (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/009">Shortcut Modification</a>)</li>
        <li>Software Packing (revoked by Obfuscated Files or Information: <a href="/techniques/T1027/002">Software Packing</a>)</li>
        <li>Space after Filename (revoked by Masquerading: <a href="/techniques/T1036/006">Space after Filename</a>)</li>
        <li>Spearphishing Attachment (revoked by Phishing: <a href="/techniques/T1566/001">Spearphishing Attachment</a>)</li>
        <li>Spearphishing Link (revoked by Phishing: <a href="/techniques/T1566/002">Spearphishing Link</a>)</li>
        <li>Spearphishing via Service (revoked by Phishing: <a href="/techniques/T1566/003">Spearphishing via Service</a>)</li>
        <li>Standard Cryptographic Protocol (revoked by <a href="/techniques/T1573">Encrypted Channel</a>)</li>
        <li>Startup Items (revoked by Boot or Logon Initialization Scripts: <a href="/techniques/T1037/005">Startup Items</a>)</li>
        <li>Stored Data Manipulation (revoked by Data Manipulation: <a href="/techniques/T1565/001">Stored Data Manipulation</a>)</li>
        <li>Sudo (revoked by Abuse Elevation Control Mechanism: <a href="/techniques/T1548/003">Sudo and Sudo Caching</a>)</li>
        <li>Sudo Caching (revoked by Abuse Elevation Control Mechanism: <a href="/techniques/T1548/003">Sudo and Sudo Caching</a>)</li>
        <li>System Firmware (revoked by Pre-OS Boot: <a href="/techniques/T1542/001">System Firmware</a>)</li>
        <li>Systemd Service (revoked by Create or Modify System Process: <a href="/techniques/T1543/002">Systemd Service</a>)</li>
        <li>Time Providers (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/003">Time Providers</a>)</li>
        <li>Timestomp (revoked by Indicator Removal on Host: <a href="/techniques/T1070/006">Timestomp</a>)</li>
        <li>Transmitted Data Manipulation (revoked by Data Manipulation: <a href="/techniques/T1565/002">Transmitted Data Manipulation</a>)</li>
        <li>Trap (revoked by Event Triggered Execution: <a href="/techniques/T1546/005">Trap</a>)</li>
        <li>Uncommonly Used Port (revoked by <a href="/techniques/T1571">Non-Standard Port</a>)</li>
        <li>Web Session Cookie (revoked by Use Alternate Authentication Material: <a href="/techniques/T1550/004">Web Session Cookie</a>)</li>
        <li>Web Shell (revoked by Server Software Component: <a href="/techniques/T1505/003">Web Shell</a>)</li>
        <li>Windows Admin Shares (revoked by Remote Services: <a href="/techniques/T1021/002">SMB/Windows Admin Shares</a>)</li>
        <li>Windows Management Instrumentation Event Subscription (revoked by Event Triggered Execution: <a href="/techniques/T1546/003">Windows Management Instrumentation Event Subscription</a>)</li>
        <li>Windows Remote Management (revoked by Remote Services: <a href="/techniques/T1021/006">Windows Remote Management</a>)</li>
        <li>Winlogon Helper DLL (revoked by Boot or Logon Autostart Execution: <a href="/techniques/T1547/004">Winlogon Helper DLL</a>)</li>
        </ul>
        <p>Technique deprecations:</p>
        <ul>
        <li><a href="/techniques/T1043">Commonly Used Port</a> - Deprecated from ATT&amp;CK because the behavior is redundant and describes most benign network communications.</li>
        <li><a href="/techniques/T1175">Component Object Model and Distributed COM</a> - Deprecated and split into separate Component Object Model and Distributed Component Object Model sub-techniques. Existing Group/Software procedure examples were remapped appropriately</li>
        <li><a href="/techniques/T1061">Graphical User Interface</a> - Deprecated from ATT&amp;CK because the behavior is redundant and implied by use of remote desktop tools like Remote Desktop Protocol. Existing Group/Software procedure examples were remapped appropriately</li>
        <li><a href="/techniques/T1062">Hypervisor</a> - Deprecated from ATT&amp;CK due to lack of in the wild use</li>
        <li><a href="/techniques/T1149">LC_MAIN Hijacking</a> - Deprecated from ATT&amp;CK due to lack of in the wild use</li>
        <li><a href="/techniques/T1026">Multiband Communication</a> - Deprecated from ATT&amp;CK due to lack of in the wild use. Existing Group/Software procedure examples did not fit the core idea behind the technique</li>
        <li><a href="/techniques/T1034">Path Interception</a> - Deprecated and split into separate Unquoted Path, PATH Environment Variable, and Search Order Hijacking sub-techniques. Existing Group/Software procedure examples were remapped appropriately</li>
        <li><a href="/techniques/T1108">Redundant Access</a> - Deprecated from ATT&amp;CK because the behavior is too high level and is sufficiently covered by Valid Accounts and External Remote Services. Existing Group/Software procedure examples were remapped appropriately</li>
        <li><a href="/techniques/T1064">Scripting</a> - Deprecated and split into separate Unix Shell, Visual Basic, JavaScript/Jscript, and Python sub-techniques of Command and Scripting Interpreter. Existing Group/Software procedure examples were remapped appropriately</li>
        <li><a href="/techniques/T1051">Shared Webroot</a> - Deprecated from ATT&amp;CK due to lack of in the wild use</li>
        <li><a href="/techniques/T1153">Source</a> - Deprecated from ATT&amp;CK due to lack of in the wild use</li>
        </ul>
        <p><strong>PRE-ATT&amp;CK</strong></p>
        <p>New Techniques:
        No changes</p>
        <p>Technique changes:
        No changes</p>
        <p>Minor Technique changes:
        No changes</p>
        <p>Technique revocations:
        No changes</p>
        <p>Technique deprecations:</p>
        <ul>
        <li>DNSCalc</li>
        <li>Fast Flux DNS</li>
        </ul>
        <p><strong>Mobile</strong></p>
        <p>
            View mobile technique updates in the ATT&CK Navigator <a href="https://mitre-attack.github.io/attack-navigator/mobile/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fattack-navigator%2Fmaster%2Flayers%2Fdata%2Fupdate_layers%2FJuly_2020%2FJuly_2020_mobile_attack.json" target="_blank">here</a>.
        </p>
        <p>New Techniques:</p>
        <ul>
        <li><a href="/techniques/T1540">Code Injection</a></li>
        <li><a href="/techniques/T1577">Compromise Application Executable</a></li>
        <li><a href="/techniques/T1541">Foreground Persistence</a></li>
        <li><a href="/techniques/T1579">Keychain</a></li>
        <li><a href="/techniques/T1575">Native Code</a></li>
        <li><a href="/techniques/T1544">Remote File Copy</a></li>
        <li><a href="/techniques/T1576">Uninstall Malicious Application</a></li>
        </ul>
        <p>Technique changes:</p>
        <ul>
        <li><a href="/techniques/T1402">Broadcast Receivers</a></li>
        <li><a href="/techniques/T1448">Carrier Billing Fraud</a></li>
        <li><a href="/techniques/T1417">Input Capture</a></li>
        <li><a href="/techniques/T1516">Input Injection</a></li>
        <li><a href="/techniques/T1411">Input Prompt</a></li>
        <li><a href="/techniques/T1444">Masquerade as Legitimate Application</a></li>
        <li><a href="/techniques/T1513">Screen Capture</a></li>
        <li><a href="/techniques/T1508">Suppress Application Icon</a></li>
        <li><a href="/techniques/T1422">System Network Configuration Discovery</a></li>
        </ul>
        <p>Minor Technique changes:</p>
        <ul>
        <li><a href="/techniques/T1517">Access Notifications</a></li>
        <li><a href="/techniques/T1510">Clipboard Modification</a></li>
        <li><a href="/techniques/T1476">Deliver Malicious App via Other Means</a></li>
        <li><a href="/techniques/T1426">System Information Discovery</a></li>
        </ul>
        <p>Technique revocations:
        No changes</p>
        <p>Technique deprecations:
        No changes</p>
        <h3>Software</h3>
        <p><strong>Enterprise</strong></p>
        <p>New Software:</p>
        <ul>
        <li><a href="/software/S0469">ABK</a></li>
        <li><a href="/software/S0456">Aria-body</a></li>
        <li><a href="/software/S0438">Attor</a></li>
        <li><a href="/software/S0473">Avenger</a></li>
        <li><a href="/software/S0470">BBK</a></li>
        <li><a href="/software/S0475">BackConfig</a></li>
        <li><a href="/software/S0482">Bundlore</a></li>
        <li><a href="/software/S0465">CARROTBALL</a></li>
        <li><a href="/software/S0462">CARROTBAT</a></li>
        <li><a href="/software/S0454">Cadelspy</a></li>
        <li><a href="/software/S0460">Get2</a></li>
        <li><a href="/software/S0477">Goopy</a></li>
        <li><a href="/software/S0431">HotCroissant</a></li>
        <li><a href="/software/S0434">Imminent Monitor</a></li>
        <li><a href="/software/S0437">Kivars</a></li>
        <li><a href="/software/S0447">Lokibot</a></li>
        <li><a href="/software/S0451">LoudMiner</a></li>
        <li><a href="/software/S0449">MAZE</a></li>
        <li><a href="/software/S0443">MESSAGETAP</a></li>
        <li><a href="/software/S0459">MechaFlounder</a></li>
        <li><a href="/software/S0455">Metamorfo</a></li>
        <li><a href="/software/S0457">Netwalker</a></li>
        <li><a href="/software/S0439">Okrum</a></li>
        <li><a href="/software/S0435">PLEAD</a></li>
        <li><a href="/software/S0428">PoetRAT</a></li>
        <li><a href="/software/S0453">Pony</a></li>
        <li><a href="/software/S0441">PowerShower</a></li>
        <li><a href="/software/S0481">Ragnar Locker</a></li>
        <li><a href="/software/S0458">Ramsay</a></li>
        <li><a href="/software/S0433">Rifdoor</a></li>
        <li><a href="/software/S0448">Rising Sun</a></li>
        <li><a href="/software/S0446">Ryuk</a></li>
        <li><a href="/software/S0461">SDBot</a></li>
        <li><a href="/software/S0450">SHARPSTATS</a></li>
        <li><a href="/software/S0464">SYSCON</a></li>
        <li><a href="/software/S0444">ShimRat</a></li>
        <li><a href="/software/S0445">ShimRatReporter</a></li>
        <li><a href="/software/S0468">Skidmap</a></li>
        <li><a href="/software/S0436">TSCookie</a></li>
        <li><a href="/software/S0467">TajMahal</a></li>
        <li><a href="/software/S0452">USBferry</a></li>
        <li><a href="/software/S0442">VBShower</a></li>
        <li><a href="/software/S0476">Valak</a></li>
        <li><a href="/software/S0466">WindTail</a></li>
        <li><a href="/software/S0430">Winnti for Linux</a></li>
        <li><a href="/software/S0471">build_downer</a></li>
        <li><a href="/software/S0472">down_new</a></li>
        </ul>
        <p>Software changes:</p>
        <ul>
        <li><a href="/software/S0066">3PARA RAT</a></li>
        <li><a href="/software/S0065">4H RAT</a></li>
        <li><a href="/software/S0045">ADVSTORESHELL</a></li>
        <li><a href="/software/S0073">ASPXSpy</a></li>
        <li><a href="/software/S0331">Agent Tesla</a></li>
        <li><a href="/software/S0092">Agent.btz</a></li>
        <li><a href="/software/S0373">Astaroth</a></li>
        <li><a href="/software/S0347">AuditCred</a></li>
        <li><a href="/software/S0129">AutoIt backdoor</a></li>
        <li><a href="/software/S0344">Azorult</a></li>
        <li><a href="/software/S0031">BACKSPACE</a></li>
        <li><a href="/software/S0245">BADCALL</a></li>
        <li><a href="/software/S0128">BADNEWS</a></li>
        <li><a href="/software/S0127">BBSRAT</a></li>
        <li><a href="/software/S0017">BISCUIT</a></li>
        <li><a href="/software/S0190">BITSAdmin</a></li>
        <li><a href="/software/S0069">BLACKCOFFEE</a></li>
        <li><a href="/software/S0360">BONDUPDATER</a></li>
        <li><a href="/software/S0114">BOOTRASH</a></li>
        <li><a href="/software/S0014">BS2005</a></li>
        <li><a href="/software/S0043">BUBBLEWRAP</a></li>
        <li><a href="/software/S0414">BabyShark</a></li>
        <li><a href="/software/S0093">Backdoor.Oldrea</a></li>
        <li><a href="/software/S0337">BadPatch</a></li>
        <li><a href="/software/S0234">Bandook</a></li>
        <li><a href="/software/S0239">Bankshot</a></li>
        <li><a href="/software/S0268">Bisonal</a></li>
        <li><a href="/software/S0089">BlackEnergy</a></li>
        <li><a href="/software/S0252">Brave Prince</a></li>
        <li><a href="/software/S0025">CALENDAR</a></li>
        <li><a href="/software/S0222">CCBkdr</a></li>
        <li><a href="/software/S0023">CHOPSTICK</a></li>
        <li><a href="/software/S0212">CORALDECK</a></li>
        <li><a href="/software/S0137">CORESHELL</a></li>
        <li><a href="/software/S0119">Cachedump</a></li>
        <li><a href="/software/S0274">Calisto</a></li>
        <li><a href="/software/S0077">CallMe</a></li>
        <li><a href="/software/S0351">Cannon</a></li>
        <li><a href="/software/S0030">Carbanak</a></li>
        <li><a href="/software/S0335">Carbon</a></li>
        <li><a href="/software/S0348">Cardinal RAT</a></li>
        <li><a href="/software/S0261">Catchamas</a></li>
        <li><a href="/software/S0144">ChChes</a></li>
        <li><a href="/software/S0220">Chaos</a></li>
        <li><a href="/software/S0107">Cherry Picker</a></li>
        <li><a href="/software/S0020">China Chopper</a></li>
        <li><a href="/software/S0054">CloudDuke</a></li>
        <li><a href="/software/S0154">Cobalt Strike</a></li>
        <li><a href="/software/S0338">Cobian RAT</a></li>
        <li><a href="/software/S0369">CoinTicker</a></li>
        <li><a href="/software/S0126">ComRAT</a></li>
        <li><a href="/software/S0244">Comnie</a></li>
        <li><a href="/software/S0050">CosmicDuke</a></li>
        <li><a href="/software/S0046">CozyCar</a></li>
        <li><a href="/software/S0115">Crimson</a></li>
        <li><a href="/software/S0235">CrossRAT</a></li>
        <li><a href="/software/S0213">DOGCALL</a></li>
        <li><a href="/software/S0334">DarkComet</a></li>
        <li><a href="/software/S0187">Daserf</a></li>
        <li><a href="/software/S0243">DealersChoice</a></li>
        <li><a href="/software/S0354">Denis</a></li>
        <li><a href="/software/S0021">Derusbi</a></li>
        <li><a href="/software/S0200">Dipsind</a></li>
        <li><a href="/software/S0281">Dok</a></li>
        <li><a href="/software/S0186">DownPaper</a></li>
        <li><a href="/software/S0134">Downdelph</a></li>
        <li><a href="/software/S0384">Dridex</a></li>
        <li><a href="/software/S0038">Duqu</a></li>
        <li><a href="/software/S0062">DustySky</a></li>
        <li><a href="/software/S0024">Dyre</a></li>
        <li><a href="/software/S0064">ELMER</a></li>
        <li><a href="/software/S0377">Ebury</a></li>
        <li><a href="/software/S0081">Elise</a></li>
        <li><a href="/software/S0082">Emissary</a></li>
        <li><a href="/software/S0367">Emotet</a></li>
        <li><a href="/software/S0363">Empire</a></li>
        <li><a href="/software/S0091">Epic</a></li>
        <li><a href="/software/S0396">EvilBunny</a></li>
        <li><a href="/software/S0152">EvilGrab</a></li>
        <li><a href="/software/S0401">Exaramel for Linux</a></li>
        <li><a href="/software/S0343">Exaramel for Windows</a></li>
        <li><a href="/software/S0361">Expand</a></li>
        <li><a href="/software/S0181">FALLCHILL</a></li>
        <li><a href="/software/S0267">FELIXROOT</a></li>
        <li><a href="/software/S0036">FLASHFLOOD</a></li>
        <li><a href="/software/S0173">FLIPSIDE</a></li>
        <li><a href="/software/S0095">FTP</a></li>
        <li><a href="/software/S0076">FakeM</a></li>
        <li><a href="/software/S0171">Felismus</a></li>
        <li><a href="/software/S0120">Fgdump</a></li>
        <li><a href="/software/S0182">FinFisher</a></li>
        <li><a href="/software/S0355">Final1stspy</a></li>
        <li><a href="/software/S0143">Flame</a></li>
        <li><a href="/software/S0381">FlawedAmmyy</a></li>
        <li><a href="/software/S0277">FruitFly</a></li>
        <li><a href="/software/S0410">Fysbis</a></li>
        <li><a href="/software/S0026">GLOOXMAIL</a></li>
        <li><a href="/software/S0417">GRIFFON</a></li>
        <li><a href="/software/S0168">Gazer</a></li>
        <li><a href="/software/S0049">GeminiDuke</a></li>
        <li><a href="/software/S0249">Gold Dragon</a></li>
        <li><a href="/software/S0237">GravityRAT</a></li>
        <li><a href="/software/S0342">GreyEnergy</a></li>
        <li><a href="/software/S0132">H1N1</a></li>
        <li><a href="/software/S0037">HAMMERTOSS</a></li>
        <li><a href="/software/S0246">HARDRAIN</a></li>
        <li><a href="/software/S0391">HAWKBALL</a></li>
        <li><a href="/software/S0135">HIDEDRV</a></li>
        <li><a href="/software/S0232">HOMEFRY</a></li>
        <li><a href="/software/S0376">HOPLIGHT</a></li>
        <li><a href="/software/S0070">HTTPBrowser</a></li>
        <li><a href="/software/S0047">Hacking Team UEFI Rootkit</a></li>
        <li><a href="/software/S0170">Helminth</a></li>
        <li><a href="/software/S0087">Hi-Zor</a></li>
        <li><a href="/software/S0394">HiddenWasp</a></li>
        <li><a href="/software/S0009">Hikit</a></li>
        <li><a href="/software/S0203">Hydraq</a></li>
        <li><a href="/software/S0398">HyperBro</a></li>
        <li><a href="/software/S0189">ISMInjector</a></li>
        <li><a href="/software/S0357">Impacket</a></li>
        <li><a href="/software/S0259">InnaputRAT</a></li>
        <li><a href="/software/S0260">InvisiMole</a></li>
        <li><a href="/software/S0015">Ixeshe</a></li>
        <li><a href="/software/S0389">JCry</a></li>
        <li><a href="/software/S0044">JHUHUGIT</a></li>
        <li><a href="/software/S0201">JPIN</a></li>
        <li><a href="/software/S0163">Janicab</a></li>
        <li><a href="/software/S0215">KARAE</a></li>
        <li><a href="/software/S0271">KEYMARBLE</a></li>
        <li><a href="/software/S0156">KOMPROGO</a></li>
        <li><a href="/software/S0356">KONNI</a></li>
        <li><a href="/software/S0088">Kasidet</a></li>
        <li><a href="/software/S0265">Kazuar</a></li>
        <li><a href="/software/S0387">KeyBoy</a></li>
        <li><a href="/software/S0276">Keydnap</a></li>
        <li><a href="/software/S0250">Koadic</a></li>
        <li><a href="/software/S0162">Komplex</a></li>
        <li><a href="/software/S0236">Kwampirs</a></li>
        <li><a href="/software/S0042">LOWBALL</a></li>
        <li><a href="/software/S0349">LaZagne</a></li>
        <li><a href="/software/S0395">LightNeuron</a></li>
        <li><a href="/software/S0211">Linfo</a></li>
        <li><a href="/software/S0362">Linux Rabbit</a></li>
        <li><a href="/software/S0397">LoJax</a></li>
        <li><a href="/software/S0372">LockerGoga</a></li>
        <li><a href="/software/S0121">Lslsass</a></li>
        <li><a href="/software/S0010">Lurid</a></li>
        <li><a href="/software/S0233">MURKYTOP</a></li>
        <li><a href="/software/S0282">MacSpy</a></li>
        <li><a href="/software/S0409">Machete</a></li>
        <li><a href="/software/S0413">MailSniper</a></li>
        <li><a href="/software/S0167">Matroyshka</a></li>
        <li><a href="/software/S0339">Micropsia</a></li>
        <li><a href="/software/S0179">MimiPenguin</a></li>
        <li><a href="/software/S0002">Mimikatz</a></li>
        <li><a href="/software/S0051">MiniDuke</a></li>
        <li><a href="/software/S0280">MirageFox</a></li>
        <li><a href="/software/S0084">Mis-Type</a></li>
        <li><a href="/software/S0083">Misdat</a></li>
        <li><a href="/software/S0080">Mivast</a></li>
        <li><a href="/software/S0149">MoonWind</a></li>
        <li><a href="/software/S0284">More_eggs</a></li>
        <li><a href="/software/S0256">Mosquito</a></li>
        <li><a href="/software/S0272">NDiskMonitor</a></li>
        <li><a href="/software/S0034">NETEAGLE</a></li>
        <li><a href="/software/S0198">NETWIRE</a></li>
        <li><a href="/software/S0353">NOKKI</a></li>
        <li><a href="/software/S0228">NanHaiShu</a></li>
        <li><a href="/software/S0336">NanoCore</a></li>
        <li><a href="/software/S0247">NavRAT</a></li>
        <li><a href="/software/S0039">Net</a></li>
        <li><a href="/software/S0056">Net Crawler</a></li>
        <li><a href="/software/S0033">NetTraveler</a></li>
        <li><a href="/software/S0118">Nidiran</a></li>
        <li><a href="/software/S0368">NotPetya</a></li>
        <li><a href="/software/S0138">OLDBAIT</a></li>
        <li><a href="/software/S0165">OSInfo</a></li>
        <li><a href="/software/S0402">OSX/Shlayer</a></li>
        <li><a href="/software/S0352">OSX_OCEANLOTUS.D</a></li>
        <li><a href="/software/S0346">OceanSalt</a></li>
        <li><a href="/software/S0340">Octopus</a></li>
        <li><a href="/software/S0365">Olympic Destroyer</a></li>
        <li><a href="/software/S0052">OnionDuke</a></li>
        <li><a href="/software/S0264">OopsIE</a></li>
        <li><a href="/software/S0229">Orz</a></li>
        <li><a href="/software/S0072">OwaAuth</a></li>
        <li><a href="/software/S0016">P2P ZeuS</a></li>
        <li><a href="/software/S0158">PHOREAL</a></li>
        <li><a href="/software/S0254">PLAINTEE</a></li>
        <li><a href="/software/S0216">POORAIM</a></li>
        <li><a href="/software/S0150">POSHSPY</a></li>
        <li><a href="/software/S0145">POWERSOURCE</a></li>
        <li><a href="/software/S0223">POWERSTATS</a></li>
        <li><a href="/software/S0371">POWERTON</a></li>
        <li><a href="/software/S0184">POWRUNER</a></li>
        <li><a href="/software/S0196">PUNCHBUGGY</a></li>
        <li><a href="/software/S0197">PUNCHTRACK</a></li>
        <li><a href="/software/S0208">Pasam</a></li>
        <li><a href="/software/S0048">PinchDuke</a></li>
        <li><a href="/software/S0124">Pisloader</a></li>
        <li><a href="/software/S0013">PlugX</a></li>
        <li><a href="/software/S0012">PoisonIvy</a></li>
        <li><a href="/software/S0378">PoshC2</a></li>
        <li><a href="/software/S0139">PowerDuke</a></li>
        <li><a href="/software/S0194">PowerSploit</a></li>
        <li><a href="/software/S0393">PowerStallion</a></li>
        <li><a href="/software/S0113">Prikormka</a></li>
        <li><a href="/software/S0279">Proton</a></li>
        <li><a href="/software/S0238">Proxysvc</a></li>
        <li><a href="/software/S0029">PsExec</a></li>
        <li><a href="/software/S0078">Psylo</a></li>
        <li><a href="/software/S0147">Pteranodon</a></li>
        <li><a href="/software/S0192">Pupy</a></li>
        <li><a href="/software/S0269">QUADAGENT</a></li>
        <li><a href="/software/S0262">QuasarRAT</a></li>
        <li><a href="/software/S0055">RARSTONE</a></li>
        <li><a href="/software/S0241">RATANKBA</a></li>
        <li><a href="/software/S0258">RGDoor</a></li>
        <li><a href="/software/S0003">RIPTIDE</a></li>
        <li><a href="/software/S0112">ROCKBOOT</a></li>
        <li><a href="/software/S0240">ROKRAT</a></li>
        <li><a href="/software/S0148">RTM</a></li>
        <li><a href="/software/S0169">RawPOS</a></li>
        <li><a href="/software/S0172">Reaver</a></li>
        <li><a href="/software/S0153">RedLeaves</a></li>
        <li><a href="/software/S0019">Regin</a></li>
        <li><a href="/software/S0332">Remcos</a></li>
        <li><a href="/software/S0375">Remexi</a></li>
        <li><a href="/software/S0166">RemoteCMD</a></li>
        <li><a href="/software/S0125">Remsec</a></li>
        <li><a href="/software/S0379">Revenge RAT</a></li>
        <li><a href="/software/S0400">RobbinHood</a></li>
        <li><a href="/software/S0270">RogueRobin</a></li>
        <li><a href="/software/S0090">Rover</a></li>
        <li><a href="/software/S0358">Ruler</a></li>
        <li><a href="/software/S0253">RunningRAT</a></li>
        <li><a href="/software/S0085">S-Type</a></li>
        <li><a href="/software/S0185">SEASHARPEE</a></li>
        <li><a href="/software/S0063">SHOTPUT</a></li>
        <li><a href="/software/S0218">SLOWDRIFT</a></li>
        <li><a href="/software/S0159">SNUGRIDE</a></li>
        <li><a href="/software/S0157">SOUNDBITE</a></li>
        <li><a href="/software/S0035">SPACESHIP</a></li>
        <li><a href="/software/S0390">SQLRat</a></li>
        <li><a href="/software/S0074">Sakula</a></li>
        <li><a href="/software/S0053">SeaDuke</a></li>
        <li><a href="/software/S0345">Seasalt</a></li>
        <li><a href="/software/S0382">ServHelper</a></li>
        <li><a href="/software/S0140">Shamoon</a></li>
        <li><a href="/software/S0007">Skeleton Key</a></li>
        <li><a href="/software/S0226">Smoke Loader</a></li>
        <li><a href="/software/S0273">Socksbot</a></li>
        <li><a href="/software/S0374">SpeakUp</a></li>
        <li><a href="/software/S0058">SslMM</a></li>
        <li><a href="/software/S0188">Starloader</a></li>
        <li><a href="/software/S0380">StoneDrill</a></li>
        <li><a href="/software/S0142">StreamEx</a></li>
        <li><a href="/software/S0018">Sykipot</a></li>
        <li><a href="/software/S0242">SynAck</a></li>
        <li><a href="/software/S0060">Sys10</a></li>
        <li><a href="/software/S0098">T9000</a></li>
        <li><a href="/software/S0164">TDTESS</a></li>
        <li><a href="/software/S0146">TEXTMATE</a></li>
        <li><a href="/software/S0199">TURNEDUP</a></li>
        <li><a href="/software/S0263">TYPEFRAME</a></li>
        <li><a href="/software/S0011">Taidoor</a></li>
        <li><a href="/software/S0004">TinyZBot</a></li>
        <li><a href="/software/S0183">Tor</a></li>
        <li><a href="/software/S0266">TrickBot</a></li>
        <li><a href="/software/S0094">Trojan.Karagany</a></li>
        <li><a href="/software/S0001">Trojan.Mebromi</a></li>
        <li><a href="/software/S0178">Truvasys</a></li>
        <li><a href="/software/S0302">Twitoor</a></li>
        <li><a href="/software/S0333">UBoatRAT</a></li>
        <li><a href="/software/S0275">UPPERCUT</a></li>
        <li><a href="/software/S0136">USBStealer</a></li>
        <li><a href="/software/S0221">Umbreon</a></li>
        <li><a href="/software/S0130">Unknown Logger</a></li>
        <li><a href="/software/S0386">Ursnif</a></li>
        <li><a href="/software/S0257">VERMIN</a></li>
        <li><a href="/software/S0207">Vasport</a></li>
        <li><a href="/software/S0180">Volgmer</a></li>
        <li><a href="/software/S0109">WEBC2</a></li>
        <li><a href="/software/S0366">WannaCry</a></li>
        <li><a href="/software/S0206">Wiarp</a></li>
        <li><a href="/software/S0059">WinMM</a></li>
        <li><a href="/software/S0005">Windows Credential Editor</a></li>
        <li><a href="/software/S0176">Wingbird</a></li>
        <li><a href="/software/S0141">Winnti for Windows</a></li>
        <li><a href="/software/S0161">XAgentOSX</a></li>
        <li><a href="/software/S0117">XTunnel</a></li>
        <li><a href="/software/S0341">Xbash</a></li>
        <li><a href="/software/S0388">YAHOYAH</a></li>
        <li><a href="/software/S0086">ZLib</a></li>
        <li><a href="/software/S0251">Zebrocy</a></li>
        <li><a href="/software/S0230">ZeroT</a></li>
        <li><a href="/software/S0330">Zeus Panda</a></li>
        <li><a href="/software/S0412">ZxShell</a></li>
        <li><a href="/software/S0202">adbupd</a></li>
        <li><a href="/software/S0110">at</a></li>
        <li><a href="/software/S0106">cmd</a></li>
        <li><a href="/software/S0105">dsquery</a></li>
        <li><a href="/software/S0404">esentutl</a></li>
        <li><a href="/software/S0032">gh0st RAT</a></li>
        <li><a href="/software/S0008">gsecdump</a></li>
        <li><a href="/software/S0071">hcdLoader</a></li>
        <li><a href="/software/S0068">httpclient</a></li>
        <li><a href="/software/S0278">iKitten</a></li>
        <li><a href="/software/S0283">jRAT</a></li>
        <li><a href="/software/S0108">netsh</a></li>
        <li><a href="/software/S0385">njRAT</a></li>
        <li><a href="/software/S0067">pngdowner</a></li>
        <li><a href="/software/S0006">pwdump</a></li>
        <li><a href="/software/S0111">schtasks</a></li>
        <li><a href="/software/S0227">spwebmember</a></li>
        <li><a href="/software/S0248">yty</a></li>
        <li><a href="/software/S0350">zwShell</a></li>
        </ul>
        <p>Minor Software changes:
        No changes</p>
        <p>Software revocations:
        No changes</p>
        <p>Software deprecations:
        No changes</p>
        <p><strong>PRE-ATT&amp;CK</strong></p>
        <p>New Software:
        No changes</p>
        <p>Software changes:
        No changes</p>
        <p>Minor Software changes:
        No changes</p>
        <p>Software revocations:
        No changes</p>
        <p>Software deprecations:
        No changes</p>
        <p><strong>Mobile</strong></p>
        <p>New Software:</p>
        <ul>
        <li><a href="/software/S0440">Agent Smith</a></li>
        <li><a href="/software/S0422">Anubis</a></li>
        <li><a href="/software/S0432">Bread</a></li>
        <li><a href="/software/S0480">Cerberus</a></li>
        <li><a href="/software/S0426">Concipit1248</a></li>
        <li><a href="/software/S0425">Corona Updates</a></li>
        <li><a href="/software/S0479">DEFENSOR ID</a></li>
        <li><a href="/software/S0420">Dvmap</a></li>
        <li><a href="/software/S0478">EventBot</a></li>
        <li><a href="/software/S0423">Ginp</a></li>
        <li><a href="/software/S0421">GolfSpy</a></li>
        <li><a href="/software/S0463">INSOMNIA</a></li>
        <li><a href="/software/S0419">SimBad</a></li>
        <li><a href="/software/S0424">Triada</a></li>
        <li><a href="/software/S0427">TrickMo</a></li>
        <li><a href="/software/S0418">ViceLeaker</a></li>
        </ul>
        <p>Software changes:</p>
        <ul>
        <li><a href="/software/S0182">FinFisher</a></li>
        <li><a href="/software/S0407">Monokle</a></li>
        </ul>
        <p>Minor Software changes:</p>
        <ul>
        <li><a href="/software/S0289">Pegasus for iOS</a></li>
        </ul>
        <p>Software revocations:
        No changes</p>
        <p>Software deprecations:
        No changes</p>
        <h3>Groups</h3>
        <p><strong>Enterprise</strong></p>
        <p>New Groups:</p>
        <ul>
        <li><a href="/groups/G0099">APT-C-36</a></li>
        <li><a href="/groups/G0098">BlackTech</a></li>
        <li><a href="/groups/G0108">Blue Mockingbird</a></li>
        <li><a href="/groups/G0097">Bouncing Golf</a></li>
        <li><a href="/groups/G0058">Charming Kitten</a></li>
        <li><a href="/groups/G0105">DarkVishnya</a></li>
        <li><a href="/groups/G0101">Frankenstein</a></li>
        <li><a href="/groups/G0100">Inception</a></li>
        <li><a href="/groups/G0103">Mofang</a></li>
        <li><a href="/groups/G0106">Rocke</a></li>
        <li><a href="/groups/G0104">Sharpshooter</a></li>
        <li><a href="/groups/G0107">Whitefly</a></li>
        <li><a href="/groups/G0112">Windshift</a></li>
        <li><a href="/groups/G0102">Wizard Spider</a></li>
        </ul>
        <p>Group changes:</p>
        <ul>
        <li><a href="/groups/G0006">APT1</a></li>
        <li><a href="/groups/G0005">APT12</a></li>
        <li><a href="/groups/G0026">APT18</a></li>
        <li><a href="/groups/G0073">APT19</a></li>
        <li><a href="/groups/G0007">APT28</a></li>
        <li><a href="/groups/G0016">APT29</a></li>
        <li><a href="/groups/G0022">APT3</a></li>
        <li><a href="/groups/G0050">APT32</a></li>
        <li><a href="/groups/G0064">APT33</a></li>
        <li><a href="/groups/G0067">APT37</a></li>
        <li><a href="/groups/G0082">APT38</a></li>
        <li><a href="/groups/G0087">APT39</a></li>
        <li><a href="/groups/G0096">APT41</a></li>
        <li><a href="/groups/G0001">Axiom</a></li>
        <li><a href="/groups/G0060">BRONZE BUTLER</a></li>
        <li><a href="/groups/G0008">Carbanak</a></li>
        <li><a href="/groups/G0003">Cleaver</a></li>
        <li><a href="/groups/G0080">Cobalt Group</a></li>
        <li><a href="/groups/G0052">CopyKittens</a></li>
        <li><a href="/groups/G0070">Dark Caracal</a></li>
        <li><a href="/groups/G0079">DarkHydrus</a></li>
        <li><a href="/groups/G0012">Darkhotel</a></li>
        <li><a href="/groups/G0009">Deep Panda</a></li>
        <li><a href="/groups/G0074">Dragonfly 2.0</a></li>
        <li><a href="/groups/G0066">Elderwood</a></li>
        <li><a href="/groups/G0020">Equation</a></li>
        <li><a href="/groups/G0051">FIN10</a></li>
        <li><a href="/groups/G0085">FIN4</a></li>
        <li><a href="/groups/G0053">FIN5</a></li>
        <li><a href="/groups/G0037">FIN6</a></li>
        <li><a href="/groups/G0046">FIN7</a></li>
        <li><a href="/groups/G0061">FIN8</a></li>
        <li><a href="/groups/G0036">GCMAN</a></li>
        <li><a href="/groups/G0084">Gallmaker</a></li>
        <li><a href="/groups/G0047">Gamaredon Group</a></li>
        <li><a href="/groups/G0078">Gorgon Group</a></li>
        <li><a href="/groups/G0043">Group5</a></li>
        <li><a href="/groups/G0072">Honeybee</a></li>
        <li><a href="/groups/G0004">Ke3chang</a></li>
        <li><a href="/groups/G0094">Kimsuky</a></li>
        <li><a href="/groups/G0032">Lazarus Group</a></li>
        <li><a href="/groups/G0077">Leafminer</a></li>
        <li><a href="/groups/G0065">Leviathan</a></li>
        <li><a href="/groups/G0095">Machete</a></li>
        <li><a href="/groups/G0059">Magic Hound</a></li>
        <li><a href="/groups/G0002">Moafee</a></li>
        <li><a href="/groups/G0021">Molerats</a></li>
        <li><a href="/groups/G0069">MuddyWater</a></li>
        <li><a href="/groups/G0019">Naikon</a></li>
        <li><a href="/groups/G0014">Night Dragon</a></li>
        <li><a href="/groups/G0049">OilRig</a></li>
        <li><a href="/groups/G0071">Orangeworm</a></li>
        <li><a href="/groups/G0068">PLATINUM</a></li>
        <li><a href="/groups/G0040">Patchwork</a></li>
        <li><a href="/groups/G0011">PittyTiger</a></li>
        <li><a href="/groups/G0033">Poseidon Group</a></li>
        <li><a href="/groups/G0024">Putter Panda</a></li>
        <li><a href="/groups/G0048">RTM</a></li>
        <li><a href="/groups/G0075">Rancor</a></li>
        <li><a href="/groups/G0029">Scarlet Mimic</a></li>
        <li><a href="/groups/G0091">Silence</a></li>
        <li><a href="/groups/G0083">SilverTerrier</a></li>
        <li><a href="/groups/G0093">Soft Cell</a></li>
        <li><a href="/groups/G0054">Sowbug</a></li>
        <li><a href="/groups/G0038">Stealth Falcon</a></li>
        <li><a href="/groups/G0086">Stolen Pencil</a></li>
        <li><a href="/groups/G0041">Strider</a></li>
        <li><a href="/groups/G0039">Suckfly</a></li>
        <li><a href="/groups/G0062">TA459</a></li>
        <li><a href="/groups/G0092">TA505</a></li>
        <li><a href="/groups/G0088">TEMP.Veles</a></li>
        <li><a href="/groups/G0089">The White Company</a></li>
        <li><a href="/groups/G0028">Threat Group-1314</a></li>
        <li><a href="/groups/G0027">Threat Group-3390</a></li>
        <li><a href="/groups/G0076">Thrip</a></li>
        <li><a href="/groups/G0081">Tropic Trooper</a></li>
        <li><a href="/groups/G0010">Turla</a></li>
        <li><a href="/groups/G0090">WIRTE</a></li>
        <li><a href="/groups/G0018">admin@338</a></li>
        <li><a href="/groups/G0045">menuPass</a></li>
        </ul>
        <p>Minor Group changes:</p>
        <ul>
        <li><a href="/groups/G0034">Sandworm Team</a></li>
        <li><a href="/groups/G0044">Winnti Group</a></li>
        </ul>
        <p>Group revocations:
        No changes</p>
        <p>Group deprecations:
        No changes</p>
        <p>Group deletions:</p>
        <ul>
        <li>Charming Kitten</li>
        </ul>
        <p><strong>PRE-ATT&amp;CK</strong></p>
        <p>New Groups:
        No changes</p>
        <p>Group changes:</p>
        <ul>
        <li><a href="/groups/G0006">APT1</a></li>
        <li><a href="/groups/G0007">APT28</a></li>
        <li><a href="/groups/G0003">Cleaver</a></li>
        <li><a href="/groups/G0014">Night Dragon</a></li>
        <li><a href="/groups/G0088">TEMP.Veles</a></li>
        </ul>
        <p>Minor Group changes:
        No changes</p>
        <p>Group revocations:
        No changes</p>
        <p>Group deprecations:
        No changes</p>
        <p><strong>Mobile</strong></p>
        <p>New Groups:</p>
        <ul>
        <li><a href="/groups/G0097">Bouncing Golf</a></li>
        </ul>
        <p>Group changes:</p>
        <ul>
        <li><a href="/groups/G0007">APT28</a></li>
        <li><a href="/groups/G0070">Dark Caracal</a></li>
        </ul>
        <p>Minor Group changes:
        No changes</p>
        <p>Group revocations:
        No changes</p>
        <p>Group deprecations:
        No changes</p>
        <h3>Mitigations</h3>
        <p><strong>Enterprise</strong></p>
        <p>New Mitigations:
        No changes</p>
        <p>Mitigation changes:</p>
        <ul>
        <li><a href="/mitigations/M1015">Active Directory Configuration</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1049">Antivirus/Antimalware</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1048">Application Isolation and Sandboxing</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1047">Audit</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1045">Code Signing</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1043">Credential Access Protection</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1053">Data Backup</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1042">Disable or Remove Feature or Program</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1038">Execution Prevention</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1050">Exploit Protection</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1030">Network Segmentation</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1028">Operating System Configuration</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1026">Privileged Account Management</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1025">Privileged Process Integrity</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1022">Restrict File and Directory Permissions</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1054">Software Configuration</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1052">User Account Control</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1018">User Account Management</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1017">User Training</a> - Sub or technique relationships updated</li>
        <li><a href="/mitigations/M1016">Vulnerability Scanning</a> - Sub or technique relationships updated</li>
        </ul>
        <p>Minor Mitigation changes:</p>
        <ul>
        <li><a href="/mitigations/M1046">Boot Integrity</a></li>
        <li><a href="/mitigations/M1037">Filter Network Traffic</a></li>
        <li><a href="/mitigations/M1035">Limit Access to Resource Over Network</a></li>
        <li><a href="/mitigations/M1034">Limit Hardware Installation</a></li>
        </ul>
        <p>Mitigation revocations:
        No changes</p>
        <p>Mitigation deprecations:
        No changes</p>
        <p>Mitigation deletions:</p>
        <p>These are old mitigations that are no longer in use.</p>
        <ul>
        <li>Account Manipulation Mitigation</li>
        <li>Command-Line Interface Mitigation</li>
        <li>Connection Proxy Mitigation</li>
        <li>Execution through API Mitigation</li>
        <li>Exfiltration Over Alternative Protocol Mitigation</li>
        <li>File Permissions Modification Mitigation</li>
        <li>Input Capture Mitigation</li>
        <li>Obfuscated Files or Information Mitigation</li>
        <li>Office Application Startup Mitigation</li>
        <li>Process Injection Mitigation</li>
        <li>Remote Services Mitigation</li>
        <li>Signed Binary Proxy Execution Mitigation</li>
        <li>Standard Application Layer Protocol Mitigation</li>
        <li>Trusted Developer Utilities Mitigation</li>
        <li>Virtualization/Sandbox Evasion Mitigation</li>
        <li>Windows Management Instrumentation Mitigation</li>
        </ul>
        <p><strong>PRE-ATT&amp;CK</strong></p>
        <p>New Mitigations:
        No changes</p>
        <p>Mitigation changes:
        No changes</p>
        <p>Minor Mitigation changes:
        No changes</p>
        <p>Mitigation revocations:
        No changes</p>
        <p>Mitigation deprecations:
        No changes</p>
        <p><strong>Mobile</strong></p>
        <p>New Mitigations:
        No changes</p>
        <p>Mitigation changes:
        No changes</p>
        <p>Minor Mitigation changes:</p>
        <ul>
        <li><a href="/mitigations/M1012">Enterprise Policy</a></li>
        </ul>
        <p>Mitigation revocations:
        No changes</p>
        <p>Mitigation deprecations:
        No changes</p>
    </div>
    <div class="tab-pane" role="tabpanel" id="v7-pane" aria-labelledby="v7-tab">

        <p>The July 2020 (v7) ATT&amp;CK release  updates Techniques, Groups, and Software for both Enterprise and Mobile. ATT&amp;CK with sub-techniques was released as a beta in March 2020 (v7-beta), this changelog represents the updates made between the beta and final release. </p>
        <h3>Major errata fixed from the v7 (March 2020) Beta</h3>
        <ul>
        <li><a href="/techniques/T1205">Traffic Signaling</a> Was incorrectly re-IDd to T1545, restored to T1205 and its sub-technique was changed to T1205.001</li>
        <li><a href="/techniques/T1070">Indicator Removal on Host</a> Was incorrectly re-IDd to T1551, restored to T1070 and its sub-techniques were changed to T1070.001, T1070.002, T1070.003, T1070.004, T1070.005, and T1070.006</li>
        <li><a href="/techniques/T1043">Commonly Used Port</a> Was revoked by T1571 in the beta, corrected to now be deprecated</li>
        </ul>
        <h3>Techniques</h3>
        <p><strong>Enterprise</strong></p>
        <p>
            View enterprise technique updates in the ATT&CK Navigator <a href="https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fattack-navigator%2Fmaster%2Flayers%2Fdata%2Fupdate_layers%2FJuly_2020%2FJuly_2020_enterprise_attack_beta.json" target="_blank">here</a>.
        </p>
        <p>New Techniques:</p>
        <ul>
        <li>Account Manipulation: <a href="/techniques/T1098/004">SSH Authorized Keys</a> - Created as distinct behavior within Account Manipulation</li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/007">JavaScript/JScript</a> - Created as distinct behavior within Command and Scripting Interpreter</li>
        <li>Execution Guardrails: <a href="/techniques/T1480/001">Environmental Keying</a> - Broken out from pre-defined behavior within Execution Guardrails</li>
        <li>Hide Artifacts: <a href="/techniques/T1564/005">Hidden File System</a> - Created as distinct behavior within Hide Artifacts</li>
        <li>Hide Artifacts: <a href="/techniques/T1564/006">Run Virtual Instance</a> - Created as distinct behavior within Hide Artifacts</li>
        <li>Hijack Execution Flow: <a href="/techniques/T1574/012">COR_PROFILER</a> - Created as distinct behavior within Hijack Execution Flow</li>
        <li>Impair Defenses: <a href="/techniques/T1562/007">Disable or Modify Cloud Firewall</a> - Created as distinct behavior within Impair Defenses</li>
        <li>Modify Authentication Process: <a href="/techniques/T1556/003">Pluggable Authentication Modules</a> - Created as distinct behavior within Modify Authentication Process</li>
        <li><a href="/techniques/T1578">Modify Cloud Compute Infrastructure</a> - Created to consolidate behaviors around defense evasion through the cloud compute service<ul>
        <li><a href="/techniques/T1578/002">Create Cloud Instance</a> - Created as distinct behavior within Modify Cloud Compute Infrastructure</li>
        <li><a href="/techniques/T1578/001">Create Snapshot</a> - Created as distinct behavior within Modify Cloud Compute Infrastructure</li>
        <li><a href="/techniques/T1578/003">Delete Cloud Instance</a> - Created as distinct behavior within Modify Cloud Compute Infrastructure</li>
        <li><a href="/techniques/T1578/004">Revert Cloud Instance</a> - Existing technique that became a sub-technique</li>
        </ul>
        </li>
        </ul>
        <p>Technique changes:</p>
        <ul>
        <li><a href="/techniques/T1098">Account Manipulation</a> - New sub-technique added</li>
        <li><a href="/techniques/T1526">Cloud Service Discovery</a> - Minor description update</li>
        <li><a href="/techniques/T1059">Command and Scripting Interpreter</a> New sub-techniques added<ul>
        <li><a href="/techniques/T1059/004">Unix Shell</a> - Sub-technique renamed</li>
        </ul>
        </li>
        <li><a href="/techniques/T1480">Execution Guardrails</a> - New sub-technique added</li>
        <li><a href="/techniques/T1564">Hide Artifacts</a> - New sub-techniques added</li>
        <li><a href="/techniques/T1574">Hijack Execution Flow</a> - New sub-technique added</li>
        <li><a href="/techniques/T1562">Impair Defenses</a> - New sub-technique added</li>
        <li><a href="/techniques/T1070">Indicator Removal on Host</a> - Technique renumbered<ul>
        <li><a href="/techniques/T1070/003">Clear Command History</a> - Sub-technique renumbered</li>
        <li><a href="/techniques/T1070/002">Clear Linux or Mac System Logs</a> - Sub-technique renumbered</li>
        <li><a href="/techniques/T1070/001">Clear Windows Event Logs</a> - Sub-technique renumbered</li>
        <li><a href="/techniques/T1070/004">File Deletion</a> - Sub-technique renumbered</li>
        <li><a href="/techniques/T1070/005">Network Share Connection Removal</a> - Sub-technique renumbered</li>
        <li><a href="/techniques/T1070/006">Timestomp</a> - Sub-technique renumbered</li>
        </ul>
        </li>
        <li><a href="/techniques/T1556">Modify Authentication Process</a> - New sub-technique added</li>
        <li>Process Injection: <a href="/techniques/T1055/008">Ptrace System Calls</a> - Platform removed</li>
        <li>Process Injection: <a href="/techniques/T1055/014">VDSO Hijacking</a> - Platform removed</li>
        <li>Process Injection: <a href="/techniques/T1055/009">Proc Memory</a> - Platform removed</li>
        <li><a href="/techniques/T1205">Traffic Signaling</a> - Technique renumbered and scope broadened<ul>
        <li><a href="/techniques/T1205/001">Port Knocking</a> - Sub-technique renumbered</li>
        </ul>
        </li>
        </ul>
        <p>Minor Technique changes:</p>
        <ul>
        <li><a href="/techniques/T1548">Abuse Elevation Control Mechanism</a><ul>
        <li><a href="/techniques/T1548/002">Bypass User Access Control</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1134">Access Token Manipulation</a><ul>
        <li><a href="/techniques/T1134/004">Parent PID Spoofing</a></li>
        </ul>
        </li>
        <li>Account Manipulation: <a href="/techniques/T1098/001">Additional Azure Service Principal Credentials</a></li>
        <li>Account Manipulation: <a href="/techniques/T1098/002">Exchange Email Delegate Permissions</a></li>
        <li><a href="/techniques/T1119">Automated Collection</a></li>
        <li><a href="/techniques/T1547">Boot or Logon Autostart Execution</a><ul>
        <li><a href="/techniques/T1547/006">Kernel Modules and Extensions</a></li>
        <li><a href="/techniques/T1547/011">Plist Modification</a></li>
        <li><a href="/techniques/T1547/004">Winlogon Helper DLL</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1115">Clipboard Data</a></li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/002">AppleScript</a></li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/001">PowerShell</a></li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/006">Python</a></li>
        <li>Command and Scripting Interpreter: <a href="/techniques/T1059/005">Visual Basic</a></li>
        <li><a href="/techniques/T1074">Data Staged</a><ul>
        <li><a href="/techniques/T1074/001">Local Data Staging</a></li>
        <li><a href="/techniques/T1074/002">Remote Data Staging</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1213">Data from Information Repositories</a></li>
        <li><a href="/techniques/T1005">Data from Local System</a></li>
        <li><a href="/techniques/T1491">Defacement</a><ul>
        <li><a href="/techniques/T1491/002">External Defacement</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1546">Event Triggered Execution</a><ul>
        <li><a href="/techniques/T1546/008">Accessibility Features</a></li>
        <li><a href="/techniques/T1546/011">Application Shimming</a></li>
        <li><a href="/techniques/T1546/003">Windows Management Instrumentation Event Subscription</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1133">External Remote Services</a></li>
        <li><a href="/techniques/T1187">Forced Authentication</a></li>
        <li>Hijack Execution Flow: <a href="/techniques/T1574/002">DLL Side-Loading</a></li>
        <li>Hijack Execution Flow: <a href="/techniques/T1574/004">Dylib Hijacking</a></li>
        <li>Hijack Execution Flow: <a href="/techniques/T1574/006">LD_PRELOAD</a></li>
        <li>Hijack Execution Flow: <a href="/techniques/T1574/007">Path Interception by PATH Environment Variable</a></li>
        <li>Hijack Execution Flow: <a href="/techniques/T1574/011">Services Registry Permissions Weakness</a></li>
        <li><a href="/techniques/T1202">Indirect Command Execution</a></li>
        <li><a href="/techniques/T1534">Internal Spearphishing</a></li>
        <li><a href="/techniques/T1036">Masquerading</a><ul>
        <li><a href="/techniques/T1036/005">Match Legitimate Name or Location</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1106">Native API</a></li>
        <li><a href="/techniques/T1003">OS Credential Dumping</a><ul>
        <li><a href="/techniques/T1003/001">LSASS Memory</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1027">Obfuscated Files or Information</a><ul>
        <li><a href="/techniques/T1027/001">Binary Padding</a></li>
        <li><a href="/techniques/T1027/003">Steganography</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1137">Office Application Startup</a><ul>
        <li><a href="/techniques/T1137/001">Office Template Macros</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1542">Pre-OS Boot</a><ul>
        <li><a href="/techniques/T1542/003">Bootkit</a></li>
        <li><a href="/techniques/T1542/001">System Firmware</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1055">Process Injection</a><ul>
        <li><a href="/techniques/T1055/004">Asynchronous Procedure Call</a></li>
        <li><a href="/techniques/T1055/001">Dynamic-link Library Injection</a></li>
        <li><a href="/techniques/T1055/011">Extra Window Memory Injection</a></li>
        <li><a href="/techniques/T1055/002">Portable Executable Injection</a></li>
        <li><a href="/techniques/T1055/013">Process DoppelgÃ€nging</a></li>
        <li><a href="/techniques/T1055/012">Process Hollowing</a></li>
        <li><a href="/techniques/T1055/003">Thread Execution Hijacking</a></li>
        <li><a href="/techniques/T1055/005">Thread Local Storage</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1090">Proxy</a><ul>
        <li><a href="/techniques/T1090/004">Domain Fronting</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1219">Remote Access Software</a></li>
        <li><a href="/techniques/T1018">Remote System Discovery</a></li>
        <li><a href="/techniques/T1014">Rootkit</a></li>
        <li><a href="/techniques/T1505">Server Software Component</a><ul>
        <li><a href="/techniques/T1505/003">Web Shell</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1218">Signed Binary Proxy Execution</a><ul>
        <li><a href="/techniques/T1218/003">CMSTP</a></li>
        <li><a href="/techniques/T1218/001">Compiled HTML File</a></li>
        <li><a href="/techniques/T1218/002">Control Panel</a></li>
        <li><a href="/techniques/T1218/004">InstallUtil</a></li>
        <li><a href="/techniques/T1218/005">Mshta</a></li>
        <li><a href="/techniques/T1218/007">Msiexec</a></li>
        <li><a href="/techniques/T1218/008">Odbcconf</a></li>
        <li><a href="/techniques/T1218/009">Regsvcs/Regasm</a></li>
        <li><a href="/techniques/T1218/010">Regsvr32</a></li>
        <li><a href="/techniques/T1218/011">Rundll32</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1216">Signed Script Proxy Execution</a><ul>
        <li><a href="/techniques/T1216/001">PubPrn</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1518">Software Discovery</a><ul>
        <li><a href="/techniques/T1518/001">Security Software Discovery</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1539">Steal Web Session Cookie</a></li>
        <li><a href="/techniques/T1553">Subvert Trust Controls</a><ul>
        <li><a href="/techniques/T1553/001">Gatekeeper Bypass</a></li>
        <li><a href="/techniques/T1553/003">SIP and Trust Provider Hijacking</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1569">System Services</a><ul>
        <li><a href="/techniques/T1569/001">Launchctl</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1080">Taint Shared Content</a></li>
        <li><a href="/techniques/T1221">Template Injection</a></li>
        <li><a href="/techniques/T1127">Trusted Developer Utilities Proxy Execution</a><ul>
        <li><a href="/techniques/T1127/001">MSBuild</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1552">Unsecured Credentials</a><ul>
        <li><a href="/techniques/T1552/006">Group Policy Preferences</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1078">Valid Accounts</a></li>
        <li><a href="/techniques/T1497">Virtualization/Sandbox Evasion</a><ul>
        <li><a href="/techniques/T1497/001">System Checks</a></li>
        <li><a href="/techniques/T1497/003">Time Based Evasion</a></li>
        <li><a href="/techniques/T1497/002">User Activity Based Checks</a></li>
        </ul>
        </li>
        <li><a href="/techniques/T1047">Windows Management Instrumentation</a></li>
        <li><a href="/techniques/T1220">XSL Script Processing</a></li>
        </ul>
        <p>Technique revocations:</p>
        <ul>
        <li>Revert Cloud Instance (revoked by Modify Cloud Compute Infrastructure: <a href="/techniques/T1578/004">Revert Cloud Instance</a>)</li>
        </ul>
        <p>Technique deprecations:</p>
        <ul>
        <li><a href="/techniques/T1043">Commonly Used Port</a> - Was incorrectly revoked in the beta release, is now deprecated</li>
        </ul>
        <p>Technique deletions:</p>
        <p><strong>PRE-ATT&amp;CK</strong></p>
        <p>New Techniques:
        No changes</p>
        <p>Technique changes:
        No changes</p>
        <p>Minor Technique changes:
        No changes</p>
        <p>Technique revocations:
        No changes</p>
        <p>Technique deprecations:
        No changes</p>
        <p><strong>Mobile</strong></p>
        <p>
            View mobile technique updates in the ATT&CK Navigator <a href="https://mitre-attack.github.io/attack-navigator/mobile/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2Fmitre-attack%2Fattack-navigator%2Fmaster%2Flayers%2Fdata%2Fupdate_layers%2FJuly_2020%2FJuly_2020_mobile_attack_beta.json" target="_blank">here</a>.
        </p>
        <p>New Techniques:</p>
        <ul>
        <li><a href="/techniques/T1577">Compromise Application Executable</a></li>
        <li><a href="/techniques/T1579">Keychain</a></li>
        <li><a href="/techniques/T1575">Native Code</a></li>
        <li><a href="/techniques/T1576">Uninstall Malicious Application</a></li>
        </ul>
        <p>Technique changes:</p>
        <ul>
        <li><a href="/techniques/T1417">Input Capture</a></li>
        <li><a href="/techniques/T1516">Input Injection</a></li>
        <li><a href="/techniques/T1411">Input Prompt</a></li>
        <li><a href="/techniques/T1444">Masquerade as Legitimate Application</a></li>
        <li><a href="/techniques/T1513">Screen Capture</a></li>
        <li><a href="/techniques/T1422">System Network Configuration Discovery</a></li>
        </ul>
        <p>Minor Technique changes:</p>
        <ul>
        <li><a href="/techniques/T1448">Carrier Billing Fraud</a></li>
        </ul>
        <p>Technique revocations:
        No changes</p>
        <p>Technique deprecations:
        No changes</p>
        <h3>Software</h3>
        <p><strong>Enterprise</strong></p>
        <p>New Software:</p>
        <ul>
        <li><a href="/software/S0469">ABK</a></li>
        <li><a href="/software/S0456">Aria-body</a></li>
        <li><a href="/software/S0438">Attor</a></li>
        <li><a href="/software/S0473">Avenger</a></li>
        <li><a href="/software/S0470">BBK</a></li>
        <li><a href="/software/S0475">BackConfig</a></li>
        <li><a href="/software/S0482">Bundlore</a></li>
        <li><a href="/software/S0465">CARROTBALL</a></li>
        <li><a href="/software/S0462">CARROTBAT</a></li>
        <li><a href="/software/S0454">Cadelspy</a></li>
        <li><a href="/software/S0460">Get2</a></li>
        <li><a href="/software/S0477">Goopy</a></li>
        <li><a href="/software/S0431">HotCroissant</a></li>
        <li><a href="/software/S0434">Imminent Monitor</a></li>
        <li><a href="/software/S0437">Kivars</a></li>
        <li><a href="/software/S0447">Lokibot</a></li>
        <li><a href="/software/S0451">LoudMiner</a></li>
        <li><a href="/software/S0449">MAZE</a></li>
        <li><a href="/software/S0443">MESSAGETAP</a></li>
        <li><a href="/software/S0459">MechaFlounder</a></li>
        <li><a href="/software/S0455">Metamorfo</a></li>
        <li><a href="/software/S0457">Netwalker</a></li>
        <li><a href="/software/S0439">Okrum</a></li>
        <li><a href="/software/S0435">PLEAD</a></li>
        <li><a href="/software/S0428">PoetRAT</a></li>
        <li><a href="/software/S0453">Pony</a></li>
        <li><a href="/software/S0441">PowerShower</a></li>
        <li><a href="/software/S0481">Ragnar Locker</a></li>
        <li><a href="/software/S0458">Ramsay</a></li>
        <li><a href="/software/S0433">Rifdoor</a></li>
        <li><a href="/software/S0448">Rising Sun</a></li>
        <li><a href="/software/S0446">Ryuk</a></li>
        <li><a href="/software/S0461">SDBot</a></li>
        <li><a href="/software/S0450">SHARPSTATS</a></li>
        <li><a href="/software/S0464">SYSCON</a></li>
        <li><a href="/software/S0444">ShimRat</a></li>
        <li><a href="/software/S0445">ShimRatReporter</a></li>
        <li><a href="/software/S0468">Skidmap</a></li>
        <li><a href="/software/S0436">TSCookie</a></li>
        <li><a href="/software/S0467">TajMahal</a></li>
        <li><a href="/software/S0452">USBferry</a></li>
        <li><a href="/software/S0442">VBShower</a></li>
        <li><a href="/software/S0476">Valak</a></li>
        <li><a href="/software/S0466">WindTail</a></li>
        <li><a href="/software/S0430">Winnti for Linux</a></li>
        <li><a href="/software/S0471">build_downer</a></li>
        <li><a href="/software/S0472">down_new</a></li>
        </ul>
        <p>Software changes:</p>
        <ul>
        <li><a href="/software/S0356">KONNI</a></li>
        <li><a href="/software/S0141">Winnti for Windows</a></li>
        </ul>
        <p>Minor Software changes:</p>
        <ul>
        <li><a href="/software/S0331">Agent Tesla</a></li>
        <li><a href="/software/S0373">Astaroth</a></li>
        <li><a href="/software/S0114">BOOTRASH</a></li>
        <li><a href="/software/S0089">BlackEnergy</a></li>
        <li><a href="/software/S0252">Brave Prince</a></li>
        <li><a href="/software/S0220">Chaos</a></li>
        <li><a href="/software/S0154">Cobalt Strike</a></li>
        <li><a href="/software/S0126">ComRAT</a></li>
        <li><a href="/software/S0354">Denis</a></li>
        <li><a href="/software/S0062">DustySky</a></li>
        <li><a href="/software/S0024">Dyre</a></li>
        <li><a href="/software/S0367">Emotet</a></li>
        <li><a href="/software/S0343">Exaramel for Windows</a></li>
        <li><a href="/software/S0417">GRIFFON</a></li>
        <li><a href="/software/S0249">Gold Dragon</a></li>
        <li><a href="/software/S0087">Hi-Zor</a></li>
        <li><a href="/software/S0009">Hikit</a></li>
        <li><a href="/software/S0398">HyperBro</a></li>
        <li><a href="/software/S0357">Impacket</a></li>
        <li><a href="/software/S0228">NanHaiShu</a></li>
        <li><a href="/software/S0368">NotPetya</a></li>
        <li><a href="/software/S0352">OSX_OCEANLOTUS.D</a></li>
        <li><a href="/software/S0223">POWERSTATS</a></li>
        <li><a href="/software/S0196">PUNCHBUGGY</a></li>
        <li><a href="/software/S0013">PlugX</a></li>
        <li><a href="/software/S0279">Proton</a></li>
        <li><a href="/software/S0147">Pteranodon</a></li>
        <li><a href="/software/S0192">Pupy</a></li>
        <li><a href="/software/S0240">ROKRAT</a></li>
        <li><a href="/software/S0148">RTM</a></li>
        <li><a href="/software/S0019">Regin</a></li>
        <li><a href="/software/S0358">Ruler</a></li>
        <li><a href="/software/S0253">RunningRAT</a></li>
        <li><a href="/software/S0382">ServHelper</a></li>
        <li><a href="/software/S0140">Shamoon</a></li>
        <li><a href="/software/S0018">Sykipot</a></li>
        <li><a href="/software/S0263">TYPEFRAME</a></li>
        <li><a href="/software/S0183">Tor</a></li>
        <li><a href="/software/S0221">Umbreon</a></li>
        <li><a href="/software/S0386">Ursnif</a></li>
        <li><a href="/software/S0366">WannaCry</a></li>
        <li><a href="/software/S0341">Xbash</a></li>
        <li><a href="/software/S0388">YAHOYAH</a></li>
        <li><a href="/software/S0283">jRAT</a></li>
        </ul>
        <p>Software revocations:
        No changes</p>
        <p>Software deprecations:
        No changes</p>
        <p><strong>PRE-ATT&amp;CK</strong></p>
        <p>New Software:
        No changes</p>
        <p>Software changes:
        No changes</p>
        <p>Minor Software changes:
        No changes</p>
        <p>Software revocations:
        No changes</p>
        <p>Software deprecations:
        No changes</p>
        <p><strong>Mobile</strong></p>
        <p>New Software:</p>
        <ul>
        <li><a href="/software/S0440">Agent Smith</a></li>
        <li><a href="/software/S0422">Anubis</a></li>
        <li><a href="/software/S0432">Bread</a></li>
        <li><a href="/software/S0480">Cerberus</a></li>
        <li><a href="/software/S0426">Concipit1248</a></li>
        <li><a href="/software/S0425">Corona Updates</a></li>
        <li><a href="/software/S0479">DEFENSOR ID</a></li>
        <li><a href="/software/S0478">EventBot</a></li>
        <li><a href="/software/S0423">Ginp</a></li>
        <li><a href="/software/S0463">INSOMNIA</a></li>
        <li><a href="/software/S0424">Triada</a></li>
        <li><a href="/software/S0427">TrickMo</a></li>
        </ul>
        <p>Software changes:
        No changes</p>
        <p>Minor Software changes:
        No changes</p>
        <p>Software revocations:
        No changes</p>
        <p>Software deprecations:
        No changes</p>
        <h3>Groups</h3>
        <p><strong>Enterprise</strong></p>
        <p>New Groups:</p>
        <ul>
        <li><a href="/groups/G0099">APT-C-36</a></li>
        <li><a href="/groups/G0098">BlackTech</a></li>
        <li><a href="/groups/G0108">Blue Mockingbird</a></li>
        <li><a href="/groups/G0058">Charming Kitten</a></li>
        <li><a href="/groups/G0105">DarkVishnya</a></li>
        <li><a href="/groups/G0101">Frankenstein</a></li>
        <li><a href="/groups/G0100">Inception</a></li>
        <li><a href="/groups/G0103">Mofang</a></li>
        <li><a href="/groups/G0106">Rocke</a></li>
        <li><a href="/groups/G0104">Sharpshooter</a></li>
        <li><a href="/groups/G0107">Whitefly</a></li>
        <li><a href="/groups/G0112">Windshift</a></li>
        <li><a href="/groups/G0102">Wizard Spider</a></li>
        </ul>
        <p>Group changes:</p>
        <ul>
        <li><a href="/groups/G0050">APT32</a></li>
        <li><a href="/groups/G0004">Ke3chang</a></li>
        <li><a href="/groups/G0059">Magic Hound</a></li>
        <li><a href="/groups/G0019">Naikon</a></li>
        </ul>
        <p>Minor Group changes:</p>
        <ul>
        <li><a href="/groups/G0073">APT19</a></li>
        <li><a href="/groups/G0064">APT33</a></li>
        <li><a href="/groups/G0067">APT37</a></li>
        <li><a href="/groups/G0087">APT39</a></li>
        <li><a href="/groups/G0096">APT41</a></li>
        <li><a href="/groups/G0060">BRONZE BUTLER</a></li>
        <li><a href="/groups/G0080">Cobalt Group</a></li>
        <li><a href="/groups/G0070">Dark Caracal</a></li>
        <li><a href="/groups/G0079">DarkHydrus</a></li>
        <li><a href="/groups/G0009">Deep Panda</a></li>
        <li><a href="/groups/G0020">Equation</a></li>
        <li><a href="/groups/G0085">FIN4</a></li>
        <li><a href="/groups/G0037">FIN6</a></li>
        <li><a href="/groups/G0046">FIN7</a></li>
        <li><a href="/groups/G0047">Gamaredon Group</a></li>
        <li><a href="/groups/G0072">Honeybee</a></li>
        <li><a href="/groups/G0032">Lazarus Group</a></li>
        <li><a href="/groups/G0077">Leafminer</a></li>
        <li><a href="/groups/G0021">Molerats</a></li>
        <li><a href="/groups/G0069">MuddyWater</a></li>
        <li><a href="/groups/G0049">OilRig</a></li>
        <li><a href="/groups/G0040">Patchwork</a></li>
        <li><a href="/groups/G0048">RTM</a></li>
        <li><a href="/groups/G0034">Sandworm Team</a></li>
        <li><a href="/groups/G0091">Silence</a></li>
        <li><a href="/groups/G0083">SilverTerrier</a></li>
        <li><a href="/groups/G0041">Strider</a></li>
        <li><a href="/groups/G0092">TA505</a></li>
        <li><a href="/groups/G0081">Tropic Trooper</a></li>
        <li><a href="/groups/G0010">Turla</a></li>
        <li><a href="/groups/G0044">Winnti Group</a></li>
        </ul>
        <p>Group revocations:
        No changes</p>
        <p>Group deprecations:
        No changes</p>
        <p>Group deletions:</p>
        <ul>
        <li>Charming Kitten</li>
        </ul>
        <p><strong>PRE-ATT&amp;CK</strong></p>
        <p>New Groups:
        No changes</p>
        <p>Group changes:
        No changes</p>
        <p>Minor Group changes:
        No changes</p>
        <p>Group revocations:
        No changes</p>
        <p>Group deprecations:
        No changes</p>
        <p><strong>Mobile</strong></p>
        <p>New Groups:
        No changes</p>
        <p>Group changes:
        No changes</p>
        <p>Minor Group changes:</p>
        <ul>
        <li><a href="/groups/G0070">Dark Caracal</a></li>
        </ul>
        <p>Group revocations:
        No changes</p>
        <p>Group deprecations:
        No changes</p>
        <h3>Mitigations</h3>
        <p><strong>Enterprise</strong></p>
        <p>New Mitigations:
        No changes</p>
        <p>Mitigation changes:</p>
        <ul>
        <li><a href="/mitigations/M1045">Code Signing</a></li>
        </ul>
        <p>Minor Mitigation changes:</p>
        <ul>
        <li><a href="/mitigations/M1015">Active Directory Configuration</a></li>
        <li><a href="/mitigations/M1046">Boot Integrity</a></li>
        <li><a href="/mitigations/M1038">Execution Prevention</a></li>
        <li><a href="/mitigations/M1050">Exploit Protection</a></li>
        <li><a href="/mitigations/M1037">Filter Network Traffic</a></li>
        <li><a href="/mitigations/M1035">Limit Access to Resource Over Network</a></li>
        <li><a href="/mitigations/M1034">Limit Hardware Installation</a></li>
        <li><a href="/mitigations/M1030">Network Segmentation</a></li>
        <li><a href="/mitigations/M1028">Operating System Configuration</a></li>
        <li><a href="/mitigations/M1025">Privileged Process Integrity</a></li>
        <li><a href="/mitigations/M1022">Restrict File and Directory Permissions</a></li>
        <li><a href="/mitigations/M1018">User Account Management</a></li>
        </ul>
        <p>Mitigation revocations:
        No changes</p>
        <p>Mitigation deprecations:
        No changes</p>
        <p><strong>PRE-ATT&amp;CK</strong></p>
        <p>New Mitigations:
        No changes</p>
        <p>Mitigation changes:
        No changes</p>
        <p>Minor Mitigation changes:
        No changes</p>
        <p>Mitigation revocations:
        No changes</p>
        <p>Mitigation deprecations:
        No changes</p>
        <p><strong>Mobile</strong></p>
        <p>New Mitigations:
        No changes</p>
        <p>Mitigation changes:
        No changes</p>
        <p>Minor Mitigation changes:</p>
        <ul>
        <li><a href="/mitigations/M1012">Enterprise Policy</a></li>
        </ul>
        <p>Mitigation revocations:
        No changes</p>
        <p>Mitigation deprecations:
        No changes</p>

    </div>
</div>