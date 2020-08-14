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
      <div
        id="BarraCentral"
      >
        <v-btn
          class="ml-1"
          min-width="0"
          text
          to="/"
        >
          <span class="mr-1">Availability</span>
        </v-btn>

        <v-btn
          class="ml-1"
          min-width="0"
          text
          to="/"
        >
          <span class="mr-1">All-Nighters</span>
        </v-btn>

        <v-btn
          class="ml-1"
          min-width="0"
          text
          to="/ST/faults"
        >
          <span class="mr-1">Faults</span>
        </v-btn>
        <v-btn
          class="ml-1"
          min-width="0"
          text
          to="/ST/CreateUser"
        >
          <span class="mr-1">Create Operator</span>
        </v-btn>
        <v-btn
          class="ml-1"
          min-width="0"
          text
          to="/ST/Inventory"
        >
          <span class="mr-1">Inventory Report</span>
        </v-btn>
        <v-btn
          class="ml-1"
          min-width="0"
          text
          to="/ST/myhours"
        >
          <span class="mr-1">My hours</span>
        </v-btn>
        <v-btn
          class="ml-1"
          min-width="0"
          text
          to="/ST/aprovehours"
        >
          <span class="mr-1">Aprove hours</span>
        </v-btn>
        <v-btn
          class="ml-1"
          min-width="0"
          text
          to="/ST/Operators"
        >
          <span class="mr-1">Operator Hours</span>
        </v-btn>
      </div>
      <v-spacer />
      <v-spacer />
      <v-btn
        sclass="ml-1"
        min-width="0"
        text
        to="/ST/myaccount"
      >
        <span class="mr-1">My account</span>
        <v-icon>mdi-account</v-icon>
      </v-btn>
      <v-btn
        to="/"
        text
        @click="deleteUserLogged"
      >
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <!--<dashboard-core-drawer /> -->

    <dashboard-core-view />

    <dashboard-core-settings />
  </v-app>
</template>

<script>
  export default {
    name: 'DashboardIndex',

    components: {
      // DashboardCoreAppBar: () => import('./components/core/AppBar'),
      // DashboardCoreDrawer: () => import('./components/core/Drawer'),
      DashboardCoreSettings: () => import('./components/core/Settings'),
      DashboardCoreView: () => import('./components/core/View'),
    },

    data: () => ({
      expandOnHover: false,
    }),
    methods: {
      deleteUserLogged () {
        this.$auth.deleteUserLogged()
      },
    },
  }
</script>
