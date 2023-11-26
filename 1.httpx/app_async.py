import asyncio
from time import perf_counter

import httpx
from constants import IMAGES


async def log_request(request: httpx.Request):
    print("-" * 20)
    print(f"-- Request: {request.method} {request.url}")


async def main():
    # response = httpx.get("https://jsonplaceholder.typicode.com/posts")
    # if response.status_code == 200:
    #     print(response.json())

    # response = httpx.post(
    #     "https://jsonplaceholder.typicode.com/posts",
    #     headers={'Content-type': 'application/json; charset=UTF-8'},
    #     json={
    #         'title': 'foo',
    #         'body': 'bar',
    #         'userId': 1,
    #     }
    # ).raise_for_status().json()
    # print(response)

    # async with httpx.AsyncClient(base_url="https://jsonplaceholder.typicode.com", event_hooks={"request": [log_request]}) as client:
    #     response = (await client.get("/posts")).raise_for_status().json()
    #     print(response)

    #     response = (await client.post(
    #         "/posts",
    #         headers={'Content-type': 'application/json; charset=UTF-8'},
    #         json={
    #             'title': 'foo',
    #             'body': 'bar',
    #             'userId': 1,
    #         }
    #     )).raise_for_status().json()
    #     print(response)

    start = perf_counter()

    async def download_image(client, i, image):
        async with client.stream("GET", image) as response:
            with open(f"images/async_image_{i}.png", "wb") as file:
                async for chunk in response.aiter_bytes():
                    file.write(chunk)

    client = httpx.AsyncClient()
    await asyncio.gather(*[download_image(client, i, image) for i, image in enumerate(IMAGES * 20)])
    print(f"Sync: {round(perf_counter() - start, 2)}")


if __name__ == "__main__":
    asyncio.run(main())
