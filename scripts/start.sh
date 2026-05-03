#!/bin/bash
# Abhraka Cloud Dashboard - Quick Start Script

echo "🚀 Starting Abhraka Cloud Platform..."

# Activate virtual environment
source venv/bin/activate

# Check if LocalStack is running
if ! curl -s http://localhost:4566/_localstack/health > /dev/null; then
    echo "⚠️ LocalStack is not running. Starting..."
    localstack start &
    sleep 5
fi

# Start dashboard
echo "📊 Starting dashboard at http://localhost:5000"
python src/.py

chmod +x scripts/start.sh
