import aiofiles

async def load_tls_credentials():
    async with aiofiles.open('certs/server.key', 'rb') as f:
        private_key = await f.read()
    async with aiofiles.open('certs/server.crt', 'rb') as f:
        certificate_chain = await f.read()
    return private_key, certificate_chain
