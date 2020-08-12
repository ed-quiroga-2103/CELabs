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
        <v-row>
          <v-btn
            class="ml-1"
            min-width="0"
            text
            to="/adm/availability"
          >
            <span class="mr-1">Availability</span>
          </v-btn>
          <v-btn
            class="ml-1"
            min-width="0"
            text
            to="/availability"
          >
            <span class="mr-1">Reservations</span>
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
            to="/"
          >
            <span class="mr-1">Faults</span>
          </v-btn>
          <v-btn
            class="ml-1"
            min-width="0"
            text
            to="/pages/user"
          >
            <span class="mr-1">Inventory</span>
          </v-btn>
          <v-btn
            class="ml-1"
            min-width="0"
            text
            to="/pages/user"
          >
            <span class="mr-1">Approve hours</span>
          </v-btn>
        </v-row>
      </div>
      <v-spacer />
      <v-spacer />
      <v-btn
        class="ml-1"
        min-width="0"
        text
        to="/pages/user"
      >
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
