namespace WinFormsApp12
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBoxButtons buttons = MessageBoxButtons.AbortRetryIgnore;
            DialogResult result = MessageBox.Show("Message Box Content", "Message Box Title", buttons, MessageBoxIcon.Information, MessageBoxDefaultButton.Button2);
            label2.Text = result.ToString();
        }
    }
}
