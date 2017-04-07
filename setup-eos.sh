sudo apt update
sudo apt dist-upgrade -y
sudo apt install software-properties-common
sudo apt update
sudo add-apt-repository ppa:philip.scott/elementary-tweaks && sudo apt install elementary-tweaks -y
sudo apt install deluge vim -y
sudo apt install dconf-editor -y
gsettings set org.gnome.desktop.wm.preferences focus-mode 'mouse'
gsettings org.gnome.desktop.peripherals.touchpad send-events 'disabled-on-external-mouse'
