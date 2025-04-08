from OpenSSL import crypto
import os

def generate_certificate(ip_address: str, cert_dir: str = "certs") -> None:
    """
    Generates a self-signed TLS certificate with given IP as SAN.
    :param ip_address: The IP to embed in Subject Alternative Name.
    :param cert_dir: Directory to store the generated cert and key.
    """
    os.makedirs(cert_dir, exist_ok=True)

    key_path = os.path.join(cert_dir, "server.key")
    cert_path = os.path.join(cert_dir, "server.crt")

    # Generate private key
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 4096)

    # Generate certificate
    cert = crypto.X509()
    cert.set_version(2)
    cert.set_serial_number(1)
    cert.get_subject().CN = "marzban-node"
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # 1 year validity
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)

    # Add Subject Alternative Name (SAN)
    san = f"IP:{ip_address}"
    san_extension = crypto.X509Extension(
        b"subjectAltName", False, san.encode()
    )
    cert.add_extensions([san_extension])

    # Sign the certificate
    cert.sign(key, 'sha512')

    # Save private key and cert
    with open(key_path, "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

    with open(cert_path, "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

    print(f"\u2705 Generated self-signed cert for IP: {ip_address} in `{cert_dir}/`")


ip = os.getenv("IP_ADDRESS", "127.0.0.1")
generate_certificate(ip)
