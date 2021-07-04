<template>
    <div class="container-fluid">
      <h3 class="mb-4 text-center">This is a prod search page</h3>
        <div class="row py-3">
          <div class="col col-md-2 py-3">
            <section class="categs-space">
              <app-categs></app-categs>
            </section>
          </div>
          <div class="col col-md-8 py-3">
            <app-products :api-url="apiUrl"></app-products>
          </div>
          
        </div>      
    </div>
</template>
<script>
import AppProducts from '@/components/Products'
import AppCategs from '@/components/categs/Categs'
export default {
    name:'AppIdeaGeneral',
    components:{
        AppProducts,
        AppCategs,        
    },
    computed:{
        searchTerm() {
          return this.$route.params.term
    },
        apiUrl(){
          return `/api/v1/products/product/?search=${this.searchTerm}`
    }
  }    
}
</script>
<style scoped>
.row > div{
  border:1px solid black;
}
</style>