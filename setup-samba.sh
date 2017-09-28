#!/usr/bin/sudo


sudo apt update
sudo apt install samba -y
echo "Creating a Samba user stux"
sudo smbpasswd -a stux

sudo su -c 'printf "[WD]
path = /media/stux/WD Backup
avaliabe = yes
valid users = stux
read only = no
browsable = yes
public = yes
writable = yes" >> /etc/samba/smb.conf'

sudo service smbd restart
