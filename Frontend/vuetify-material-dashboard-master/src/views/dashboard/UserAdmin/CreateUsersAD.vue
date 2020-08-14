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
                <v-toolbar-title>Login form</v-toolbar-title>
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
                    validation="required"
                  />
                  <FormulateInput
                    class="input-group-alternative mb-3"
                    type="text"
                    name="lastname1"
                    label="First Last Name"
                    validation="required"
                  />
                  <FormulateInput
                    class="input-group-alternative mb-3"
                    type="text"
                    name="lastname2"
                    label="Second Last Name"
                    validation="required"
                  />
                  <FormulateInput
                    class="input-group-alternative mb-3"
                    type="text"
                    name="id_number"
                    label="Id Number"
                    validation="required|number"
                  />
                  <FormulateInput
                    class="input-group-alternative mb-3"
                    type="text"
                    name="phone_number"
                    label="Phone Number"
                    validation="required|number"
                  />
                  <FormulateInput
                    class="input-group-alternative mb-3"
                    type="text"
                    name="university_id"
                    label="University ID"
                    validation="required|number"
                  />
                  <FormulateInput
                    class="input-group-alternative mb-3"
                    type="email"
                    name="email"
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
                  />
                  <FormulateInput
                    type="select"
                    name="user_type"
                    label="User type"
                    :options="{ 2: 'Operator', 5:'Support Team'}"
                  />
                  <v-spacer />
                  <FormulateInput
                    type="submit"
                    class="btn btn-primary"
                    label="Create User"
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
    name: 'Register',
    data: () => ({
      pass: '',
      formValues: {
        name: '',
        lastname1: '',
        lastname2: '',
        id_number: '',
        password: '',
        email: '',
        phone_number: '',
        university_id: '',
        user_type: '',
      },
    }),
    created () {},
    methods: {
      handleSubmit () {
        console.log(this.formValues)
        this.register()
        this.formValues = {
          name: '',
          lastname1: '',
          lastname2: '',
          id_number: '',
          password: '',
          email: '',
          phone_number: '',
          university_id: '',
          user_type: '',
        }
      },
      async register () {
        this.formValues.password = this.$md5(this.pass)
        delete this.formValues.password1
        console.log(this.formValues)
        try {
          await this.$auth.registerAD(this.formValues)
        } catch (error) {
        }
      },
    },
  }
</script>
