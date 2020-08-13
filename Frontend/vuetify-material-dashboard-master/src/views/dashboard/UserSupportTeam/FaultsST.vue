<template>
  <v-row class="">
    <v-col>
      <!--------------PUT the log here------------------------------------------------------>
      <div id="app">
        <v-app id="inspire">
          <v-data-table
            :headers="headers"
            :items="reports"
            :single-expand="true"
            :expanded.sync="expanded"
            :items-per-page="15"
            item-key="reportNo"
            show-expand
            class="elevation-1"
          >
            <template v-slot:item.actions="{ item }">
              <!-- v-if="item.delete === 1" -->
              <v-icon
                small
                class="mr-2"
                @click="openChangeDialog(item.worklogid)"
              >
                Change Status
              </v-icon>
            </template>
          </v-data-table>
        </v-app>
      </div>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      expanded: [],
      headers: [
        {
          text: 'Report Number',
          align: 'start',
          value: 'reportNo',
        },
        { text: 'Report Date', value: 'reportD' },
        { text: 'Report Time', value: 'reportT' },
        { text: 'Laboratory Number', value: 'labNo' },
        { text: 'ID(Faulty part)', value: 'faultypartID' },
        { text: 'Change Status', value: 'actions', sortable: false },
        { text: '', value: 'data-table-expand' },
      ],
      reports: [],
      radios: '',
      Idnumb: '',
      textarea: '',
      faultReport: false,
    }),
    mounted () {
      this.getFaultReports()
    },
    methods: {
      addFault () {
        try {
          if (this.radios && this.Idnumb && this.textarea) {
            this.submitFault()
          } else {
            alert('Complete all the fields')
          }
        } catch (error) {

        }
      },
      async submitFault () {
        this.faultReport = false
        try {
          await this.$auth.submitFault(this.radios, this.Idnumb, this.textarea)
          setTimeout(() => { this.getFaultReports() }, 1000)
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
      async getFaultReports () {
        try {
          this.reports = []
          await this.$auth.getFaultReports().then(
            response => {
              var res = response.data
              console.log(res)
              for (var i = 0; i < res.length; i++) {
                this.reports.push({
                  description: res[i][2],
                  reportD: res[i][0].slice(0, 10),
                  reportT: res[i][0].slice(10, 16),
                  labNo: res[i][4] === 1 ? 'F2-09' : 'F2-10',
                  faultypartID: res[i][1],
                  reportNo: res[i][5],
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
