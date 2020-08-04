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
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
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
        <span class="mr-1">Login</span>
        <v-spacer />
        <v-spacer />
      </v-btn>
      <v-btn
        class="ml-1"
        min-width="0"
        text
        to="/register"
      >
        <span class="mr-1">Register</span>
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
