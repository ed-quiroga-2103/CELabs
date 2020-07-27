<template>
        <div class="row justify-content-center">
            <div class="col-lg-5 col-md-7">
                <div class="card bg-secondary shadow border-0">
                  
                    <div class="card-body px-lg-5 py-lg-5">
                        <div class="text-center text-muted mb-4">
                            <small>Sign in</small>
                        </div>
                        <FormulateForm v-model="formValues" @submit="handleSubmit()">
                                <FormulateInput 
                                class="input-group-alternative mb-3"
                                addon-left-icon="ni ni-email-83"
                                type="email" 
                                name="email" 
                                label="Email" 
                                validation="required|email"/>
                                <FormulateInput 
                                class="input-group-alternative"
                                addon-left-icon="ni ni-lock-circle-open"
                                
                                type ="password" 
                                name="password1" 
                                label="Password" 
                                v-model = "pass" 
                                @input="encriptar" 
                                validation="required|max:16|min:8"/>
                                <FormulateInput
                                type="select"
                                name="type"
                                label="Type"
                                :options="{operador: 'Operator', profesor: 'Professor', administrativo: 'Administrative'}"
                                />
                                
                                <div class="text-center">
                                    <FormulateInput type="submit" class="my-4" label="Sign in"/>
                                </div>
                        </FormulateForm>
                        <h3>Values:</h3>
                         {{formValues}}
                    </div>
                </div>
                <div class="row mt-3">
                    <div class="col-6">
                        <a href="#" class="text-light"><small>Forgot password?</small></a>
                    </div>
                    <div class="col-6 text-right">
                        <router-link to="/register" class="text-light"><small>Create new professor or administrative account</small></router-link>
                    </div>
                </div>
            </div>
        </div>
</template>


<script>
import axios from "axios";
const API = "https://jsonplaceholder.typicode.com";
export default {
      created() {
    
  },
  data: () => ({
    pass: '',
    formValues: {      
    }
  }),
  methods: {
    encriptar(){
       this.formValues.password = this.$md5(this.pass)
       

    },
    handleSubmit(){
        console.log(this.get())
        delete this.formValues.password1
        console.log(this.formValues)
        
      //axios.get('https://jsonplaceholder.typicode.com/todos/1').then((result) => {
      //console.log(result.data);
    //})
  },
    get() {
        return axios.get(API+'/todos');
    },
    create(todo) {
        return axios.post(API+'/todos', todo);
    }
  }

};


    
    

</script>

<style>
</style>
