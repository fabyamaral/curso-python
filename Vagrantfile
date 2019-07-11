Vagrant.configure("2") do |config|
  # Ubuntu 18.04 - Bionic Beaver
  config.vm.define "ubuntu" do |ubuntu|
    ubuntu.vm.box = "bento/ubuntu-18.04"
    ubuntu.vm.hostname = "cursopython"
    ubuntu.vm.network "private_network", ip: "192.168.81.8"
    # configuration
    ubuntu.vm.provider "virtualbox" do |v|
      v.memory = 1024
    end
  end
end
