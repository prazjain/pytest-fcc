### Install uv tox uv_tox

>pip install uv  
>pip install tox  
>pip install tox-uv  
>pip install ruff  

Initialize uv in current dir and using venv environment created above. If you provide `uv init` this will create a new virtual environment `.venv`  

>uv init 
-----
If you have environment by another name then
Create environment by name venv  
>uv venv venv  

Initialize uv in current dir and using venv environment created above    
>export VIRTUAL_ENV=venv
>uv init  

Above init step creates pyproject.toml and .python-version files in the project directory  

Activate environment  
>venv/bin/activate  

Add packages :  (for --active flag to work, we need to have VIRTUAL_ENV environment variable set)
>uv add pytest --active  
or 
>uv pip install pytest --active   

Sync dependencies with uv  
>uv sync  

Run tests 
>pytest tests/test_circle.py -s  

-s shows the print statement printed from tests  

Check linting errors  
>ruff check .  

Fix fixable errors  
>ruff check . --fix  


Run tests :  
Below command will run tests in test_rectangle.py and show messages from print statements  
>pytest tests/test_rectangle.py -s  

Below command will run only tests that are marked as slow using `@pytest.mark.slow`  
>pytest tests/test_rectangle.py -m slow  



