<template>
    <div class="container">
      <div class="flash-msg"></div>
         <div class="row">            
            <div class="col col-md-10" >
              <b-form @submit.prevent="onSubmit">     
     
                <b-form-group
                  id="input-group-1"
                  class="mb-1"
                  label-for="input-1"
                  description="We'll never share your email with anyone else."
                >
                  <b-form-input
                    id="input-1"
                    v-model="email"
                    type="email"
                    placeholder="Enter email"          
                  ></b-form-input>
                </b-form-group>
                <!-- server errors: email errors -->
                <div class="warn mb-1" v-if="emailErr">
                  <ul>
                    <li v-for="err in emailErr" :key="err.id">
                      {{err}}
                    </li>
                  </ul>
                </div>
                <b-form-group id="input-group-5"  label-for="input-3" class="mb-2">
                  <b-form-input
                    id="input-5"
                    type="password"
                    v-model="psw"
                    placeholder="Enter password"          
                  ></b-form-input>
                </b-form-group>   
                <!-- server errors: password errors -->
                <div class="warn mb-1" v-if="pswErr">
                  <ul>
                    <li v-for="err in pswErr" :key="err.id">
                      {{err}}
                    </li>
                  </ul>
                </div>   
                <!-- server errors: non-field errors -->
                <div class="warn mb-1" v-if="nonFieldErr">
                  <ul>
                    <li v-for="err in nonFieldErr" :key="err.id">
                      {{err}}
                    </li>
                  </ul>
                </div>
                <!-- django server is down -->
                <div class="warn mb-3" v-if="netWorkErr">
                  <div class="px-1">Sorry. Our server has temporary problems.Please try to login later</div>
                </div>
                <div class="warn mb-3" v-if="unAuthorized">
                  <div>{{unAuthorized}}</div>
                </div>
                <div class="warn mb-3" v-if="finalErr">
                  <div>Something went wrong during login session.</div>
                </div>
                <div class="flesh-msg mb-3" v-if="successMsg">
                  <div>{{successMsg}}</div>
                </div>
                <b-row class="text-center">
                  <b-col cols="6">
                    <b-button type="submit" variant="primary">Submit</b-button>
                  </b-col >       
                </b-row>
            </b-form> 
        <p class="mt-3">Not registed?<span class="mute-link"><router-link :to='{name:"signup"}'>Sign Up</router-link></span>
        </p>
        <p class="mt-3">Forgot yout password?<span class="mute-link"><a href="#">Here</a></span></p>               
      </div>
    </div>
  </div>         
</template>
                        
<script>
import {actionTypes} from '@/store/modules/auth'
export default {
    name:"AppLogin",
    data(){
      return {
        user:{},
        email:'',
        psw:'',        
        status:'',        
        emailErr:null,
        pswErr:null,
        nonFieldErr:null,
        netWorkErr:null,
        unAuthorized:null,
        finalErr:false,
        successMsg:''
      } 
    },   
    methods:{
       onSubmit(){
         let data={email:this.email,password:this.psw}
         // first request to get tokens
         this.$store.dispatch(actionTypes.login,data)
         .then((resp)=>{  
           console.log("got resp from store:",resp)
           if(resp.status ===200){
             console.log("Login comp and status 200")
           this.$store.dispatch(actionTypes.getUser)
           .then((resp)=>{ 
              console.log("do smth with this resp",resp)
              if(resp){
                console.log("status",resp.status)
                this.successMsg = "Success in login"
                setTimeout(()=>{
                 this.$router.push({name:"home"})
               },2000)
              }             
                                      
             }).catch((err)=>{
               console.log(err)
             })            
           }else if(resp.response.status === 401){
             // No active account found with the given credentials
             console.log(Object.keys(resp.response.data))
             this.unAuthorized = resp.response.data.detail            
           }else if(resp.response.status === 400){
             // This field (email/psw) may not be blank (user sent empty form)
             this.emailErr=resp.response.data.email
             this.pswErr=resp.response.data.password             
           } else{
             this.netWorkErr = 'Network Error; no response from the server'
           }        
         }) 
         .catch((err)=>{   
           // user banned?        
             console.log("catch in login component")
             console.dir(err) 
             alert("A server/network error occured.Sorry about this - we will get it fixed shortly. ");
                          
           })          
       }
  } 
}    
</script>

<style>
.warn {
  background-color: rgb(240, 194, 194);
  border-radius: 3px;
}
.warn ul li{
  list-style-type:none;
}
.flesh-msg{
  background-color: darkgoldenrod;
}

</style>
                    
                              
        