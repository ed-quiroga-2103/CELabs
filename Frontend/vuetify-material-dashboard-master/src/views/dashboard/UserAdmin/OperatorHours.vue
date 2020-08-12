<template>
  <v-row class="">
    <v-col>
      <!--------------PUT the log here------------------------------------------------------>
      <v-sheet height="600">
        <v-data-table
          :headers="headers"
          :items="hours"
          :items-per-page="5"
          class="elevation-1"
        >
          <template v-slot:item.actions="{ item }">
            <!-- v-if="item.delete === 1" -->
            <v-icon
              small
              class="mr-2"
              @click="delet(item)"
            >
              mdi-check
            </v-icon>
            <!-- v-if="item.delete === 1" -->
            <v-icon
              small
              class="mr-2"
              @click="aprove(item)"
            >
              mdi-close
            </v-icon>
          </template>
        </v-data-table>
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
        { text: 'Operador', value: 'operator' },
        { text: 'Description of work performed', value: 'workDescription' },
        { text: 'State', value: 'state' },
        { text: 'Aprove', value: 'actions', sortable: false },
      ],
      hours: [],
      operator: '',
      uniId: '14578878548',
      assignedH: '28',
      complH: '3',
      description: '',
      time2: null,
      time: null,
      modal: false,
      modal2: false,
      end: null,
      hourReport: false,
      date: '',
      deldialog: false,
      curritem: [],
    }),
    mounted () {
      this.getHours()
    },
    methods: {
      ChangeDate (date) {
        var date2 = date[8] + date[9] + '/' + date[5] + date[6] + '/' + date[0] + date[1] + date[2] + date[3]
        return date2
      },
      async getHours () {
        try {
          // getAllUserhours
          await this.$auth.getHours().then(
            response => {
              var res = response.data
              this.hours = []
              for (var i = 0; i < res.length; i++) {
                this.hours.push({
                  shiftDate: res[i][0].slice(0, 10),
                  shiftStart: res[i][1].slice(0, 5),
                  shiftEnd: res[i][2].slice(0, 5),
                  // operator: res[i][5]
                  workDescription: res[i][3],
                  state: res[i][4] === 1 ? 'pending' : 'accepted',
                })
              }
            })
        } catch (error) {
          this.error = true
        }
      },
      delet (item) {
        this.curritem = item
      },
      async delitem () {
        try {
          await this.$auth.disaproveHourReport(this.curritem).then(
            response => {
              var res = response.data
              console.log(res)
            })
        } catch (error) {
          this.error = true
        }
      },
      aprove (item) {
        this.aproveitem = item
      },
      async aproveitem () {
        try {
          await this.$auth.aproveHourReport(this.curritem).then(
            response => {
              var res = response.data
              console.log(res)
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
