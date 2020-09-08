# 2020-Linux Advanced Networking - Training - Notes 

## Prerequisites 

```
We will use Centos 8 for the training 
```


## Topics 

### 1. Similarities New Distributions 

  * systemd 
  * journald 
  * firewalld 
  * ip 
  
### 2. DNS 

#### Overview 

#### Tools 

### 3. Managing System Services 

#### Overview 

  * System V 
  * Upstart
  * Systemd 
  
#### Layers of systemd 

  * /usr/lib 
  * /run/systemd
  * /etc/systemd/system 
  
#### Systemd commands -> Services  

```
# Start/Stop/Status
systemctl status sshd.service 
systemctl start sshd.service
systemctl stop sshd.service 

# See configuration of a service 
systemctl cat sshd.service 

# Show all running services 
systemctl list-units -t service 
systemctl -t service 

# Show all services 
systemctl list-unit-files -t service 

# disable/enable a service / is-enabled 
systemctl disable sshd 
systemctl enable sshd 
systemctl is-enabled sshd 
echo $? 

# mask/unmask 
systemctl mask sshd 
systemctl unmask sshd 

```

### 4. Network Configuration 

#### Runtime 

```
# main.example.com 
# adjust interface from eth0 -> ? 
ip addr add 10.200.45.100/24 dev eth0

# secondary.example 
# adjust interface from eth0 -> ?
# ip addr add 10.200.45.110/24 dev eth0

# Test the link from main.example.com -> secondary.example.com 
ping 10.200.45.110
# Test the link from secondary.example.com -> main.example.com
ping 10.200.45.100
```

#### Boot Time 
```
###
main.example.com 
###
# nano /etc/sysconfig/network-scripts/ifcfg-eth0:0
# And configure the settings:

DEVICE=eth0:0
BOOTPROTO=static
IPADDR=10.200.45.100
NETMASK=255.255.255.0
ONBOOT=yes

###
secondary.example.com 
###
# nano /etc/sysconfig/network-scripts/ifcfg-eth0:0
# And configure the settings:

DEVICE=eth0:0
BOOTPROTO=static
IPADDR=10.200.45.110
NETMASK=255.255.255.0
ONBOOT=yes

```

### 5. Network Troubleshooting and Monitoring 

#### Tools #### 

  * ping
  * traceroute
  * nmap
  * DNS and IP address testing
  
#### HTTPS - Client troubleshooting ####

```
openssl s_client -connect www.heise.de:https
# STEP 2: Within the connection  
openssl s_client -connect www.heise.de:https
GET / HTTP/1.1
HOST: www.thomas-krenn.com
```

### 6. Remote Access 

#### Cryptography Intro 


#### Secure Remote Access 


#### Remote Graphics 


### 7. Domain Name Service 

#### Overview of DNS 


#### BIND (named) Server 


#### BIND Zone Configuration 


### 8. HTTP Servers 

#### Apache 

#### Apache Configuration 

#### Apache Virtual Hosts 

#### Apache Security 


### 9. Advanced HTTP Servers 

#### mod_rerite 

#### mod_alias 

#### mod_status 

#### mod_perl 

#### Performance considerations 


### 10. Email Servers 

#### Email Overview 

#### Postfix 

#### Dovecot 

### 11. File Sharing 

#### FTP

#### vsftpd 

#### rsync 

#### SSH Based Protocols 

#### Other Protocols 

### 12. Advanced Networking 

#### Routing

#### VLANs 

#### DHCP

#### NTP 

### 13. HTTP Caching 

#### Overview 

#### Squid Configuration 

### 14. NFS 

#### NFS 

#### SMB/CIFS 

#### Other Network File Systems 

### 15. Introduction to Network Security 

#### Security Concepts 

#### Security Practices 

#### Security Tools 

### 16. Firewalls 

#### TCP Wrappers 

#### netfilter Concepts 

#### iptables Command 

#### Managing IPTables 

#### Advanced Firewalls 

### 17. Virtualization Overview 

#### Virtualization History 

#### libvirt 

#### Docker Example 

### 18. High Availability 

#### Overview 

#### DRDB 

### 19. System log 

#### Overview 

#### Remote Logging Client

#### Remote Logging Server 

### 20. Package Management 

#### Building RPM Packages 

https://image.slidesharecdn.com/els304-100324145410-phpapp02/95/configure-pack-and-distribute-an-rpm-creation-workshop-11-728.jpg?cb=1269442566

#### RPM Spec File Sections/Example  

http://ftp.rpm.org/max-rpm/s1-rpm-build-creating-spec-file.html

#### Build 

```
cd /usr/src/redhat/SPECS
rpmbuild -ba cdplayer-1.0.spec
```




