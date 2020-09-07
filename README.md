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

### Network Troubleshooting and Monitoring 

#### Tools #### 

  • ping
  • traceroute
  • nmap
  • DNS and IP address testing

