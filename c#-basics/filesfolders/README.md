# C# files and folders notes

## printing CWD
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string path = Directory.GetCurrentDirectory();
            Console.WriteLine("The current directory is {0}", path);
        }
    }
}
```

## Check if directory exists
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
         
            if (!Directory.Exists("./somefolder"))
            {
                Console.WriteLine("Doesnt exist");
            }
        }
    }
}
```

## path combine
remember not to use your own separators
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string basePath = Directory.GetCurrentDirectory();
            string directory = "somefolder";

            if (Directory.Exists(Path.Combine(basePath, directory)))
            {
                Console.WriteLine("Directory exists!");
            }
        }
    }
}
```

## create directory
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string basePath = Directory.GetCurrentDirectory();
            string directory = @"somefolder2";
            string path = Path.Combine(basePath, directory);
            Console.WriteLine(path);

            if (!Directory.Exists(path))
            {
                Console.WriteLine("Creating directory!");
                Directory.CreateDirectory(path);
            }
        }
    }
}
```

## Change CWD
### First way
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string target = @"C:\somepath";
            if (!Directory.Exists(target))
            {
                Directory.CreateDirectory(target);
            }
            Environment.CurrentDirectory = (target);
            Console.WriteLine(Directory.GetCurrentDirectory());
        }
    }
}
```
### Second way
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string target = @"C:\somepath";
            if (!Directory.Exists(target))
            {
                Directory.CreateDirectory(target);
            }
            Directory.SetCurrentDirectory(target);
            Console.WriteLine(Directory.GetCurrentDirectory());
        }
    }
}
```

## getfiles
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\somepath";

            if (!Directory.Exists(target))
            {
                Directory.CreateDirectory(target);
            }

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string[] files = Directory.GetFiles(cwd, "*");

            foreach (string file in files)
            {
                Console.WriteLine(file);
            }
        }
    }
}
```
## get filename
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\somepath";

            if (!Directory.Exists(target))
            {
                Directory.CreateDirectory(target);
            }

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string[] files = Directory.GetFiles(cwd, "*");

            foreach (string file in files)
            {
                Console.WriteLine(Path.GetFileName(file));
            }
        }
    }
}
```

## StreamWriter writing to a file
```cs
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string[] lines = { "First line", "Second line", "Third line" };

            using (StreamWriter outputFile = new StreamWriter(Path.Combine(cwd, "WriteLines.txt")))
            {
                foreach (string line in lines)
                    outputFile.WriteLine(line);
            }
        }
    
    }
}
```

## streamwriter append to a file
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string[] lines = { "First line", "Second line", "Third line" };

            using (StreamWriter outputFile = new StreamWriter(Path.Combine(cwd, "WriteLines.txt"), append: true))
            {
                foreach (string line in lines)
                    outputFile.WriteLine(line);
            }
        }
    
    }
}
```
## exists
and interpolation in c#
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string path = Path.Combine(cwd, "WriteLines.txt");

            if (File.Exists(path))
            {
                Console.WriteLine($"Working directory: {cwd}");
                Console.WriteLine($"File {Path.GetFileName(path)} exists!");
            }
        }
    
    }
}
```

## delete a file
```cs
using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string path = Path.Combine(cwd, "WriteLines.txt");

            if (File.Exists(path))
            {
                Console.WriteLine($"Working directory: {cwd}");
                Console.WriteLine($"File {Path.GetFileName(path)} exists!");
                File.Delete(path);
            }
            if (!File.Exists(path))
            {
                Console.WriteLine($"Working directory: {cwd}");
                Console.WriteLine($"File {Path.GetFileName(path)} no loner exists!");
            }

        }
    
    }
}
```
## reading file
```cs
using System;
using System.IO;
using System.Text;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string path = Path.Combine(cwd, "WriteLines.txt");

            if (File.Exists(path))
            {
                using (FileStream fs = File.OpenRead(path))
                {
                    byte[] b = new byte[1024];
                    UTF8Encoding temp = new UTF8Encoding(true);
                    int readLen;
                    while ((readLen = fs.Read(b, 0, b.Length)) > 0)
                    {
                        Console.WriteLine(temp.GetString(b, 0, readLen));
                    }
                }
            }
           

        }
    
    }
}
```

