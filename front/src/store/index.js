import Vue from "vue";
import Vuex from "vuex";
import auth from '@/store/modules/auth'
import categs from '@/store/modules/categs'
Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    auth,
    categs
  },
});