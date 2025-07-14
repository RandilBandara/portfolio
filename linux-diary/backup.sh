#!/bin/bash
BACKUP_SRC="/data"
BACKUP_DEST="/backup"
DATE=$(date +%Y-%m-%d)
BACKUP_FILE="$BACKUP_DEST/backup-$DATE.tar.gz"

mkdir -p $BACKUP_DEST
tar -czf $BACKUP_FILE $BACKUP_SRC
echo "Backup completed: $BACKUP_FILE"
