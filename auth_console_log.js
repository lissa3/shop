import authAPI from '@/api/auth'



const state ={
  signUpFailure:false,
  showEmailCheck:'',
  confirmation:false,
  
}


const mutations = {
  registerFailure(state){
    state.signUpFailure = true;
  },
  PASS_EMAIL_POTENTIAL_USER(state,email) {
    console.log("inside mutation PASS EMAIL POT USER with email",email)
    state.showEmailCheck=email;
  },
  SET_CONFIRM(state){
    state.confirmation = true
  }
  
}

const actions = {
    register({commit},creds){   
        // object servResp для передачи данных в компонент   
      let servResp = {
        status:"",
        firstNameErr:[],
        lastNameErr:[],
        emailErr:[],
        pswErr:[],          //ошибки в password-e
        nonFieldErr:[],    // general errors (ex: email already exists...)
      };
      return new Promise((resolve,reject)=>{
        authAPI.register(creds)
        .then((resp)=>{          
          servResp.status = resp.status;
          servResp.email = resp.data.email;          
          commit('PASS_EMAIL_POTENTIAL_USER',resp.data.email);          
          resolve (servResp)
        })
        .catch(err=>{  
           // collect all errors        
          servResp.status = err.response.status
          servResp.firstNameErr = err.response.data.first_name;
          servResp.lastNameErr = err.response.data.last_name;
          servResp.emailErr = err.response.data.email;
          servResp.pswErr = err.response.data.password;
          servResp.nonFieldErr = err.response.data.non_field_errors;         
          reject(servResp)
        }
      )
    })
  },
  activate({commit},creds){
    // endpoint will return only: response status=204, no data
    return new Promise((resolve,reject)=>{
      let status = ""
      authAPI.activate(creds)
      .then((resp)=>{
        console.log("resp in activate store is ",resp);
        console.log("resp status in activate store is 204? ",resp.status);
        commit('SET_CONFIRM');
        console.log("msg from store: email confirmed")
        status = resp.status
        resolve(status)
      })
      .catch((err)=>{
        console.log("err during email confirmation");
        status = err.response.status;
        commit('registerFailure')
        reject(status)
      })

    })
  }

}  





export default {
  state,  
  mutations,
  actions
  
}