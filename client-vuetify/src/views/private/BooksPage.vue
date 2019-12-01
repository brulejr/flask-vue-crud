<template>
  <app-crud :columns="columns"
            :items="getBooks"
            :no-data-message="$t('pages.BooksPage.table.noData')"
            :form="form"
            @on-delete-item="deleteBook">
  </app-crud>
</template>

<script>
import _ from 'lodash'
import { mapGetters } from 'vuex'
import { AppCrud } from '@/modules/crud'
import { DeviceMixin, PageMixin } from '@/modules/core'
import { BooksService } from '@/modules/books'

function renderMark (value) {
  return value ? 'X' : ''
}

function renderOptional (value) {
  return value || 'n/a'
}

export default {
  name: 'BooksPage',
  mixins: [
    DeviceMixin(),
    PageMixin()
  ],
  created: function () {
    BooksService.findAllBooks()
    BooksService.getBookGenres()
  },
  computed: {
    ...mapGetters(['getBooks', 'getBookGenres']),
    columns () {
      return [
        { text: this.$t('pages.BooksPage.table.headers.title'), value: 'title' },
        { text: this.$t('pages.BooksPage.table.headers.author'), value: 'author', render: renderOptional },
        { text: this.$t('pages.BooksPage.table.headers.genre'), value: 'genre', render: renderOptional },
        { text: this.$t('pages.BooksPage.table.headers.read'), value: 'read', render: renderMark }
      ]
    },
    form () {
      const self = this
      return {
        'title': {
          type: 'v-text-field',
          value: '',
          default: '',
          'field-wrapper': { xs12: true, sm6: true },
          'field-input': {
            label: this.$t('pages.BooksPage.form.fields.title.label'),
            clearable: true
          }
        },
        'author': {
          type: 'v-text-field',
          value: '',
          default: '',
          'field-wrapper': { xs12: true, sm6: true },
          'field-input': {
            label: this.$t('pages.BooksPage.form.fields.author.label'),
            clearable: true
          }
        },
        'genre': {
          type: 'v-autocomplete',
          value: '',
          default: '',
          'field-wrapper': { xs12: true, sm6: true },
          'field-input': {
            label: this.$t('pages.BooksPage.form.fields.genre.label'),
            clearable: true
          },
          getSelectItems () {
            return self.getBookGenres
          }
        }
      }
    }
  },
  methods: {
    deleteBook (book) {
      console.log('delete book', book)
      BooksService.deleteBook(book.bookId).then(() => {
        BooksService.findAllBooks()
      })
    },
    getId (book) {
      return _.get(book, 'bookId')
    }
  },
  components: {
    AppCrud
  }
}
</script>
