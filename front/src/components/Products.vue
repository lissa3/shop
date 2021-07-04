<template>
    <div class="container">        
        <div v-if="isLoading"><app-loader></app-loader></div>
        <div  v-if="prods" class="wrapper">    
            <div class="row main-row" v-for="prod in prods" :key="prod.id">
                <div   class="col-lg-4 col-md-12 col-sm-12">
                    <div class="prod-img mb-2">
                        <img src="@/assets/logo.png" alt="img" class="img-fluid">
                    </div>
                    <div class="row">
                        <div class="col-sm-12 mb-2">
                            <ul class="list-group list-group-horizontal ul-cls">
                                <li class="list-group-item">
                                    <b-icon icon="bookmark-heart-fill"></b-icon>
                                    
                                </li>
                                <!-- <li class="list-group-item tooltip"> -->
                                <li class="list-group-item">
                                    <b-icon icon="person-fill"></b-icon>
                                    <!-- <span class="tooltiptext">See author profile</span> -->
                                </li>
                                <li class="list-group-item">
                                    <b-icon icon="envelope"></b-icon>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-lg-8 col-md-12 col-sm-12">
                <div class="prod-title mb-1 mt-1">
                        <h3>{{prod.name}}</h3>
                </div> 
                <div class="idea-title mb-2">
                    <p>price <strong>$ {{prod.price}}</strong></p>    
                </div> 
                <div class="idea-title mb-2">
                        <p>Rating: {{prod.avg_rate}}</p>
                        
                </div> 
                <div class="mb-2">
                    <div class="row">
                        <div class="col-lg-9 col-md-9 col-sm-9">
                           <div class="idea-date mb-2">
                            <span>sold: {{prod.sold}}</span>
                            </div>
                        </div>
                        <div class="col-lg-1 col-md-1 col-sm-1">
                                <b-icon icon="heart-fill"></b-icon>
                        </div>
                        <div class="col-lg-1 col-md-1 col-sm-1">
                                <p>Likes: {{prod.an_likes}}</p>
                        </div>
                    </div>
                </div>                
                <div class="prod-main-text mb-2">
                    <p>{{prod.description}}</p>
                </div>
                <div class="prod-read-more mb-2">
                    <button class="btn btn-outline-dark">Read More</button>
                </div>
                <div class="prod-read-more mb-2">
                    <div >...</div>
                    
                </div>
              </div>
            </div>
        </div>
        <div v-else>No products yet</div>
        <!-- <div v-if="error">smth went wrong</div> -->
        <div class="col-lg-8 col-md-12 col-sm-12 pagination">
            <app-pagination  
            :currentPage="currentPage" 
            :total="total"
            :limit="limit"
            :url="baseUrl"
            :next="next"
            :prev="prev"
            :last="last">
            </app-pagination>           
        </div>
    </div>
</template>
<script>

import {stringify, parseUrl} from 'query-string'
import {actionTypes} from '@/store/modules/prods'
import {limit} from '@/helpers/vars'
import {mapState} from 'vuex'
import  AppPagination from '@/components/Pagination'
import AppLoader from '@/components/Loader'
export default {
    name:'AppProduct',
    components:{
         AppPagination,
         AppLoader
    },
    props:{
        apiUrl:{
            type:String,
            required:true
        }
    },    
    created(){
        this.fetchProducts()

    },
    computed:{            
        ...mapState({
             prods:state=>state.prods.data,
             total:state=>state.prods.count,
             isLoading:state=>state.prods.isLoading,
             error:state=>state.prods.error,
             prev:state=>state.prods.prev,
             next:state=>state.prods.next           
        }),
        baseUrl() {
            // vue route: const = /
            return this.$route.path
        },
        currentPage() {
            //console.log("rout query page",this.$route.query.page)
            return Number(this.$route.query.page || '1')
        },
        limit(){
            return limit
        },
        offset() {
            // 1st page = 1*2 -2 = zero
         return this.currentPage * limit - limit
        },
        last(){
            return Math.ceil(this.total/this.limit)
        }
    },    
    watch: {
        currentPage() {           
            // if query.page changes => make request with a new page again
            this.fetchProducts()
        },
        // вопрос: насколько здесь нужен  watch (baseUrl),т.к. watch currentPage
        // уже ослеживает vue.js url = this.$route.query.page c ?page=....
        // отв: to fix moment when you go to left side bar to click on categories
         baseUrl(){
            //no reaction on changing url; logic = const / (Home)
            this.fetchProducts()
        }
    },    
    methods:{
        fetchProducts(){
            const parsedUrl = parseUrl(this.apiUrl)
            // console.log("parsedUrl",parsedUrl)
            // console.log("parsedUrl.url:   ",parsedUrl.url)
            // console.log("parsedUrl.query:  ",parsedUrl.query)

            const stringifiedParams = stringify({
                limit,
                offset: this.offset,
                ...parsedUrl.query
            })
            const apiUrlWithParams = `${parsedUrl.url}?${stringifiedParams}`
            // const apiUrlWithParams = `${parsedUrl.url}` 
            // console.log("url izzz:",apiUrlWithParams)           
             this.$store.dispatch(actionTypes.getProds, {apiUrl: apiUrlWithParams})       
             },           
    },    
    
}
</script>
<style>
.main-row{
    margin:8%;
    background-color: blanchedalmond;
    box-shadow: 0 0 10px 10px rgba(0,0,0,.05);
    border-radius: 0.5rem;
}
.prod-img   >   img{
    width:100%;
    height:100%;
    /* transform: translateY(-30px); */
    object-fit: cover;
    border-radius:0.5rem;
    box-shadow: 0 0 8px 3px rgba(0,0,0,.3);

}

.ul-cls{
    justify-content: center;
}
.ul-cls li{
    cursor: pointer;
}
.prod-title >h3{
    font-weight: 400;
    font-style: normal;
}
.prod-main-text{
    font-style: normal;
    line-height: 2;
}
/* tooltip */
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
  background-color: black;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;
  
  /* Position the tooltip */
  position: absolute;
  z-index: 1;
  top: -5px;
  left: 105%;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
}

</style>