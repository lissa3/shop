import fetchAPI from '@/api/categs'

export const mutationTypes = {  
  SET_CATEGS_LOADING:'[categs] GET_CATEGS_LOADING',
  GET_CATEGS_SUCCESS:'[categs] GET_CATEGS_SUCCESS',
  SET_CATEGS_FAILURE:'[categs] GET_CATEGS_FAILURE'

}
export const actionTypes = {
  getCategories:'[categs] get categs',  
}

const state ={  
  isLoading:false,
  errors:null,
  data:null 

}

const mutations = {
  [mutationTypes.SET_CATEGS_LOADING](state){
    state.isLoading = true    
  },  
  [mutationTypes.GET_CATEGS_SUCCESS](state,payload){
    state.data = payload
    state.isLoading = false
  },
  [mutationTypes.SET_CATEGS_FAILURE](state,errors){
    state.errors = errors
  },  
  
  
}
const actions = {
    async [actionTypes.getCategories]({commit}){
        console.log("store dispatching categories ")
        commit(mutationTypes.SET_CATEGS_LOADING); 
        try{
        const resp = await fetchAPI.getCategTree()        
          // console.log("response is",resp) 
          commit(mutationTypes.GET_CATEGS_SUCCESS,resp.data);          
          return resp
        }catch(err){
            console.log("Can't fetch categories")
            commit(mutationTypes.SET_CATEGS_FAILURE)
        }            
  },
  
  
  
} 

export default {
  state,   
  mutations,
  actions
  
}