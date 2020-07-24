# CELabs
Proyecto del curso Especificación y Diseño de Software CE4101


# HTTP Methods for API

## HTTP Basic Auth

The HTTP Basic Auth **must** use a POST method to sent the request. Values of `username` and `password`
must be included in the `auth` parameters of the request.

Example with Axio library for Vue:

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

