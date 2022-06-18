import subprocess
import urllib.request
import tarfile

# Install OpenJDK
subprocess.run(["sudo", "yum", "-y", "install", "java-11-openjdk-devel"])

# Download Apache Zeppelin
url = 'https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz'
urllib.request.urlretrieve(url, 'zeppelin-0.10.1-bin-all.tgz')

file = tarfile.open('zeppelin-0.10.1-bin-all.tgz')
file.extractall()

# Start Apache Zeppelin
subprocess.run(["/home/vagrant/zeppelin-0.10.1-bin-all/bin/zeppelin-daemon.sh", "start"])
