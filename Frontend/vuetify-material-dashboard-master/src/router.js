import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/views/dashboard/IndexOP.vue'
import IndexAD from '@/views/dashboard/IndexAD.vue'
import IndexLogin from '@/views/dashboard/IndexLogin.vue'
import IndexP from '@/views/dashboard/IndexP.vue'
import IndexA from '@/views/dashboard/IndexA.vue'
import IndexSat from '@/views/dashboard/IndexSat.vue'
Vue.use(Router)

export default new Router({
  linkExactActiveClass: 'active',
  routes: [
    {
      path: '/op',
      redirect: '/op/availability',
      component: Index,
      children: [
        {
          path: 'allnighter',
          name: 'allnighter2',
          component: () => import('./views/dashboard/UserOperator/AllNightersOP.vue'),
        },
        {
          path: 'myan',
          name: 'myan2',
          component: () => import('./views/dashboard/UserOperator/MyAN.vue'),
        },
        {
          path: 'availability',
          name: 'availability1',
          component: () => import('./views/dashboard/UserOperator/AvailabilityOP.vue'),
        },
        {
          path: 'faults',
          name: 'faults',
          component: () => import('./views/dashboard/UserOperator/ReportFaultsOP.vue'),
        },
        {
          path: 'myaccount',
          name: 'myaccount',
          component: () => import('./views/dashboard/UserOperator/MyAccountOP.vue'),
        },
        {
          path: 'myhours',
          name: 'myhours',
          component: () => import('./views/dashboard/UserOperator/MyHoursOP.vue'),
        },
        {
          path: 'inventory',
          name: 'inventory',
          component: () => import('./views/dashboard/UserOperator/InventoryReportOP.vue'),
        },
      ],
    },
    {
      path: '/adm',
      redirect: '/adm/availability',
      component: IndexAD,
      children: [
        {
          path: 'dashboard',
          name: 'dashboard',
          component: () => import('./views/dashboard/Dashboard.vue'),
        },
        {
          path: 'availability',
          name: 'availability2',
          component: () => import('./views/dashboard/UserAdmin/AvailabilityAD.vue'),
        },
        {
          path: 'OPHours',
          name: 'OPHours',
          component: () => import('./views/dashboard/UserAdmin/OperatorHours.vue'),
        },
        {
          path: 'Inventory',
          name: 'Inventory',
          component: () => import('./views/dashboard/UserAdmin/InventoryReportAD.vue'),
        },
        {
          path: 'Faults',
          name: 'Faults',
          component: () => import('./views/dashboard/UserAdmin/FaultsAD.vue'),
        },
      ],
    },
    {
      path: '/prof',
      redirect: '/prof/availability',
      component: IndexP,
      children: [
        {
          path: 'availability',
          name: 'availability3',
          component: () => import('./views/dashboard/UserProfessor/AvailabilityP.vue'),
        },
        {
          path: 'myaccount',
          name: 'myaccount2',
          component: () => import('./views/dashboard/UserProfessor/MyAccountP.vue'),
        },
        {
          path: 'myreservations',
          name: 'myres',
          component: () => import('./views/dashboard/UserProfessor/MyReservationsP.vue'),
        },
      ],
    },
    {
      path: '/pa',
      redirect: '/pa/availability',
      component: IndexA,
      children: [
        {
          path: 'availability',
          name: 'availability4',
          component: () => import('./views/dashboard/UserAdministrative/AvailabilityA.vue'),
        },
        {
          path: 'myreservations',
          name: 'myres2',
          component: () => import('./views/dashboard/UserAdministrative/MyReservationsA.vue'),
        },
      ],
    },
    {
      path: '/',
      redirect: 'login',
      component: IndexLogin,
      children: [
        {
          path: '/login',
          name: 'login',
          component: () => import('./views/dashboard/Out/Login.vue'),
        },
        {
          path: '/register',
          name: 'register',
          component: () => import('./views/dashboard/Out/Register.vue'),
        },
      ],
    },
    {
      path: '/satisfaccion',
      redirect: '/satisfaccion/form',
      component: IndexSat,
      children: [
        {
          path: 'form',
          name: 'form',
          component: () => import('./views/dashboard/Out/Satisfaccion.vue'),
        },
      ],
    },
  ],
})
