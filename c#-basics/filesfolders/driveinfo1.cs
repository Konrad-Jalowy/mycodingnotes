namespace ConsoleApp13
{
    class Program
    {
        
        static void Main(string[] args)
        {
            DriveInfo driveInfo = new DriveInfo("c:");
            Console.WriteLine("Name: " + driveInfo.Name);
            Console.WriteLine("Drive Type: " + driveInfo.DriveType);
            Console.WriteLine("Volume Label: " + driveInfo.VolumeLabel);
            Console.WriteLine("Root Directory: " + driveInfo.RootDirectory);
            Console.WriteLine("Total Size: " + (driveInfo.TotalSize / 1024 / 1024 / 1024) + " gb");
            Console.WriteLine("Free space: " + (driveInfo.AvailableFreeSpace / 1024 / 1024 / 1024) + " gb");
        }
    }
}
