##Getting Started Trouble Shooting - Step 4: Launch##
If your device's browser is not able to access the Fusion Interface, please check these items:  
>
>
- If you are unable to access the Fusion Interface using the **my.bot** URL, please check to see if your computer/device has any other active network connections.  Generally, when another network connection is active, (particularly a **wired** connection to the Internet), the computer tries to use that connection to convert the URL to an IP Address.  If this is the case, enter the IP Address for the Fusion Controller directly:  **http://192.168.50.1:8080**.  
>
- If neither the **my.bot** URL nor the IP Address http://192.168.50.1:8080 will open the Fusion Interface, check to see if you have any anti-malware software that is providing a local firewall installed on your device.  Very often, local firewalls are set to aggressively protect your computer and will block access on non-standard ports.  Check with your computer administrator to see if port 8080 can be opened to allow communication with the Fusion.  
>
- If your browser reports a security error when trying to access the Fusion, it suggests that your computer administrator may have set a policy that requires a **secure** connection.  Look at the address bar to see if you are still trying to access http://192.168.50.1:8080, or if the address bar now reads http**s**:192.168.50.1:8080.  If the browser has changed http:// to https://, it indicates that the computer is configured to only allow secure connections.  The Fusion does not support https connections at this time.  


