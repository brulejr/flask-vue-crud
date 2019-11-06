<template>
  <v-app>
    <app-toolbar :title="$t('appl.title')"></app-toolbar>
    <app-nav-menu :views="views"></app-nav-menu>
    <v-content>
      <transition name="fade">
        <router-view/>
      </transition>
    </v-content>
    <confirm ref="confirm"></confirm>
  </v-app>
</template>

<script>
import _ from 'lodash'
import idleTimeout from 'idle-timeout'
import { AppNavMenu, AppToolbar } from '@/modules/layout'
import { AuthService } from '@/modules/auth'
import { Confirm } from '@/modules/notify'
import { mapGetters } from 'vuex'
function _logout () {
  AuthService.logout().then(() => {
    location.reload()
  })
}
function _logoutWithConfirm (self) {
  self.$refs.confirm.open({
    title: self.$t('dialogs.sessionExpired.title'),
    message: self.$t('dialogs.sessionExpired.details'),
    affirmativeText: self.$t('text.ok')
  }).then((confirm) => {
    if (confirm) _logout()
  })
}
export default {
  name: 'MainPage',
  created () {
    this.$bus.on(this.$events.LOGOUT, (event) => {
      if (_.get(event, 'payload.force')) {
        _logoutWithConfirm(this)
      } else {
        this.$refs.confirm.open({
          title: this.$t('dialogs.logoutConfirmation.title'),
          message: this.$t('dialogs.logoutConfirmation.details'),
          affirmativeText: this.$t('text.yes'),
          negativeText: this.$t('text.no')
        }).then((confirm) => {
          if (confirm) _logout()
        })
      }
    })
    this.idleTimeout = idleTimeout(() => {
      _logoutWithConfirm(this)
    }, {
      timeout: 1000 * 60 * 15
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
  mounted () {
    this.$root.$confirm = this.$refs.confirm.open
  },
  components: {
    AppNavMenu,
    AppToolbar,
    Confirm
  }
}
</script>
