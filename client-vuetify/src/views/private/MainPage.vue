<template>
  <v-app>
    <app-toolbar :title="$t('appl.title')"></app-toolbar>
    <app-nav-menu :views="views"></app-nav-menu>
    <v-content>
      <transition name="fade">
        <router-view/>
      </transition>
    </v-content>
  </v-app>
</template>

<script>
import _ from 'lodash'
import { AppNavMenu, AppToolbar } from '@/modules/layout'
import { AuthService } from '@/modules/auth'
import { mapGetters } from 'vuex'
function _logout () {
  AuthService.logout().then(() => {
    location.reload()
  })
}
export default {
  name: 'MainPage',
  created () {
    this.$bus.on(this.$events.LOGOUT, (event) => {
      if (_.get(event, 'payload.force')) {
        if (confirm('Do you want to logout')) {
          _logout()
        }
      } else {
        _logout()
      }
    })
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'loading'])
  },
  data () {
    return {
      views: [
        { icon: 'home', text: this.$t('pages.HomePage.title'), route: 'home' },
        { icon: 'book', text: this.$t('pages.BooksPage.title'), route: 'books' }
      ]
    }
  },
  components: {
    AppNavMenu,
    AppToolbar
  }
}
</script>
