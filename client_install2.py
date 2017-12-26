import subprocess

disk = [
	'/dev/sdb'
]

sysnetwork = {
	'network':'tcp1',
	'card':'enp0s8',
}

host = {
	'mds':{
		'host':'192.168.1.201',
	},
	'osd': {
		'host':'192.168.1.202',
		'index':0
	},
	'client':{
		'host':'192.168.1.203'
	},
}

ishost = 'client'

wget = [
	{
		'name':'kmod-lustre-client-2.10.0-1.el7.x86_64.rpm',
		'url':'https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/client/RPMS/x86_64/kmod-lustre-client-2.10.0-1.el7.x86_64.rpm',
	},
	{
		'name':'lustre-client-2.10.0-1.el7.x86_64.rpm',
		'url':'https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/client/RPMS/x86_64/lustre-client-2.10.0-1.el7.x86_64.rpm',
	},
	{
		'name':'lustre-iokit-2.10.0-1.el7.x86_64.rpm',
		'url':'https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/client/RPMS/x86_64/lustre-iokit-2.10.0-1.el7.x86_64.rpm',
	},
]

for pkg in wget:
	download_file = 'wget '+pkg['url']
	subprocess.call(download_file, shell=True)

pkg_file = 'yum install -y'
for pkg in wget:
	pkg_file = pkg_file +' '+ pkg['name'] + ' '

subprocess.call(pkg_file, shell=True)

f = open("/etc/modprobe.d/lustre.conf", 'w')
f.write('options lnet networks="'+sysnetwork['network']+'('+sysnetwork['card']+')"')
f.close()
subprocess.call('modprobe lustre', shell=True)
subprocess.call('lsmod | egrep "lustre|lnet"', shell=True)

subprocess.call('mkdir -p /lustre', shell=True)
subprocess.call('chmod 1777 /lustre', shell=True)
subprocess.call('mount -t lustre  '+host['mds']['host']+'@'+sysnetwork['network']+':/mylustre  /lustre', shell=True)
subprocess.call('echo "192.168.1.201@tcp1:/mylustre	/lustre	lustre defaults,_netdev 0 0" >> /etc/fstab', shell=True)

# subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/client/RPMS/x86_64/kmod-lustre-client-2.10.0-1.el7.x86_64.rpm', shell=True)
# subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/client/RPMS/x86_64/lustre-client-2.10.0-1.el7.x86_64.rpm', shell=True)
# subprocess.call('wget https://downloads.hpdd.intel.com/public/lustre/lustre-2.10.0/el7/client/RPMS/x86_64/lustre-iokit-2.10.0-1.el7.x86_64.rpm', shell=True)
# subprocess.call('yum -y localinstall kmod-lustre-client-2.10.0-1.el7.x86_64.rpm lustre-client-2.10.0-1.el7.x86_64.rpm lustre-iokit-2.10.0-1.el7.x86_64.rpm', shell=True)


# f = open("/etc/modprobe.d/lustre.conf", 'w')
# f.write('options lnet networks="tcp1(enp0s8)"')
# f.close()
# subprocess.call('modprobe lustre', shell=True)
# subprocess.call('lsmod | egrep "lustre|lnet"', shell=True)
# subprocess.call('mkdir /mnt/lustre', shell=True)

# subprocess.call('mount -t lustre  192.168.1.201@tcp1:/mylustre  /mnt/lustre', shell=True)
# subprocess.call('echo "192.168.1.201@tcp1:/mylustre	/mnt/lustre	lustre defaults,_netdev 0 0" >> /etc/fstab', shell=True)
