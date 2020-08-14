<template>
  <v-row class="">
    <v-col>
      <v-sheet height="64">
        <v-toolbar
          flat
          color="white"
        >
          <v-row align="center">
            <v-col
              class="ml-8 mr-8"
              cols="8"
              sm="6"
            >
              <v-btn-toggle
                rounded
              >
                <v-btn @click="l1 = true">
                  F2-09
                </v-btn>
                <v-btn @click="l1 = false">
                  F2-10
                </v-btn>
              </v-btn-toggle>
            </v-col>
          </v-row>
          <v-spacer />
          <v-btn
            fab
            text
            smalls
            color="grey darken-2"
            @click="prev"
          >
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="next"
          >
            <v-icon small>
              mdi-chevron-right
            </v-icon>
          </v-btn>
          <v-spacer />
          <v-spacer />
          <v-btn
            class="mr-4"
            outlined
            color="grey darken-2"
            @click="dialogo = true"
          >
            Reservation
          </v-btn>
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="setToday"
          >
            Today
          </v-btn>
          <v-menu
            ref="startMenu"
            v-model="startMenu"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="start"
            transition="scale-transition"
            min-width="290px"
            offset-y
          >
            <template v-slot:activator="{ on }">
              <v-btn
                fab
                text
                dense
                readonly
                outlined
                hide-details
                color="grey darken-2"
                v-on="on"
              >
                <v-icon x-large>
                  {{ calendarmonth }}
                </v-icon>
              </v-btn>
            </template>
            <v-date-picker
              v-model="start"
              no-title
              scrollable
            >
              <v-spacer />
              <v-btn
                text
                color="primary"
                @click="startMenu = false"
              >
                Cancel
              </v-btn>
              <v-btn
                text
                color="primary"
                @click="$refs.startMenu.save(start)"
              >
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>
          <v-menu
            bottom
            right
          />
        </v-toolbar>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          v-show="l1"
          ref="calendar"
          v-model="start"
          color="primary"
          :short-weekdays="shortWeekdays"
          :interval-count="intervals.count"
          :first-interval="intervals.first"
          :interval-minutes="intervals.minutes"
          :weekdays="weekdays"
          :min-weeks="1"
          :max-days="1"
          :start="start"
          :events="events"
          :type="type"
          @click:event="showEvent"
        />
        <v-calendar
          v-show="!l1"
          ref="calendar"
          v-model="start"
          color="primary"
          :short-weekdays="shortWeekdays"
          :interval-count="intervals.count"
          :first-interval="intervals.first"
          :interval-minutes="intervals.minutes"
          :weekdays="weekdays"
          :min-weeks="1"
          :max-days="1"
          :start="start"
          :events="events2"
          :type="type"
          @click:event="showEvent"
        />
        <!--------------Add event------------------------------------------------------>
        <v-dialog v-model="dialogo">
          <v-card>
            <v-container>
              <v-form @submit.prevent="addReservation">
                <template>
                  <v-row align="center">
                    <v-col cols="12">
                      <v-text-field
                        v-model="prof"
                        :rules="[rules.email]"
                        filled
                        color="deep-purple"
                        label="User"
                        type="email"
                      />
                      <v-text-field
                        v-model="start"
                        type="date"
                        :allowed-dates="allowedDates"
                        label="Date of the request"
                        readonly
                      >
                        >
                      </v-text-field>
                      <v-text-field
                        v-model="date"
                        :allowed-dates="allowedDates"
                        type="date"
                        label="Requested date"
                        min="start"
                        max="2020-12-20"
                      >
                        >
                      </v-text-field>
                      <!-----------------------START---------------------------------------------->
                      <v-dialog
                        ref="dialog"
                        v-model="modal"
                        :return-value.sync="time"
                        persistent
                        width="290px"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="time"
                            label="Begins at"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          />
                        </template>
                        <v-time-picker
                          v-if="modal"
                          v-model="time"
                          min="7:30"
                          max="21:59"
                          full-width
                        >
                          <v-spacer />
                          <v-btn
                            text
                            color="primary"
                            @click="modal = false"
                          >
                            Cancel
                          </v-btn>
                          <v-btn
                            text
                            color="primary"
                            @click="$refs.dialog.save(time)"
                          >
                            OK
                          </v-btn>
                        </v-time-picker>
                      </v-dialog>
                      <!----------------------END------------------------------------------------->
                      <v-dialog
                        ref="dialog2"
                        v-model="modal2"
                        :return-value.sync="time2"
                        persistent
                        width="290px"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="time2"
                            label="Ends at"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          />
                        </template>
                        <v-time-picker
                          v-if="modal2"
                          v-model="time2"
                          full-width
                          min="7:30"
                          max="21:59"
                        >
                          <v-spacer />
                          <v-btn
                            text
                            color="primary"
                            @click="modal2 = false"
                          >
                            Cancel
                          </v-btn>
                          <v-btn
                            text
                            color="primary"
                            @click="$refs.dialog2.save(time2)"
                          >
                            OK
                          </v-btn>
                        </v-time-picker>
                      </v-dialog>
                      <!------------------------------------>
                      <v-combobox
                        v-model="course"
                        :items="iCourses"
                        label="Course"
                        placeholder="Choose a course of the list"
                        item-text="name"
                        item-value="code"
                        :return-object="false"
                      />
                      <v-select
                        v-model="lab"
                        :items="items"
                        :menu-props="{ top: true, offsetY: true}"
                        label="Laboratory"
                      />
                    </v-col>
                  </v-row>
                </template>

                <v-textarea
                  v-model="description"
                  counter
                  label="Justification"
                />
                <v-text-field
                  v-model="operador"
                  filled
                  color="white"
                  label="Operator"
                  type="email"
                  readonly
                />
                <v-btn
                  type="submit"
                  color="primary"
                  class="mr-4"
                  @click.stop="dialogo = false"
                >
                  Add
                </v-btn>
              </v-form>
            </v-container>
          </v-card>
        </v-dialog>

        <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card
            color="grey lighten-4"
            min-width="350px"
            flat
          >
            <v-toolbar
              color="blue"
              dark
            >
              <v-toolbar-title v-html="selectedEvent.name" />
              <v-spacer />
            </v-toolbar>
            <v-card-text>
              <v-list
                two-line
                subheader
              >
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Start: </v-list-item-title>
                    <v-list-item-subtitle v-html="selectedEvent.start" />
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>End: </v-list-item-title>
                    <v-list-item-subtitle v-html="selectedEvent.end" />
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Encargado: </v-list-item-title>
                    <v-list-item-subtitle v-html="selectedEvent.encargado" />
                  </v-list-item-content>
                </v-list-item>
              </v-list>
              <span v-html="selectedEvent.details" />
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="secondary"
                @click="selectedOpen = false"
              >
                OK
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-sheet>
    </v-col>
  </v-row>
