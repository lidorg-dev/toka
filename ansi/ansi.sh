#!/bin/bash
sudo apt update -y
sudo apt install software-properties-common -y
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y
cd ansible
if ! command -v ansible-playbook &> /dev/null
then
    echo "ansible could not be found, the scirpt exit in ERROR"
    exit
fi


ansible-playbook playbooks/web.yaml
