import asyncio

from . import client, detectors


async def detect_nginx(domains):
    _client = client.HttpxClient()
    nginx_detector = detectors.Nginx(client=_client)

    print('###', [domain.name for domain in domains])
    detect_results = await asyncio.gather(
        *[nginx_detector(domain) for domain in domains]
    )
    print('!!!', [domain.name for domain in detect_results])

    await _client.close()

    return detect_results
