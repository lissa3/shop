<template>
  <div>
    <div>
      <div v-for="node in treeData" :key="node.id">
        <div v-if="node.children && node.children.length" class="left-shift">
          <app-node-tree
            :name="node.name"
            :children="node.children"
            :depth="0"
            :slug="node.slug"            
          ></app-node-tree>
          <!-- :depth otherwise a string will be passed to a child component -->
        </div>
        <div class="left-shift" v-else>          
           <router-link :to="{name:'categ',params:{slug:node.slug}}" class="categ">
                <b-badge variant="secondary" class="categ px-2 mx-1">{{node.name}}</b-badge>          
            </router-link> 
        </div>
        
      </div>
    </div>
  </div>
</template>
<script>
import AppNodeTree from "@/components/categs/NodeTree.vue";

export default {
    name:'AppCategTree',
    components: { AppNodeTree },
    props: ["treeData"],     
    
  
};
</script>

<style scoped>
.left-shift {
  text-align: left;
  padding: 0.2rem 0 0.5rem 0.5rem;
  margin-left: 0.5rem;
  cursor: pointer;
}
/* .zoo{
  transform: translate(25px);
  eq: translate(25px, 0) = only in horizontal direction
} */
</style>>