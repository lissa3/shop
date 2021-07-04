<template>
    <div class="container-fluid">
      <h3 class="mb-4 text-center">This is a home page</h3>
        <div class="row py-3">
          <div class="col col-md-2 py-3">
            <section class="categs-space">
              <p>categories</p>
              <app-categs></app-categs>
            </section>
          </div>
          <div class="col col-md-10 py-3">
            <app-products :api-url="apiUrl"></app-products>
          </div>
          
        </div>      
    </div>
</template>
<script>
import AppProducts from '@/components/Products'
import AppCategs from '@/components/categs/Categs'

export default {
    name:'home',
    components:{
        AppProducts,        
        AppCategs,        
    },
    data(){
      return {
        apiUrl:'/api/v1/products/product/'
        
      }
    },    
}
</script>
<style scoped>
.row > div{
  border:1px solid black;
}
</style>
