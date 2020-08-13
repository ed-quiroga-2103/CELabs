<template>
  <v-row class="">
    <v-col>
      <template>
        <v-card
          class="mx-auto"
          color="#607D8B"
          dark
          max-width="400"
        >
          <v-card-title class="d-flex justify-content-center">
            <v-icon
              large
              left
            >
              mdi-account
            </v-icon>
            <span class="title font-weight-light ">Account Information</span>
          </v-card-title>

          <v-card-text class="headline font-weight-bold ">
            <v-row>
              <h2>Name:</h2>
            </v-row>
            <v-row>
              <label v-text="user" />
            </v-row>
            <v-row>
              <h2>Last name:</h2>
            </v-row>
            <v-row>
              <label v-text="apellido1" />
            </v-row>
            <v-row>
              <h2>Second last name:</h2>
            </v-row>
            <v-row>
              <label v-text="apellido2" />
            </v-row>
            <v-row>
              <h2>ID number:</h2>
            </v-row>
            <v-row>
              <label v-text="Idnumb" />
            </v-row>
            <v-row>
              <h2>ID University IDr:</h2>
            </v-row>
            <v-row>
              <label v-text="Iduni" />
            </v-row>
            <v-row>
              <h2>Email:</h2>
            </v-row>
            <v-row>
              <label v-text="email" />
            </v-row>
            <v-row>
              <h2>Phone number:</h2>
            </v-row>
            <v-row>
              <label v-text="numero" />
            </v-row>
          </v-card-text>
        </v-card>
      </template>
    </v-col>
    <v-col>
      <v-sheet height="200">
        <v-toolbar
          flat
          color="white"
        >
          <v-col />
          <v-spacer />
          <v-spacer />
          <v-col>
            <v-row>
              <h2>a</h2>
            </v-row>
            <v-row>
              <h2>a</h2>
            </v-row>
            <v-btn
              outlined
              color="grey darken-2"
              class="mr-8"
              @click="Reporthour = true"
            >
              All-Nighter Requests
            </v-btn>
            <v-btn
              outlined
              color="grey darken-2"
              class="mr-8"
              @click="Reporthour = true"
            >
              Disable Account
            </v-btn>
            <v-btn
              outlined
              color="grey darken-2"
              class="mr-8"
              @click="Reporthour = true"
            >
              All-Nighter Requests
            </v-btn>
            <v-menu
              bottom
              right
            />
          </v-col>
        </v-toolbar>
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      headers: [
        {
          text: 'Shift Date',
          align: 'start',
          value: 'shiftDate',
        },
        { text: 'Shift start time', value: 'shiftStart' },
        { text: 'Shift end time', value: 'shiftEnd' },
        { text: 'Description of work performed', value: 'workDescription' },
        { text: 'State', value: 'state' },
        { text: 'Delete', value: 'delete' },
      ],
      hours: [],
      user: 'Kimberly',
      apellido1: 'Calderón',
      apellido2: 'Prado',
      Idnumb: '28',
      Iduni: '3',
      description: '',
      email: 'kimberlycalderonprado@gmail.com',
      numero: '87764320',
      time2: null,
      time: null,
      modal: false,
      modal2: false,
      end: null,
      hourReport: false,
      date: '',
    }),
    mounted () {
      this.getHours()
    },
    methods: {
      ChangeDate (date) {
        var date2 = date[8] + date[9] + '/' + date[5] + date[6] + '/' + date[0] + date[1] + date[2] + date[3]
        return date2
      },
      addHours () {
        try {
          if (this.description && this.time && this.time2 && this.date) {
            var date2 = this.ChangeDate(this.date)
            this.submitHours(date2,
                             this.time + ':00',
                             this.time2 + ':00',
                             this.description)
          } else {
            alert('Complete all the fields')
          }
        } catch (error) {

        }
      },
      async submitHours (date, time, time2, description) {
        try {
          await this.$auth.submitHours(date, time, time2, description)
        } catch (error) {
          this.error = true
          alert('Error submiting report')
        }
        this.reportValues = {
          radios: '',
          Idnumb: '',
          textarea: '',
        }
      },
      async getHours () {
        try {
          await this.$auth.getHours().then(
            response => {
              var res = response.data
              for (var i = 0; i < res.length; i++) {
                this.hours.push({
                  shiftDate: res[i][0].slice(0, 10),
                  shiftStart: res[i][1].slice(0, 5),
                  shiftEnd: res[i][2].slice(0, 5),
                  workDescription: res[i][3],
                  state: res[i][4] === 1 ? 'pending' : 'accepted',
                  delete: res[i][4] === 1 ? 'x' : '',
                })
              }
            })
        } catch (error) {
          this.error = true
        }
      },
    },
  }
</script>
<style scoped>
.controls {
  position: relative;
}
.css
h1 {
  color: #6c2eb9;
  font-weight: normal;
  font-size: 20px;
  font-family: Arial;
  text-transform: uppercase;
}
h2 {
  color: #40C4FF;
  font-size: 15px;
  text-transform: uppercase;
}
</style>
