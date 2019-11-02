<template>
  <v-data-table :headers="headers"
                :items="getBooks"
                hide-default-footer>
    <template slot="item" slot-scope="props">
      <tr>
        <td>{{ getTitle(props.item) }}</td>
        <td>{{ getAuthor(props.item) }}</td>
        <td>{{ getRead(props.item) }}</td>
        <td>
          <v-icon small
                  class="mr-2"
                  @click="editItem(props.item)">edit</v-icon>
          <v-icon small
                  @click="deleteItem(props.item)">delete</v-icon>
        </td>
      </tr>
    </template>
    <template slot="no-data">{{$t('pages.BooksPage.table.noData')}}</template>
  </v-data-table>
</template>

<script>
import _ from 'lodash'
import { mapGetters } from 'vuex'
import { DeviceMixin, PageMixin } from '@/modules/core'
import { BooksService } from '@/modules/books'
export default {
  name: 'BooksPage',
  mixins: [
    DeviceMixin(),
    PageMixin()
  ],
  created: function () {
    BooksService.findAllBooks()
  },
  computed: {
    ...mapGetters(['getBooks']),
    headers () {
      return [
        { text: this.$t('pages.BooksPage.table.headers.title'), value: 'title' },
        { text: this.$t('pages.BooksPage.table.headers.author'), value: 'author' },
        { text: this.$t('pages.BooksPage.table.headers.read'), value: 'read' },
        { text: this.$t('pages.BooksPage.table.headers.actions'), value: 'action', sortable: false }
      ]
    }
  },
  methods: {
    deleteItem (item) {
      if (confirm('Are you sure you want to delete this item?')) {
        console.log('deleting', item)
      }
    },
    getAuthor (item) {
      return _.get(item, 'author', 'n/a')
    },
    getRead (item) {
      return _.get(item, 'read', 'n/a')
    },
    getTitle (item) {
      return _.get(item, 'title', 'ERROR')
    }
  }
}
</script>
