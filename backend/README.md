# Apetite Backend

Python version: 3.6.5

Setup:
    download:
        pip
        virtualenv
        
    ```
    virtualenv venv # create virtual env
    source venv/bin/activate # activate virtual env. It is for MacOS
    pip install -r requirement.txt # download dependencies
    
    # start the app
    export FLASK_ENV=development # You should use the development env
    export FLASK_APP=server.py
    flask run # server is running at port 5000
    ``` 

