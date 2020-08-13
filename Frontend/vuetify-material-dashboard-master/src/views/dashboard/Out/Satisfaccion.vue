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
                <v-toolbar-title>Satisfaction</v-toolbar-title>
                <v-spacer />
              </v-toolbar>
              <FormulateForm
                v-model="formValues"
                @submit="handleSubmit()"
              >
                <v-card-text ml="10">
                  <FormulateInput
                    type="select"
                    name="calificacion"
                    label="How would you rate the lab's service?"
                    validation="required"
                    :options="{1: '1', 2: '2', 3:'3', 4: '4', 5: '5', 6: '6', 7:'7', 8:'8', 9:'9', 10:'10'}"
                  />
                  <FormulateInput
                    name="what"
                    type="textarea"
                    label="what did you not like?"
                    validation="required"
                    error-behavior="live"
                  />

                  <FormulateInput
                    name="how"
                    type="textarea"
                    label="How do you think it could be improved?"
                    validation="required"
                    error-behavior="live"
                  />
                  <FormulateInput
                    type="submit"
                    class="btn btn-primary"
                    label="Send"
                  />
                </v-card-text>
              </FormulateForm>
              <v-spacer />
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    props: {
      // eslint-disable-next-line vue/require-default-prop
      source: String,
    },
    data: () => ({
      pass: '',
      formValues: {
        calificacion: '',
        what: '',
        how: '',

      },
    }),
    methods: {
      encriptar () {
        this.formValues.password = this.$md5(this.pass)
      },
      handleSubmit () {
        this.postSatisfaccion(this.formValues.calificacion, this.formValues.what, this.formValues.how)
        this.formValues = {
          calificacion: '',
          what: '',
          how: '',
        }
      },
      async postSatisfaccion (score, comment, comment2) {
        try {
          await this.$auth.postSatisfaccion(score, comment, comment2)
        } catch (error) {
          this.error = true
          alert('Error sending events')
        }
      },

      async login () {
        try {
          await this.$auth.login(this.formValues.username, this.formValues.password).then(
            response => {
              console.log(response.data.user_type)
              // eslint-disable-next-line eqeqeq
              if (response.data.user_type === 2) {
                this.$router.push('/op')
              } else if (response.data.user_type === 1) {
                this.$router.push('/adm')
              } else if (response.data.user_type === 3) {
                this.$router.push('/prof')
              } else if (response.data.user_type === 4) {
                this.$router.push('/pa')
              }
            })
        } catch (error) {
          this.error = true
          alert('The email or password is incorrect')
        }
      },
    },

  }

</script>
