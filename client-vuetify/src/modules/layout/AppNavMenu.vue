<template>
  <v-navigation-drawer :mini-variant="isNavMenuCollapsed"
                       mini-variant-width="60"
                       :value="isNavMenuActive"
                       app
                       clipped
                       stateless>
      <v-list dense>
        <v-list-item v-for="(view, i) in views"
                     :key="i"
                     :to="{name: view.route}">
          <v-list-item-action>
            <v-icon v-html="view.icon"></v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="view.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item value="true"
                     default
                     @click.stop="toggleMiniVariant"
                     v-if="isNotMobile()">
          <v-list-item-action>
            <v-icon v-html="pickMiniVariantIcon()"></v-icon>
          </v-list-item-action>
        </v-list-item>
      </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapGetters } from 'vuex'
import { DeviceMixin } from '@/modules/core'
export default {
  mixins: [
    DeviceMixin()
  ],
  created () {
    this.$bus.on(this.$events.RESIZE, (event) => {
      if (event.payload.mobile) {
        this.$store.commit('setNavMenuCollapsed', true)
      }
    })
  },
  computed: {
    ...mapGetters(['isNavMenuActive', 'isNavMenuCollapsed'])
  },
  data () {
    return {
      sideNav: 'home'
    }
  },
  methods: {
    pickMiniVariantIcon: function () {
      return this.isNavMenuCollapsed ? 'chevron_right' : 'chevron_left'
    },
    toggleMiniVariant: function () {
      this.$store.commit('toggleNavMenuCollapsed')
    }
  },
  props: [
    'views'
  ],
  name: 'AppNavMenu'
}
</script>
<style lang="scss">
  .v-navigation-drawer {
    &--mini-variant {
      .v-list__tile--link {
        padding-left: 5px;
        padding-right: 5px;
      }
    }
  }
</style>
