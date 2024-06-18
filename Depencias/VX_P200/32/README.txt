VeriFone Unified USB Driver Installer (32-bit): VerifoneUnifiedDriverInstaller.msi version 5.0.4.0
Build 10

This version contains a unified driver for Mx and Vx devices.

 - The installation/uninstall MUST be performed with administrative privileges
 - We recommend connecting your VeriFone device after finishing this
   installation, but if you have already connected it then simply cancel
   any "Found New Hardware" dialogs that pops up.

*** This release supports :*** 

    Windows platforms : 
           
        Win 10               32 bit    Microsoft Signed
        Win 8.1              32 bit    Microsoft Signed
        Win 8                32 bit    Microsoft Signed
        Win 7                32 bit    Microsoft Signed
        Win Vista            32 bit    Microsoft Signed
        Win XP               32 bit    Microsoft Signed
					
	Terminal Series	:
       
        Vx (both Verix V and eVo ).

			VX 510 Ethernet Terminal 
			VX 510 GPRS Terminal 
			VX 610 Terminal 
			VX 570 Terminal 
			VX 670 Terminal 
			VX 700 Terminal 
			VX 800 PIN Pad 
			VX 810 PIN Pad 
			VX 680 Terminal 
			VX 520 Terminal 
			VX 820 PIN pad 
			VX 805 Terminal 
			VX 825 Terminal 
			VX 520 GPRS Terminal 
			VX 680 CDMA Terminal  
			FD60 Terminal 
			V5/VMT USB UART Device
			VX 680 BlueTooth Terminal 
			VX 680 WiFi Terminal 
			VX 520 Sprocket Printer Terminal 
			VX 675 Terminal 
			VX 680 3G Terminal 
			VX GEN3 Terminal 
			VX 675 3G Terminal 
			VX 820 DUET base Terminal
			VX 805 DUET base Terminal
			VX 690 3G Terminal
			VX 685 Terminal
			VSP100 Terminal
			VX 600 payware mobile reader
			VX 690 BASE
			PP1000 Next Gen(V3)
			C520H Terminal
			C680 Terminal 

		Mx and UX

			Mx8 Terminal
			Mx9 Terminal
			Ux100 Terminal
			Ux200 Terminal
			Ux300 Terminal

		Engage Terminal
               
		
*** INSTALLATION PARAMETERS ***

PORT=#		        Specify port number (eg: "PORT=9", default is 9)
SINGLE_DEVICE_SYSTEM	Specify whether the system  will have one or many devices on it.  1 for one, 0 for many.
PORT_ROOT_LINK_NAME	Specify a custom symbolic link name.  Rather that COM<number>  you can specify ABC or any text.
DELAY_FOR_IO            Specify a delay for open/close calls.(eg: DELAY_FOR_IO=250). Default value is 250
INSTALL_RNDIS           Specify RNDIS installation for Windows OS prior to Windows 7. (eg: INSTALL_RNDIS=1 )
FILE_LOGGING_OFF        Specify File logging to be OFF or ON. (eg: FILE_LOGGING_OFF=1) 
                         default is 1 , file logging OFF. Use FILE_LOGGING_OFF=0 to make file logging ON.
IGNOREHWSERNUM          Specify to ignore harwdware serial number for PIDs AAAA & AAA0(eg: IGNOREHWSERNUM=1)
                         default is 0 , for enable use 1.

NOTE: If VerifoneUnifiedDriverInstaller.msi is ran without any parameters, the install will
      display a GUI allowing the user to select the installation options.


*** INSTALLATION OF BOTH  VX AND MX DEVICES ON SPECIFIC COM PORTS ***

This is a specific customer request.
Change the silent_install.bat file accordingly to support this feature. An example is shown below, 

msiexec /qn /i VerifoneUnifiedDriverInstaller.msi PORT_RETAIN=1 PORT_VX=6 PORT_MX=7 PORT_ROOT_LINK_NAME=COM

In the above example it has been set VX =COM6 and Mx =COM7 . It can change to any desired port on installation.

*** UNINSTALL ***

The VeriFone USB Driver Installer and installed drivers can be uninstalled from:
  - the Start Menu (All Programs->VeriFone->VeriFone USB Driver Installer->
    Uninstall VeriFone USB Driver Installer)
  - in Add/Remove Programs
  - Silent uninstall: run "msiexec /qn /x VerifoneUnifiedDriverInstaller.msi" 
    with administrative privileges


To change COM port AFTER device is installed and connected:
  - Regular: Run VerifoneUnifiedDriverInstaller.msi and follow the instructions to "Modify" 
             the install.
  - Silent: Re-run "VerifoneUnifiedDriverInstaller.msi  PORT=#" and pass in 
            the desired COM port parameters
  - Manual: in Device Manager, open the device properties and manually change the COM port
Note: the device COM port should be closed before trying to change the port #

Note: After un-installation of the VeriFone USB Driver Installer ny connected  devices will be disabled. The Found New Hardware
Wizard may not display when re-connecting the VeriFone device to the same port. The drivers will need 
to be reinstalled in order to use the device again.

Individual devices can be deleted from the system with the Verifone Device Manager in the Control Panel