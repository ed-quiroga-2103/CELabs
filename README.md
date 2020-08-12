# CELabs
Proyecto del curso Especificación y Diseño de Software CE4101

# Table of Contents

- [API](#api)
  * [Development Details](#development-details)
- [HTTP Methods for API](#http-methods-for-api)
  * [HTTP Basic Auth](#http-basic-auth)
  * [Registration](#registration)
  * [Reservation](#reservation)
  * [All-Nighters](#all-nighters)
  * [Evaluations](#evaluations)
  * [Events](#events)
  * [Worklog](#worklog)
  * [Fault Report](#fault_report)
  * [Inventory](#inventory)
  * [Course](#course)

# Node.js

The commands to build the GUI are:
```
npm init
npm install
npm run serve
```


# API

This section details the usage and development details of the API for CELabs.

## Development Details

To get the proper enviorment for developing, the file **metadata.py** must be executed before the usage of the **ce_labs_api.py** to initialize the CELabs database.

# HTTP Methods for API


## Axios Managment

All Axios requests are done in a similar way. Therefore, the general managment of the HTTP requests will be specified here, while the data that has to be inputed into the requests, and the data outputed by the requests will be specified in their respective sections.
If theres a case of a specific request that has to be handled differently from the general managment, it will also be specified in its respective section.

### POST

Fields in __ALL CAPS__ has to be replaced with the respective data that the name specifies.
Example of a POST request with Axios:

```
    var data = JSON.stringify(

        {
            Here the data has to be specified as a JSON object. 
            Check each section for further examples.
        }

    );
    var config = {
        method: 'post',
        url: 'http://IP_ADDRESS:PORT_NUMBER/ROUTE',
        headers: { 
        'x-access-token': TOKEN, 
        'Authorization': 'Basic QWRtaW46MTIzNDU=', 
        'Content-Type': 'application/json'
        },
        data: data
    };

    axios(config) 
        .then(response => {
        this.posts = response.data;
        console.log(this.posts['message']);
        }
        ).catch(e =>{
        console.error(e.data['message']);
    });
```



### GET

Fields in __ALL CAPS__ has to be replaced with the respective data that the name specifies.
Example of a GET request with Axios:
```
    var data = '';

    var config = {
    method: 'get',
    url: 'http://IP_ADDRESS:PORT_NUMBER/ROUTE',
    headers: { 
        'x-access-token': TOKEN, 
        'Authorization': 'Basic QWRtaW46MTIzNDU=', 
        'Content-Type': 'application/json'
    },
        data: data
    };

    axios(config).then(response=>{
        this.info = JSON.stringify(response.data)
    })
```


## HTTP Basic Auth

The HTTP Basic Auth **must** use a POST method to sent the request. Values of `username` and `password`
must be included in the `auth` parameters of the request.
The route for this request is `/login`

Example with Axios library:

```
axios.post(`http://localhost:port/login`, {
        headers: {}
    }, 
    {
        auth: {
          username: 'Admin',
          password: 'admin'
        }
    }).then(response => {
        console.log(response.data['token']);
    }
);
```

This request returns the following response:
```
{
  "token": "Token as string",
  "user_type": 3
}
```
The user types are specified in the __Registration__ section.

## Registration 

Registrarion is a POST method. The route for this request is `/user`

The inputed JSON has the following format:

```
data:{

    name: 'Name',
    lastname1: 'Last Name 1',
    lastname2: 'Last Name 2',
    id_number: 'id_number as string',
    password: 'password',
    email: 'email@email.com',
    phone_number: 'phone as string',
    university_id: 'university_id as string',
    user_type: code_for_the_user_type

}
```

The codes for the user types are shown in the the following table:


| User Type | Code |
| ----------- | ----------- |
| Administrator | 1 |
| Operator | 2 |
| Professor | 3 |
| Administrative | 4 |

Example with Axios library for Vue:

```
axios.post(`http://127.0.0.1:5001/user`, 
           {
                name: this.name,
                lastname1: this.lastname1,
                lastname2: this.lastname2,
                id_number: this.id_number,
                password: this.password,
                email: this.email,
                phone_number: this.phone_number,
                university_id: this.university_id,
                user_type: this.user_type
            }
        ) 
        .then(response => {
        this.posts = response.data;
        console.log(this.posts['message']);
      }
      );
```

The request sends a confirmation message with the following format:

```
{'message' : 'New user created!'}
```


## Reservation
The route for this request is `/reservation`

### POST

The inputed JSON has the following format:

```
    data: {
          "request_date": "Date of the request",
          "requested_date": "Requested Date",
          "requesting_user": "requesting_user@email.com",
          "init_time": "HH:MM:SS",
          "final_time": "HH:MM:SS",
          "subject": "University Subject"(Curso),
          "description": "Description of the reservation",
          "lab": "Lab name (E.g. F2-09)",
          "operator": "operator@email.com"
          }
```       

If there is no operator, then operator can be null or blank.


The request sends a confirmation message with the following format:

```
{'message' : 'New reservation created!'}
```

### GET


The request returns a JSONArray with all the current reservations in the database with the following format:
```
[
    ["12/12/2020","12/12/2020","Espe","Revision de proyectos","Prof"],
    ["13/12/2020","13/12/2020","Espe","Revision de proyectos","Prof"],
    ["13/12/2020","13/12/2020","Espe","Revision de proyectos","Prof"]
]
```
The order of the data in the array is:
```
    ['Request Data', 'Requested Date', 'Subject', 'Description', 'User that Requested']
```

## All-Nighters
The route for this request is `/allnighter`

### POST

The inputed JSON has the following format:

```
    data: {
          "request_date": "Date of the request",
          "requested_date": "Requested Date",
          "description": "Description of the reservation",
          "lab": "Lab name (E.g. F2-09)",
          "init_time": "00:00:00",
          "final_time": "01:00:00"
          }
```       



The request sends a confirmation message with the following format:

```
{'message' : 'New All-Nighter created!'}
```
### GET

The request returns a JSONArray with all the current reservations in the database with the following format:
```
[
    ["12/12/2020", "12/12/2020","12:12:12","13:00:00", "Desarrollo de proyecto", 0, "Op"],
    ["13/12/2020", "13/12/2020","12:12:12","13:00:00", "Desarrollo de proyecto", 1, "Op"],
    ["14/12/2020", "14/12/2020","12:12:12","13:00:00", "Desarrollo de proyecto", 2, "Op"]
]
```
The order of the data in the array is:
```
    ['Request Data', 'Requested Date', 'init_time', 'final_time', 'Description', 'State of the Request', 'User that Requested']
```

The state of the requests is described in the following table:

| State| Code |
| ----------- | ----------- |
| Pending | 0 |
| Approved | 1 |
| Denied | 2 |

## Evaluations
The route for this request is `/evaluation`

## POST 

The POST request for evaluation __does not__ need an access token, therefore, the request `config` parameter can be specified like this:

```
    var config = {
        method: 'post',
        url: 'http://IP_ADDRESS:PORT_NUMBER/ROUTE',
        headers: { 
        'Authorization': 'Basic QWRtaW46MTIzNDU=', 
        'Content-Type': 'application/json'
        },
        data: data
    };
```

The data that has to be sent has the following format:
```
data: {
          "comment": "Comment",
          "score": "1"
          }
```

The request returns the following message:
```
{"message": "New Evaluation created!"}
```

## GET

The GET request needs the access token to be executed, therefore, it can be done in the same way that all the other GET requests are done.

The request returns a JSON Array with the following format:
```

[
  ["31/07/2020 18:10:33","comment",5],
  ["01/08/2020 15:05:40","comment",5],
  ["01/08/2020 15:06:30","comment",10]
]
```
The order of the data in the array is:
```
    ['Date Time', 'Comment', 'Score']
```


## Events
The route for this request is `/event`

## POST 

The data that has to be sent has the following format:
```
data:   {
          "description": "Taller de GIT",
          "init_time": "01:00:00",
          "final_time": "02:00:00",
          "week_day": "L,K,M,J,V,S,U",
          "is_repeatable": "1",
          "date":"",
          "lab":"F2-09"
        }
```

For events, repeatable events __must__ include week days, while non-repeatable events __must__ include a date.

The request returns the following message:
```
{"message": "New Event created!"}
```

## GET

The GET request needs the access token to be executed, therefore, it can be done in the same way that all the other GET requests are done.

The request returns a JSON Array with the following format:
```
[
  [
    "01:00:00",
    "02:00:00",
    "",
    [
      "2020-08-12",
      "2020-08-13",
      "2020-08-14",
      "2020-08-15",
      "2020-08-17",
      "2020-08-18",
      "2020-08-19",
      "2020-08-20",
      "2020-08-21",
      "2020-08-22",
      "2020-08-24",
      "2020-08-25",
      "2020-08-26",
      "2020-08-27",
      "2020-08-28",
      "2020-08-29",
      "2020-08-31",
      "2020-09-01",
      "2020-09-02",
      "2020-09-03",
      "2020-09-04",
      "2020-09-05",
      "2020-09-07",
      "2020-09-08",
      "2020-09-09",
      "2020-09-10",
      "2020-09-11",
      "2020-09-12",
      "2020-09-14",
      "2020-09-15",
      "2020-09-16",
      "2020-09-17",
      "2020-09-18",
      "2020-09-19",
      "2020-09-21",
      "2020-09-22",
      "2020-09-23",
      "2020-09-24",
      "2020-09-25",
      "2020-09-26",
      "2020-09-28",
      "2020-09-29",
      "2020-09-30",
      "2020-10-01",
      "2020-10-02",
      "2020-10-03",
      "2020-10-05",
      "2020-10-06",
      "2020-10-07",
      "2020-10-08",
      "2020-10-09",
      "2020-10-10",
      "2020-10-12",
      "2020-10-13",
      "2020-10-14",
      "2020-10-15",
      "2020-10-16",
      "2020-10-17",
      "2020-10-19",
      "2020-10-20",
      "2020-10-21",
      "2020-10-22",
      "2020-10-23",
      "2020-10-24",
      "2020-10-26",
      "2020-10-27",
      "2020-10-28",
      "2020-10-29",
      "2020-10-30",
      "2020-10-31",
      "2020-11-02",
      "2020-11-03",
      "2020-11-04",
      "2020-11-05",
      "2020-11-06",
      "2020-11-07",
      "2020-11-09",
      "2020-11-10",
      "2020-11-11",
      "2020-11-12",
      "2020-11-13",
      "2020-11-14",
      "2020-11-16",
      "2020-11-17",
      "2020-11-18",
      "2020-11-19",
      "2020-11-20",
      "2020-11-21",
      "2020-11-23",
      "2020-11-24",
      "2020-11-25",
      "2020-11-26",
      "2020-11-27",
      "2020-11-28",
      "2020-11-30",
      "2020-12-01",
      "2020-12-02",
      "2020-12-03",
      "2020-12-04",
      "2020-12-05",
      "2020-12-07",
      "2020-12-08",
      "2020-12-09",
      "2020-12-10",
      "2020-12-11",
      "2020-12-12",
      "2020-12-14",
      "2020-12-15",
      "2020-12-16",
      "2020-12-17",
      "2020-12-18"
    ],
    "Taller de GIT",
    true,
    "F2-09"
  ],
  ["12:12:12","13:00:00","12/12/2020","","Espe", false,"F2-09"]
]
```
The order of the data in the array is:
```
    ['init_time', 'final_time', 'date', 'week_day', 'description', 'is_repeatable', 'lab name']
```

## Worklog
The route for this request is `/worklog`

### POST

The data that has to be sent has the following format:
```
data: {
    "date_time": "13/08/2020",
    "init_time": "08:23:23",
    "final_time": "10:23:23",
    "description": "Realice el inventario del equipo"
    }
```

The request sends a confirmation message with the following format:

```
{'message' : 'New worklog created!'}
```

## GET
The GET request needs the access token to be executed, therefore, it can be done in the same way that all the other GET requests are done.

The request returns a JSON Array with the following format:

[
  [
    "23/08/2020 00:00:00",
    "08:23:23",
    "09:23:23",
    "No hice nada",
    1,
    "Op",
    "Op",
    "Op",
    "Op",
    20,
    50
  ],
  [
    "31/08/2020 00:00:00",
    "08:23:23",
    "09:23:23",
    "Conte un chiste",
    1,
    "Oscar",
    "Gonzalez",
    "Alfaro",
    "2017xxxxxx",
    0,
    0
  ]
]
The order of the data in the array is:
```
    ['date_time', 'init_time', 'final_time','description', 'id_status','name','lastname1','lastname2','university_id','pending_hours',
    'approved_hours']
```

### GET FROM A SPECIFIC USER (WITH TOOKEN)
The route for this request is `/worklog/user`

same as above

## Fault Report
The route for this request is `/fault`

### POST

The data that has to be sent has the following format:

``` 
    data:   {
            "id_fault_part": "Maquina No. 5",
            "description": "No enciende",
            "lab":"F2-09"
            }
```  

The request sends a confirmation message with the following format:

```
{'message' : 'New fault report created!'}
```

### GET
The GET request needs the access token to be executed, therefore, it can be done in the same way that all the other GET requests are done.

The request returns a JSON Array with the following format:

[
  [
    "12/08/2020 04:58:40",
    "Maquina No. 5",
    "No enciende",
    1,
    1,
    1
  ]
]
The order of the data in the array is:
```
    ['date_time', 'id_fault_part', 'description','id_status', 'id_lab','id_report']
```

## Inventory Report
The route for this request is `/inventory`

### POST

The data that has to be sent has the following format:

``` 
    data:   {
            "complete_computers": "5",
            "incomplete_computers": "4",
            "number_projectors": "3",
            "number_chairs": "2",
            "number_fire_extinguishers": "1",
            "lab":"F2-09",
            "description":"Me encontre un paragüas"
            }
```  

The request sends a confirmation message with the following format:

```
{'message' : 'New inventory report created!'}
```

### GET OF ALL

The GET request needs the access token to be executed, therefore, it can be done in the same way that all the other GET requests are done.

The request returns a JSON Array with the following format:
```
[
  [
    "12/08/2020 04:32:04",
    5,
    4,
    3,
    2,
    1,
    "Me encontre un paragüas",
    1,
    3,
    1
  ],
  [
    "12/08/2020 04:32:33",
    5,
    4,
    3,
    2,
    1,
    "Me encontre un celular",
    1,
    1,
    2
  ]
]
```
The order of the data in the array is:
```
    ['date', 'complete_computers', 'incomplete_computers','number_projectors',
    'number_chairs','number_fire_extinguishers',
    'description','id_lab','id_user',id_report]
```

### GET FROM A SPECIFIC USER (WITH TOOKEN)
The route for this request is `/inventory/user`

same as above

## Course
The route for this request is `/course`

### POST

The data that has to be sent has the following format:

``` 
    data:   {
                "code": "CE-4401",
                "name": "Especificacion y  Diseño de Software",
                "group": "1"
            }

```  

The request sends a confirmation message with the following format:

```
{'message' : 'The course has been added to the course list!'}
```

## GET

The GET request needs the access token to be executed, therefore, it can be done in the same way that all the other GET requests are done.

The request returns a JSON Array with the following format:
```
[
  [
    "CE-4401",
    "1",
    "Especificacion y  Diseño de Software"
  ]
]
```
The order of the data in the array is:
```
    ['code', 'group', 'name']
```