<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://i.ibb.co/txtdCJ1/logo.png"
          transition="scale-transition"
          min-width="70"
          width="40"
        />
        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          width="40"
        />
      </div>
      <v-spacer />
      <div
        class="mx-3"
      />
      <v-btn
        class="ml-1"
        min-width="0"
        text
        to="/login"
      >
        <span class="mr-1">Log In</span>
        <v-spacer />
        <v-spacer />
      </v-btn>
      <v-btn
        class="ml-1"
        min-width="0"
        text
        to="/register"
      >
        <span class="mr-1">Sign up</span>
        <v-spacer />
        <v-spacer />
      </v-btn>
    </v-app-bar>

    <dashboard-core-view />

    <dashboard-core-settings />
  </v-app>
</template>

<script>
  export default {
    name: '',

    components: {
      // DashboardCoreAppBar: () => import('./compOperator/AppBarOP'),
      DashboardCoreSettings: () => import('./components/core/Settings'),
      DashboardCoreView: () => import('./components/core/View'),
    },

    data: () => ({
      expandOnHover: false,
    }),
  }
</script>
