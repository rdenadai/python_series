from datetime import datetime
from socket import gethostname
from time import perf_counter
from uuid import NAMESPACE_DNS, uuid5

import netifaces
import psutil


def gen_uuid(name: str) -> str:
    return str(uuid5(NAMESPACE_DNS, name))


def to_gb(mem: float) -> float:
    return round(mem / 1073741824, 2)


def get_cpu_info() -> dict:
    percts = psutil.cpu_percent(percpu=True)
    freqs = psutil.cpu_freq(percpu=True)
    return {
        "cpu": [
            {
                "cpu_utilization": f"{perct}%",
                "cpu_freq": {"min": freq.min, "max": freq.max, "current": freq.current},
            }
            for perct, freq in zip(percts, freqs)
        ]
    }


def get_mem_info() -> dict:
    vmem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        "memory": {
            "total": to_gb(vmem.total),
            "used": to_gb(vmem.used),
            "available": to_gb(vmem.available),
            "free": to_gb(vmem.free),
        },
        "swap": {
            "total": to_gb(swap.total),
            "used": to_gb(swap.used),
            "free": to_gb(swap.free),
        },
    }


def get_disk_info() -> dict:
    partitions = psutil.disk_partitions()
    return {
        "disk": [
            {
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "fstype": partition.fstype,
                "usage": {
                    "total": to_gb(usage.total),
                    "used": to_gb(usage.used),
                    "free": to_gb(usage.free),
                    "percent": usage.percent,
                },
            }
            for partition in partitions
            if (usage := psutil.disk_usage(partition.mountpoint))
        ]
    }


def get_boot_time() -> dict:
    return {"boottime": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")}


def get_network_info() -> dict:
    return {
        "network": list(
            filter(
                None,
                (
                    {interface: netifaces.ifaddresses(interface).get(netifaces.AF_INET, None)}
                    for interface in netifaces.interfaces()
                ),
            )
        )
    }


def get_process_info() -> dict:
    process = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(
                attrs=[
                    "pid",
                    "name",
                    "username",
                    "cpu_percent",
                    "cpu_num",
                    "num_threads",
                    "memory_percent",
                ]
            )
            pinfo["memory_percent"] = round(pinfo["memory_percent"], 2)
            process.append(pinfo)
        except psutil.NoSuchProcess:
            ...
    return {"process": process}


def get_users_info() -> dict:
    return {"user": [{"name": user.name, "tty": user.terminal, "pid": user.pid} for user in psutil.users()]}


def main() -> None:
    start = perf_counter()
    name = gethostname()
    info = {
        "uuid": gen_uuid(name),
        "name": name,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data": get_boot_time()
        | get_cpu_info()
        | get_mem_info()
        | get_disk_info()
        | get_network_info()
        | get_process_info()
        | get_users_info(),
    }
    print(info)
    print(f"Time: {perf_counter() - start:.4f}s")


if __name__ == "__main__":
    main()
