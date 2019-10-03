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


INSTALLATION
-------------
To install and use the blackrock-api container run the below cmds

<p> >docker pull zeke13210/blackrock:prod</p>
<p> >docker container run -it -p 5000:5000 zeke13210/blackrock:prod</p>
<p> >cd app/blackrock_backend</p>
<p> >python app.py</p>


TaskManager API
----------------
API for Techs of Color - BlackRock - TaskManager challenge

Request project details here:

  -web: https://techsofcolor.org
  -slack: https://technologistsofcolor.slack.com/messages/CDZU6JR3L
  -meetup: https://www.meetup.com/Technologists/

ERROR REQUESTS
--------------

Create Task
-------------
POST Create a task - Invalid Name
>http://127.0.0.1:5000/task_create
Create a task with an invalid name

HEADERS
Content-Typeapplication/x-www-form-urlencoded
BODY  *urlencoded*
descriptionBuilding a paper bath
Optional

name
1 or more alphanumaric characters required

priority1
1 - 5 (high - low)

runtimeHours0
0 - 23

runtimeMinutes4
0 - 59

runtimeSeconds0
0 - 59



Example Request
-Invalid Input Request
curl --location --request POST "http://127.0.0.1:5000/task_create" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data "description=%3Cstring%3E&name=%3Cstring%3E&priority=2&runtimeHours=%3Cinteger%3E&runtimeMinutes=%3Cinteger%3E&runtimeSeconds=%3Cinteger%3E&status=PENDING"
Example Response
-422 － Bad Request
{
  "error": "422 Unprocessable Entity: name must be 1 or more alphanumeric characters"
}


POST Create a task - Invalid Priority
--------------------------------------
>http://127.0.0.1:5000/task_create
Create a task with an invalid priority

HEADERS
Content-Typeapplication/x-www-form-urlencoded

BODY urlencoded
descriptionBuilding a paper bath
Optional

name
Build a bath
1 or more alphanumaric characters required

priority11
1 - 5 (high - low)

runtimeHours0
0 - 23

runtimeMinutes4
0 - 59

runtimeSeconds0
0 - 59



Example Request
curl --location --request POST "http://127.0.0.1:5000/task_create" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data "description=Building%20a%20paper%20bath&name=Build%20a%20bath&priority=11&runtimeHours=0&runtimeMinutes=4&runtimeSeconds=0"
Example Response
422 － Bad Request
{
  "error": "422 Unprocessable Entity: priority (11) must be betwen 1 - 5"
}

POST Create a task - Invalid Hour
----------------------------------
>http://127.0.0.1:5000/task_create
Create a task with an invalid Hour value

HEADERS
Content-Typeapplication/x-www-form-urlencoded

BODY urlencoded
descriptionBuilding a paper bath
Optional

nameBuild a bath
1 or more alphanumaric characters required

priority2
1 - 5 (high - low)

runtimeHours25
0 - 23

runtimeMinutes4
0 - 59

runtimeSeconds0
0 - 59



Example Request
curl --location --request POST "http://127.0.0.1:5000/task_create" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data "description=Building%20a%20paper%20bath&name=Build%20a%20bath&priority=2&runtimeHours=25&runtimeMinutes=4&runtimeSeconds=0"
Example Response
422 － Bad Request
{
  "error": "422 Unprocessable Entity: Hour (25) must be less than 24"
}

POST Create a task - Invalid Minute
-----------------------------------
>http://127.0.0.1:5000/task_create
Create a task with an invalid Minute value

HEADERS
Content-Typeapplication/x-www-form-urlencoded
BODY urlencoded
descriptionBuilding a paper bath
Optional

nameBuild a bath
1 or more alphanumaric characters required

priority2
1 - 5 (high - low)

runtimeHours1
0 - 23

runtimeMinutes60
0 - 59

runtimeSeconds0
0 - 59



Example Request
curl --location --request POST "http://127.0.0.1:5000/task" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data "description=%3Cstring%3E&name=%3Cstring%3E&priority=2&runtimeHours=%3Cinteger%3E&runtimeMinutes=%3Cinteger%3E&runtimeSeconds=%3Cinteger%3E&status=PENDING"
Example Response
500 － Internal Server Error
{
  "statusCode": "<string>",
  "message": "<string>"
}
  
POST Create a task - Invalid Second
------------------------------------
>http://127.0.0.1:5000/task_create
Create a task with an invalid second value

HEADERS
Content-Typeapplication/x-www-form-urlencoded

BODY urlencoded
descriptionBuilding a paper bath
Optional

nameBuild a bath
1 or more alphanumaric characters required

priority2
1 - 5 (high - low)

runtimeHours1
0 - 23

runtimeMinutes0
0 - 59

runtimeSeconds60
0 - 59



Example Request
curl --location --request POST "http://127.0.0.1:5000/task_create" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data "description=Building%20a%20paper%20bath&name=Build%20a%20bath&priority=2&runtimeHours=0&runtimeMinutes=64&runtimeSeconds=0"
Example Response
422 － Bad Request
{
  "error": "422 Unprocessable Entity: Minute (60) must be less than 60"
}

POST Create a task - Invalid Time
---------------------------------
>http://127.0.0.1:5000/task_create
Create a task with an invalid total time

