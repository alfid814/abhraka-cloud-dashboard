#!/bin/bash
# Abhraka Cloud Dashboard - Automated Setup Script

set -e

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║     Abhraka Cloud Dashboard - Professional Setup              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Docker
echo -e "${YELLOW}[1/6] Checking Docker...${NC}"
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker not found. Please install Docker Desktop${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Docker found${NC}"

# Check Python
echo -e "${YELLOW}[2/6] Checking Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Python $(python3 --version)${NC}"

# Create virtual environment
echo -e "${YELLOW}[3/6] Creating virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate
echo -e "${GREEN}✅ Virtual environment created${NC}"

# Install dependencies
echo -e "${YELLOW}[4/6] Installing dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements.txt
echo -e "${GREEN}✅ Dependencies installed${NC}"

# Check LocalStack
echo -e "${YELLOW}[5/6] Checking LocalStack...${NC}"
if ! command -v localstack &> /dev/null; then
    echo -e "${YELLOW}⚠️ LocalStack not found. Installing...${NC}"
    pipx install localstack
fi
echo -e "${GREEN}✅ LocalStack ready${NC}"

# Setup complete
echo -e "${YELLOW}[6/6] Setup complete!${NC}"
echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  🚀 Next steps:                                              ║${NC}"
echo -e "${GREEN}║  1. Start LocalStack: localstack start                       ║${NC}"
echo -e "${GREEN}║  2. Activate venv: source venv/bin/activate                  ║${NC}"
echo -e "${GREEN}║  3. Run dashboard: python src/monitor_interaktif.py          ║${NC}"
echo -e "${GREEN}║  4. Open browser: http://localhost:5000                      ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"

chmod +x scripts/setup.shEOF
