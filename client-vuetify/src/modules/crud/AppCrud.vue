<template>
  <v-data-table :headers="headers"
                :items="items"
                hide-default-footer>
    <template v-slot:item="data">
      <tr>
        <td v-for='header in headers' :key='header.value'>
          <component v-if="header.component" :is="header.component" v-bind="data.item"></component>
          <span v-else v-html="render(header, data.item)"></span>
          <span v-if="header.value === 'action'">
            <v-icon small
                    class="mr-2"
                    @click="editItem(data.item)">edit</v-icon>
            <v-icon small
                    @click="deleteItem(data.item)">delete</v-icon>
          </span>
        </td>
      </tr>
    </template>
    <template v-slot:no-data>{{noDataMessage}}</template>
  </v-data-table>
</template>

<script>
import _ from 'lodash'

const ACTION = { value: 'action', sortable: false }

export default {
  name: 'AppCrud',
  props: [
    'columns',
    'items',
    'noDataMessage',
    'readonly'
  ],
  computed: {
    headers () {
      return (this.readonly) ? this.columns : _.concat(_.clone(this.columns), ACTION)
    }
  },
  methods: {
    editItem (item) {
      console.log('editItem', item)
    },
    deleteItem (item) {
      this.$emit('delete-item', item)
    },
    render (header, item) {
      return header.render ? header.render(item[header.value], header.value, item) : item[header.value]
    }
  }
}
</script>
