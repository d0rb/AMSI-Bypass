
<div align="center">

[![Profile Visitors](https://komarev.com/ghpvc/?username=d0rb&label=Visitors&color=0e75b6&style=flat)](https://komarev.com/ghpvc/?username=d0rb)

 #  🇮🇱  **#BringThemHome #NeverAgainIsNow**   🇮🇱

**We demand the safe return of all citizens who have been taken hostage by the terrorist group Hamas. We will not rest until every hostage is released and returns home safely. You can help bring them back home.
https://stories.bringthemhomenow.net/**



# AMSI Write Raid 0day Vulnerability

🛡️ **Introduction**

This repository contains a proof of concept exploit for the AMSI Write Raid 0day Vulnerability discovered by OffSec Technical Trainer Victor Khoury (Vixx). This vulnerability allows bypassing AMSI (Anti-Malware Scan Interface) without using the VirtualProtect API and without changing memory protection settings.

🔍 **Vulnerability Details**

Microsoft's AMSI is designed to help detect and prevent malware by integrating security applications into software and inspecting their behavior before execution. The vulnerability discovered by Victor Khoury involves a writable entry inside System.Management.Automation.dll, which contains the address of AmsiScanBuffer. This entry should have been marked read-only but was not, allowing it to be manipulated to bypass AMSI.

💡 **Exploit Overview**

The exploit leverages the writable entry to overwrite the address of AmsiScanBuffer with a dummy function, effectively bypassing AMSI without invoking VirtualProtect. The proof of concept code is provided in both PowerShell and Python languages.

🚀 **Usage**

To execute the exploit:

1. Clone this repository to your local machine.
2. Open PowerShell or Python and execute the provided script.
3. Ensure that the desired payload is included in the exploit code before execution.
4. Monitor the execution to verify successful bypass of AMSI.

🔒 **Disclaimer**

This exploit is provided for educational and research purposes only. Use it responsibly and ethically. The authors do not take any responsibility for any misuse or damage caused by the exploitation of this vulnerability.

📎 **References**

- [OffSec Blog Post](https://www.offsec.com/offsec/amsi-write-raid-0day-vulnerability/)


👨‍💻 **Credits**

- **Victor Khoury (Vixx)** - Offsec Technical Trainer


</div>
