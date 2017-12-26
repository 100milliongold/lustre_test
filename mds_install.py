import subprocess


subprocess.call('wget https://downloads.hpdd.intel.com/public/e2fsprogs/1.42.13.wc6/el7/RPMS/x86_64/libcom_err-1.42.13.wc6-7.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/e2fsprogs/1.42.13.wc6/el7/RPMS/x86_64/e2fsprogs-libs-1.42.13.wc6-7.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/e2fsprogs/1.42.13.wc6/el7/RPMS/x86_64/libss-1.42.13.wc6-7.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/e2fsprogs/1.42.13.wc6/el7/RPMS/x86_64/e2fsprogs-1.42.13.wc6-7.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/server/RPMS/x86_64/kmod-lustre-2.10.0-1.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/server/RPMS/x86_64/lustre-osd-ldiskfs-mount-2.10.0-1.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/server/RPMS/x86_64/kmod-lustre-osd-ldiskfs-2.10.0-1.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/server/RPMS/x86_64/kmod-lustre-2.10.0-1.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/server/RPMS/x86_64/lustre-2.10.0-1.el7.x86_64.rpm', shell=True)
subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/server/RPMS/x86_64/lustre-iokit-2.10.0-1.el7.x86_64.rpm', shell=True)


subprocess.call('yum -y localinstall libcom_err-1.42.13.wc6-7.el7.x86_64.rpm e2fsprogs-libs-1.42.13.wc6-7.el7.x86_64.rpm libss-1.42.13.wc6-7.el7.x86_64.rpm e2fsprogs-1.42.13.wc6-7.el7.x86_64.rpm kmod-lustre-2.10.0-1.el7.x86_64.rpm lustre-osd-ldiskfs-mount-2.10.0-1.el7.x86_64.rpm kmod-lustre-osd-ldiskfs-2.10.0-1.el7.x86_64.rpm lustre-2.10.0-1.el7.x86_64.rpm lustre-iokit-2.10.0-1.el7.x86_64.rpm', shell=True)

f = open("/etc/modprobe.d/lustre.conf", 'w')
f.write('options lnet networks="tcp1(enp0s8)"')
f.close()
subprocess.call('modprobe lustre', shell=True)
subprocess.call('mkfs.lustre --fsname=mylustre --mdt --mgs --index=0 /dev/sdb', shell=True)
subprocess.call('mkdir /mnt/mdt1', shell=True)
subprocess.call('mount -t lustre /dev/sdb /mnt/mdt1', shell=True)
subprocess.call('echo "/dev/sdb	/mnt/mdt1	lustre defaults,_netdev 0 0" >> /etc/fstab', shell=True)
#curfiles = subprocess.check_output('ls -w', shell=True).split()
#print curfiles