import prodAPI from '@/api/products'

const state = {
    data:null,
    isLoading:false,
    error:null,    
    // pagination          
    count:0,
    prev:'',
    next:'',
    
}

export const mutationTypes = {
    SET_PRODS_LOADING:'[prods] Load prods start',
    GET_PRODS_SUCCESS:'[prods] Get prods success',
    GET_PRODS_FAILURE:'[prods] Get prods failure',
    
    SET_COUNT:'[prods] Set prods count',
    SET_PREV:'[prods] Set prods prev',
    SET_NEXT:'[prods] Set prods next',    
       

}

export const actionTypes = {
    getProds:'[prods] Get products',
    // searchIt:'[prods] Make search in prods'
}

const actions = {
    async [actionTypes.getProds]({commit},{apiUrl}){
        // console.log("store dispatching getprods")
        //console.log("api url in store is",apiUrl)
        commit(mutationTypes.SET_PRODS_LOADING);
        try{
            // instead of apiUrl(str)=> {object, к можно деструктурировать}
           const resp = await prodAPI.getProds(apiUrl)            
            // console.log("response getprods is",resp.data)
            commit(mutationTypes.GET_PRODS_SUCCESS,resp.data.results)
            commit(mutationTypes.SET_NEXT,resp.data.next)
            commit(mutationTypes.SET_PREV,resp.data.previous)
            commit(mutationTypes.SET_COUNT,resp.data.count)             
            return resp            

        } catch(err){
            console.log("error by getIdea request",err)
            commit(mutationTypes.GET_PRODS_FAILURE)
        }          
    },

}
const mutations = {
    [mutationTypes.SET_PRODS_LOADING](state){
        state.isLoading = true
        // let op: all prev data will be out|=> met een schone lei beginnen
        state.data = null
      },
    [mutationTypes.GET_PRODS_SUCCESS](state,payload){
        state.isLoading = false
        state.data = payload
    }, 
    [mutationTypes.GET_PRODS_FAILURE](state,error){
        // at this point I don't know what errors I'll get
        state.isLoading = false
        state.error=error
    },
    [mutationTypes.SET_COUNT](state,count){        
        state.count = count
    },     
    [mutationTypes.SET_PREV](state,prev){        
        state.prev = prev
    },     
    [mutationTypes.SET_NEXT](state,next){        
        state.next = next
    },      
    // [mutationTypes.GET_TERM_LOOKUP](state,term){        
    //     state.lookUp = term
    // },      
    
}


export default {
    state,
    mutations,
    actions
    
  }

  // GET_TERM_LOOKUP:'[prods] Get lookUp search',
    // SEARCH_PRODS_LOADING:'[prods] Search prods start',
    // SEARCH_PRODS_SUCCESS:'[prods] Search prods success',
    // SEARCH_PRODS_FAILURE:'[prods] search prods failure',