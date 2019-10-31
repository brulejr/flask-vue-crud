<template>
  <v-btn icon @click.prevent="logout">
    <v-icon>exit_to_app</v-icon>
  </v-btn>
</template>

<script>
export default {
  methods: {
    logout () {
      this.$bus.emit(this.$events.LOGOUT)
    }
  }
}
</script>

<style scoped>
</style>
