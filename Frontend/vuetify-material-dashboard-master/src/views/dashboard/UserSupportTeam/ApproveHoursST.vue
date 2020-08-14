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
              v-if="item.state === 'pending'"
              small
              class="mr-2"
              @click="declinehours(item.worklogid)"
            >
              mdi-check
            </v-icon>
            <!-- v-if="item.delete === 1" -->
            <v-icon
              v-if="item.state === 'pending'"
              small
              class="mr-2"
              @click="aprovehours(item.worklogid)"
            >
              mdi-close
            </v-icon>
          </template>
        </v-data-table>
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
    }),
    mounted () {
      this.getHours()
    },
    methods: {
      async getHours () {
        try {
          await this.$auth.getHours().then(
            response => {
              var res = response.data
              this.hours = []
              console.log(res)
              for (var i = 0; i < res.length; i++) {
                this.hours.push({
                  shiftDate: res[i][0].slice(0, 10),
                  shiftStart: res[i][1].slice(0, 5),
                  shiftEnd: res[i][2].slice(0, 5),
                  operator: res[i][5],
                  workDescription: res[i][3],
                  state: res[i][4] === 1 ? 'pending' : res[i][4] === 2 ? 'approved' : 'not approved',
                  worklogid: res[i][11],
                })
              }
            })
        } catch (error) {
          this.error = true
        }
      },
      aprovehours (id) {
        this.changeHours(id, 'Denied')
      },
      declinehours (id) {
        this.changeHours(id, 'Completed')
      },
      async changeHours (id, newStatus) {
        console.log(id, newStatus)
        try {
          await this.$auth.changeHourReport(id, newStatus)
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
</style>
