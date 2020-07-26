# CELabs
Proyecto del curso Especificación y Diseño de Software CE4101


# HTTP Methods for API

## HTTP Basic Auth

The HTTP Basic Auth **must** use a POST method to sent the request. Values of `username` and `password`
must be included in the `auth` parameters of the request.

Example with Axios library for Vue:

```
axios.post(`http://webservice:port/login`, {
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

## [POST] Registration 

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
| Admin. Assistant | 2 |
| Operator | 3 |
| Professor | 4 |
| Administrative | 5 |

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