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
  
#### Systemd commands -> Services  

```
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


#### Boot Time 


