from time import perf_counter

import httpx
from constants import IMAGES


def log_request(request: httpx.Request):
    print("-" * 20)
    print(f"-- Request: {request.method} {request.url}")


def main():
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

    # with httpx.Client(base_url="https://jsonplaceholder.typicode.com", event_hooks={"request": [log_request]}) as client:
    #     response = client.get("/posts").raise_for_status().json()
    #     print(response)

    #     response = client.post(
    #         "/posts",
    #         headers={'Content-type': 'application/json; charset=UTF-8'},
    #         json={
    #             'title': 'foo',
    #             'body': 'bar',
    #             'userId': 1,
    #         }
    #     ).raise_for_status().json()
    #     print(response)

    start = perf_counter()
    client = httpx.Client()
    for i, image in enumerate(IMAGES * 20):
        with open(f"images/sync_image_{i}.png", "wb") as file, client.stream("GET", image) as response:
            for chunk in response.iter_bytes():
                file.write(chunk)
    print(f"Sync: {round(perf_counter() - start, 2)}")


if __name__ == "__main__":
    raise SystemExit(main())
