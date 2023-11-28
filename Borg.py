 
# to create a Borg repo
> borg init --encryption=repokey  path_repo_directory

# to create an archive
> borg create --progress --list --info repo::archive src_directory

# to get info about a repo
> borg info repo

# to list the content of a repo
> borg list repo
> borg list --short repo

# to list the content of an archive
> borg list repo::archive
> borg list --short repo::archive

# to delete an archive
> borg delete repo::archive

# to extract an archive
> borg extract --progress --list repo::archive path_without_leading_slash extract_directory

# to extract a single file
> borg extract --progress --list repo::archive path_without_leading_slash_to_file extract_directory

# to extract a single file without the full path
> borg extract --progress --list --strip-components Number repo::archive path_without_slash_to_file extract_directory
Number : number of leading elements in the path.

