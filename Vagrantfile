# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "mds" do |mds|
     mds.vm.box = "CentosBox/Centos7-v7.3-Minimal"
     mds.vm.hostname = 'mds'
     mds.vm.network "public_network", ip: "192.168.1.201", bridge: "en1: Wi-Fi (AirPort)"
     #mds.vm.network :private_network, ip: "192.168.1.201"

     mds.vm.provider :virtualbox do |v|
       unless File.exist?('./mds1_2.vdi')
         v.customize ['createhd', '--filename', './mds1_2.vdi', '--variant', 'Fixed', '--size', 10 * 1024]
       end
       v.customize ['storageattach', :id,  '--storagectl', 'SATA', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', './mds1_2.vdi']
       v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
       v.customize ["modifyvm", :id, "--memory", 1024]
       v.customize ["modifyvm", :id, "--name", "mds"]
     end

     mds.vm.synced_folder ".", "/vagrant",disabled: true

   end

    config.vm.define "oss" do |oss|
      oss.vm.box = "CentosBox/Centos7-v7.3-Minimal"
      oss.vm.hostname = 'oss'
      oss.vm.network "public_network", ip: "192.168.1.202", bridge: "en1: Wi-Fi (AirPort)"
      #oss.vm.network :private_network, ip: "192.168.1.202"

      oss.vm.provider :virtualbox do |v|
        unless File.exist?('./oss1_2.vdi')
          v.customize ['createhd', '--filename', './oss1_2.vdi', '--variant', 'Fixed', '--size', 10 * 1024]
        end
        v.customize ['storageattach', :id,  '--storagectl', 'SATA', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', './oss1_2.vdi']
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--memory", 1024]
        v.customize ["modifyvm", :id, "--name", "oss"]
      end

      # Use NFS for the shared folder
      oss.vm.synced_folder ".", "/vagrant",disabled: true
    end

    config.vm.define "oss2" do |oss2|
      oss2.vm.box = "CentosBox/Centos7-v7.3-Minimal"
      oss2.vm.hostname = 'oss2'
      oss2.vm.network "public_network", ip: "192.168.1.204", bridge: "en1: Wi-Fi (AirPort)"
      #oss2.vm.network :private_network, ip: "192.168.1.202"

      oss2.vm.provider :virtualbox do |v|
        unless File.exist?('./oss1_3.vdi')
          v.customize ['createhd', '--filename', './oss1_3.vdi', '--variant', 'Fixed', '--size', 10 * 1024]
        end
        v.customize ['storageattach', :id,  '--storagectl', 'SATA', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', './oss1_3.vdi']
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--memory", 1024]
        v.customize ["modifyvm", :id, "--name", "oss2"]
      end

      # Use NFS for the shared folder
      oss2.vm.synced_folder ".", "/vagrant",disabled: true
    end
    
    config.vm.define "client" do |client|
      client.vm.box = "CentosBox/Centos7-v7.3-Minimal"
      client.vm.hostname = 'client'
      client.vm.network "public_network", ip: "192.168.1.203", bridge: "en1: Wi-Fi (AirPort)"
      #client.vm.network :private_network, ip: "192.168.1.203"

      client.vm.provider :virtualbox do |v|
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--memory", 1024]
        v.customize ["modifyvm", :id, "--name", "client"]
      end

      # Use NFS for the shared folder
      client.vm.synced_folder ".", "/vagrant",disabled: true
    end
end