<template>
    <div class="container-fluid">
      <h3 class="mb-4 text-center">This is a main idea place</h3>
        <div class="row py-3">
          <div class="col col-md-2 py-3">
            <section class="categs-space">
              <p>categories</p>
              <app-categs></app-categs>
            </section>
          </div>
          <div class="col col-md-10 py-3">
            <app-product :api-url="apiUrl"></app-product>
          </div>
          
        </div>      
    </div>
</template>
<script>
import AppProduct from '@/components/Product'
import AppCategs from '@/components/categs/Categs'

export default {
    name:'home',
    components:{
        AppProduct,        
        AppCategs,        
    },
    data(){
      return {
        apiUrl:'/api/v1/product-collection/products/'
        // apiUrl:'/api/v1/ideas-collection/ideas/'
      }
    },    
}
</script>
<style scoped>
.row > div{
  border:1px solid black;
}
</style>
