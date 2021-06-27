<template>
 <header class="bg-dark"> 
<div>
  
  <b-navbar toggleable="lg" type="dark" variant="dark" class="bg-info-2">
     <b-navbar-brand href="#">      
        <b-icon icon="house-fill"></b-icon>  
        <router-link :to="{ name: 'home' }" class="link-decor"></router-link>          
    </b-navbar-brand> 
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">
          <router-link :to="{ name: 'home' }" class="link-decor" exact active-class="active">Home</router-link>         
        </b-nav-item>
        <template v-if="isAnonymous">
          <b-nav-item href="#">Link</b-nav-item>
          <b-nav-item href="#">Anonymous</b-nav-item>
          <b-nav-item href="#" >
            <router-link :to="{ name: 'login' }" class="link-decor" active-class="active">Login</router-link>
          </b-nav-item>
          <b-nav-item href="#" >
            <router-link :to="{ name: 'signup' }" class="link-decor" active-class="active">SignUp</router-link>
          </b-nav-item>
          <b-nav-item href="#" >
            <router-link :to="{ name: 'google' }" class="link-decor" active-class="active"
              >Login via Google</router-link>
          </b-nav-item>
         </template>        
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>    
        <template v-if="isLoggedIn">
              <b-nav-item href="#">Link</b-nav-item>
              <b-nav-item href="#">IsLoggedIn</b-nav-item>              
              <b-nav-item href="#" >
                <a href="#" @click="doSignOut" class="link-decor" >Sign Out</a>
              </b-nav-item> 
              <b-nav-item href="#" >
                <b-icon icon="person-fill"></b-icon>
                <a href="#" class="link-decor" >Welcome, &nbsp;{{currentUser.first_name}}</a>
              </b-nav-item> 
              <!-- <b-navbar-item href="#">       -->
                
                <!-- {{currentUser.first_name}} {{currentUser.last_name}}  
              </b-navbar-item>
                   -->
        </template>
        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
  </header>
</template>

<script>
import {actionTypes} from '@/store/modules/auth'
import {getterTypes} from '@/store/modules/auth'
import {mapGetters} from 'vuex'


export default {
    name:'AppMenu',
    computed:{
      ...mapGetters({
        currentUser:getterTypes.currentUser,
        isLoggedIn:getterTypes.isLoggedIn,
        isAnonymous:getterTypes.isAnonymous})
      // currentUser(){
      //   return this.$store.getters[getterTypes.currentUser]
      // },
     
     
    },
    methods:{
      doSignOut(){
        console.log("Sign out...")
        this.$store.dispatch( actionTypes.signOut)
        location.reload();
      }
    },
    mounted(){
      this.$store.dispatch(actionTypes.getUser)
      console.log("menu mounted, call for getUser from store")
    }
}
</script>
<style>
.bg-info-2{
  background-color: brown;
  color:white;
}

.link-decor{
  color:white;
  text-decoration:none;
}

.link-decor:hover{
  color:black;
}
.active{
  background-color: rgb(214, 193, 193);
}
</style>