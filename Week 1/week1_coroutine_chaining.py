#one async function awaiting another async function to build a multi step flow
#when two await are chained its sequential inside the function


import asyncio #imports the asyncio module which helps run the programs concurrently with its tools
import random
import time 

async def main():
    user_ids=[1,2,3]
    start=time.perf_counter() #records the start time of the main function
    await asyncio.gather(*(get_user_with_posts(user_id) for user_id in user_ids)) # *unpacks the args into individual args, gathers takes multiple coroutines as seperate coroutines and them all concurrently and waits for all to complete
    end=time.perf_counter()
    print(f"\n==> Total Time:{end-start:.2f} seconds")


async def get_user_with_posts(user_id): #here the 2 coroutines are chained
    user=await fetch_user(user_id) #calls the awaitable func and pauses execution until fethc_user is completed
    await fetch_posts(user) #waits for fetch_user to complete so the execution goes to event loop to handle and run another coroutine 

async def fetch_user(user_id):
    delay=random.uniform(0.5,2.0) #we set a random delay
    print(f"User coro:fetching user by {user_id=}...")
    await asyncio.sleep(delay) #we mimic a network request delay here
    user={"id":user_id,"name":f"User{user_id}"}
    print(f"User coro: fetched user with {user_id=} (done in {delay:.1f}s).")
    return user #return user when success



async def fetch_posts(user):
    delay = random.uniform(0.5, 2.0)
    print(f"Post coro: retrieving posts for {user['name']}...")
    await asyncio.sleep(delay) #pauses execution without blocking other coroutines
    posts = [f"Post {i} by {user['name']}" for i in range(1, 3)] #list comprehension:loop in range and create posts items inside the array according to the number of range limit
    print(
        f"Post coro: got {len(posts)} posts by {user['name']}"
        f" (done in {delay:.1f}s):"
    )
    for post in posts:
        print(f" - {post}")

if __name__ == "__main__": #entry point to the program
    random.seed(444) #we start with a seed number so random numbers are always same
    asyncio.run(main()) #creates event loop and starts the main coroutines
    

