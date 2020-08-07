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
      console.log(this.posts.message)
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

    axios(config).then(response => {
        this.temp = response.data
        this.sortEvents()
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
      console.log(response.data.token)
  },
)
  },
  sortEvents () {
    this.events = []
    for (var i = 0; i < this.temp.length; i++) {
      var dt = this.temp[i][2].slice(6, 10) + '-' + this.temp[i][2].slice(3, 5) + '-' + this.temp[i][2].slice(0, 2)
      this.events.push({
        description: this.temp[i][4],
        init_time: dt + ' ' + this.temp[i][0].slice(0, 5),
        final_time: dt + ' ' + this.temp[i][1].slice(0, 5),
        week_day: this.temp[i][3],
        is_repeatable: this.temp[i][5],
        lab: this.temp[i][6],
        date: dt,
      })
    }
    console.log(this.events)
  },
    }
