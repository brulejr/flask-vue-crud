<template>
  <div>
    <component :is="'div'" v-show="!showForm">
      <v-card>
        <v-card-title>
          <span>TBD GRID</span>
        </v-card-title>
        <v-card-text>
          <v-data-table :headers="headers"
                        :items="items"
                        hide-default-footer>
            <template v-slot:item="data">
              <tr @click="formOpen(data.item)">
                <td v-for='header in headers' :key='header.value'>
                  <component v-if="header.component" :is="header.component" v-bind="data.item"></component>
                  <span v-else v-html="render(header, data.item)"></span>
                  <span v-if="header.value === 'action'">
                    <v-icon small
                            @click.stop="deleteItem(data.item)">delete</v-icon>
                  </span>
                </td>
              </tr>
            </template>
            <template v-slot:no-data>{{noDataMessage}}</template>
          </v-data-table>
        </v-card-text>
      </v-card>
    </component>
    <component :is="'div'" v-if="showForm">
      <v-card>
        <v-card-title>
          <span>TBD EDIT</span>
          <v-spacer/>
          <v-btn icon @click.prevent="formClose">
            <v-icon>close</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <v-form v-bind="selectedItem">
            <v-container fluid>
              <v-layout row wrap>
                <template v-for="(item, i) in form">
                  <v-flex :key="i" v-if="!_isHidden(item.hidden)" v-bind="item['field-wrapper']">
                    <v-autocomplete v-if="item.type == 'v-autocomplete'"
                                    v-model="item.value"
                                    v-bind="item['field-input']"
                                    :items="_getSelectItems(item)"
                                    :disabled="_isReadOnly(item.readonly)"/>
                    <v-select v-else-if="item.type == 'v-select'"
                              v-model="item.value"
                              v-bind="item['field-input']"
                              :items="_getSelectItems(item)"
                              :disabled="_isReadOnly(item.readonly)"/>
                    <component v-else
                               :is="item.type"
                               v-model="item.value"
                               v-bind="item['field-input']"
                               :disabled="_isReadOnly(item.readonly)"/>
                  </v-flex>
                </template>
              </v-layout>
            </v-container>
          </v-form>
        </v-card-text>
      </v-card>
    </component>
  </div>
</template>

<script>
import _ from 'lodash'

const ACTION = { value: 'action', sortable: false }

export default {
  name: 'AppCrud',
  props: [
    'columns',
    'fnGetId',
    'form',
    'items',
    'noDataMessage',
    'readonly'
  ],
  computed: {
    headers () {
      return (this.readonly) ? this.columns : _.concat(_.clone(this.columns), ACTION)
    }
  },
  data () {
    return {
      selectedItem: null,
      showForm: false
    }
  },
  methods: {
    deleteItem (item) {
      this.$root.$confirm({
        title: this.$t('dialogs.deleteConfirmation.title'),
        message: this.$t('dialogs.deleteConfirmation.details'),
        affirmativeText: this.$t('text.yes'),
        negativeText: this.$t('text.no'),
        color: 'warning'
      }).then((confirm) => {
        if (confirm) {
          this.$emit('on-delete-item', item)
        }
      })
    },
    async formOpen (item) {
      this.getRecord(item)
      this.showForm = true
      this.$emit('form-open', this.form)
    },
    formClose () {
      this.showForm = false
      this.$emit('form-close')
    },
    getId (item) {
      return this.fnGetId ? this.fnGetId(item) : 'id'
    },
    getRecord (item) {
      for (let key in this.form) {
        this.form[key].value = this.form[key].render ? this.form[key].render(item[key]) : item[key]
      }
    },
    render (header, item) {
      return header.render ? header.render(item[header.value], header.value, item) : item[header.value]
    },
    _getSelectItems (item) {
      return item.getSelectItems(item)
    },
    _isHidden (hidden) {
      return (hidden === 'add' && !this.selectedId) || (hidden === 'edit' && !!this.selectedId) || hidden === 'all'
    },
    _isReadOnly (readonly) {
      return (readonly === 'add' && !this.selectedId) || (readonly === 'edit' && !!this.selectedId) || readonly === 'all'
    }
  }
}
</script>
