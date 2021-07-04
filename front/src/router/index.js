import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home";
import ProdSearch from "@/views/ProdSearch";
import ProdFilter from "@/views/ProdFilter";
import CategProds from "@/views/CategProds";
import SignUp from "@/views/auth/SignUp";
import ConfirmEmail from '@/views/auth/ConfirmEmail'
import Login from '@/views/auth/Login'
import Activate from '@/views/auth/Activate'
import Google from '@/views/auth/Google'
import GoogleForm from '@/views/auth/GoogleForm'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    // to render all ideas for search
    path: '/product-search/:term',
    name: 'search',
    component: ProdSearch
  },
  {
    // to render all ideas for search
    path: '/product-filter/:sort',
    name: 'filter',
    component: ProdFilter
  },
  {
    // to render all ideas for a given category
    path: '/category-idea/:slug',
    name: 'categ',
    component: CategProds 
  },
  {
    path: "/signup",
    name: "signup",
    component: SignUp,
  },
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/google-login",
    name: "google",
    component: Google,
  },
  {
    path: "/google",
    name: "google-form",
    component: GoogleForm,
  },
  {
    path: "/confirm-email-link/",
    name: "confirmEmail",
    component: ConfirmEmail,
  },
  {
    path: "/activate/:uid/:token",
    name: "activate",
    component: Activate,
    props:true
  },  
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;