Total time cannot be less than 5 seconds
Total time cannot be more than 24 hours
HEADERS
Content-Typeapplication/x-www-form-urlencoded

BODY urlencoded
descriptionBuilding a paper bath
Optional

nameBuild a bath
1 or more alphanumaric characters required

priority1
1 - 5 (high - low)

runtimeHours0
0 - 23

runtimeMinutes0
0 - 59

runtimeSeconds4
0 - 59



Example Request
curl --location --request POST "http://127.0.0.1:5000/task" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data "description=Building%20a%20paper%20bath&name=Build%20a%20bath&priority=1&runtimeHours=0&runtimeMinutes=0&runtimeSeconds=4"
Example Response
422 － Bad Request
{
  "error": "422 Unprocessable Entity: Total runtime (4 seconds) must be greater than 5 seconds"
}

PUT Create a task - Bad Request
-------------------------------
>http://127.0.0.1:5000/task_create
Create a task with an invalid method request

This API requires a POST request
NOTE: We will try to force all errors to return as JSON with a future release
HEADERS
Content-Typeapplication/x-www-form-urlencoded
BODY urlencoded
description
Optional

nameBuild a bath
1 or more alphanumaric characters required

priority1
1 - 5 (high - low)

runtimeHours0
0 - 23

runtimeMinutes4
0 - 59

runtimeSeconds0
0 - 59



Example Request
curl --location --request POST "http://127.0.0.1:5000/task_create" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data "description=&name=Build%20a%20bath&priority=1&runtimeHours=0&runtimeMinutes=4&runtimeSeconds=0"
Example Response
405 － Bad Request
405 METHOD NOT ALLOWED
  
PUT Update task- Bad status
---------------------------
>http://127.0.0.1:5000/task_update/1
Update the specified task with an invalid status

Statuses should be one of the following:

PENDING: Initial state of a task prior to execution
ACTIVE: State of a task while in action
COMPLETED: Final state, once a task is complete
HEADERS
Content-Typeapplication/json
BODY raw
{
    "status": "STARTING"
}


Example Request
Bad Status Update
curl --location --request PUT "http://127.0.0.1:5000/task_update/1" \
  --header "Content-Type: application/json" \
  --data "{
    \"status\": \"STARTING\"
}"
Example Response
422 － Bad Request
{
  "error": "422 Unprocessable Entity: Status (STARTING) not valid. Expecting: PENDING, ACTIVE or COMPLETED"
}
GET Get task - Bad Task ID
>http://127.0.0.1:5000/task/100000
Request a task that does not exist



Example Request
curl --location --request GET "http://127.0.0.1:5000/task/0"
Example Response
404 － Not Found
{
  "error": "404 Not Found: Task not found"
}

POST Get all tasks - Bad Request
--------------------------------
>http://127.0.0.1:5000/tasks
Request all tasks with an invalid request method

NOTE: We will try to force all errors to return as JSON with a future release


Example Request
Bad Method Request
curl --location --request GET "http://127.0.0.1:5000/tasks"
Example Response
405 － Method Not Allowed
METHOD NOT ALLOWED

GET Get task
------------
>http://127.0.0.1:5000/task/1
Return the requested task

EX: http://HOST.URL/task/task_id
In our example task_id = 1


Example Request
Client - Server Request
curl --location --request GET "http://127.0.0.1:5000/task/1"
Example Response
200 － OK
{
  "priority": 1,
  "status": "ACTIVE",
  "name": "Two min",
  "task_id": 1,
  "currenttime": "2019-09-22 12:43:39.568674",
  "createdtime": "2019-09-21 23:27:57.650238",
  "endtime": "2019-09-22 00:28:58.650238",
  "starttime": "2019-09-21 23:27:57.650238",
  "description": "2 and done"
}

POST Create task
-----------------
>http://127.0.0.1:5000/task_create
Create a new task

Only client apps should create new tasks
NOTE: This expects the request data from a form.
HEADERS
Content-Typeapplication/x-www-form-urlencoded
BODY urlencoded
descriptionSample description
Optional

nameSample name
1 or more alphanumaric characters required

priority1
1 - 5 (high - low)

runtimeHours0
0 - 23

runtimeMinutes4
0 - 59

runtimeSeconds0
0 - 59



Example Request
Client Request
curl --location --request POST "http://127.0.0.1:5000/task_create" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data "description=TEST%20DESCRIPTION&name=TEST%20NAME&priority=2&runtimeHours=1&runtimeMinutes=1&runtimeSeconds=1"
Example Response
200 － OK
{
  "message": "Task created"
}

PUT Update task
---------------
>http://127.0.0.1:5000/task_update/1
Update the specified task

EX: http://HOST.URL/task_update/task_id
In our example task_id = 1
HEADERS
Content-Typeapplication/json
BODY raw
{
    "status": "ACTIVE"
}


Example Request
Server Request
curl --location --request PUT "http://127.0.0.1:5000/task_update/1" \
  --header "Content-Type: application/json" \
  --data "{
    \"status\": \"COMPLETED\"
}"
Example Response
200 － OK
{
  "message": "Task updated"
}

GET Get all tasks
------------------
>http://127.0.0.1:5000/tasks
Return all tasks

