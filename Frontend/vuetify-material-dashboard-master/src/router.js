import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/views/dashboard/IndexOP.vue'
import IndexAD from '@/views/dashboard/IndexAD.vue'
import IndexLogin from '@/views/dashboard/IndexLogin.vue'
import IndexP from '@/views/dashboard/IndexP.vue'
import IndexA from '@/views/dashboard/IndexA.vue'
import IndexST from '@/views/dashboard/IndexST.vue'
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
          name: 'allnighter',
          component: () => import('./views/dashboard/UserOperator/AllNightersOP.vue'),
        },
        {
          path: 'myan',
          name: 'myan',
          component: () => import('./views/dashboard/UserOperator/MyAN.vue'),
        },
        {
          path: 'availability',
          name: 'availability',
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
          name: 'dashboard2',
          component: () => import('./views/dashboard/Dashboard.vue'),
        },
        {
          path: 'availability',
          name: 'availability2',
          component: () => import('./views/dashboard/UserAdmin/AvailabilityAD.vue'),
        },
        {
          path: 'OPHours',
          name: 'OPHours2',
          component: () => import('./views/dashboard/UserAdmin/OperatorHours.vue'),
        },
        {
          path: 'Inventory',
          name: 'Inventory2',
          component: () => import('./views/dashboard/UserAdmin/InventoryReportAD.vue'),
        },
        {
          path: 'Faults',
          name: 'Faults2',
          component: () => import('./views/dashboard/UserAdmin/FaultsAD.vue'),
        },
        {
          path: 'Operators',
          name: 'Operators2',
          component: () => import('./views/dashboard/UserAdmin/Operators.vue'),
        },
        {
          path: 'AddCourse',
          name: 'AddCourse2',
          component: () => import('./views/dashboard/UserAdmin/AddCourseAD.vue'),
        },
        {
          path: 'CreateUser',
          name: 'CreateUser2',
          component: () => import('./views/dashboard/UserAdmin/CreateUsersAD.vue'),
        },
        {
          path: 'myaccount',
          name: 'myac',
          component: () => import('./views/dashboard/UserAdmin/MyaccountAD.vue'),
        },
      ],
    },
    {
      path: '/ST',
      component: IndexST,
      children: [
        {
          path: '',
          name: 'dashboard3',
          component: () => import('./views/dashboard/Dashboard.vue'),
        },
        {
          path: 'Inventory',
          name: 'Inventory3',
          component: () => import('./views/dashboard/UserSupportTeam/InventoryReportST.vue'),
        },
        {
          path: 'Faults',
          name: 'Faults3',
          component: () => import('./views/dashboard/UserSupportTeam/FaultsST.vue'),
        },
        {
          path: 'CreateUser',
          name: 'CreateUser3',
          component: () => import('./views/dashboard/UserSupportTeam/CreateOperator.vue'),
        },
        {
          path: 'myhours',
          name: 'myhours3',
          component: () => import('./views/dashboard/UserSupportTeam/MyHoursST.vue'),
        },
        {
          path: 'aproveHours',
          name: 'aproveHours3',
          component: () => import('./views/dashboard/UserSupportTeam/ApproveHoursST.vue'),
        },
        {
          path: 'Operators',
          name: 'Operators3',
          component: () => import('./views/dashboard/UserSupportTeam/OperatorsST.vue'),
        },
        {
          path: 'myaccount',
          name: 'myaccount3',
          component: () => import('./views/dashboard/UserSupportTeam/MyAccountST.vue'),
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
          name: 'availability4',
          component: () => import('./views/dashboard/UserProfessor/AvailabilityP.vue'),
        },
        {
          path: 'myaccount',
          name: 'myaccount4',
          component: () => import('./views/dashboard/UserProfessor/MyAccountP.vue'),
        },
        {
          path: 'myaccount2',
          name: 'myaccount42',
          component: () => import('./views/dashboard/UserProfessor/MyAccountP.vue'),
        },
        {
          path: 'myreservations',
          name: 'myres4',
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
          name: 'availability5',
          component: () => import('./views/dashboard/UserAdministrative/AvailabilityA.vue'),
        },
        {
          path: 'myaccount',
          name: 'myaccount5',
          component: () => import('./views/dashboard/UserAdministrative/MyAccountA.vue'),
        },
        {
          path: 'myreservations',
          name: 'myres5',
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
