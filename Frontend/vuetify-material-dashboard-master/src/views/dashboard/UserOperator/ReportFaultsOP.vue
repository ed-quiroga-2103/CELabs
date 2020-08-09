<template>
  <v-app id="inspire">
    <v-main>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="elevation-12">
              <v-toolbar
                color="primary"
                dark
                flat
              >
                <v-toolbar-title>Report Fault</v-toolbar-title>
                <v-spacer />
                <v-tooltip bottom>
                  <span>Source</span>
                </v-tooltip>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-radio-group
                    v-model="radios"
                    :mandatory="false"
                  >
                    <v-radio
                      label="Laboratorio 1"
                      value="Laboratorio1"
                    />
                    <v-radio
                      label="Laboratorio 2"
                      value="2"
                    />
                  </v-radio-group>
                  <v-text-field
                    id="IDNo"
                    v-model="Idnumb"
                    label="IDNo"
                    name="ID No."
                    type="text"
                  />
                  <v-textarea
                    v-model="textarea"
                    solo
                    name="input-7-4"
                    label="Fault description"
                  />
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn
                  color="primary"
                  @click="submitFault()"
                >
                  Submit
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      pass: '',
      reportValues: {
        radios: '',
        Idnumb: '',
        textarea: '',
      },
    }),
    methods: {
      async submitFault (){
        this.submitFault()
        try{
          await this.$auth.submitFault(this.reportValues)
          this.$router.push('/start')
        } catch (error) {
          this.error = true;
          alert('Error submiting report')
        }
        this.reportValues = {
        radios: '',
        Idnumb: '',
        textarea: '',
        }
      },
    },
  }

</script>