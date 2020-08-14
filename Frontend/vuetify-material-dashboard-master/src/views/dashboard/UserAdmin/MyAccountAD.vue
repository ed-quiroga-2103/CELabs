<template>
  <v-row class="">
    <v-col>
      <template>
        <v-card
          class="mx-auto"
          color="#607D8B"
          dark
          max-width="400"
        >
          <v-card-title class="d-flex justify-content-center">
            <v-icon
              large
              left
            >
              mdi-account
            </v-icon>
            <span class="title font-weight-light ">Account Information</span>
          </v-card-title>

          <v-card-text class="headline font-weight-bold ">
            <v-row>
              <h2>Name:</h2>
            </v-row>
            <v-row>
              <label v-text="user" />
            </v-row>
            <v-row>
              <h2>Last name:</h2>
            </v-row>
            <v-row>
              <label v-text="apellido1" />
            </v-row>
            <v-row>
              <h2>Second last name:</h2>
            </v-row>
            <v-row>
              <label v-text="apellido2" />
            </v-row>
            <v-row>
              <h2>ID number:</h2>
            </v-row>
            <v-row>
              <label v-text="Idnumb" />
            </v-row>
            <v-row>
              <h2>ID University IDr:</h2>
            </v-row>
            <v-row>
              <label v-text="Iduni" />
            </v-row>
            <v-row>
              <h2>Email:</h2>
            </v-row>
            <v-row>
              <label v-text="email" />
            </v-row>
            <v-row>
              <h2>Phone number:</h2>
            </v-row>
            <v-row>
              <label v-text="numero" />
            </v-row>
          </v-card-text>
        </v-card>
      </template>
    </v-col>
    <v-col>
      <v-sheet height="200">
        <v-toolbar
          flat
          color="white"
        >
          <v-col />
          <v-spacer />
          <v-spacer />
          <v-col>
            <v-btn
              outlined
              color="grey darken-2"
              class="mr-8"
              @click="visible= true"
            >
              Edit
            </v-btn>
            <v-menu
              bottom
              right
            />
          </v-col>
        </v-toolbar>
      </v-sheet>
    </v-col>
    <v-dialog
      v-model="visible"
    >
      <v-card
        class="elevation-12"
      >
        <v-toolbar
          color="primary"
          dark
          flat
        >
          <v-toolbar-title>Edit personal information</v-toolbar-title>
          <v-spacer />
        </v-toolbar>
        <FormulateForm
          v-model="formValues"
          @submit="handleSubmit()"
        >
          <v-card-text ml="10">
            <FormulateInput
              class="input-group-alternative mb-3"
              type="text"
              name="name"
              label="Name"
            />
            <FormulateInput
              class="input-group-alternative mb-3"
              type="text"
              name="apellido1"
              label="First Last Name"
            />
            <FormulateInput
              class="input-group-alternative mb-3"
              type="text"
              name="apellido2"
              label="Second Last Name"
            />
            <FormulateInput
              class="input-group-alternative mb-3"
              type="text"
              name="idnumb"
              label="Id Number"
              validation="number"
            />
            <FormulateInput
              class="input-group-alternative mb-3"
              type="text"
              name="numero"
              label="Phone Number"
              validation="number"
            />
            <FormulateInput
              class="input-group-alternative mb-3"
              type="text"
              name="iduni"
              label="University ID"
              validation="number"
            />
            <v-spacer />
            <FormulateInput
              type="submit"
              class="btn btn-primary"
              label="Save"
            />
            <v-btn
              @click="visible = false"
            >
              Cancel
            </v-btn>
          </v-card-text>
        </FormulateForm>
        <v-spacer />
      </v-card>
    </v-dialog>
    <template>
      <v-row justify="center">
        <v-dialog
          v-model="visible2"
          persistent
          max-width="290"
        >
          <v-card>
            <v-card-title class="headline">
              Are you shure you want to delete your account?
            </v-card-title>
            <v-card-text>This action doesn't delete your activity</v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn
                color="blue darken-1"
                text
                @click="
                  visible2 = false
                  putDelete()"
              >
                Delete
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="visible2 = false"
              >
                Cancel
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
    </template>
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
        { text: 'Description of work performed', value: 'workDescription' },
        { text: 'State', value: 'state' },
        { text: 'Delete', value: 'delete' },
      ],
      formValues: {},
      visible: false,
      visible2: false,
      hours: [],
      user: 'Kimberly',
      apellido1: 'Calderón',
      apellido2: 'Prado',
      Idnumb: '28',
      Iduni: '3',
      description: '',
      email: 'kimberlycalderonprado@gmail.com',
      numero: '87764320',
      time2: null,
      time: null,
      modal: false,
      modal2: false,
      end: null,
      hourReport: false,
      date: '',
    }),
    mounted () {
      this.getPerfil()
    },
    methods: {
      ChangeDate (date) {
        var date2 = date[8] + date[9] + '/' + date[5] + date[6] + '/' + date[0] + date[1] + date[2] + date[3]
        return date2
      },
      addHours () {
        try {
          if (this.description && this.time && this.time2 && this.date) {
            var date2 = this.ChangeDate(this.date)
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
      async submitHours (date, time, time2, description) {
        try {
          await this.$auth.submitHours(date, time, time2, description)
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
      async getPerfil () {
        try {
          await this.$auth.getPerfil().then(
            response => {
              console.log(response)
              var res = response.data
              this.user = res[0]
              this.apellido1 = res[1]
              this.apellido2 = res[2]
              this.Idnumb = res[3]
              this.Iduni = res[6]
              this.numero = res[5]
              this.email = res[4]
              this.formValues =
                {
                  name: this.user,
                  apellido1: this.apellido1,
                  apellido2: this.apellido2,
                  idnumb: this.Idnumb,
                  iduni: this.Iduni,
                  numero: this.numero,
                  email2: this.email,
                }
            })
        } catch (error) {
          this.error = true
        }
      },
      async handleSubmit () {
        console.log(this.formValues)
        try {
          await this.$auth.putPerfil(this.formValues.name, this.formValues.apellido1, this.formValues.apellido2, this.formValues.idnumb, this.formValues.numero, this.formValues.iduni)
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
      async putDelete () {
        try {
          await this.$auth.putDelete()
          this.$router.push('/')
        } catch (error) {
          this.error = true
          alert('Error submiting report')
        }
      },
    },
  }
</script>
<style scoped>
.controls {
  position: relative;
}
.css
h1 {
  color: #6c2eb9;
  font-weight: normal;
  font-size: 20px;
  font-family: Arial;
  text-transform: uppercase;
}
h2 {
  color: #40C4FF;
  font-size: 15px;
  text-transform: uppercase;
}
</style>
