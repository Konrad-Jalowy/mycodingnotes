namespace WinFormsApp15
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            label3.Text = DateTime.Now.ToString("MM-dd-yy");
            label4.Text = new DateTime(DateTime.Now.Year+1, 1, 1).ToString("MM-dd-yy");

            TimeSpan difference =  new DateTime(DateTime.Now.Year+1, 1, 1) - DateTime.Now;
            if(difference.Days > 1)
            {
                label6.Text = difference.Days.ToString() + " dni";
            }
            else if (difference.Days == 1)
            {
                label6.Text = "1 dzień";
            } else
            {
                label6.Text = "Dzisiaj";
            }
            
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            TimeSpan differenceNow = new DateTime(DateTime.Now.Year + 1, 1, 1) - DateTime.Now;
            int daysLeft = differenceNow.Days;
            int hoursLeft = (daysLeft * 24) + differenceNow.Hours;
            label8.Text = $"{hoursLeft}:{differenceNow.Minutes}:{differenceNow.Seconds}";
        }
    }
}
