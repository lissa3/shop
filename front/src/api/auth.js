import axios from '@/api/axios'

const register = (creds)=>{
    return axios.post('/auth/users/',creds)
}
const activate = (creds)=>{
    return axios.post('/auth/users/activation/',creds)
}
const login = (creds)=>{
    return axios.post('/auth/jwt/create/',creds)
}

// getAPI = with Authorization JWT header
const getUser = ()=>{
    return axios.get('/auth/users/me/')
}
// const getUser = ()=>{
//     console.log("token is")
//     const headers ={
//             'Content-Type':'application/json',
//             Authorization: localStorage.getItem('accessToken')
// 			? 'JWT ' + localStorage.getItem('accessToken')
// 			: null,
//         }
//     axios.defaults.headers = headers    
//     return axios.get('/auth/users/me/')
// }

const registerGoogle = ()=>{
    console.log("api auth prepares url to send ")
    let url = 'http://localhost:8080'
    axios.get(`/auth/o/google-oauth2/?redirect_uri=${url}/google`)
}
const googleAuth = async (state,code)=>{
    if(state&&code&& !localStorage.getItem('accessToken')){
        const config = {
            headers:{
                'Content-Type':'application/x-www-form-urlencoded'
            }
        }
        const details = {
            'state':state,
            'code':code
        }
        const formBody = Object.keys(details).map(key=> encodeURIComponent(key)+'='+encodeURIComponent(details[key])).join('&')
        try{
            
            const resp = await axios.post(`/auth/o/google-oauth2/${formBody}`,config);
            console.log("resp is",resp)
            if(resp.data.access){
                console.log("google gives me an access token")
            }
        }catch(err){
            console.log("signing up with google is failed")
        }
    }
}


export default {
    register,
    activate,
    login,
    getUser,
    registerGoogle,
    googleAuth

}    
