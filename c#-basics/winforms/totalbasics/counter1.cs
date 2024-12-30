namespace WinFormsApp13
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            bool ok = int.TryParse(label2.Text, out int clickCount);

            if (!ok)
            {
                return;
            }

            clickCount++;

            label2.Text = clickCount.ToString();

        }
    }
}
