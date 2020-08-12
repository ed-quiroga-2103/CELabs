<template>
  <v-row class="">
    <v-col>
      <!--------------PUT the log here------------------------------------------------------>
      <v-sheet height="600">
        <v-data-table
          :headers="headers"
          :items="reports"
          class="elevation-1"
        >
          <template v-slot:item.actions="{ item }">
            <v-icon
              small
              class="mr-2"
              @click="seeMore(item)"
            >
              See More
            </v-icon>
          </template>
        </v-data-table>
        <v-dialog
          v-model="dialog2"
          max-width="500px"
        >
          <v-card>
            <v-card-text>
              <v-container>
                <v-col>
                  <v-row>
                    <v-text-field
                      v-model="showInv.completeComp"
                      disabled
                      label="Complete computers"
                      type="number"
                    />
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="showInv.incompleteComp"
                      disabled
                      label="Incomplete Computers"
                      type="number"
                    />
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="showInv.projectors"
                      disabled
                      label="Projectors"
                      type="number"
                    />
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="showInv.chairs"
                      disabled
                      label="Chairs"
                      type="number"
                    />
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="showInv.fireExt"
                      disabled
                      label="Fire Extiguishers"
                      type="number"
                    />
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="showInv.det"
                      disabled
                      label="Details"
                      type="text"
                    />
                  </v-row>
                </v-col>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Ok
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <template v-slot:expanded-item="{ headers, item }">
          <td :colspan="headers.length">
            {{ item.descript }}
          </td>
        </template>
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      headers: [
        {
          text: 'Report Number',
          align: 'start',
          sortable: false,
          value: 'reportNo',
        },
        { text: 'Report Date', value: 'reportD' },
        { text: 'Report Time', value: 'reportT' },
        { text: 'Laboratory Number', value: 'labNo' },
        { text: 'Report', value: 'actions', sortable: false },
        { text: 'Details', value: 'det' },
      ],
      reports: [],
      dialog: false,
      dialog2: false,
      radios: '',
      completeComp: '',
      incompleteComp: '',
      projectors: '',
      chairs: '',
      fireExt: '',
      showInv: {
        completeComp: '',
        incompleteComp: '',
        projectors: '',
        chairs: '',
        fireExt: '',
        det: '',
      },
      det: '',
      invReport: false,
    }),
    mounted () {
      this.getInvReports()
    },
    methods: {
      seeMore (item) {
        this.showInv.completeComp = item.completeComp
        this.showInv.incompleteComp = item.incompleteComp
        this.showInv.projectors = item.projectors
        this.showInv.chairs = item.chairs
        this.showInv.fireExt = item.fireExt
        this.showInv.det = item.det
        this.dialog2 = true
      },
      close () {
        this.dialog2 = false
      },
      async submitInv () {
        try {
          if (this.radios && this.completeComp && this.incompleteComp && this.projectors && this.chairs && this.fireExt) {
            await this.$auth.submitInv(this.radios, this.completeComp, this.incompleteComp, this.projectors, this.chairs, this.fireExt, this.det)
            this.invReport = false
          } else {
            alert('Complete all the fields')
          }
        } catch (error) {
          alert('Error submiting report')
        }
      },
      async getInvReports () {
        try {
          await this.$auth.getInvReports().then(
            response => {
              var res = response.data
              console.log(res)
              for (var i = 0; i < res.length; i++) {
                this.reports.push({
                  reportD: res[i][0].slice(0, 10),
                  reportT: res[i][0].slice(11, 16),
                  labNo: res[i][4] === 1 ? 'F2-09' : 'F2-10',
                  Detail: res[i][1],
                  reportNo: res[i][5],
                  completeComp: res[i][1],
                  incompleteComp: res[i][2],
                  projectors: res[i][3],
                  chairs: res[i][4],
                  fireExt: res[i][5],
                  det: res[i][6],
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
