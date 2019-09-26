# blackrock_backend
This repo is meant to hold the backend code for the TOC + Blackrock coding project

KD: I could not access the server outside of the container with "flask run". Instead, I had to use this command:
flask run --host=0.0.0.0

KD: To use the new development database table (named: tasks_dev), set the DB_TABLE env var BEFORE executing the "flask run" command. The code will default to using the production DB table, unless the environment var is set.

- To set the dev table, execute:
export DB_TABLE=tasks_dev

- To unset the dev table (revert to prod version), execute:
unset DB_TABLE
