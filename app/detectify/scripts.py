import asyncio

from . import client, detectors


async def detect_nginx(domains):
    _client = client.HttpxClient()
    nginx_detector = detectors.Nginx(client=_client)

    detect_results = await asyncio.gather(
        *[nginx_detector(domain) for domain in domains]
    )

    await _client.close()

    return detect_results
