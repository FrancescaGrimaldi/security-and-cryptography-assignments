<template>
  <Login />
  <Registration />
</template>

<script>
import Login from './Login.vue';
import Registration from './Registration.vue';

export default {
    name: 'Home-page',
    components: { Login, Registration }
}
</script>


<style scoped>
  @import '../assets/main.css';
  
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
