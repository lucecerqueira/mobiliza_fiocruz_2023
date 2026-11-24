#!/usr/bin/env python
import os
import sys
import time
import shutil
import socket
import subprocess


def garantir_container_postgres(host="127.0.0.1", port=5436, container="postgres_mobiliza"):
    if os.getenv("DATABASE_URL") or not shutil.which("docker"):
        return
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)
        if s.connect_ex((host, port)) == 0:
            return
    print(f"[Docker] Iniciando container '{container}' na porta {port}...")
    subprocess.run(["docker", "start", container], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(15):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            if s.connect_ex((host, port)) == 0:
                print(f"[Docker] Container '{container}' pronto!")
                return
        time.sleep(1)


if __name__ == "__main__":
    garantir_container_postgres()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
