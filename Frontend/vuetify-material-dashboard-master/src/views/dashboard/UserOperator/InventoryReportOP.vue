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
            @click="invReport = true"
          >
            Inventory Report
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
          :items="reports"
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar
              flat
              color="white"
            >
              <v-spacer />
              <v-dialog
                v-model="dialog"
                max-width="500px"
              >
                <v-card>
                  <v-card-actions>
                    <v-spacer />
                    <v-btn
                      color="blue darken-1"
                      text
                      @click="close"
                    >
                      Cancel
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
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
                    />
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="showInv.incompleteComp"
                      disabled
                      label="Incomplete Computers"
                    />
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="showInv.projectors"
                      disabled
                      label="Projectos"
                    />
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="showInv.chairs"
                      disabled
                      label="Chairs"
                    />
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="showInv.fireExt"
                      disabled
                      label="Fire Extiguishers"
                    />
                  </v-row>
                  <v-row>
                    <v-text-field
                      v-model="showInv.det"
                      disabled
                      label="Details"
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
        <!--------------Add event------------------------------------------------------>
        <v-dialog v-model="invReport">
          <v-card>
            <v-container>
              <v-form>
                <v-radio-group
                  v-model="radios"
                  :mandatory="false"
                >
                  <v-radio
                    label="F2-09"
                    value="F2-09"
                  />
                  <v-radio
                    label="F2-10"
                    value="F2-10"
                  />
                </v-radio-group>
                <v-text-field
                  id="completeComp"
                  v-model="completeComp"
                  label="Number of complete computers"
                  name="completeComp"
                  type="number"
                />
                <v-text-field
                  id="incompleteComp"
                  v-model="incompleteComp"
                  label="Number of incomplete computers"
                  name="incompleteComp"
                  type="number"
                />
                <v-text-field
                  id="numbProjectors"
                  v-model="projectors"
                  label="Number of Projectors"
                  name="numbProjectors"
                  type="number"
                />
                <v-text-field
                  id="numChairs"
                  v-model="chairs"
                  label="Number of chairs"
                  name="numChairs"
                  type="number"
                />
                <v-text-field
                  id="fireExt"
                  v-model="fireExt"
                  label="Number of fire extinguishers"
                  name="fireExt"
                  type="number"
                />
                <v-textarea
                  v-model="textarea"
                  solo
                  name="input-7-4"
                  label="Details"
                />
              </v-form>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="primary"
                  @click="submitInv()"
                >
                  Submit
                </v-btn>
              </v-card-actions>
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
          text: 'Report Number',
          align: 'start',
          sortable: false,
          value: 'reportNo',
        },
        { text: 'Report Date', value: 'reportD' },
        { text: 'Report Time', value: 'reportT' },
        { text: 'Laboratory Number', value: 'labNo' },
        { text: 'Report', value: 'actions', sortable: false },
        { text: 'Details', value: 'detail' },
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
      textarea: '',
      invReport: false,
    }),
    mounted () {
      this.getInvReports()
    },
    methods: {
      seeMore (item) {
        console.log(item)
        this.showInv.completeComp = item.completeComp
        this.showInv.incompleteComp = item.incompleteComp
        this.showInv.projectors = item.projectors
        this.showInv.chairs = item.chairs
        this.showInv.fireExt = item.fireExt
        this.det = item.det
        this.dialog2 = true
      },
      close () {
        this.dialog2 = false
      },
      async submitInv () {
        this.invReport = false
        try {
          if (this.radios && this.completeComp && this.incompleteComp && this.projectors && this.chairs && this.fireExt) {
            await this.$auth.submitInv(this.radios, this.completeComp, this.incompleteComp, this.projectors, this.chairs, this.fireExt)
          } else {
            alert('Complete all the fields')
          }
        } catch (error) {
          alert('Error submiting report')
        }
        this.reportValues = {
          radios: '',
          Idnumb: '',
          textarea: '',
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
                  det: 'Not implemented yet',
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
