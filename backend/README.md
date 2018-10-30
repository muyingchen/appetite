# Apetite Backend

Python version: 3.6.5

Setup:
    download:
        pip
        virtualenv
        
    ```
    virtualenv apetite # create virtual env
    source apetite/bin/activate # activate virtual env. It is for MacOS
    pip install -r requirement.txt # download dependencies
    
    # start the app
    export FLASK_ENV=development # You should use the development env
    export FLASK_APP=server.py
    flask run
    ``` 

