import axios from 'axios'
import Cookies from 'js-cookie'

const ENDPOINT_PATH = 'http://127.0.0.1:5001/'
export default {
  // Function to save cookies
  setUserLogged (userLogged) {
    Cookies.set('userLogged', userLogged)
  },
  // Function to obtein cookies
  getUserLogged () {
    return Cookies.get('userLogged')
  },

  // Function to call register on API
  register (formValue) {
    const user = formValue
    return axios.post(ENDPOINT_PATH + 'user', user)
  },
  // Function to call login on API
  login (u, p) {
    return axios.post(ENDPOINT_PATH + 'login', {
        headers: {},
    },
    {
        auth: {
          username: u,
          password: p,
        },
    }).then(response => {
      this.setUserLogged(response.data)
      console.log(response.data)
  },
)
  },
    }
