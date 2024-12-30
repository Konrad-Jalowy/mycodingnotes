# csharp winforms total basics
notes on basics of winforms

## Showing messagebox on click
```cs
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
            MessageBox.Show("Hello World!");
        }
    }
}
```

## MessageBox title and content
```cs
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
            MessageBox.Show("Message Box Content", "Message Box Title");
        }
    }
}
```

## Saving output to DialogResult and display
```cs
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
            DialogResult result = MessageBox.Show("Message Box Content", "Message Box Title");
            label2.Text = result.ToString();
        }
    }
}
```
## MessageBoxButtons
```cs
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
            MessageBoxButtons buttons = MessageBoxButtons.YesNo;
            DialogResult result = MessageBox.Show("Message Box Content", "Message Box Title", buttons);
            label2.Text = result.ToString();
        }
    }
}
```
## More MessageBoxButtons
```cs
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
            DialogResult result = MessageBox.Show("Message Box Content", "Message Box Title", buttons);
            label2.Text = result.ToString();
        }
    }
}
```
## MessageBoxIcon
you can always google them up
```cs
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
            DialogResult result = MessageBox.Show("Message Box Content", "Message Box Title", buttons, MessageBoxIcon.Warning);
            label2.Text = result.ToString();
        }
    }
}
```

## Default button
```cs
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
```

## Very simple counter winforms
```cs
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
```

## Read from file and show
```cs
namespace WinFormsApp13
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

       
        private void SetText(string text)
        {
            textBox1.Text = text;
        }


        private void button2_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    var sr = new StreamReader(openFileDialog1.FileName);
                    SetText(sr.ReadToEnd());
                }
                catch (SecurityException ex)
                {
                    MessageBox.Show($"Security error.\n\nError message: {ex.Message}\n\n" +
                    $"Details:\n\n{ex.StackTrace}");
                }
            }
        }
    }
}
```