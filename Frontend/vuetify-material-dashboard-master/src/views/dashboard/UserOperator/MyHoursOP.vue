<template>
  <v-row class="">
    <v-col>
      <v-sheet height="64">
        <v-toolbar
          flat
          color="white"
        >
          <v-spacer />
          <v-spacer />
          <v-btn
            outlined
            color="grey darken-2"
            @click="hourReport = true"
          >
            Reservation
          </v-btn>
          <v-menu
            bottom
            right
          />
        </v-toolbar>
      </v-sheet>
      <!--------------PUT the log here------------------------------------------------------>
      <v-sheet height="600">
        <v-data-table
          :headers="headers"
          :items="hours"
          :items-per-page="5"
          class="elevation-1"
        />
        <!--------------Add event------------------------------------------------------>
        <v-dialog v-model="hourReport">
          <v-card>
            <v-container>
              <v-form @submit.prevent="addEvent">
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
          sortable: false,
          value: 'shiftDate',
        },
        { text: 'Shift start time', value: 'shiftStart' },
        { text: 'Shift end time', value: 'shiftEnd' },
        { text: 'Description of work performed', value: 'workDescription' },
        { text: 'State', value: 'state' },
        { text: 'Delete', value: 'delete' },
      ],
      hours: [{
        shiftStart: '10:10',
        shiftEnd: '11:20',
        workDescription: 'Se hizo el brete',
        state: 'Pending',
        delete: 'X',
        shiftDate: '09/08/2020',
      }],
      description: '',
      time2: null,
      time: null,
      modal: false,
      modal2: false,
      end: null,
      hourReport: false,
      date: '',
    }),
    methods: {
      ChangeDate (date) {
        date = date[8] + date[9] + '/' + date[5] + date[6] + '/' + date[0] + date[1] + date[2] + date[3]
        return date
      },
      addEvent () {
        console.log(this.lab)
        console.log(this.description)
        try {
          if (this.description && this.time && this.time2 && this.date) {
            const date2 = this.ChangeDate(this.date)
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
      async submitHours () {
        try {
          await this.$auth.submitHours(this.date, this.time, this.time2, this.description)
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
    },
  }
</script>
<style scoped>
.controls {
  position: relative;
}
</style>
