#! /usr/bin/env bash

set -euf -o pipefail

# virtual environment directory
VENV_DIR=".venv"
PYTHON_SCRIPT="main.py"
REQUIREMENTS_FILE="requirements.txt"
VERBOSE=0

log() {
  if [ "$VERBOSE" -eq 1 ]; then
    echo "$1"
  fi
}

while [[ "$#" -gt 0 ]]; do
  case $1 in
    -v|--verbose) VERBOSE=1 ;;
    *) echo "UNKNOWN PARAMETER PASSED: $1"; exit 1 ;;
  esac
  shift
done

# check if venv exists
if [ -d "$VENV_DIR" ]; then
  log "This VENV already exists in '$VENV_DIR'"
else
  log "No VENV exists. Creating one in '$VENV_DIR'"

  # create venv
  python3 -m venv "$VENV_DIR"

  if [ -d "$VENV_DIR" ]; then
    log "Virtual environment successfully created in '$VENV_DIR'."
  else
    echo "Failed to create virtual environment"
    exit 1
  fi
fi

log "Activating the virtual environment..."
source "$VENV_DIR/bin/activate"

if [ "$VIRTUAL_ENV" != "" ]; then
  log "Virtual environment activated: $VIRTUAL_ENV"
else
  echo "Failed to activate the virtual environment."
  exit 1
fi

if [ -f "$REQUIREMENTS_FILE" ]; then
  log "Installing dependencies from '$REQUIREMENTS_FILE'..."
  pip install -r "$REQUIREMENTS_FILE"
  if [ $? -eq 0 ]; then
    log "Dependencies installed successfully"
  else
    echo "Failed to install dependencies."
    exit 1
  fi
else
  log "No requirements found"
fi

log "Running Python script: $PYTHON_SCRIPT"
python "$PYTHON_SCRIPT"

deactivate
log "end."