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
                <v-toolbar-title>Log In</v-toolbar-title>
                <v-spacer />
              </v-toolbar>
              <FormulateForm
                v-model="formValues"
                @submit="handleSubmit()"
              >
                <v-card-text ml="10">
                  <FormulateInput
                    class="input-group-alternative mb-3"
                    type="email"
                    name="username"
                    label="Email"
                    validation="required|email"
                  />
                  <FormulateInput
                    v-model="pass"
                    class="input-group-alternative"
                    type="password"
                    name="password1"
                    label="Password"
                    validation="required|max:16|min:8"
                    @input="encriptar"
                  />
                  <v-spacer />
                  <FormulateInput
                    type="submit"
                    class="btn btn-primary"
                    label="Sign in"
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
        username: '',
        password1: '',
        password: '',

      },
    }),
    methods: {
      encriptar () {
        this.formValues.password = this.$md5(this.pass)
      },
      handleSubmit () {
        this.login()
        this.formValues = {
          username: '',
          password1: '',
          password: '',
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
