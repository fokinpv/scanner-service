from app.detectify import scripts
from app.storage.models import Task


async def find_nginx(storage, domains):
    task = Task(domains)
    await storage.add(task)

    domain_infos = task.as_detectify_domains()
    domain_infos = await scripts.detect_nginx(domain_infos)

    task.domain_infos = domain_infos
    await storage.update(task)

    return [
        domain.name for domain in domain_infos
        if domain.properties.get('nginx', False)
    ]
