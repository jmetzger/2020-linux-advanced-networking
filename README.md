# 2020-LFS416-remote
LFS416 - Remote - Training - Notes 

## Tricky systemctl commands ## 

```
# show all services 

systemctl -t service
systemctl list-units -t service 

# show service httpd (not enabled / no running 
systemctl list-unit-files -t services --no-pager | grep httpd 

```

## Install Extension Pack Virtualbox ##

```
# enables autoscale + usb 2.0 
# Schritt 1:
# https://download.virtualbox.org/virtualbox/6.1.12/Oracle_VM_VirtualBox_Extension_Pack-6.1.12.vbox-extpack
# Schritt 2: (in virtualbox)
Datei -> Einstellungen -> Zusatzpakete
```

## Kali - Linux - Change Keyboard setting 

```
o Kali->Icon (Top,Left)-> Settings Keyboard
o Tab -> Layout -> Uncheck -> Use System Settings
o Add German 
o Change Layout Option: e.g. ALT + Space 
```

## Telekom - Security - Framework ##

```
# That is a really good guidance 
https://github.com/telekomsecurity/TelekomSecurity.Compliance.Framework
```

## SCAP ##

  * gesprochen es-cap 
  * Begriffsklärung: https://de.wikipedia.org/wiki/Security_Content_Automation_Protocol#:~:text=Das%20Security%20Content%20Automation%20Protocol,der%20US%2DRegierung%20f%C3%BCr%20SCAP.
