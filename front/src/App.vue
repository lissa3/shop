<template>
  <div id="app">
    <div class="container-fluid">
    <app-menu></app-menu>  
    <div class="container">
      <router-view />
    </div>
   </div>
  </div>
  
  
</template>
<script>
import AppMenu from '@/components/Menu'


export default { 
  name:'App',
  components:{
    AppMenu
  },
  
}
</script>

<style>
#app{
  background-color: cornsilk;
  height: 100vh;
}
</style>