
<!-- ![alt airflow image](./img_src/airflowlogo.png) -->
<img src="./img_src/airflowlogo.png" height='250 rem' width='300 rem'></img> 
# airflow
<br>
For tutorial: 

https://www.youtube.com/watch?v=K9AnJ9_ZAXE&list=PLwFJcsJ61oujAqYpMp1kdUBcPG0sE0QMT


1.  What is `airflow` and why do we `need` it ?
    -   Airflow is a `workflow orchestration platform` that allows users to programmatically create, schedule, and monitor workflows.
            It's often used to automate machine learning tasks and create complex `data pipelines`. 


## Installation on local environment

1.  try method A or B
<br>
`method A`

    ```sh
    AIRFLOW_VERSION=2.10.4

    # Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
    # See above for supported versions.
    PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

    CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
    # For example this would install 2.10.4 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.10.4/constraints-3.8.txt

    pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

    ```
Or, use 
<br>
`method B`

```sh
# this installs the requirement for airflow specified in requirement.txt
pip install -r requirements.txt
```

2.  Specify the AIRFLOW_HOME dir 
<br>
For default behaviour  use 

```sh
export AIRFLOW_HOME=~/airflow
```
for using airflow in current directory use

```sh
export AIRFLOW_HOME=.
```


3. create `airflow.cfg` file and add the file
```sh
# add absolute Path to sqlite after //// slashes
[core]
sql_alchemy_conn = sqlite:////abs/path/to/project/dir/airflow.db
# replace abs/path/to/project/dir with absolute project path dir or dir where you want to create an airflow sqlite database
```

4.  Run Airflow Standalone:

    The airflow standalone command initializes the database, creates a user, and starts all component
    
```sh
airflow standalone
```

5. use this as cred (as it is shown in terminal after running step 4)
```sh
Login with username: admin  password: 7a4HAYQ2cmwDAHDy
```
for the UI interface goto (default)

http://localhost:8080 
