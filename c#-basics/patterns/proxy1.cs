using System;

interface IService {
    void PerformOperation();
}

class RealService : IService {
    public void PerformOperation() {
        Console.WriteLine("Performing a real operation.");
    }
}

class ServiceProxy : IService {
    private readonly IService _realService;

    public ServiceProxy(IService realService) {
        _realService = realService;
    }

    public void PerformOperation() {
        Console.WriteLine("Logging: Operation is about to be performed.");
        _realService.PerformOperation();
        Console.WriteLine("Logging: Operation has been completed.");
    }
}

// Użycie
class Program {
    static void Main(string[] args) {
        IService realService = new RealService();
        IService proxy = new ServiceProxy(realService);

        proxy.PerformOperation();
    }
}
