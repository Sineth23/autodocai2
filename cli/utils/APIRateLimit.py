
import asyncio

class APIRateLimit:
    def __init__(self, max_concurrent_calls: int = 50):
        self.queue = asyncio.Queue()
        self.in_progress = 0
        self.max_concurrent_calls = max_concurrent_calls

    async def call_api(self, api_function):
        def execute_call():
            self.in_progress += 1
            try:
                result = asyncio.run(api_function())
                return result
            except Exception as error:
                raise error
            finally:
                self.in_progress -= 1
                asyncio.create_task(self.dequeue_and_execute())

        await self.queue.put(execute_call)

        # Trigger the dequeue and execute operation when there are available slots for concurrent calls
        if self.in_progress < self.max_concurrent_calls:
            await self.dequeue_and_execute()

    async def dequeue_and_execute(self):
        while not self.queue.empty() and self.in_progress < self.max_concurrent_calls:
            next_call = await self.queue.get()
            await asyncio.create_task(next_call())

# Example usage:
# Define your API function, for example:
# async def my_api_function():
#     # Your API call here...
#     # Replace this with your actual API call implementation.
#     return "API call result"

# Define the APIRateLimit instance
# rate_limit = APIRateLimit(max_concurrent_calls=50)

# Call the API with rate limiting
# result = await rate_limit.call_api(my_api_function)
# print(result)
