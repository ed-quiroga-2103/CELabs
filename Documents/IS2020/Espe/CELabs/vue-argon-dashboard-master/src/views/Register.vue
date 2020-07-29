<template>
    <div class="row justify-content-center">
        <div class="col-lg-5 col-md-7">
            <div class="card bg-secondary shadow border-0">
                <div class="card-body px-lg-5 py-lg-5">
                    <div class="text-center text-muted mb-4">
                        <small>Or sign up with credentials</small>
                    </div>
                     <FormulateForm v-model="formValues" @submit="handleSubmit()">
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
                                class="input-group-alternative"
                                type ="password" 
                                name="password1" 
                                label="Password" 
                                v-model = "pass" 
                                @input="encriptar" 
                                validation="required|max:16|min:8"/>
                                <FormulateInput
                                type="select"
                                name="user_type"
                                label="User type"
                                :options="{1: 'Administrator', 2: 'Operator', 3: 'Professor', 4: 'Administrative'}"
                                />
                                
                                <div class="text-center">
                                    <FormulateInput type="submit" class="my-4" label="Sign in"/>
                                </div>
                        </FormulateForm>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col-6">
                    <a href="#" class="text-light">
                        <small>Forgot password?</small>
                    </a>
                </div>
                <div class="col-6 text-right">
                    <router-link to="/login" class="text-light">
                        <small>Login into your account</small>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
  import axios from "axios";
  export default {
    name: 'register',
    created() {},
    data: () => ({
    pass: '',
    formValues:{
                name: '',
                lastname1: '',
                lastname2: '',
                id_number: '',
                password: '',
                email: '',
                phone_number: '',
                university_id: '',
                user_type: ''
     }
  }),
    methods: {
    encriptar(){
       this.formValues.password = this.$md5(this.pass)
       

    },
    handleSubmit(){
        delete this.formValues.password1
        console.log(this.formValues)
        this.register()
        this.formValues ={
                name: '',
                lastname1: '',
                lastname2: '',
                id_number: '',
                password: '',
                email: '',
                phone_number: '',
                university_id: '',
                user_type: ''
     }
        

  
  }, 
  register(){
      axios.post(`http://127.0.0.1:5001/user`, 
           this.formValues
        ) 
        .then(response => {
        this.posts = response.data;
        alert(this.posts['message']);
      }
      );
  
  }


  }
  }
</script>
<style>
</style>
