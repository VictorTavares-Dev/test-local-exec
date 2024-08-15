#!/bin/bash

# Define a log function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1"
}

# Example usage
log "Starting script execution"

DIR_NAME=$(date +%Y%m%d)

# Create a new directory
log "Creating directory './$DIR_NAME'"

mkdir $DIR_NAME

# Check if the directory was created successfully
if [ $? -eq 0 ]; then
    log "Directory created successfully"
else
    log "Failed to create directory. Aborting script execution."
    exit 1
fi

# Run pytest on test_script.py
log "Running 'pytest test_script.py'"
pytest test_script.py | tee $DIR_NAME/test_results.txt

# Check the exit code of pytest
if [ $? -eq 0 ]; then
    log "No errors detected. Running script.py..."
    python script.py | tee $DIR_NAME/output.txt
else
    log "Errors detected. Aborting script execution."
    exit 1
fi