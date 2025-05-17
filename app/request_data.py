"""Вынос конструкции 'async with session' в разные функции для сокращения кода"""


async def request_data_get(url, params, session):
    resp = await session.get(url, params=params)
    return resp.json()


async def request_data_post(url, data, headers, session):
    resp = await session.post(url, data=data, headers=headers)
    return resp.text
