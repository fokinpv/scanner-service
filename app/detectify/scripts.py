import asyncio

from . import detectors


async def detect_nginx(domains):
    _client = detectors.nginx.HttpxClient()
    nginx_detector = detectors.Nginx(client=_client)

    detect_results = await asyncio.gather(
        *[nginx_detector(domain) for domain in domains]
    )

    await _client.close()

    return detect_results


async def detect_ip(domains):
    _client = detectors.ip.SocketClient()
    ip_detector = detectors.IP(client=_client)

    detect_results = await asyncio.gather(
        *[ip_detector(domain) for domain in domains]
    )

    return detect_results
