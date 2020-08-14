<template>
  <v-row class="">
    <v-col>
      <v-sheet height="200">
        <v-toolbar
          flat
          color="white"
        >
          <v-col>
            <v-row>
              <!---Esta as es para el lineamiento de los labels-->
              <h2>a</h2>
            </v-row>
            <v-row>
              <h2>a</h2>
            </v-row>
            <v-row>
              <h2>a</h2>
            </v-row>
            <v-row>
              <h2>a</h2>
            </v-row>
            <v-row>
              <h2>' '</h2>
            </v-row>

            <v-row>
              <h2 />
            </v-row>
            <v-row>
              <h2 />
            </v-row>
            <v-row>
              <h2>Operator:</h2>
            </v-row>
            <v-row>
              <label v-text="operator" />
            </v-row>
            <v-row>
              <h2>University ID:</h2>
            </v-row>
            <v-row>
              <label v-text="uniId" />
            </v-row>
            <v-row>
              <h2>Assigned Hours:</h2>
            </v-row>
            <v-row>
              <label v-text="assignedH" />
            </v-row>
            <v-row>
              <h2>Hours Completed:</h2>
            </v-row>
            <v-row>
              <label v-text="complH" />
            </v-row>
          </v-col>
          <v-spacer />
          <v-spacer />
          <v-col>
            <v-btn
              outlined
              color="grey darken-2"
              @click="hourReport = true"
            >
              Report Hours
            </v-btn>
            <v-menu
              bottom
              right
            />
          </v-col>
        </v-toolbar>
      </v-sheet>
      <!--------------PUT the log here------------------------------------------------------>
      <v-sheet height="600">
        <v-data-table
          :headers="headers"
          :items="hours"
          :items-per-page="5"
          class="elevation-1"
        >
          <template v-slot:item.actions="{ item }">
            <v-icon
              v-if="item.delete === 1"
              small
              class="mr-2"
              @click="delet(item)"
            >
              mdi-delete
            </v-icon>
          </template>
        </v-data-table>
        <v-dialog
          v-model="deldialog"
          width="500"
          height="300"
        >
          <v-card>
            <v-card-title class="headline grey lighten-2">
              Delete confirmation.
            </v-card-title>
            <v-card-text>
              Are you sure you wish to delete this report?
            </v-card-text>
            <v-divider />
            <v-card-actions>
              <v-btn
                color="primary"
                text
                @click="delitem()"
              >
                Yes
              </v-btn>
              <v-spacer />
              <v-btn
                color="primary"
                text
                @click="deldialog = false"
              >
                No
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!--------------Add event------------------------------------------------------>
        <v-dialog v-model="hourReport">
          <v-card>
            <v-container>
              <v-form @submit.prevent="addHours">
                <v-text-field
                  v-model=" date"
                  type="date"
                  label="Date"
                >
                  >
                </v-text-field>
                <v-dialog
                  ref="dialog"
                  v-model="modal"
                  :return-value.sync="time"
                  persistent
                  width="290px"
                >
                  <!-----------------------START---------------------------------------------->
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
                <v-text-field
                  v-model="description"
                  type="text"
                  label="Description"
                >
                  >
                </v-text-field>
                <v-btn
                  type="submit"
                  color="primary"
                  class="mr-4"
                  @click.stop="hourReport = false"
                >
                  Add
                </v-btn>
              </v-form>
            </v-container>
          </v-card>
        </v-dialog>
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
        { text: 'Delete', value: 'actions', sortable: false },
      ],
      hours: [],
      operator: '',
      uniId: '',
      assignedH: '',
      complH: '',
      description: '',
      time2: null,
      time: null,
      modal: false,
      modal2: false,
      end: null,
      hourReport: false,
      date: '',
      deldialog: false,
      currdel: [],
    }),
    mounted () {
      this.getUser()
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
            this.date = ''
            this.time = ''
            this.time2 = ''
            this.description = ''
          } else {
            alert('Complete all the fields')
          }
        } catch (error) {

        }
      },
      async submitHours (date, time, time2, description) {
        console.log(date, time, time2, description)
        try {
          await this.$auth.submitHours(date, time, time2, description)
          setTimeout(() => { this.getHours() }, 1000)
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
          await this.$auth.getUserHours().then(
            response => {
              var res = response.data
              console.log(res)
              this.hours = []
              for (var i = 0; i < res.length; i++) {
                this.hours.push({
                  shiftDate: res[i][0].slice(0, 10),
                  shiftStart: res[i][1].slice(0, 5),
                  shiftEnd: res[i][2].slice(0, 5),
                  workDescription: res[i][3],
                  id: res[i][12],
                  state: res[i][4] === 1 ? 'pending' : res[i][4] === 2 ? 'approved' : 'not approved',
                  delete: res[i][4],
                })
              }
            })
        } catch (error) {
          this.error = true
        }
      },
      async getUser () {
        try {
          await this.$auth.getUser().then(
            response => {
              var res = response.data
              console.log(res)
              for (var i = 0; i < res.length; i++) {
                this.operator = res[0]
                this.uniId = res[3]
                this.assignedH = res[1]
                this.complH = res[2]
              }
            })
        } catch (error) {
          this.error = true
        }
      },
      delet (item) {
        this.currdel = item
        this.deldialog = true
        console.log(item)
      },
      async delitem () {
        try {
          this.deldialog = false
          await this.$auth.delHourReport(this.currdel.id)
          setTimeout(() => { this.getHours() }, 1000)
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
  color: #3c1b66;
  font-weight: normal;
  font-size: 15px;
  font-family: Arial;
  text-transform: uppercase;
}
h3 {
  color: #443963;
  font-weight: normal;
  font-size: 30px;
  font-family: Arial;
  text-transform: lowercase;
}
h4 {
  color: #4f4866;
  font-weight: normal;
  font-size: 25px;
  font-family: Arial;
  text-transform: lowercase;
}
h5 {
  color: #656172;
  font-weight: normal;
  font-size: 20px;
  font-family: Arial;
  text-transform: lowercase;
}
h6 {
  color: #747377;
  font-weight: normal;
  font-size: 18px;
  font-family: Arial;
  text-transform: lowercase;
}
</style>
