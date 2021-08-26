#!/usr/bin/python3
"""doing a deploming for all the services"""

import os
from re import A
import re
from fabric.api import *

env.hosts = ["34.73.50.135", "52.73.46.71"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """uploading a file to the remotes servers"""
    if not os.path.isfile(archive_path):
        return False

    upload = put(archive_path, "/tmp/")
    if upload.failed:
        return False

    file_ex = archive_path.split("/")
    file_out_ext = file_ex[1].split(".")

    direct = run(
        "mkdir -p /data/web_static/releases/{}".format(file_out_ext[0]))
    if direct.failed:
        return False

    uncompress = run(
        "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            file_ex[1], file_out_ext[0]))
    if uncompress.failed:
        return False

    removed = run("rm /tmp/{}".format(file_ex[1]))
    if removed.failed:
        return False

    movinf_file = run(
        "mv /data/web_static/releases/{}/web_static/*\
         /data/web_static/releases/{}".format(
            file_out_ext[0], file_out_ext[0]))
    if movinf_file.failed:
        return False

    link_rm = run("rm -rf /data/web_static/current")
    if link_rm.failed:
        return False

    new_link = run(
        "ln -s /data/web_static/releases/{} /data/web_static/current".format(
            file_out_ext[0]))
    if new_link.failed:
        return False

    return True
