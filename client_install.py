import subprocess

subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/client/RPMS/x86_64/kmod-lustre-client-2.10.0-1.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/client/RPMS/x86_64/lustre-client-2.10.0-1.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/client/RPMS/x86_64/lustre-iokit-2.10.0-1.el7.x86_64.rpm', shell=True)
subprocess.call('yum -y localinstall kmod-lustre-client-2.10.0-1.el7.x86_64.rpm lustre-client-2.10.0-1.el7.x86_64.rpm lustre-iokit-2.10.0-1.el7.x86_64.rpm', shell=True)


f = open("/etc/modprobe.d/lustre.conf", 'w')
f.write('options lnet networks="tcp1(enp0s8)"')
f.close()
subprocess.call('modprobe lustre', shell=True)
subprocess.call('lsmod | egrep "lustre|lnet"', shell=True)
subprocess.call('mkdir /mnt/lustre', shell=True)

subprocess.call('mount -t lustre  192.168.1.201@tcp1:/mylustre  /mnt/lustre', shell=True)
subprocess.call('echo "192.168.1.120@tcp1:/mylustre	/mnt/lustre	lustre defaults,_netdev 0 0" >> /etc/fstab', shell=True)
