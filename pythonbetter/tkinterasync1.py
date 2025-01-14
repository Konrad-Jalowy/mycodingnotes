import tkinter as tk
from tkinter import ttk
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Callable

class AsyncApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Async Tkinter App")

        # Create widgets
        self.label = tk.Label(root, text="Enter a number to square:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(root)
        self.entry.pack(pady=10)

        self.button = ttk.Button(root, text="Calculate", command=self.start_task)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.pack(pady=10)

        self.progress = ttk.Progressbar(root, mode="indeterminate")

        # ThreadPoolExecutor for async tasks
        self.executor = ThreadPoolExecutor(max_workers=2)

    def start_task(self):
        """Start the async task."""
        number = self.entry.get()
        if not number.isdigit():
            self.result_label.config(text="Result: Please enter a valid number.")
            return

        self.progress.pack(pady=10)
        self.progress.start()

        asyncio.run_coroutine_threadsafe(self.async_task(int(number)), asyncio.get_event_loop())

    async def async_task(self, number: int):
        """Run a time-consuming calculation asynchronously."""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(self.executor, self.calculate_square, number)

        self.progress.stop()
        self.progress.pack_forget()

        self.result_label.config(text=f"Result: {result}")

    @staticmethod
    def calculate_square(number: int) -> int:
        """Simulate a time-consuming calculation."""
        import time
        time.sleep(3)  # Simulate delay
        return number * number

if __name__ == "__main__":
    root = tk.Tk()
    app = AsyncApp(root)

    # Create and run the asyncio event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    def run_asyncio_loop():
        loop.run_forever()

    executor = ThreadPoolExecutor()
    executor.submit(run_asyncio_loop)

    root.mainloop()

    loop.stop()
    executor.shutdown()
