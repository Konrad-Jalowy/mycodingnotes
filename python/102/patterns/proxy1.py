class HeavyResource:
    def __init__(self):
        print("HeavyResource created!")

    def perform_task(self):
        print("Performing a heavy task...")

class ResourceProxy:
    def __init__(self):
        self._real_resource = None

    def perform_task(self):
        if self._real_resource is None:
            print("Initializing real resource...")
            self._real_resource = HeavyResource()
        self._real_resource.perform_task()

# Użycie
proxy = ResourceProxy()
proxy.perform_task()  # Real resource is initialized lazily
proxy.perform_task()  # Reuses the initialized resource