</template>

name: 'Reservado',
              description: temp[i][5],
              start: dt + ' ' + temp[i][2].slice(0, 5),
              end: dt + ' ' + temp[i][3].slice(0, 5),
              encargado: temp[i][7],
              lab: temp[i][8],
              subject: temp[i][4],
              date:
<script>
  import { mdiCalendarMonth } from '@mdi/js'
  const weekdaysDefault = [1, 2, 3, 4, 5, 6]
  export default {
    data: () => ({
      item: 1,
      iCourses: [
        { name: 'Especificación y Diseño de Software', code: 'CE-0001', group: ' ' },
        { name: 'Introducción a la programación', code: 'CE-0002', group: ' ' },
      ],
      d_weeks: '',
      items4: [
        { id: 'L', name: 'Monday' },
        { id: 'K', name: 'Tuesday' },
        { id: 'M', name: 'Wednesday' },
        { id: 'J', name: 'Thursday' },
        { id: 'V', name: 'Friday' },
        { id: 'S', name: 'Saturday' },
      ],
      form: {
        id: null,
        name: '',
        name2: '',
      },
      rules: {
        email: v => !!(v || '').match(/@/) || 'Please enter a valid email',
        required: v => !!v || 'This field is required',
      },
      l1: false,
      calendarmonth: mdiCalendarMonth,
      intervals: {
        first: 14,
        minutes: 30,
        count: 29,
        height: 48,
      },
      weekdays: weekdaysDefault,
      startMenu: false,
      items: ['F2-10', 'F2-09'],
      description: '',
      description2: '',
      operador: 'operador@gmail.com',
      prof: '',
      lab: '',
      lab2: '',
      course: '',
      week_day: ' ',
      is_repeatable: 0,
      date: '',
      date2: '',
      date1: '',
      shortWeekdays: false,
      time2: null,
      time: null,
      time3: null,
      time4: null,
      modal: false,
      modal2: false,
      start: new Date().toISOString().substr(0, 10),
      type: 'week',
      end: null,
      name: null,
      details: null,
      color: '#197602',
      dialogo: false,
      dialogo2: false,
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      currentlyEditing: null,
      events: [],
      events2: [],
    }),
    watch: {
      events (nuevoValor, valorAnterior) {
        console.log("Los eventos pasaron de '%s' a '%s'", valorAnterior, nuevoValor)
      },
    },
    mounted () {
      this.getReservations()
      this.getEvents()
      this.$refs.calendar.checkChange()
      this.getPerfil()
      this.getCourses()
    },
    methods: {
      allowedDates: val => parseInt(val.split('-')[2], 10) % 2 === 0,
      viewDay ({ date }) {
        this.start = date
        this.type = 'day'
      },
      setToday () {
        this.start = new Date().toISOString().substr(0, 10)
      },
      prev () {
        this.$refs.calendar.prev()
      },
      next () {
        this.$refs.calendar.next()
      },
      showEvent ({ nativeEvent, event }) {
        const open = () => {
          this.selectedEvent = event
          this.selectedElement = nativeEvent.target
          setTimeout(() => {
            // eslint-disable-next-line no-return-assign
            return this.selectedOpen = true
          }, 10)
        }
        if (this.selectedOpen) {
          this.selectedOpen = false
          setTimeout(open, 10)
        } else {
          open()
        }
        nativeEvent.stopPropagation()
      },
      showEvent2 ({ nativeEvent, event }) {
        const open = () => {
          this.selectedEvent = event
          this.selectedElement = nativeEvent.target
          setTimeout(() => {
            // eslint-disable-next-line no-return-assign
            return this.selectedOpen = true
          }, 10)
        }
        if (this.selectedOpen) {
          this.selectedOpen = false
          setTimeout(open, 10)
        } else {
          open()
        }
        nativeEvent.stopPropagation()
      },
      ChangeDate (date) {
        date = date[8] + date[9] + '/' + date[5] + date[6] + '/' + date[0] + date[1] + date[2] + date[3]
        return date
      },
      addReservation () {
        try {
          if (this.date && this.time && this.time2 && this.description && this.lab && this.course) {
            const date2 = this.ChangeDate(this.date)
            const date3 = this.ChangeDate(this.start)
            console.log(date2, date3, this.prof, this.time + ':00', this.time2 + ':00', this.course, this.description, this.lab, this.operator)
            this.postReservation(date2,
                                 date3,
                                 this.prof,
                                 this.time + ':00',
                                 this.time2 + ':00',
                                 this.course,
                                 this.description,
                                 this.lab,
                                 this.operador)
          } else {
            alert('Complete all the fields')
          }
        } catch (error) {
        }
      },
      async getReservations () {
        try {
          await this.$auth.getReservations().then(
            response => {
              this.sortReservations(response.data)
            })
        } catch (error) {
          this.error = true
        }
      },
      // eslint-disable-next-line camelcase
      async postReservation (request_date, requested_date, requesting_user, init_time, final_time, subject, description, lab, operator) {
        try {
          await this.$auth.postReservation(request_date, requested_date, requesting_user, init_time, final_time, subject, description, lab, operator).then(
            response => {
              // eslint-disable-next-line eqeqeq
              alert(response.data.message)
              location.reload()
              // eslint-disable-next-line eqeqeq
            })
          console.log(request_date)
          this.$refs.calendar.checkChange()
        } catch (error) {
          this.error = true
          alert('Error sending events')
        }
      },
      sortReservations (temp) {
        for (var i = 0; i < temp.length; i++) {
          var dt = temp[i][0].slice(6, 10) + '-' + temp[i][0].slice(3, 5) + '-' + temp[i][0].slice(0, 2)
          // eslint-disable-next-line eqeqeq
          if (temp[i][8] == 'F2-09') {
            this.events.push({
              name: 'Reservado',
              description: temp[i][5],
              start: dt + ' ' + temp[i][2].slice(0, 5),
              end: dt + ' ' + temp[i][3].slice(0, 5),
              encargado: temp[i][7],
              lab: temp[i][8],
              subject: temp[i][4],
              date: dt,
            })
          } else {
            this.events2.push({
              name: 'Reservado',
              description: temp[i][5],
              start: dt + ' ' + temp[i][2].slice(0, 5),
              end: dt + ' ' + temp[i][3].slice(0, 5),
              encargado: temp[i][7],
              lab: temp[i][8],
              subject: temp[i][4],
              date: dt,
            })
          }
        }
      },
      async getPerfil () {
        try {
          await this.$auth.getPerfil().then(
            response => {
              var res = response.data
              this.operador = res[4]
              console.log(res[4])
            })
        } catch (error) {
          this.error = true
        }
      },
      async getCourses () {
        try {
          await this.$auth.getCourses().then(
            response => {
              var res = response.data
              for (var i = 0; i < res.length; i++) {
                this.iCourses = []
                console.log(response.data)
                this.iCourses.push(
                  {
                    name: res[i][2],
                    code: res[i][0],
                    group: res[i][1],
                  },
                )
                console.log(this.iCourses)
              }
            })
        } catch (error) {
          this.error = true
        }
      },
      async getEvents () {
        this.events = []
        try {
          await this.$auth.getEvents().then(
            response => {
              this.sortEvents(response.data)
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
</style>
