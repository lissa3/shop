<template>
  <div class="container">
    <div>
      <p>Here comes a form</p>
    <b-form @submit.prevent="onSubmit" v-if="show">
      <b-form-group id="input-group-2"  label-for="input-2" class="mb-2">
        <b-form-input
          id="input-2"
          v-model="firstName"
          placeholder="Enter first name"          
        ></b-form-input>
      </b-form-group> 
      <!-- server side: first name errors -->
      <div class="warn mb-1" v-if="servResp.firstNameErr">  
        <ul>      
          <li v-for="firstNameErr in servResp.firstNameErr" :key="firstNameErr.id">
            {{firstNameErr}}
          </li> 
        </ul>         
      </div>
      <b-form-group id="input-group-3"  label-for="input-2" class="mb-2">
        <b-form-input
          id="input-3"
          v-model="lastName"
          placeholder="Enter last name"          
        ></b-form-input>
      </b-form-group> 
      <!-- server errors: last name errors -->
      <div class="warn mb-1" v-if="servResp.lastNameErr">
        <ul>
          <li v-for="lastNameErr in servResp.lastNameErr" :key="lastNameErr.id">
            {{lastNameErr}}
          </li>
        </ul>
      </div>
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
      <div class="warn mb-1" v-if="servResp.emailErr">
        <ul>
          <li v-for="emailErr in servResp.emailErr" :key="emailErr.id">
            {{emailErr}}
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
      <div class="warn mb-1" v-if="servResp.pswErr">
        <ul>
          <li v-for="pswErr in servResp.pswErr" :key="pswErr.id">
            {{pswErr}}
          </li>
        </ul>
      </div>   
      <b-form-group id="input-group-4" label-for="input-4" class="mb-1">
        <b-form-input
          id="input-4"
          type="password"
          v-model="psw2"
          placeholder="Confirm password"         
        ></b-form-input>
      </b-form-group>
      <!-- server errors: non-field errors -->
      <div class="warn mb-1" v-if="servResp.nonFieldErr">
        <ul>
          <li v-for="err in servResp.nonFieldErr" :key="err.id">
            {{err}}
          </li>
        </ul>
      </div>
      <!-- django server is down -->
      <div class="warn mb-3" v-if="servResp.netWorkErr">
        <div class="px-1">{{servResp.netWorkErr}}</div>
      </div>
      <b-row class="text-center">
        <b-col cols="6">
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-col >
        <b-col cols="6">
          <b-button type="reset" variant="danger">Reset</b-button>

        </b-col>
      </b-row>
    </b-form>
    <p class="mt-3">Already have an account?<span class="mute-link"><router-link :to='{name:"login"}'>Sign Up</router-link></span></p>
    
    <!-- <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{form}} <braces class=""></braces></pre>
    </b-card> -->
  </div>
  </div>
</template>

<script>
import {actionTypes} from '@/store/modules/auth'
export default {
  name: "AppSignUp",
  data(){
    return {
      show:true,
      email:"",
      firstName:"",
      lastName:"",
      psw:"",
      psw2:"",
      servResp:{
        status:'',
        firstNameErr:null,
        lastNameErr:null,
        emailErr:null,
        pswErr:null,
        nonFieldErr:null,
        netWorkErr:null
      }      
    }
  },
  methods:{
    onSubmit(){
      console.log("submitting the form");
      this.$store.dispatch(actionTypes.register,{
        email:this.email,
        first_name:this.firstName,
        last_name:this.lastName,
        password:this.psw,
        re_password:this.psw2
      })
      .then((resp)=>{
       console.log("resp comp SignUp",resp); // greet from module.auth.register
       console.log("resp status comp SignUp",resp.status); // greet from module.auth.register
       //from store: resp (email,status),
         if(resp.status===200||resp.status===201){          
           this.submitStatus = "PENDING";
           this.$router.push({name:"confirmEmail"})
        }           
      })
      .catch((err)=>{
        // error response undefined should be above the rest         
        // because django server down and not responding 
        console.log(err)
        console.log(Object.keys(err))
        if(err.response===undefined&&err.toJSON().message==='Network Error'){
            this.servResp.netWorkErr = 'Sorry. Our server is enduring some problems.Please try to create account later'
            
        }else if(err.response.status ===400){
          this.servResp.status = 400
          this.servResp.firstNameErr = err.response.data.first_name;
          this.servResp.lastNameErr = err.response.data.last_name;
          this.servResp.emailErr = err.response.data.email;
          this.servResp.pswErr = err.response.data.password;
          this.servResp.nonFieldErr = err.response.data.non_field_errors;
         }else if (err.response.status ===404){
           
           console.log("Page not found")
         }else if (err.response.status ===401){
           // url is not correct
           console.log("Not auth-ed")
         }else if (err.response.status ===500){
           // ex: url without / at the end
           console.log("server resp 500")
         }
         else{
           console.log("Server can't be reach; check your internet connection, please")
         }
          // TODO: create mutation to catch err msg
         
         
        
      })
    },    
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

</style>