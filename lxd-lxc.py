lxd
----
$ lxd init
to initialize lxd.

$ lxc image list
to list all images locally downloaded.

$ lxc remote list
to list all remore repositories from which to download images.

$ lxc list
to list all current containers and its states.

$ lxc start/stop container_name
to start or stop a container.

$ lxc image delete fingerprint
to delete an image

$ lxc exec container -- command
to execute a command directely in a container.

$ lxc file edit container/path
to edit a file in a container.

$ lxc file push path container/path
to push a local file to a specific path in a container.

$ lxc snapshot container snapshot_name
to create a snapshot of a container.

$ lxc info container
to get some info about a container.

$ lxc restore container snapshot_name
to restore a container to a specific snapshot state.

$ lxc copy container/snapshot_name containerX
to create a containerX from a specific snapshot state.

$ lxc move containerX containerY
to rename a containerX to containerY.

$ lxc delete container/snapshot_name
to delete a specific snapshot_name.

$ lxc image list images:
to list all images in repo images.

$ lxc launch images:fingerprint container_name
to launch a container from an image.

$ lxc config set container_name limits.memory 2GB
to set a limit for a memory for a container.

$ lxc config set container_name limits.cpu 1
to set a limit for cpus for a container.

$ lxc storage list
to list all storage pools available.

$ lxc storage create storage2 dir
to create a new storage pool with driver dir.

$ lxc storage create storage3 zfs source=/dev/sdb
to create a new storage pool with driver zfs.

$ lxc launch image container_name --storage storage2
to launch a container in the new created stoage.

$ lxc list -c ns46tSb
to list all containers with specific columns.
