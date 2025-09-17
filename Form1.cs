using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TextFileSplitter
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnBrowseInput_Click(object sender, EventArgs e)
        {
            openFileDialog.Filter = "Text Files|*.txt|All Files|*.*";
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                txtInputFile.Text = openFileDialog.FileName;
            }
        }

        private void btnBrowseOutput_Click(object sender, EventArgs e)
        {
            if (folderBrowserDialog.ShowDialog() == DialogResult.OK)
            {
                txtOutputDir.Text = folderBrowserDialog.SelectedPath;
            }
        }

        private async void btnSplit_Click(object sender, EventArgs e)
        {
            // Validate inputs
            if (string.IsNullOrEmpty(txtInputFile.Text))
            {
                MessageBox.Show("Please select an input file.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            if (string.IsNullOrEmpty(txtChunkSize.Text))
            {
                MessageBox.Show("Please enter a chunk size.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            if (!int.TryParse(txtChunkSize.Text, out int chunkSize) || chunkSize <= 0)
            {
                MessageBox.Show("Please enter a valid chunk size (positive integer).", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            string inputFile = txtInputFile.Text;
            string outputDir = txtOutputDir.Text;

            // If output directory is not specified, use the same directory as input file
            if (string.IsNullOrEmpty(outputDir))
            {
                outputDir = Path.GetDirectoryName(inputFile) ?? ".";
            }

            // Create output directory if it doesn't exist
            if (!Directory.Exists(outputDir))
            {
                try
                {
                    Directory.CreateDirectory(outputDir);
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Error creating output directory: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }
            }

            // Disable UI during processing
            btnSplit.Enabled = false;
            btnBrowseInput.Enabled = false;
            btnBrowseOutput.Enabled = false;
            txtInputFile.Enabled = false;
            txtChunkSize.Enabled = false;
            txtOutputDir.Enabled = false;

            try
            {
                await SplitFileAsync(inputFile, outputDir, chunkSize);
                lblStatus.Text = "File splitting completed successfully!";
                MessageBox.Show("File splitting completed successfully!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (Exception ex)
            {
                lblStatus.Text = "Error occurred during file splitting";
                MessageBox.Show($"Error occurred during file splitting: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally
            {
                // Re-enable UI
                btnSplit.Enabled = true;
                btnBrowseInput.Enabled = true;
                btnBrowseOutput.Enabled = true;
                txtInputFile.Enabled = true;
                txtChunkSize.Enabled = true;
                txtOutputDir.Enabled = true;
                progressBar.Value = 0;
            }
        }

        private async Task SplitFileAsync(string inputFile, string outputDir, int chunkSize)
        {
            // Check if input file exists
            if (!File.Exists(inputFile))
            {
                throw new FileNotFoundException("Input file not found.", inputFile);
            }

            lblStatus.Text = "Reading input file...";
            progressBar.Value = 10;

            // Read all lines from the input file
            string[] lines = await Task.Run(() => File.ReadAllLines(inputFile, Encoding.UTF8));
            
            lblStatus.Text = "Filtering lines...";
            progressBar.Value = 20;

            // Filter out empty lines and comments (lines starting with #)
            var filteredLines = lines.Where(line => !string.IsNullOrWhiteSpace(line) && !line.TrimStart().StartsWith("#")).ToList();
            
            int totalLines = filteredLines.Count;
            lblStatus.Text = $"Found {totalLines} valid lines to split...";
            progressBar.Value = 30;

            // Calculate number of chunks needed
            int numChunks = (totalLines + chunkSize - 1) / chunkSize;
            lblStatus.Text = $"Creating {numChunks} chunk files...";
            progressBar.Value = 40;

            // Create hosts_chunks subdirectory
            string chunksDir = Path.Combine(outputDir, "hosts_chunks");
            if (!Directory.Exists(chunksDir))
            {
                Directory.CreateDirectory(chunksDir ?? ".");
            }

            // Split into chunks
            for (int i = 0; i < numChunks; i++)
            {
                int startIdx = i * chunkSize;
                int endIdx = Math.Min(startIdx + chunkSize, totalLines);
                var chunkLines = filteredLines.GetRange(startIdx, endIdx - startIdx);

                // Create chunk filename
                string chunkFilename = $"hosts_part_{i + 1:00}_of_{numChunks:00}.txt";
                string chunkPath = Path.Combine(chunksDir ?? ".", chunkFilename);

                // Update progress
                int progress = 40 + (i * 50 / numChunks);
                lblStatus.Text = $"Writing chunk {i + 1} of {numChunks}...";
                progressBar.Value = progress;

                // Write chunk to file
                await Task.Run(() =>
                {
                    File.WriteAllLines(chunkPath ?? "chunk.txt", chunkLines, Encoding.UTF8);
                });

                // Update UI with created file info
                this.Invoke((MethodInvoker)delegate
                {
                    lblStatus.Text = $"Created: {chunkFilename} ({chunkLines.Count} lines)";
                });
            }

            progressBar.Value = 100;
            lblStatus.Text = $"All chunk files created in: {chunksDir ?? outputDir}";
        }
    }
}