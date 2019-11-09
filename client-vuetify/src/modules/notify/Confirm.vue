<template>
  <v-dialog v-model="dialog" :max-width="options.width" :style="{ zIndex: options.zIndex }" @keydown.esc="cancel">
    <v-card>
      <v-toolbar dark :color="options.color" dense flat>
        <v-toolbar-title class="white--text">{{options.title}}</v-toolbar-title>
      </v-toolbar>
      <v-card-text v-show="!!options.message" class="pa-4">{{options.message}}</v-card-text>
      <v-card-actions class="pt-0">
        <v-spacer></v-spacer>
        <v-btn v-if="!!options.affirmativeText" color="primary darken-1" text @click.native="agree">{{options.affirmativeText}}</v-btn>
        <v-btn v-if="!!options.negativeText" color="grey" text @click.native="cancel">{{options.negativeText}}</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import _ from 'lodash'

const DEFAULT_OPTIONS = {
  affirmativeText: null,
  color: 'primary',
  message: null,
  negativeText: null,
  title: null,
  width: 290,
  zIndex: 200
}
export default {
  data: () => ({
    dialog: false,
    resolve: null,
    reject: null,
    options: {}
  }),
  methods: {
    open (options) {
      this.dialog = true
      this.options = _.merge(_.clone(DEFAULT_OPTIONS), options)
      return new Promise((resolve, reject) => {
        this.resolve = resolve
        this.reject = reject
      })
    },
    agree () {
      this.resolve(true)
      this.dialog = false
    },
    cancel () {
      this.resolve(false)
      this.dialog = false
    }
  }
}
</script>