## Copy file
```cs
using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string sourcePath = Path.Combine(cwd, "WriteLines.txt");
            string destPath = Path.Combine(cwd, "WriteLinesCopy.txt");

            bool sourceExists = File.Exists(sourcePath);
            bool destExists = File.Exists(destPath);

            if (sourceExists)
            {
                if (!destExists)
                {
                    File.Copy(sourcePath, destPath);
                }
            }
        }
    }
}
```

## moving file
```cs
using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string sourcePath = Path.Combine(cwd, "WriteLinesCopy.txt");
         
            bool sourceExists = File.Exists(sourcePath);
            bool copiesExists = Directory.Exists(Path.Combine(cwd, "copies"));
            
            if (sourceExists && copiesExists)
            {
                string destPath = Path.Combine(cwd, "copies", "WriteLinesCopy.txt");
                File.Move(sourcePath, destPath);
            }            
        }
    }
}
```

## readalltext
```cs
using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string filePath = Path.Combine(cwd, "WriteLines.txt");

            if (File.Exists(filePath))
            {
                string text = File.ReadAllText(filePath);
                Console.Write(text);
            }
                  
        }
    }
}
```

## write all text append all text
```cs
using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string filePath = Path.Combine(cwd, "WriteLines2.txt");

            if (!File.Exists(filePath))
            {
                string createText = "Hello and Welcome" + Environment.NewLine;
                File.WriteAllText(filePath, createText);
            } else
            {
                string appendText = "File already exists, so we append that line" + Environment.NewLine;
                File.AppendAllText(filePath, appendText);
            }
        }
    }
}
```

## fileinfo
### check if exists, get fullname
```cs
using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting App!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string filePath = Path.Combine(cwd, "WriteLines3.txt");

            FileInfo myfile = new FileInfo(filePath);
            if (!myfile.Exists)
            {
                Console.WriteLine($"File {myfile.FullName} doesnt exist!");
            }
        }
    }
}
```
### FullName, Name, Create and Close
```cs
using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting App!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string filePath = Path.Combine(cwd, "WriteLines3.txt");

            FileInfo myfile = new FileInfo(filePath);
            if (!myfile.Exists)
            {
                myfile.Create().Close();
                Console.WriteLine($"File {myfile.FullName} created!");
            } else
            {
                Console.WriteLine($"File {myfile.Name} exists!");
            }
        }
    }
}
```
### CopyTo, DirectoryName
```cs
using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting App!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string filePath = Path.Combine(cwd, "WriteLines3.txt");

            FileInfo myfile = new FileInfo(filePath);
            if (myfile.Exists)
            {
                string destPath = Path.Combine(myfile.DirectoryName, $"Copy_{myfile.Name}");
                myfile.CopyTo(destPath);
            } 
        }
    }
}
```
### CopyTo returns another FileInfo (about our copy)
```cs
using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting App!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string filePath = Path.Combine(cwd, "WriteLines3.txt");

            FileInfo myfile = new FileInfo(filePath);
            if (myfile.Exists)
            {
                string destPath = Path.Combine(myfile.DirectoryName, $"Copy2_{myfile.Name}");
                FileInfo myCopy = myfile.CopyTo(destPath);
                Console.WriteLine(myfile.FullName);
                Console.WriteLine(myCopy.FullName);
            } 
        }
    }
}
```
### MoveTo method
returns void
```cs
using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting App!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string filePath = Path.Combine(cwd, "WriteLines3.txt");

            FileInfo myfile = new FileInfo(filePath);
            if (myfile.Exists)
            {
                string destPath = Path.Combine(myfile.DirectoryName, "moved", $"Moved_{myfile.Name}");
                myfile.MoveTo(destPath); //void
            } 
        }
    }
}
```