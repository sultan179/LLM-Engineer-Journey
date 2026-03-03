import asyncio
#this is a mock demo to present how context manager Async with works under the hood
class FakeAPISession:
    async def __aenter__(self):#this is called when entering async with block, this basically opens the connection 
        print("Opening API session...")
        await asyncio.sleep(1)
        print("API session opened.")
        return self 

    async def request(self, url):
        print(f"Requesting {url}...")
        await asyncio.sleep(1)
        return f"Response from {url}"

    async def __aexit__(self, exc_type, exc_val, exc_tb): #this is called when exits, this is a cleanup function , if any error is raised it handles it by the parameters
        print("Closing API session...")
        await asyncio.sleep(1)
        print("API session closed.")


async def main():
    async with FakeAPISession() as session:  #async because api calls or connections are awaitable
        response = await session.request("https://example.com")
        print(response)

asyncio.run(main())