import axios from 'axios'
import Cookies from 'js-cookie'

const ENDPOINT_PATH = 'http://127.0.0.1:5001/'
export default {

  // Function to push events
  // eslint-disable-next-line camelcase
  postEvent (description, init_time, final_time, week_day, is_repeatable, lab, date) {
    var data = JSON.stringify(
      {
        description: description,
        init_time: init_time,
        final_time: final_time,
        week_day: week_day,
        is_repeatable: is_repeatable,
        lab: lab,
        date: date,
      },

  )
  var config = {
      method: 'post',
      url: ENDPOINT_PATH + 'event',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
  }

   axios(config)
      .then(response => {
      this.posts = response.data
      // console.log(this.posts.message)
      },
      ).catch(e => {
      console.error(e.data.message)
  })
  },
  // Function to get events
  getEvents () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'event',
    headers: {
        'x-access-token': this.getUserLogged(),
        Authorization: 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
    },
        data: data,
    }

     return axios(config).then(response => {
        return response
    })
  },
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
      this.setUserLogged(response.data.token)
      return response
     //  console.log(response.data.token)
  },
)
  },
  deleteUserLogged () {
    Cookies.remove('userLogged')
  },
    }
