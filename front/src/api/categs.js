import axios from '@/api/axios'
  
const getCategTree = ()=>{    
    return axios.get(`/api/v1/categories/`)
}
export default {    
    getCategTree
    

}    