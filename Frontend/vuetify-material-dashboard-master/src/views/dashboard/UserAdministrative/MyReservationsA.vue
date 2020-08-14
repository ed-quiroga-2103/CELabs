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
            to="/op/allnighter"
          >
            Request All-Nighter
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
          :items="an"
          :items-per-page="5"
          class="elevation-1"
        >
          <template v-slot:item.actions="{ item }">
            <v-icon
              v-if="item.delete === 1"
              small
              class="mr-2"
              @click="delet(item)"
            >
              mdi-delete
            </v-icon>
          </template>
        </v-data-table>
        <v-dialog
          v-model="deldialog"
          width="500"
          height="300"
        >
          <v-card>
            <v-card-title class="headline grey lighten-2">
              Delete confirmation.
            </v-card-title>
            <v-card-text>
              Are you sure you wish to delete this report?
            </v-card-text>
            <v-divider />
            <v-card-actions>
              <v-btn
                color="primary"
                text
                @click="delitem()"
              >
                Yes
              </v-btn>
              <v-spacer />
              <v-btn
                color="primary"
                text
                @click="deldialog = false"
              >
                No
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!--------------Add event------------------------------------------------------>
        <v-dialog v-model="faultReport">
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
                  id="IDNo"
                  v-model="Idnumb"
                  label="IDNo"
                  name="ID No."
                />
                <v-textarea
                  v-model="textarea"
                  solo
                  name="input-7-4"
                  label="Fault description"
                />
              </v-form>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="primary"
                  @click="addFault()"
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
      expanded: [],
      headers: [
        {
          text: 'Date of Request',
          align: 'start',
          value: 'DateofRequest',
        },
        { text: 'Requested Date', value: 'RequestedDate' },
        { text: 'Responsible', value: 'Responsible' },
        { text: 'Current State', value: 'CurrentState' },
        { text: 'Delete', value: 'Delete', sortable: false },
      ],
      an: [],
      radios: '',
      currdel: [],
      deldialog: false,
      Idnumb: '',
      textarea: '',
      faultReport: false,
    }),
    mounted () {
      this.getANuser()
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
      async getANuser () {
        try {
          console.log('hola')
          this.an = []
          await this.$auth.getANuser().then(
            response => {
              var res = response.data
              console.log(res)
              for (var i = 0; i < res.length; i++) {
                this.an.push({
                  DateofRequest: res[i][0].slice(0, 10),
                  RequestedDate: res[i][1].slice(0, 10),
                  Responsible: res[i][6],
                  CurrentState: res[i][5] === 0 ? 'pending' : res[i][5] === 1 ? 'approved' : 'denied',
                  Delete: res[i][5],
                })
              }
              console.log(this.an)
            })
        } catch (error) {
          this.error = true
        }
      },
      async delitem () {
        try {
          await this.$auth.delHourReport(this.currdel).then(
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
