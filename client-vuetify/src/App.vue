<template>
  <div id="app">
    <transition name="fade">
      <router-view/>
    </transition>
  </div>
</template>

<script>
function _getWindowHeight () {
  return window.outerHeight
}
function _getWindowWidth () {
  return window.outerWidth
}
export default {
  data () {
    return {
      height: _getWindowHeight(),
      width: _getWindowWidth()
    }
  },
  created () {
    window.addEventListener('resize', this.handleResize, { passive: true })
  },
  destroyed () {
    window.removeEventListener('resize', this.handleResize, { passive: true })
  },
  methods: {
    handleResize: function () {
      if (_getWindowHeight() !== this.height || _getWindowWidth() !== this.width) {
        this.height = _getWindowHeight()
        this.width = _getWindowWidth()
        this.$bus.emit(this.$events.RESIZE, {
          height: this.height,
          width: this.width,
          mobile: this.width <= this.$vuetify.breakpoint.thresholds.xs
        })
      }
    }
  }
}
</script>

<style lang="scss">
</style>
