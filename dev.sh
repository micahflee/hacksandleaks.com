#!/bin/bash

# Check if Node.js and npm are installed
if ! command -v node &> /dev/null || ! command -v npm &> /dev/null; then
    echo "Node.js and npm are required but not installed. Please install them and try again."
    exit 1
fi

# Create package.json if it doesn't exist
if [ ! -f package.json ]; then
    echo "Creating package.json"
    cat > package.json <<- EOM
{
  "name": "my_website",
  "version": "1.0.0",
  "description": "My Website using HTML, CSS, JavaScript, and Markdown",
  "scripts": {
    "start": "browser-sync start --server --files '**/*'"
  },
  "dependencies": {},
  "devDependencies": {
    "browser-sync": "^2.27.7"
  }
}
EOM
fi

# Install dependencies
echo "Installing dependencies"
npm install

# Start NPM
echo "Starting NPM"
npm start