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
            Report Fault
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
          :items-per-page="5"
          class="elevation-1"
        />
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
                  label="Number of incomplete computers"
                  name="completeComp"
                  type="text"
                />
                <v-text-field
                  id="incompleteComp"
                  v-model="incompleteComp"
                  label="Number of incomplete computers"
                  name="incompleteComp"
                  type="text"
                />
                <v-text-field
                  id="numbProjectors"
                  v-model="projectors"
                  label="Number of Projectors"
                  name="numbProjectors"
                  type="text"
                />
                <v-text-field
                  id="numChairs"
                  v-model="chairs"
                  label="Number of chairs"
                  name="numChairs"
                  type="text"
                />
                <v-text-field
                  id="fireExt"
                  v-model="fireExt"
                  label="Number of fire extinguishers"
                  name="fireExt"
                  type="text"
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
        { text: 'ID(Faulty part)', value: 'faultypartID' },
        { text: 'See More', value: 'faultypartID' },
      ],
      reports: [],
      radios: '',
      completeComp: '',
      incompleteComp: '',
      projectors: '',
      chairs: '',
      fireExt: '',
      textarea: '',
      invReport: false,
    }),
    mounted () {
      this.getFaultReports()
    },
    methods: {
      async submitInv () {
        this.invReport = false
        try {
          await this.$auth.submitInv(this.radios, this.completeComp, this.incompleteComp, this.projectors, this.chairs, this.fireExt)
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
          await this.$auth.getFaultReports().then(
            response => {
              var res = response.data
              console.log(res)
              for (var i = 0; i < res.length; i++) {
                this.reports.push({
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
