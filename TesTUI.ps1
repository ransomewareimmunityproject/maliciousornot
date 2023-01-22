# Import the necessary assemblies
Add-Type -AssemblyName PresentationFramework, WindowsBase

# Create a new WPF window
$window = New-Object System.Windows.Window

# Set the window's properties
$window.Title = "Harden Windows Against Malware"
$window.Width = 300
$window.Height = 300

# Create a Grid control
$grid = New-Object System.Windows.Controls.Grid
$grid.Margin = '10,10,0,0'
$grid.Width = 500
$grid.Height = 400

# Create a ListBox control
$listBox = New-Object System.Windows.Controls.ListBox
$listBox.Width = 400
$listBox.Height = 350
$listBox.SelectionMode = 'Multiple'
$options = "Option 1", "Option 2", "Option 3", "Option 4"
$listBox.ItemsSource = $options
$grid.Children.Add($listBox)

# Create an Execute button
$executeButton = New-Object System.Windows.Controls.Button
$executeButton.Content = "Execute"
$executeButton.Width = 100
$executeButton.Height = 30
$executeButton.Add_Click({
    foreach ($option in $listBox.SelectedItems) {
        switch ($option) {
            "Option 1" {Write-Host "You selected Option 1"}
            "Option 2" {Write-Host "You selected Option 2"}
            "Option 3" {Write-Host "You selected Option 3"}
            "Option 4" {Write-Host "You selected Option 4"}
        }
    }
})

# Create a StackPanel to hold the grid and the button
$stackPanel = New-Object System.Windows.Controls.StackPanel
$stackPanel.Orientation = 'Vertical'

# Add the grid to the stack panel
$stackPanel.Children.Add($grid)

# Add the button to the stack panel
$stackPanel.Children.Add($executeButton)

# Apply Fluent Design
$window.Resources = New-Object System.Windows.ResourceDictionary
$window.Resources.MergedDictionaries.Add((New-Object System.Windows.ResourceDictionary -ArgumentList @{
    Source = 'pack://application:,,,/Microsoft.Windows.SDK.Contracts;component/Foundation/Foundation.Xaml'
}))

# Set the window's content
$window.Content = $stackPanel

# Show the window
$window.ShowDialog() | Out-Null
