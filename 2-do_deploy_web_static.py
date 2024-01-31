#!/usr/bin/python3
# Distribute an archive to a web server.
import os.path
from fabric.api import run
from fabric.api import put
from fabric.api import env

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path to the archive to distribute.
    Returns:
        True if archive path is present else error on failure
        
    """
    if os.path.isfile(archive_path) is False:
        return False
    filename_with_extensions = archive_path.split("/")[-1]
    name = filename_with_extensions.split(".")[0]

    if put(archive_path, "/tmp/{}".format(filename_with_extensions)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(filename_with_extensions, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(filename_with_extensions)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
