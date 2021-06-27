<template>
    <div class="container">       
        <div class="row">            
            <div class="col col-md-10" >
                <div class='container'>
                    <div class="wrapper">
                        <h1>Verify your Account via Google:</h1>
                        <button @click="goToGoogle" class="btn btn-success">                
                            Create account via Google
                        </button>
                        </div>
                        
                    </div> 
            </div>
        </div>
    </div>
</template>
                        
<script>
// import axios from '@/api/axios'
import axios from 'axios'
import {actionTypes} from '@/store/modules/auth'
export default {
    name:"AppGoogleForm",
    data(){
        return{
            state:null,
            code:null,
            successMsg:"",
            errorMsg:""
        }
    },
    methods:{
        async goToGoogle(state,code){
           console.log("making config and collecting data before POST") 
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
            console.log("details are",details)
            const formBody = Object.keys(details).map(key=> encodeURIComponent(key)+'='+encodeURIComponent(details[key])).join('&')
            console.log("form body is",formBody)
            try{                
                const resp = await axios.post(`http://localhost:8000/auth/o/google-oauth2/?${formBody}`,config);
                console.log("resp is",resp)
                if(resp.data.access){
                    console.log("google gives me an access token");
                    this.$store.dispatch(actionTypes.getUser,resp.data.access)
                }
                this.$router.push({name:'home'})
            }catch(err){
                console.log("signing up with google is failed")
                console.log(Object.keys(err))
                console.dir(err)
                console.log('data',err.response.data)
            }
        }            
      }       
    },
    created(){
        let urlParams = new URLSearchParams(window.location.search);
        this.state = urlParams.get('state'); 
        this.code = urlParams.get('code')
        this.goToGoogle(this.state,this.code)
    }
}
</script>
<style>

.successMsg{
    background-color: rgb(192, 219, 164);
    height: 50px;
}
.errorMsg{
    background-color: rgb(236, 187, 195);
    height: 50px;
    
}
</style>