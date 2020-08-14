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
              <!-- v-if="item.delete === 1" -->
              <v-icon
                v-if="item.status === 'Pending'"
                small
                class="mr-2"
                @click="declineAllNighter(item.reqID)"
              >
                mdi-check
              </v-icon>
              <!-- v-if="item.delete === 1" -->
              <v-icon
                v-if="item.status === 'Pending'"
                small
                class="mr-2"
                @click="aproveAllnighter(item.reqID)"
              >
                mdi-close
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
          text: 'AllNighter Id',
          align: 'start',
          value: 'reqID',
        },
        { text: 'Request Date', value: 'requestD' },
        { text: 'AllNighter Date', value: 'allnightD' },
        { text: 'Start Time', value: 'allnightTS' },
        { text: 'Finish Time', value: 'allnightTF' },
        { text: 'Email', value: 'reqEmail' },
        { text: 'Lab', value: 'labNo' },
        { text: 'Status', value: 'status' },
        { text: 'Aprove', value: 'actions', sortable: false },
        { text: '', value: 'data-table-expand', sortable: false },
      ],
      reports: [],
    }),
    mounted () {
      this.getAllNighters()
    },
    methods: {
      async getAllNighters () {
        try {
          this.reports = []
          await this.$auth.getAllNighters().then(
            response => {
              var res = response.data
              console.log(res)
              for (var i = 0; i < res.length; i++) {
                this.reports.push({
                  allnightD: res[i][0],
                  requestD: res[i][1],
                  allnightTS: res[i][2],
                  allnightTF: res[i][3],
                  description: res[i][4],
                  status: res[i][5] === 0 ? 'Pending' : res[i][5] === 1 ? 'Approved' : 'Denied',
                  reqEmail: res[i][6],
                  labNo: res[i][7],
                  reqID: res[i][8],
                })
              }
            })
        } catch (error) {
          this.error = true
        }
      },
      aproveAllnighter (id) {
        this.changeAllNighterStatus(id, 'Denied')
      },
      declineAllNighter (id) {
        this.changeAllNighterStatus(id, 'Approved')
      },
      async changeAllNighterStatus (id, newStatus) {
        console.log(newStatus)
        this.changeDialog = false
        try {
          await this.$auth.changeAllNighterStatus(id, newStatus)
          setTimeout(() => { this.getAllNighters() }, 1000)
        } catch (error) {
          this.error = true
        }
      },
    },
  }

</script>
