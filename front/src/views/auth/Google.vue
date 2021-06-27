<template>
    <div class="container">       
        <div class="row">            
            <div class="col col-md-10" >
                <div class='container'>
                    <div class="wrapper">
                        <h1>Verify your Account:</h1>
                        <button @click="goGoogle" class="btn btn-success">                
                            Create account via Google
                        </button>
                        </div>
                        
                    </div> 
            </div>
        </div>
    </div>
</template>
                        
<script>

export default {
    name:"AppGoogle",
    data(){
        return{
            successMsg:"",
            errorMsg:""
        }
    },
    methods:{
        goGoogle(){
           console.log("auth via google statrted")
           this.$store.dispatch('registerGoogle')
           .then((resp)=>{               
            let redirectUrl = resp.data.authorization_url
            window.location.replace(redirectUrl)
           }) 
           .catch((err)=>{
               console.log('error during google auth-n',err)

           })       
        }       
    },    
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
            

           
            
           