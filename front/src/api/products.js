import axios from '@/api/axios'
  
const getProds = (apiUrl)=>{    
    return axios.get(apiUrl)
}
export default {    
    getProds    

}    