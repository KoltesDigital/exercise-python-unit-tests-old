# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/eoan64"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y libclang1 python3 python3-pip
  SHELL
end
