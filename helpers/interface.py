import os
import textwrap

import aiofiles


async def add_interface_file(interface, directory: str = "/etc/wireguard") -> bool:
    try:
        content = textwrap.dedent(f"""
            [Interface]
            Address = {interface.ip_address}
            SaveConfig = {interface.save_config}
            PreUp = {interface.pre_up or ""}
            PostUp = {interface.post_up or ""}
            PreDown = {interface.pre_down or ""}
            PostDown = {interface.post_down or ""}
            ListenPort = {interface.listen_port or ""}
            PrivateKey = {interface.private_key}
        """).strip()

        file_path = os.path.join(directory, f"{interface.name}.conf")

        if os.path.exists(file_path):
            raise Exception(f"File by name: {interface.name} already exists")

        async with aiofiles.open(file_path, mode="w") as f:
            await f.write(content)

        return True

    except Exception as e:
        print("Error:", e)
        return False
