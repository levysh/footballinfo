VENV_NAME=.venv

# Create virtual environment to incapsulate dependencies
if [ ! -e $VENV_NAME ]; then
    sudo python3 -m venv $VENV_NAME;
fi

# Activate environment
source .venv/bin/activate

# Install dependencies
# pip3 install --user matplotlib==3.1.2
pip3 install --no-cache -r requirements.txt

# Configure environment variables
export FLASK_DEBUG=1 # to run flask test server in debug mode

# Run application
flask run --with-threads
