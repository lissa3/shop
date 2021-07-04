<template>
  <div class="container-fluid">     
        <div class="row">
          <h3>I am a categ prods component</h3>
          <div class="col col-md-2">
            <section class="categs-space">
                <app-categs></app-categs>               
            </section>
          </div>
          <div class="col col-md-8">
            <app-products :api-url="apiUrl"></app-products>
          </div>
          
        </div>    
    </div>
</template>
<script>
import AppProducts from '@/components/Products'
import AppCategs from '@/components/categs/Categs'
export default {
  name:'AppCategIdeas',
  components:{
      AppProducts,
      AppCategs,
      
  },
  computed: {
    categSlug() {
      return this.$route.params.slug
    },
    apiUrl() {
      return `/api/v1/categories/${this.categSlug}/`
    }
  },
  
}
</script>