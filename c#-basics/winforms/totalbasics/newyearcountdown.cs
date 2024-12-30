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
            label6.Text = difference.Days.ToString() + " dni";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            TimeSpan differenceNow = new DateTime(DateTime.Now.Year + 1, 1, 1) - DateTime.Now;
            label8.Text = $"{differenceNow.Days} dni, {differenceNow.Hours}:{differenceNow.Minutes}:{differenceNow.Seconds}";
        }
    }
}