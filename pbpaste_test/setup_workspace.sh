#!/bin/bash

# Setup Workspace Script
# This script sets up a terminal multiplexer for data processing workflows

# Check if zellij is installed
if ! command -v zellij &> /dev/null; then
    echo "Zellij is not installed. Installing using Homebrew..."
    brew install zellij
fi

# Create directory structure if it doesn't exist
mkdir -p ~/Desktop/ETL/data-agent/{pipeline1,pipeline2,pipeline3,alerts,notebooks,kafka,models,viz,etl,logs}

# Create example scripts
cat > ~/Desktop/ETL/data-agent/pipeline1/monitor.py << 'EOL'
#!/usr/bin/env python3
print("Pipeline 1 Monitor")
print("------------------")
print("Monitoring data pipeline 1...")
input("Press Enter to exit")
EOL

cat > ~/Desktop/ETL/data-agent/pipeline2/monitor.py << 'EOL'
#!/usr/bin/env python3
print("Pipeline 2 Monitor")
print("------------------")
print("Monitoring data pipeline 2...")
input("Press Enter to exit")
EOL

cat > ~/Desktop/ETL/data-agent/pipeline3/monitor.py << 'EOL'
#!/usr/bin/env python3
print("Pipeline 3 Monitor")
print("------------------")
print("Monitoring data pipeline 3...")
input("Press Enter to exit")
EOL

cat > ~/Desktop/ETL/data-agent/etl/extract.py << 'EOL'
#!/usr/bin/env python3
print("Extract Process")
print("--------------")
print("Watching for new data sources...")
input("Press Enter to exit")
EOL

cat > ~/Desktop/ETL/data-agent/etl/transform.py << 'EOL'
#!/usr/bin/env python3
print("Transform Process")
print("----------------")
print("Watching for data transformation jobs...")
input("Press Enter to exit")
EOL

cat > ~/Desktop/ETL/data-agent/etl/load.py << 'EOL'
#!/usr/bin/env python3
print("Load Process")
print("------------")
print("Watching for data loading jobs...")
input("Press Enter to exit")
EOL

# Make the scripts executable
chmod +x ~/Desktop/ETL/data-agent/pipeline*/monitor.py
chmod +x ~/Desktop/ETL/data-agent/etl/*.py

# Create Zellij layout file
cat > ~/Desktop/ETL/pbpaste_test/data_workspace.kdl << 'EOL'
layout {
    default_tab_template {
        pane size=1 borderless=true {
            plugin location="zellij:tab-bar"
        }
        children
        pane size=2 borderless=true {
            plugin location="zellij:status-bar"
        }
    }

    tab name="ETL" {
        pane split_direction="vertical" {
            pane name="Extract" {
                command "bash"
                args "-c" "cd ~/Desktop/ETL/data-agent/etl && python extract.py"
            }
            pane name="Transform" {
                command "bash"
                args "-c" "cd ~/Desktop/ETL/data-agent/etl && python transform.py"
            }
            pane name="Load" {
                command "bash"
                args "-c" "cd ~/Desktop/ETL/data-agent/etl && python load.py"
            }
        }
    }
}
EOL

echo "Workspace setup complete!"
echo "To start the workspace, run:"
echo "  zellij --layout ~/Desktop/ETL/pbpaste_test/data_workspace.kdl"
echo ""
echo "Note: You'll need to run this command in an interactive terminal, not within Claude Code."