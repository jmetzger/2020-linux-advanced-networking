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

#### Example Build hello world  

  * https://sites.google.com/site/syscookbook/rhel/rhel-rpm-build

```
# root
dnf install rpm-build rpmdevtools git
# security concerns - do not run as root 
# non-root
exit # assuming coming from root 
cd
rpmdev-setuptree
cd ~/rpmbuild/SOURCES
mkdir HelloWorld-1.0
echo 'echo "hello world!"' > HelloWorld-1.0/HelloWorld.sh
chmod 755 HelloWorld-1.0/HelloWorld.sh
touch HelloWorld-1.0/configure
chmod 755 HelloWorld-1.0/configure
tar czvf HelloWorld-1.0.tar.gz HelloWorld-1.0
# now the spec 
cd
rpmdev-newspec rpmbuild/SPECS/HelloWorld-1.0.spec

# Now edit the settings 
vi ~/rpmbuild/SPECS/HelloWorld-1.0.spec

# Edit the following lines and change it to this:
Name: HelloWorld
Version: 1.0                       
Release: 1%{?dist}                 
Summary: Hello World Script
Group: Miscellaneous               
License: License text

# URL:
Source0: HelloWorld-1.0.tar.gz
BuildArch: noarch                  
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# BuildRequires:                   
# Requires: 

%description
This is a text describing what the Package is meant for

%prep

%setup -q

%build
# %configure                       <--- We have nothing to configure or compile
# make %{?_smp_mflags}                   so we comment these two lines out

%install

rm -rf $RPM_BUILD_ROOT

# make install DESTDIR=$RPM_BUILD_ROOT    <--- We have nothing to compile

install -d -m 0755 $RPM_BUILD_ROOT/opt/HelloWorld
install -m 0755 HelloWorld.sh $RPM_BUILD_ROOT/opt/HelloWorld/HelloWorld.sh

%clean

rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)

# %doc

/opt/HelloWorld/HelloWorld.sh       <--- We confirm the file(s) to install

%changelog
```

```
# building 
rpmbuild -ba rpmbuild/SPECS/HelloWorld-1.0.spec

# Assuming no errors occurred, new package is under the RPMS folder ready to be installed.
cd ~/rpmbuild/RPMS/noarch
ls -la 
# output 
# total 4
# -rw-rw-r-- 1 user user 2104 Sep 26 16:53 HelloWorld-1.0-1.el8.noarch.rpm

rpm -qpl HelloWorld-1.0-1.el6.noarch.rpm
# output 
# /opt/HelloWorld/HelloWorld.sh

# switch to root
sudo su 
rpm -ihv /home/user/rpmbuild/RPMS/noarch/HelloWorld-1.0-1.el8.noarch.rpm
rpm -qa HelloWorld
# Output 
# HelloWorld-1.0-1.el8.noarch

/opt/HelloWorld/HelloWorld.sh
# Output 
# Hello world!
