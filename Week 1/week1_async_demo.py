
#Summary
#asyncio provides a framework to run single threaded concurrent codes using coroutines,event loops and non-blocking I/O ops
#there is no thread management no asyncio is faster on concurrent tasks
#asyncio is useful for blcking requests like API calls, DB calls,networks requests and file access





import asyncio #imports the asyncio module which has all the tools for asynchronoous programming like asyncio.run.asyncio.gather etc
import time

async def fetch_api(name,delay): #async declares this func as asynchronous
    print(f"Fetching {name}...")
    await asyncio.sleep(delay) #this waits or pauses execution until result is return wuthout blocking other tasks
    return f"{name} done"

async def main(): #the main async function which runs the program

    results=await asyncio.gather(fetch_api("Query 1",1),fetch_api("Query 2",2),fetch_api("Query 3",3)) #gather runs multiple coroutines concurrently  and waits for all to complete
    print (results)

asyncio.run(main()) #this creates an event loop and runs the main coroutine


