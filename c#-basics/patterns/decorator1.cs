namespace ConsoleApp18
{
    using System;

    // Interfejs bazowy
    public interface INapoj
    {
        string PobierzOpis();
        double PobierzKoszt();
    }

    // Konkretny komponent
    public class Kawa : INapoj
    {
        public string PobierzOpis() => "Kawa";
        public double PobierzKoszt() => 5.00;
    }

    // Dekorator bazowy
    public abstract class NapojDekorator : INapoj
    {
        protected INapoj _napoj;

        public NapojDekorator(INapoj napoj)
        {
            _napoj = napoj;
        }

        public virtual string PobierzOpis() => _napoj.PobierzOpis();
        public virtual double PobierzKoszt() => _napoj.PobierzKoszt();
    }

    // Konkretny dekorator: Mleko
    public class Mleko : NapojDekorator
    {
        public Mleko(INapoj napoj) : base(napoj) { }

        public override string PobierzOpis() => $"{_napoj.PobierzOpis()}, Mleko";
        public override double PobierzKoszt() => _napoj.PobierzKoszt() + 1.50;
    }

    // Konkretny dekorator: Cukier
    public class Cukier : NapojDekorator
    {
        public Cukier(INapoj napoj) : base(napoj) { }

        public override string PobierzOpis() => $"{_napoj.PobierzOpis()}, Cukier";
        public override double PobierzKoszt() => _napoj.PobierzKoszt() + 0.50;
    }

    // Program
    class Program
    {
        static void Main(string[] args)
        {
            INapoj kawa = new Kawa();
            Console.WriteLine($"{kawa.PobierzOpis()} - {kawa.PobierzKoszt()} zł");

            INapoj kawaZMlekiem = new Mleko(kawa);
            Console.WriteLine($"{kawaZMlekiem.PobierzOpis()} - {kawaZMlekiem.PobierzKoszt()} zł");

            INapoj kawaZMlekiemICukrem = new Cukier(kawaZMlekiem);
            Console.WriteLine($"{kawaZMlekiemICukrem.PobierzOpis()} - {kawaZMlekiemICukrem.PobierzKoszt()} zł");
        }
    }
}
