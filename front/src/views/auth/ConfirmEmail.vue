<template>
    <div class="container">
        <div class="row">            
            <div class="col col-md-10" >
                <div class='container'>
                    <div class="wrapper">
                        <h5>Please check your 
                            email <strong>{{showEmailCheck}}</strong> to see the link to confirm
                            this email
                            <!-- extra {{store.state.autj.showEmailCheck}} -->
                        </h5>  
                                          
                    </div>                    
                </div>                
            </div>
        </div>
    </div>           
</template>

<script>
export default {
    name:'confirmEmail',    
    computed:{
        showEmailCheck(){
            return this.$store.state.auth.showEmailCheck;
        }
    }           
   
}
</script>

<style scoped>
</style>