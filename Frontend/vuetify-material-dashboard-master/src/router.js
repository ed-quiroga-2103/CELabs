import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/views/dashboard/IndexOP.vue'
import IndexAD from '@/views/dashboard/IndexAD.vue'
import IndexLogin from '@/views/dashboard/IndexLogin.vue'
import IndexP from '@/views/dashboard/IndexP.vue'
import IndexA from '@/views/dashboard/IndexA.vue'
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
          path: 'availability',
          name: 'availability1',
          component: () => import('./views/dashboard/UserOperator/AvailabilityOP.vue'),
        },
        {
          path: '/faults',
          name: 'faults',
          component: () => import('./views/dashboard/UserOperator/ReportFaultsOP.vue'),
        },
      ],
    },
    {
      path: '/adm',
      component: IndexAD,
      children: [
        {
          path: '',
          name: 'dashboard',
          component: () => import('./views/dashboard/Dashboard.vue'),
        },
        {
          path: 'availability',
          name: 'availability2',
          component: () => import('./views/dashboard/UserAdmin/AvailabilityAD.vue'),
        },
      ],
    },
    {
      path: '/prof',
      component: IndexP,
      children: [
        {
          path: '',
          name: 'dashboard1',
          component: () => import('./views/dashboard/Dashboard.vue'),
        },
        {
          path: 'availability',
          name: 'availability3',
          component: () => import('./views/dashboard/UserProfessor/AvailabilityP.vue'),
        },
      ],
    },
    {
      path: '/pa',
      component: IndexA,
      children: [
        {
          path: '',
          name: 'dashboard2',
          component: () => import('./views/dashboard/Dashboard.vue'),
        },
        {
          path: 'availability',
          name: 'availability4',
          component: () => import('./views/dashboard/UserAdministrative/AvailabilityA.vue'),
        },
        {
          path: '/myaccount',
          name: 'myaccount',
          component: () => import('./views/dashboard/UserOperator/MyAccountOP.vue'),
        },
        {
          path: '/myhours',
          name: 'myhours',
          component: () => import('./views/dashboard/UserOperator/MyHoursOP.vue'),
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
  ],
})
