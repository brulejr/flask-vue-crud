<template>
  <HelloWorld />
</template>

<script>
import HelloWorld from '../components/HelloWorld'

export default {
  components: {
    HelloWorld
  }
}
</script>
is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  }
}
</script>
