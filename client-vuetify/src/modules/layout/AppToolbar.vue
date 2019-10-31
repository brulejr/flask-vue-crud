<template>
  <v-app-bar app
             dark
             color="primary"
             clipped-left
             fixed>
    <v-app-bar-nav-icon @click.prevent="toggleNavMenu"></v-app-bar-nav-icon>
    <v-toolbar-title v-text="title"></v-toolbar-title>
    <v-spacer></v-spacer>
    <app-logout-button></app-logout-button>
  </v-app-bar>
</template>

<script>
import AppLogoutButton from './AppLogoutButton'
export default {
  name: 'AppToolbar',
  props: [
    'title'
  ],
  components: {
    AppLogoutButton
  },
  methods: {
    toggleNavMenu () {
      this.$store.commit('toggleNavMenuActive')
    }
  }
}
</script>

<style scoped lang="scss">
</style>
