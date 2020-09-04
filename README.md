# 2020-LFS416-remote
LFS416 - Remote - Training - Notes 

## openvas -> gvm (Greenbone Vulnerability Management) / mrazavi 

```
Installation on Ubuntu 20.04 LTS
https://launchpad.net/~mrazavi/+archive/ubuntu/gvm
https://www.osboxes.org/ubuntu/
```

## dnf / dnf-automatic 

```
https://cheatography.com/misterrabinhalder/cheat-sheets/dnf/
https://computingforgeeks.com/enable-automatic-software-updates-on-centos-rhel-8/
```


## Failed users 

### Remote Users 

```
journalctl -u sshd.service | grep -i "failed password" 
cat /var/log/secure | "Failed password" 
```


## nmap 

https://nmap.org/man/de/man-performance.html

### Timing templates 

https://nmap.org/man/de/man-performance.html
https://nmap.org/book/performance-timing-templates.html

### legal issues
https://nmap.org/book/legal-issues.html

## Logwatch and systemd ##

  * at least version 7.4. needed 
  * https://bugzilla.redhat.com/show_bug.cgi?id=1504984

## Linux Security pdf ##

http://schulung.t3isp.de/documents/linux-security.pdf

## Tricky systemctl commands ## 

```
# show all services 

systemctl -t service
systemctl list-units -t service 

# show service httpd (not enabled / no running 
systemctl list-unit-files -t services --no-pager | grep httpd 

```

## nftable - commands ##

```
# Show all nft rules 
nft list ruleset 
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

## OSCAP 
```
OpenScap
yum install openscap-scanner
yum install scap-security-guide
ls -l  /usr/share/xml/scap/ssg/content/ssg-*-ds.xml
oscap info  /usr/share/xml/scap/ssg/content/ssg-centos7-ds.xml
oscap xccdf eval      \--profile xccdf_org.ssgproject.content_profile_standard \--results-arf arf.xml  \--report report.html   \/usr/share/xml/scap/ssg/content/ssg-centos7-ds.xml

Report und /tmp/report.html 
```

## SCAP ##

  * gesprochen es-cap 
  * Begriffsklärung: https://de.wikipedia.org/wiki/Security_Content_Automation_Protocol#:~:text=Das%20Security%20Content%20Automation%20Protocol,der%20US%2DRegierung%20f%C3%BCr%20SCAP.
