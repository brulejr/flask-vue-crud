import 'material-design-icons-iconfont/dist/material-design-icons.css'
import Vue from 'vue'
import Vuetify, {
  VTextField, VSelect, VAutocomplete, VCombobox, VTextarea
} from 'vuetify/lib'
import { Scroll } from 'vuetify/lib/directives'

Vue.use(Vuetify, {
  components: {
    VTextField, VSelect, VAutocomplete, VCombobox, VTextarea
  },
  directives: {
    Scroll
  }
})

export default new Vuetify({
  icons: {
    iconfont: 'md'
  }
})
