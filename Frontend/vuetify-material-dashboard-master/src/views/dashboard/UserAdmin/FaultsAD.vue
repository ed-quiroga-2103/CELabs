<template>
  <v-row>
    <v-col>
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
            <template v-slot:expanded-item="{ headers, item }">
              <td :colspan="headers.length">
                {{ item.description }}
              </td>
            </template>
            <template v-slot:item.actions="{ item }">
              <v-icon
                small
                class="mr-2"
                @click="openChangeDialog(item)"
              >
                Change Status
              </v-icon>
            </template>
          </v-data-table>
          <v-dialog
            v-model="changeDialog"
            max-width="500px"
          >
            <v-card>
              <v-card-title>
                <span class="headline">Change Status</span>
              </v-card-title>
              <v-radio-group
                v-model="row"
                row
              >
                <v-radio
                  label="Pending"
                  value="Pending"
                />
                <v-radio
                  label="Completed"
                  value="Completed"
                />
                <v-radio
                  label="In process"
                  value="In process"
                />
              </v-radio-group>
              <v-card-actions>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="changeReport()"
                >
                  Save
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="changeDialog = false"
                >
                  Cancel
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
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
        { text: 'Status', value: 'status' },
        { text: 'Change Status', value: 'actions', sortable: false },
        { text: '', value: 'data-table-expand', sortable: false },
      ],
      reports: [],
      changeDialog: false,
      changeitem: [],
      row: '',
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
                  status: res[i][3] === 1 ? 'pending' : res[i][3] === 2 ? 'Completed' : 'In process',
                  reportNo: res[i][5],
                })
              }
            })
        } catch (error) {
          this.error = true
        }
      },
      openChangeDialog (item) {
        this.changeDialog = true
        this.changeitem = item
      },
      async changeReport () {
        console.log(this.row)
        console.log(this.changeitem)
        this.changeDialog = false
        try {
          await this.$auth.changeFaultReport(this.changeitem.reportNo, this.row)
          setTimeout(() => { this.getFaultReports() }, 1000)
        } catch (error) {
          this.error = true
        }
      },
    },
  }

</script>
