# Day 2: Backup Script
import datetime
def create_backup(source, dest):
    print(f'Backing up {source} to {dest} on {datetime.datetime.now()}')
    pass
create_backup('./data', './backups')
