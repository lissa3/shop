import axios from 'axios'
let baseUrl = 'http://127.0.0.1:8000'

// axios for requests without accessToken
axios.defaults.baseURL=baseUrl

axios.interceptors.request.use(config=>{
    const token = localStorage.getItem('accessToken')
    const authorizationToken = token? `JWT ${token}`: null
    console.log(authorizationToken)
    config.headers.Authorization = authorizationToken
    return config
})


export default axios