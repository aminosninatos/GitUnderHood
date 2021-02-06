Vagrant commands
------------------
$ vagrant init box_name     --> for example: vagrant init ubuntu/trusty64
this will download the box from the cloud repo and create a vagrantfile. 

$ vagrant up
to start the vm.

$ vboxmanage list runningvms    --> to see running vms
$ vboxmanage list vms           --> to list vms      

$ vagrant ssh  --> to ssh into the current vm
by default there is a shared folder between the host (./) and guest (/vagrant).

$ vagrant [suspend resume]  [halt up] [destroy]

$ vagarant status   --> to see the status of your vms

$ vagrant box [list add remove]
to manage download boxes.

Vagrant config file
--------------------
config.vm.network "forwarded_port", guest:80, host:8080    --> to forward port
config.vm.provision "shell", path:"script.sh"   --> to provison a script

Multiple vms
--------------
config.vm.define "vm1" do |vm1|
    vm1.vm.hostname = "web"
    vm1.vm.box = "web"
end
    
config.vm.define "vm2" do |vm2|
    vm2.vm.hostname = "db"
    vm2.vm.box = "db"
end

Custom box
-----------
$ vagrant package custombox
to create a custom box from an existing environment.





