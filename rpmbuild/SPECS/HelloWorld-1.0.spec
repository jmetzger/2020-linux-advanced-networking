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

%install

install -d -m 0755 $RPM_BUILD_ROOT/opt/HelloWorld
install -m 0755 HelloWorld.sh $RPM_BUILD_ROOT/opt/HelloWorld/HelloWorld.sh

%clean

rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)

# %doc

/opt/HelloWorld/HelloWorld.sh

%changelog 
