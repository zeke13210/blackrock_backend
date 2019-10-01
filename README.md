# blackrock_backend
This repo is meant to hold the backend code for the TOC + Blackrock coding project

KD: I could not access the server outside of the container with "flask run" instead, I had to use this command
flask run --host=0.0.0.0

<ul>
  <li>test</li>
  <li>test2</li>
</ul>

INSTALLATION
-------------
To install and use the blackrock-api container run the below cmds

>docker pull zeke13210/blackrock:prod
>docker container run -it -p 5000:5000 zeke13210/blackrock:prod
>cd app/blackrock_backend
>python app.py


<!doctype html>
<html>
  <head>
    <title>TaskMaster API</title>
    <style type="text/css">
      body {
      	font-family: Trebuchet MS, sans-serif;
      	font-size: 15px;
      	color: #444;
      	margin-right: 24px;
      }
      
      h1	{
      	font-size: 25px;
      }
      h2	{
      	font-size: 20px;
      }
      h3	{
      	font-size: 16px;
      	font-weight: bold;
      }
      hr	{
      	height: 1px;
      	border: 0;
      	color: #ddd;
      	background-color: #ddd;
      }
      
      .app-desc {
        clear: both;
        margin-left: 20px;
      }
      .param-name {
        width: 100%;
      }
      .license-info {
        margin-left: 20px;
      }
      
      .license-url {
        margin-left: 20px;
      }
      
      .model {
        margin: 0 0 0px 20px;
      }
      
      .method {
        margin-left: 20px;
      }
      
      .method-notes	{
      	margin: 10px 0 20px 0;
      	font-size: 90%;
      	color: #555;
      }
      
      pre {
        padding: 10px;
        margin-bottom: 2px;
      }
      
      .http-method {
       text-transform: uppercase;
      }
      
      pre.get {
        background-color: #0f6ab4;
      }
      
      pre.post {
        background-color: #10a54a;
      }
      
      pre.put {
        background-color: #c5862b;
      }
      
      pre.delete {
        background-color: #a41e22;
      }
      
      .huge	{
      	color: #fff;
      }
      
      pre.example {
        background-color: #f3f3f3;
        padding: 10px;
        border: 1px solid #ddd;
      }
      
      code {
        white-space: pre;
      }
      
      .nickname {
        font-weight: bold;
      }
      
      .method-path {
        font-size: 1.5em;
        background-color: #0f6ab4;
      }
      
      .up {
        float:right;
      }
      
      .parameter {
        width: 500px;
      }
      
      .param {
        width: 500px;
        padding: 10px 0 0 20px;
        font-weight: bold;
      }
      
      .param-desc {
        width: 700px;
        padding: 0 0 0 20px;
        color: #777;
      }
      
      .param-type {
        font-style: italic;
      }
      
      .param-enum-header {
      width: 700px;
      padding: 0 0 0 60px;
      color: #777;
      font-weight: bold;
      }
      
      .param-enum {
      width: 700px;
      padding: 0 0 0 80px;
      color: #777;
      font-style: italic;
      }
      
      .field-label {
        padding: 0;
        margin: 0;
        clear: both;
      }
      
      .field-items	{
      	padding: 0 0 15px 0;
      	margin-bottom: 15px;
      }
      
      .return-type {
        clear: both;
        padding-bottom: 10px;
      }
      
      .param-header {
        font-weight: bold;
      }
      
      .method-tags {
        text-align: right;
      }
      
      .method-tag {
        background: none repeat scroll 0% 0% #24A600;
        border-radius: 3px;
        padding: 2px 10px;
        margin: 2px;
        color: #FFF;
        display: inline-block;
        text-decoration: none;
      }
    </style>
  </head>
  <body>
  <h1>TaskMaster API</h1>
    <div class="app-desc">API for Techs of Color - BlackRock - TaskMaster challenge</div>
    <div class="app-desc">More information: <a href="https://helloreverb.com">https://helloreverb.com</a></div>
    <div class="app-desc">Contact Info: <a href="kenyatta.e.daniels@gmail.com">kenyatta.e.daniels@gmail.com</a></div>
    <div class="app-desc">Version: 1.0.1</div>
    <div class="app-desc">BasePath:/TechsOfColor/TaskMaster/1.0.0</div>
    <div class="license-info">All rights reserved</div>
    <div class="license-url">http://apache.org/licenses/LICENSE-2.0.html</div>
  <h2>Access</h2>

  <h2><a name="__Methods">Methods</a></h2>
  [ Jump to <a href="#__Models">Models</a> ]

  <h3>Table of Contents </h3>
  <div class="method-summary"></div>
  <h4><a href="#Client">Client</a></h4>
  <ul>
  <li><a href="#taskPost"><code><span class="http-method">post</span> /task</code></a></li>
  <li><a href="#taskTaskIdGet"><code><span class="http-method">get</span> /task/{taskId}</code></a></li>
  <li><a href="#tasksGet"><code><span class="http-method">get</span> /tasks</code></a></li>
  </ul>
  <h4><a href="#Daemon">Daemon</a></h4>
  <ul>
  <li><a href="#taskTaskIdPut"><code><span class="http-method">put</span> /task/{taskId}</code></a></li>
  <li><a href="#tasksGet"><code><span class="http-method">get</span> /tasks</code></a></li>
  </ul>

  <h1><a name="Client">Client</a></h1>
  <div class="method"><a name="taskPost"></a>
    <div class="method-path">
    <a class="up" href="#__Methods">Up</a>
    <pre class="post"><code class="huge"><span class="http-method">post</span> /task</code></pre></div>
    <div class="method-summary">Create a task (<span class="nickname">taskPost</span>)</div>
    <div class="method-notes">Creates a new task to be managed</div>


    <h3 class="field-label">Consumes</h3>
    This API call consumes the following media types via the <span class="header">Content-Type</span> request header:
    <ul>
      <li><code>application/json</code></li>
      <li><code>application/x-www-form-urlencoded</code></li>
    </ul>

    <h3 class="field-label">Request body</h3>
    <div class="field-items">
      <div class="param">body <a href="#FormTask">FormTask</a> (optional)</div>
      
            <div class="param-desc"><span class="param-type">Body Parameter</span> &mdash;  </div>
                </div>  <!-- field-items -->



    <h3 class="field-label">Form parameters</h3>
    <div class="field-items">
      <div class="param">name (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">description (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">priority (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">status (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">runtimeHours (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">runtimeMinutes (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>      <div class="param">runtimeSeconds (optional)</div>
      
            <div class="param-desc"><span class="param-type">Form Parameter</span> &mdash;  </div>    </div>  <!-- field-items -->

    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      <a href="#DataTask">DataTask</a>
      
    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>{
  "name" : "Boil Eggs",
  "description" : "Track the time needed to boil eggs",
  "createdTime" : "2019-08-29T09:12:33.001Z",
  "startTime" : "2019-08-29T09:12:33.001Z",
  "id" : 2013,
  "time" : "2019-08-29T09:12:33.001Z",
  "endTime" : "2019-08-29T09:12:33.001Z",
  "priority" : 5,
  "status" : "ACTIVE"
}</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    Item created
        <a href="#DataTask">DataTask</a>
    <h4 class="field-label">4XX</h4>
    invalid input, object invalid
        <a href="#"></a>
    <h4 class="field-label">5XX</h4>
    An unexpected error occured
        <a href="#inline_response_5XX">inline_response_5XX</a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="taskTaskIdGet"></a>
    <div class="method-path">
    <a class="up" href="#__Methods">Up</a>
    <pre class="get"><code class="huge"><span class="http-method">get</span> /task/{taskId}</code></pre></div>
    <div class="method-summary">Return the specified task (<span class="nickname">taskTaskIdGet</span>)</div>
    <div class="method-notes">Return the task associated with the provided taskId</div>

    <h3 class="field-label">Path parameters</h3>
    <div class="field-items">
      <div class="param">taskId (required)</div>
      
            <div class="param-desc"><span class="param-type">Path Parameter</span> &mdash;  </div>    </div>  <!-- field-items -->






    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      <a href="#DataTask">DataTask</a>
      
    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>{
  "name" : "Boil Eggs",
  "description" : "Track the time needed to boil eggs",
  "createdTime" : "2019-08-29T09:12:33.001Z",
  "startTime" : "2019-08-29T09:12:33.001Z",
  "id" : 2013,
  "time" : "2019-08-29T09:12:33.001Z",
  "endTime" : "2019-08-29T09:12:33.001Z",
  "priority" : 5,
  "status" : "ACTIVE"
}</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    Returned specified Task
        <a href="#DataTask">DataTask</a>
    <h4 class="field-label">5XX</h4>
    An unexpected error occured
        <a href="#inline_response_5XX">inline_response_5XX</a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="tasksGet"></a>
    <div class="method-path">
    <a class="up" href="#__Methods">Up</a>
    <pre class="get"><code class="huge"><span class="http-method">get</span> /tasks</code></pre></div>
    <div class="method-summary">Return a set of tasks (<span class="nickname">tasksGet</span>)</div>
    <div class="method-notes">Return all tasks or those based on specified options</div>





    <h3 class="field-label">Query parameters</h3>
    <div class="field-items">
      <div class="param">orderBy (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash; Order method </div>      <div class="param">orderDirection (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash; Order method </div>      <div class="param">status (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash; Filter results based on status </div>      <div class="param">pageSize (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash; Number of tasks to show per page (for client pagination) </div>      <div class="param">pageNumber (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash; Current pageNumber (for client pagination) format: int32</div>    </div>  <!-- field-items -->


    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      array[<a href="#DataTask">DataTask</a>]
      
    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>[ {
  "name" : "Boil Eggs",
  "description" : "Track the time needed to boil eggs",
  "createdTime" : "2019-08-29T09:12:33.001Z",
  "startTime" : "2019-08-29T09:12:33.001Z",
  "id" : 2013,
  "time" : "2019-08-29T09:12:33.001Z",
  "endTime" : "2019-08-29T09:12:33.001Z",
  "priority" : 5,
  "status" : "ACTIVE"
}, {
  "name" : "Boil Eggs",
  "description" : "Track the time needed to boil eggs",
  "createdTime" : "2019-08-29T09:12:33.001Z",
  "startTime" : "2019-08-29T09:12:33.001Z",
  "id" : 2013,
  "time" : "2019-08-29T09:12:33.001Z",
  "endTime" : "2019-08-29T09:12:33.001Z",
  "priority" : 5,
  "status" : "ACTIVE"
} ]</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    Returned array of specified Tasks
        
    <h4 class="field-label">4XX</h4>
    Bad filter option
        <a href="#"></a>
    <h4 class="field-label">5XX</h4>
    An unexpected error occured
        <a href="#inline_response_5XX">inline_response_5XX</a>
  </div> <!-- method -->
  <hr/>
  <h1><a name="Daemon">Daemon</a></h1>
  <div class="method"><a name="taskTaskIdPut"></a>
    <div class="method-path">
    <a class="up" href="#__Methods">Up</a>
    <pre class="put"><code class="huge"><span class="http-method">put</span> /task/{taskId}</code></pre></div>
    <div class="method-summary">Update a task (<span class="nickname">taskTaskIdPut</span>)</div>
    <div class="method-notes">Update the status and times for tasks</div>

    <h3 class="field-label">Path parameters</h3>
    <div class="field-items">
      <div class="param">taskId (required)</div>
      
            <div class="param-desc"><span class="param-type">Path Parameter</span> &mdash;  </div>    </div>  <!-- field-items -->

    <h3 class="field-label">Consumes</h3>
    This API call consumes the following media types via the <span class="header">Content-Type</span> request header:
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Request body</h3>
    <div class="field-items">
      <div class="param">body <a href="#body">body</a> (required)</div>
      
            <div class="param-desc"><span class="param-type">Body Parameter</span> &mdash; Task values to be updated </div>
                </div>  <!-- field-items -->




    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      <a href="#DataTask">DataTask</a>
      
    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>{
  "name" : "Boil Eggs",
  "description" : "Track the time needed to boil eggs",
  "createdTime" : "2019-08-29T09:12:33.001Z",
  "startTime" : "2019-08-29T09:12:33.001Z",
  "id" : 2013,
  "time" : "2019-08-29T09:12:33.001Z",
  "endTime" : "2019-08-29T09:12:33.001Z",
  "priority" : 5,
  "status" : "ACTIVE"
}</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    Updated Task
        <a href="#DataTask">DataTask</a>
    <h4 class="field-label">5XX</h4>
    An unexpected error occured
        <a href="#inline_response_5XX">inline_response_5XX</a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="tasksGet"></a>
    <div class="method-path">
    <a class="up" href="#__Methods">Up</a>
    <pre class="get"><code class="huge"><span class="http-method">get</span> /tasks</code></pre></div>
    <div class="method-summary">Return a set of tasks (<span class="nickname">tasksGet</span>)</div>
    <div class="method-notes">Return all tasks or those based on specified options</div>





    <h3 class="field-label">Query parameters</h3>
    <div class="field-items">
      <div class="param">orderBy (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash; Order method </div>      <div class="param">orderDirection (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash; Order method </div>      <div class="param">status (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash; Filter results based on status </div>      <div class="param">pageSize (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash; Number of tasks to show per page (for client pagination) </div>      <div class="param">pageNumber (optional)</div>
      
            <div class="param-desc"><span class="param-type">Query Parameter</span> &mdash; Current pageNumber (for client pagination) format: int32</div>    </div>  <!-- field-items -->


    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      array[<a href="#DataTask">DataTask</a>]
      
    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>[ {
  "name" : "Boil Eggs",
  "description" : "Track the time needed to boil eggs",
  "createdTime" : "2019-08-29T09:12:33.001Z",
  "startTime" : "2019-08-29T09:12:33.001Z",
  "id" : 2013,
  "time" : "2019-08-29T09:12:33.001Z",
  "endTime" : "2019-08-29T09:12:33.001Z",
  "priority" : 5,
  "status" : "ACTIVE"
}, {
  "name" : "Boil Eggs",
  "description" : "Track the time needed to boil eggs",
  "createdTime" : "2019-08-29T09:12:33.001Z",
  "startTime" : "2019-08-29T09:12:33.001Z",
  "id" : 2013,
  "time" : "2019-08-29T09:12:33.001Z",
  "endTime" : "2019-08-29T09:12:33.001Z",
  "priority" : 5,
  "status" : "ACTIVE"
} ]</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    Returned array of specified Tasks
        
    <h4 class="field-label">4XX</h4>
    Bad filter option
        <a href="#"></a>
    <h4 class="field-label">5XX</h4>
    An unexpected error occured
        <a href="#inline_response_5XX">inline_response_5XX</a>
  </div> <!-- method -->
  <hr/>

  <h2><a name="__Models">Models</a></h2>
  [ Jump to <a href="#__Methods">Methods</a> ]

  <h3>Table of Contents</h3>
  <ol>
    <li><a href="#DataTask"><code>DataTask</code></a></li>
    <li><a href="#FormTask"><code>FormTask</code></a></li>
    <li><a href="#body"><code>body</code></a></li>
    <li><a href="#inline_response_5XX"><code>inline_response_5XX</code></a></li>
  </ol>

  <div class="model">
    <h3><a name="DataTask"><code>DataTask</code></a> <a class="up" href="#__Models">Up</a></h3>
    
    <div class="field-items">
      <div class="param">id </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
          <div class="param-desc"><span class="param-type">example: 2013</span></div>
<div class="param">name </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
          <div class="param-desc"><span class="param-type">example: Boil Eggs</span></div>
<div class="param">description </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
          <div class="param-desc"><span class="param-type">example: Track the time needed to boil eggs</span></div>
<div class="param">priority </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
        <div class="param-enum-header">Enum:</div>
        <div class="param-enum">1</div><div class="param-enum">2</div><div class="param-enum">3</div><div class="param-enum">4</div><div class="param-enum">5</div>
          <div class="param-desc"><span class="param-type">example: 5</span></div>
<div class="param">status </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
        <div class="param-enum-header">Enum:</div>
        <div class="param-enum">ACTIVE</div><div class="param-enum">PENDING</div><div class="param-enum">COMPLETED</div>
          <div class="param-desc"><span class="param-type">example: ACTIVE</span></div>
<div class="param">time </div><div class="param-desc"><span class="param-type"><a href="#DateTime">Date</a></span>  format: date-time</div>
          <div class="param-desc"><span class="param-type">example: 2019-08-29T09:12:33.001Z</span></div>
<div class="param">startTime </div><div class="param-desc"><span class="param-type"><a href="#DateTime">Date</a></span>  format: date-time</div>
          <div class="param-desc"><span class="param-type">example: 2019-08-29T09:12:33.001Z</span></div>
<div class="param">endTime </div><div class="param-desc"><span class="param-type"><a href="#DateTime">Date</a></span>  format: date-time</div>
          <div class="param-desc"><span class="param-type">example: 2019-08-29T09:12:33.001Z</span></div>
<div class="param">createdTime </div><div class="param-desc"><span class="param-type"><a href="#DateTime">Date</a></span>  format: date-time</div>
          <div class="param-desc"><span class="param-type">example: 2019-08-29T09:12:33.001Z</span></div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="FormTask"><code>FormTask</code></a> <a class="up" href="#__Models">Up</a></h3>
    
    <div class="field-items">
      <div class="param">name </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
          <div class="param-desc"><span class="param-type">example: Boil Eggs</span></div>
<div class="param">description </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
          <div class="param-desc"><span class="param-type">example: Track the time needed to boil eggs</span></div>
<div class="param">priority </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
        <div class="param-enum-header">Enum:</div>
        <div class="param-enum">1</div><div class="param-enum">2</div><div class="param-enum">3</div><div class="param-enum">4</div><div class="param-enum">5</div>
          <div class="param-desc"><span class="param-type">example: 5</span></div>
<div class="param">status </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
        <div class="param-enum-header">Enum:</div>
        <div class="param-enum">ACTIVE</div><div class="param-enum">PENDING</div><div class="param-enum">COMPLETED</div>
          <div class="param-desc"><span class="param-type">example: ACTIVE</span></div>
<div class="param">runtimeHours </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
          <div class="param-desc"><span class="param-type">example: 12</span></div>
<div class="param">runtimeMinutes </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
          <div class="param-desc"><span class="param-type">example: 30</span></div>
<div class="param">runtimeSeconds </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  </div>
          <div class="param-desc"><span class="param-type">example: 24</span></div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="body"><code>body</code></a> <a class="up" href="#__Models">Up</a></h3>
    
    <div class="field-items">
      <div class="param">startTime (optional)</div><div class="param-desc"><span class="param-type"><a href="#DateTime">Date</a></span>  format: date-time</div>
          <div class="param-desc"><span class="param-type">example: 2019-08-29T09:12:33.001Z</span></div>
<div class="param">status (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
        <div class="param-enum-header">Enum:</div>
        <div class="param-enum">ACTIVE</div><div class="param-enum">PENDING</div><div class="param-enum">COMPLETED</div>
          <div class="param-desc"><span class="param-type">example: COMPLETED</span></div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="inline_response_5XX"><code>inline_response_5XX</code></a> <a class="up" href="#__Models">Up</a></h3>
    
    <div class="field-items">
      <div class="param">statusCode (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
          <div class="param-desc"><span class="param-type">example: 500</span></div>
<div class="param">message (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span>  </div>
          <div class="param-desc"><span class="param-type">example: Server access disabled</span></div>
    </div>  <!-- field-items -->
  </div>
  </body>
</html>


