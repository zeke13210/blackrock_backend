# blackrock_backend
This repo is meant to hold the backend code for the TOC + Blackrock coding project


KD: I could not access the server outside of the container with "flask run". Instead, I had to use this command:
flask run --host=0.0.0.0

KD: To use the new development database table (named: tasks_dev), set the DB_TABLE env var BEFORE executing the "flask run" command. The code will default to using the production DB table, unless the environment var is set.

- To set the dev table, execute:
export DB_TABLE=tasks_dev

- To unset the dev table (revert to prod version), execute:
unset DB_TABLE

KD: I could not access the server outside of the container with "flask run" instead, I had to use this command
flask run --host=0.0.0.0

<ul>
  <li>test</li>
  <li>test2</li>
</ul>


Getting Started
-------------
To download and utilize this API on your local machine please follow the below instructions

1. clone repo

2. Open cmd prompt run

>sudo pip install docker-compose

3. Navigate to local instance of repo and run

>docker-compose build

4. Once build is complete run cmd

>docker-compose up


Standard TaskManager API
----------------
To access the standard API docs for how to use the API please refer to the
<a href="https://documenter.getpostman.com/view/8843466/SVtPXARL?version=latest">Standard docs</a>

ERROR Testing API
--------------

To access the Error testing API please refer to the 
<a href="https://documenter.getpostman.com/view/8843466/SVtPXARL?version=latest">Error Testing API docs</a>

Admin API 
-----------
To access the admin API for the thread service docs please refer to the <a href="https://documenter.getpostman.com/view/8843466/SVtPXARH?version=latest">Admin API docs</a>

Contribution Guidelines
-----------------------

Authors
--------
To see the list of the current maintainers and contributors please refer to the <a href=" ">Authors doc</a>
