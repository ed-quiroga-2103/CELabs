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



# API

This section details the usage and development details of the API for CELabs.

## Development Details

To get the proper enviorment for developing, the file **metadata.py** must be executed before the usage of the **ce_labs_api.py** to initialize the CELabs database.

# HTTP Methods for API

## HTTP Basic Auth

The HTTP Basic Auth **must** use a POST method to sent the request. Values of `username` and `password`
must be included in the `auth` parameters of the request.

Example with Axios library for Vue:

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

## Registration 

Registrarion is a POST method. The inputed JSON has the following format:

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

### POST

The inputed JSON has the following format:

```
    data: {
          "request_date": "Date of the request",
          "requested_date": "Requested Date",
          "requesting_user": "requesting_user@email.com",
          "init_time": "HH:MM:SS",
          "final_time": "HH:MM:SS",
          "subject": "University Subject",
          "description": "Description of the reservation",
          "lab": "Lab name (E.g. F2-09)",
          "operator": "operator@email.com"
          }
```       

If there is no operator, then operator can be null or blank.

Example with Axios library for Vue:

```
var data = JSON.stringify(

    {"request_date":this.request_date,
    "requested_date":this.requested_date,
    "requesting_user":this.requesting_user,
    "init_time": this.init_time,
    "final_time": this.final_time,
    "subject": this.subject,
    "description": this.description,
    "lab": this.lab,
    "operator": this.operator
    }

);
var config = {
    method: 'post',
    url: 'http://127.0.0.1:5001/reservation',
    headers: { 
    'x-access-token': this.token, 
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
    ).catch(error =>{
    console.log(error.data['message'])
});
```

The request sends a confirmation message with the following format:

```
{'message' : 'New reservation created!'}
```

### GET

The request in Axios has the following format:
```
var data = '';
        var config = {
        method: 'get',
        url: 'http://127.0.0.1:5001/reservation',
        headers: { 
            'x-access-token': this.token, 
            'Authorization': 'Basic QWRtaW46MTIzNDU=', 
            'Content-Type': 'application/json'
        },
            data: data
        };

        axios(config).then(response=>{
            this.info = JSON.stringify(response.data)
        })
```

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

### POST

The inputed JSON has the following format:

```
    data: {
          "request_date": "Date of the request",
          "requested_date": "Requested Date",
          "description": "Description of the reservation",
          "lab": "Lab name (E.g. F2-09)",
          }
```       


Example with Axios library for Vue:

```
{
        var data = JSON.stringify(

          {"request_date":this.request_date,
          "requested_date":this.requested_date,
          "description": this.description,
          "lab": this.lab,
          }

          );
        var config = {
        method: 'post',
        url: 'http://127.0.0.1:5001/allnighter',
        headers: { 
            'x-access-token': this.token, 
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
      ).catch(error =>{
        console.log(error.data['message'])
      });
```

The request sends a confirmation message with the following format:

```
{'message' : 'New All-Nighter created!'}
```
### GET

The request in Axios has the following format:

```
var data = '';
        var config = {
        method: 'get',
        url: 'http://127.0.0.1:5001/allnighter',
        headers: { 
            'x-access-token': this.token, 
            'Authorization': 'Basic QWRtaW46MTIzNDU=', 
            'Content-Type': 'application/json'
        },
            data: data
        };

        axios(config).then(response=>{
            this.info = JSON.stringify(response.data)
        })
```
The request returns a JSONArray with all the current reservations in the database with the following format:
```
[
    ["12/12/2020", "12/12/2020", "Desarrollo de proyecto", 0, "Op"],
    ["13/12/2020", "13/12/2020", "Desarrollo de proyecto", 1, "Op"],
    ["14/12/2020", "14/12/2020", "Desarrollo de proyecto", 2, "Op"]
]
```
The order of the data in the array is:
```
    ['Request Data', 'Requested Date', 'Description', 'State of the Request', 'User that Requested']
```

The state of the requests is described in the following table:

| State| Code |
| ----------- | ----------- |
| Pending | 0 |
| Approved | 1 |
| Denied | 2 |
