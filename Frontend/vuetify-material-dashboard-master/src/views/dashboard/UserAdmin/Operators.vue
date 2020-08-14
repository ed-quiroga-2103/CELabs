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
          text: 'Uni ID',
          align: 'start',
          value: 'uniId',
        },
        { text: 'Name', value: 'name' },
        { text: 'Last Name 1', value: 'ln1' },
        { text: 'Last Name 2', value: 'ln2' },
        { text: 'Approved Hours', value: 'appHours' },
        { text: 'Pending Hours', value: 'pendHours' },
      ],
      users: [],
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
      async getUsers () {
        try {
          await this.$auth.getUsers().then(
            response => {
              var res = response.data
              this.hours = []
              console.log(res)
              for (var i = 0; i < res.length; i++) {
                this.users.push({
                  uniId:'',
                  name: '',
                  ln1: '',
                  ln2: '',
                  appHours: '',
                  pendHours: '',                  
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
