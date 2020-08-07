/* eslint-disable vue/no-parsing-error */
<template>
  <v-row class="">
    <v-col>
      <v-sheet height="64">
        <v-toolbar
          flat
          color="white"
        >
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="setToday"
          >
            Today
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="prev"
          >
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
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
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>
          <v-spacer />
          <v-btn
            outlined
            class="mr-4"
            color="grey darken-2"
            @click="dialogo = true"
          >
            New event
          </v-btn>
          <v-menu
            bottom
            right
          />
        </v-toolbar>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :events="events"
          :type="type"
          @click:event="showEvent"
          @click:more="viewDay"
          @click:date="viewDay"
        />

        <!--------------Add event------------------------------------------------------>
        <v-dialog v-model="dialogo">
          <v-card>
            <v-container>
              <v-form @submit.prevent="addEvent">
                <v-text-field
                  v-model="description"
                  type="text"
                  label="Description"
                >
                  >
                </v-text-field>
                <template>
                  <v-row align="center">
                    <v-col cols="12">
                      <v-select
                        v-model="lab"
                        :items="items"
                        :menu-props="{ top: true, offsetY: true }"
                        label="Laboratorio"
                      />
                    </v-col>
                  </v-row>
                </template>

                <v-text-field
                  v-model=" date"
                  type="date"
                  label="Start"
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
                      label="Start"
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
                      label="End"
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
              :color="selectedEvent.color"
              dark
            >
              <v-btn icon>
                <v-icon>mdi-pencil</v-icon>
              </v-btn>
              <v-toolbar-title v-html="selectedEvent.name" />
              <v-spacer />
              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <span v-html="selectedEvent.details" />
            </v-card-text>
            <v-card-actions>
              <v-btn
                text
                color="secondary"
                @click="selectedOpen = false"
              >
                Cancel
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      items: ['F2-09', 'F2-10'],
      description: '',
      lab: '',
      week_day: ' ',
      is_repeatable: 0,
      date: '',
      time2: null,
      time: null,
      modal: false,
      modal2: false,
      focus: new Date().toISOString().substr(0, 10),
      type: 'week',
      start: null,
      end: null,
      name: null,
      details: null,
      color: '#197602',
      dialogo: false,
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      currentlyEditing: null,
      events: [
        {
          name: 'Event',
          start: '2020-08-07  16:45',
          end: '2020-08-07  20:15',
          week_day: '',
          is_repeatable: 0,
          date: '2020-08-07',
          timed: false,
        }, {
          name: 'Birthday',
          start: '2020-08-07  04:30',
          end: '2020-08-07  05:00',
          week_day: '',
          is_repeatable: 0,
          date: '2020-08-07',
          timed: true,
        },
      ],
    }),
    mounted () {
      this.getEvents()
      this.$refs.calendar.checkChange()
    },
    methods: {
      viewDay ({ date }) {
        this.focus = date
        this.type = 'day'
      },
      setToday () {
        this.focus = ''
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
      ChangeDate (date) {
        date = date[8] + date[9] + '/' + date[5] + date[6] + '/' + date[0] + date[1] + date[2] + date[3]
        return date
      },
      addEvent () {
        try {
          if (this.description && this.time && this.time2) {
            this.events.push(
              {
                name: this.description,
                start: this.date + ' ' + this.time,
                end: this.date + ' ' + this.time2,
                week_day: '',
                is_repeatable: 0,
                date: this.date,
                timed: true,
              })
            this.date = this.ChangeDate(this.date)
            this.postEvent(this.description,
                           this.time + ':00',
                           this.time2 + ':00',
                           '',
                           '0',
                           this.lab,
                           this.date)
            this.name = null
            this.start = null
            this.end = null
          } else {
            alert('Complete all the fields')
          }
        } catch (error) {

        }
      },
      async getEvents () {
        try {
          await this.$auth.getEvents()
        } catch (error) {
          this.error = true
          alert('Error charging events')
        }
      },
      async postEvent (description, start, end, day, repeatable, lab, date) {
        try {
          await this.$auth.postEvent(description, start, end, day, repeatable, lab, date)
        } catch (error) {
          this.error = true
          alert('Error sending events')
        }
      },
    },
  }
</script>
