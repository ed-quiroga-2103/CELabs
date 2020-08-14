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
    return axios(config)
      .then(response => {
        alert(response.data.message)
      return response
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
  // FUnction to post events
  // eslint-disable-next-line camelcase
  postReservation (request_date, requested_date, requesting_user, init_time, final_time, subject, description, lab, operator) {
    var data = JSON.stringify(
       {
          request_date: request_date,
          requested_date: requested_date,
          requesting_user: requesting_user,
          init_time: init_time,
          final_time: final_time,
          subject: subject,
          description: description,
          lab: lab,
          operator: operator,
          },
   )
    console.log(data)

    var config = {
      method: 'post',
      url: ENDPOINT_PATH + 'reservation',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }
    console.log(data)
    return axios(config)
      .then(response => {
        alert(response.data.message)
      return response
      // console.log(this.posts.message)
      },
      ).catch(e => {
      console.error(e.data.message)
    })
  },
  // Function to put user data
  // eslint-disable-next-line camelcase
  putPerfil (name, lastname1, lastname2, id_number, phone_number, university_id) {
    var data = {
    name: name,
    lastname1: lastname1,
    lastname2: lastname2,
    id_number: id_number,
    phone_number: phone_number,
    university_id: university_id,
}
    console.log(data)

    var config = {
      method: 'put',
      url: ENDPOINT_PATH + 'user',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }
    console.log(data)
    axios(config)
      .then(response => {
        location.reload()
      alert(response.data.message)
      this.posts = response.data
      // console.log(this.posts.message)
      },
      ).catch(e => {
      console.error(e.data.message)
    })
},
     // Function all-nighters from specific user
getANuser () {
  var data = ''
  var config = {
  method: 'get',
  url: ENDPOINT_PATH + 'allnighter/user',
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
// Function reservations from specific user
getRuser () {
  var data = ''
  var config = {
  method: 'get',
  url: ENDPOINT_PATH + 'reservation/user',
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
    // Function to delete account
    putDelete () {
      var data = {
    }
      console.log(data)

      var config = {
        method: 'put',
        url: ENDPOINT_PATH + 'user/disable',
        headers: {
        'x-access-token': this.getUserLogged(),
        Authorization: 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        },
        data: data,
      }
      console.log(data)
      axios(config)
        .then(response => {
          alert(response.data.message)
        this.posts = response.data
        // console.log(this.posts.message)
        },
        ).catch(e => {
        console.error(e.data.message)
      })
    },
  // Function to post evaluation
  // eslint-disable-next-line camelcase
  postSatisfaccion (score, comment, comment2) {
    var data = JSON.stringify(
       {
          score: score,
          comment: comment,
          comment2: comment2,
       },
   )
    console.log(data)

    var config = {
      method: 'post',
      url: ENDPOINT_PATH + 'evaluation',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }
    console.log(data)
    axios(config)
      .then(response => {
        alert(response.data.message)
      this.posts = response.data
      // console.log(this.posts.message)
      },
      ).catch(e => {
      console.error(e.data.message)
    })
  },
  // Function to get Reservations
  getReservations () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'reservation',
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
    // Function to get Reservations
    getPerfil () {
      var data = ''
      var config = {
      method: 'get',
      url: ENDPOINT_PATH + 'user',
      headers: {
          'x-access-token': this.getUserLogged(),
          Authorization: 'Basic QWRtaW46MTIzNDU=',
          'Content-Type': 'application/json',
      },
          data: data,
      }
       return axios(config).then(response => {
          console.log(response.data)
          return response
      })
    },
  //  Function to get AllNighters
  getAN () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'allnighter',
    headers: {
        'x-access-token': this.getUserLogged(),
        Authorization: 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
    },
        data: data,
    }

     return axios(config).then(response => {
       // console.log(response.data)
        return response
    })
  },
  // Function to post a new AllNighter
  // eslint-disable-next-line camelcase
  postAN (request_date, requested_date, description, lab, init_time, final_time) {
    var data = JSON.stringify(
      {
        // eslint-disable-next-line no-undef
        request_date: request_date,
        // eslint-disable-next-line no-undef
        requested_date: requested_date,
        description: description,
        lab: lab,
        init_time: init_time,
        final_time: final_time,
      },

    )
    console.log(data)
    var config = {
      method: 'post',
      url: ENDPOINT_PATH + 'allnighter',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }

   axios(config)
      .then(response => {
        alert(response.data.message)
      this.posts = response.data
      // console.log(this.posts.message)
      },
      ).catch(e => {
      console.error(e.data.message)
    })
  },
  // Function to save cookies
  setUserLogged (userLogged) {
    Cookies.set('userLogged', userLogged)
  },
  // Function to obtain cookies
  getUserLogged () {
    return Cookies.get('userLogged')
  },
  // Function to call register on API
  register (formValue) {
    const user = formValue
    return axios.post(ENDPOINT_PATH + 'user', user).then(response => {
      alert(response.data.message)
      this.setUserLogged(response.data.token)
      return response
    },
      )
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
      console.log(response.data.token)
      this.setUserLogged(response.data.token)
      return response
     //  console.log(response.data.token)
   },
    )
  },
  submitFault (lab, partId, descrip) {
    var data = JSON.stringify(
      {
        lab: lab,
        id_fault_part: partId,
        description: descrip,
      },
    )
    var config = {
      method: 'post',
      url: ENDPOINT_PATH + 'fault',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
   }
    axios(config)
      .then(response => {
      alert(response.data.message)
      this.posts = response.data
      // location.reload()
      // console.log(this.posts.message)
      },
      ).catch(e => {
      console.error(e.data.message)
   })
  },
  getFaultReports () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'fault',
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
  submitHours (date, time, time2, description) {
    var data = JSON.stringify(
      {
        date_time: date,
        init_time: time,
        final_time: time2,
        description: description,
      },
    )
   var config = {
      method: 'post',
      url: ENDPOINT_PATH + 'worklog',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }
   axios(config)
      .then(response => {
        alert(response.data.message)
      this.posts = response.data
      // console.log(this.posts.message)
      },
      ).catch(e => {
      console.error(e.data.message)
    })
  },
  getHours () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'worklog',
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
  getLoggedHours () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'worklog/user',
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
  getUserHours () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'worklog/user',
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
  getLoggedUserHours () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'user/hours',
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
  delHourReport (id) {
      var data = JSON.stringify(
        {
              id_worklog: id,
        },
      )
      var config = {
        method: 'DELETE',
        url: ENDPOINT_PATH + '/worklog',
        headers: {
        'x-access-token': this.getUserLogged(),
        Authorization: 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
        },
        data: data,
      }
     axios(config)
        .then(response => {
          alert(response.data.message)
        this.posts = response.data
        },
        ).catch(e => {
        console.error(e.data.message)
      })
  },
  submitInv (labo, compCom, incompCom, projectors, chairs, fireExt, det) {
    var data = JSON.stringify(
      {
        complete_computers: compCom,
        incomplete_computers: incompCom,
        number_projectors: projectors,
        number_chairs: chairs,
        number_fire_extinguishers: fireExt,
        lab: labo,
        description: det,
      },
    )
    var config = {
      method: 'post',
      url: ENDPOINT_PATH + 'inventory',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }
   axios(config)
      .then(response => {
        alert(response.data.message)
      this.posts = response.data
      // console.log(this.posts.message)
      },
      ).catch(e => {
      console.error(e.data.message)
   })
  },
  getInvReports () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'inventory',
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
  getUser () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'user',
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
  getUsers () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'operators',
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
  changeHourReport (id, newstatus) {
    var data = JSON.stringify(
      {
        old: {
            id_worklog: id,
        },
        new: {
            status: newstatus,
        },
      },
    )
    var config = {
      method: 'put',
      url: ENDPOINT_PATH + 'worklog/state',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }
   axios(config)
      .then(response => {
        alert(response.data.message)
      this.posts = response.data
      },
      ).catch(e => {
      console.error(e.data.message)
    })
  },
  getCourses () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'course',
    headers: {
        'x-access-token': this.getUserLogged(),
        Authorization: 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
    },
        data: data,
    }
     return axios(config).then(response => {
        console.log(response.data)
        return response
    })
  },
  changeFaultReport (id, newstatus) {
    var data = JSON.stringify(
      {
        old: {
            id_report: id,
        },
        new: {
            status: newstatus,
        },
      },
    )
    var config = {
      method: 'put',
      url: ENDPOINT_PATH + 'fault/state',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }
   axios(config)
      .then(response => {
        alert(response.data.message)
      this.posts = response.data
      },
      ).catch(e => {
      console.error(e.data.message)
    })
  },
  submitNewCourse (newName, newCode, newGroup) {
    var data = JSON.stringify(
      {
        code: newCode,
        name: newName,
        group: newGroup,
      },

  )
  var config = {
      method: 'post',
      url: ENDPOINT_PATH + 'course',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }
    axios(config)
      .then(response => {
        alert(response.data.message)
      this.posts = response.data
      },
      ).catch(e => {
      console.error(e.data.message)
    })
  },
  getAllNighters () {
    var data = ''
    var config = {
    method: 'get',
    url: ENDPOINT_PATH + 'allnighter',
    headers: {
        'x-access-token': this.getUserLogged(),
        Authorization: 'Basic QWRtaW46MTIzNDU=',
        'Content-Type': 'application/json',
    },
        data: data,
    }
     return axios(config).then(response => {
        console.log(response.data)
        return response
    })
  },
  changeAllNighterStatus (id, newstatus) {
    var data = JSON.stringify(
      {
        id_allnighter: id,
        status: newstatus,
      },
    )
    var config = {
      method: 'put',
      url: ENDPOINT_PATH + 'allnighter/state',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }
   axios(config)
      .then(response => {
        alert(response.data.message)
      this.posts = response.data
      },
      ).catch(e => {
      console.error(e.data.message)
    })
  },
  delAN (id) {
    var data = JSON.stringify(
      {
            id_worklog: id,
      },
    )
    var config = {
      method: 'DELETE',
      url: ENDPOINT_PATH + '/allnighter',
      headers: {
      'x-access-token': this.getUserLogged(),
      Authorization: 'Basic QWRtaW46MTIzNDU=',
      'Content-Type': 'application/json',
      },
      data: data,
    }
   axios(config)
      .then(response => {
        alert(response.data.message)
      this.posts = response.data
      },
      ).catch(e => {
      console.error(e.data.message)
    })
},
  deleteUserLogged () {
    // eslint-disable-next-line no-undef
    Cookies.remove('userLogged')
  },
}
