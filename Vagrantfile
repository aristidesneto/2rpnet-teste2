Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"

  config.vm.network "forwarded_port", guest: 8080, host: 8080

  # config.vm.network "public_network", ip: "192.168.1.111", bridge: "enp1s0"
  config.vm.network "public_network", ip: "192.168.1.111"

  config.vm.hostname = 'teste-zeppelin'

  config.vm.disk :disk, size: "50GB", primary: true

  config.vm.provider "virtualbox" do |v|
    v.name = 'teste-zeppelin'
    v.memory = 4096
    v.cpus = 2
  end

  config.vm.provision "file", source: "provision/main.py", destination: "/home/vagrant/main.py"
  config.vm.provision "file", source: "provision/requirements.txt", destination: "/home/vagrant/requirements.txt"
  
  config.vm.provision "shell", inline: "sudo yum -y install python3-pip"
  config.vm.provision "shell", inline: "sudo pip3 install -r /home/vagrant/requirements.txt", :privileged => false
  config.vm.provision "shell", inline: "python3 /home/vagrant/main.py", :privileged => false
  
  config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "/home/vagrant/.ssh/id_rsa.pub"
  config.vm.provision "shell", inline: "cat /home/vagrant/.ssh/id_rsa.pub >> /home/vagrant/.ssh/authorized_keys"

end