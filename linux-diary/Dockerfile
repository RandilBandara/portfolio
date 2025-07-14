# Use an official Ubuntu image as base
FROM ubuntu:22.04

# Install necessary packages: openssh-server, cron, sudo, tar, nano (optional editor)
RUN apt-get update && apt-get install -y \
    openssh-server cron sudo tar nano && \
    rm -rf /var/lib/apt/lists/*

# Setup SSH server
RUN mkdir /var/run/sshd

# Create a group and a user
RUN groupadd mygroup && \
    useradd -m -s /bin/bash -G mygroup myuser && \
    echo "myuser:password" | chpasswd && \
    echo "myuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Setup permissions on /data directory
RUN mkdir /data && chown root:mygroup /data && chmod 770 /data

# Create backup directory
RUN mkdir /backup && chown myuser:mygroup /backup

# Copy backup script into container
COPY backup.sh /home/myuser/backup.sh
RUN chown myuser:mygroup /home/myuser/backup.sh && chmod +x /home/myuser/backup.sh

# Setup cron job for user myuser (run daily at 2 AM)
RUN echo "0 2 * * * /home/myuser/backup.sh >> /var/log/backup.log 2>&1" > /etc/cron.d/backup-cron && \
    chmod 0644 /etc/cron.d/backup-cron && \
    crontab -u myuser /etc/cron.d/backup-cron

# Expose SSH port
EXPOSE 22

# Start cron and sshd on container startup
CMD service cron start && /usr/sbin/sshd -D
