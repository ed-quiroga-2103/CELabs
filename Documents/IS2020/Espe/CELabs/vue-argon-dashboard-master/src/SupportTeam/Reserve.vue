<template>
  <div class="LogIn">
    <form @submit="login">
      <h3>Log In</h3>
      <p>Email:</p>
      <input type="email" v-model="email" name="email" placeholder="myemail@xtec.cr">
      <p>Password:</p>
      <input type="password" v-model="password" name="email" placeholder="********">
      <button type="submit">Log In</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LogIn',
  signIn(){
    const loginfo = {
      email:this.email,
      password:this.password
    };
    this.$emit('login-info',loginfo);
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
