<template>
  <app-crud :columns="columns"
            :items="getBooks"
            :no-data-message="$t('pages.BooksPage.table.noData')"
            @delete-item="deleteBook">
  </app-crud>
</template>

<script>
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
  },
  computed: {
    ...mapGetters(['getBooks']),
    columns () {
      return [
        { text: this.$t('pages.BooksPage.table.headers.title'), value: 'title' },
        { text: this.$t('pages.BooksPage.table.headers.author'), value: 'author', render: renderOptional },
        { text: this.$t('pages.BooksPage.table.headers.read'), value: 'read', render: renderMark }
      ]
    }
  },
  methods: {
    deleteBook (book) {
      console.log('delete book', book)
      this.$root.$confirm({
        title: this.$t('dialogs.deleteConfirmation.title'),
        message: this.$t('dialogs.deleteConfirmation.details'),
        affirmativeText: this.$t('text.yes'),
        negativeText: this.$t('text.no'),
        color: 'warning'
      }).then((confirm) => {
        BooksService.deleteBook(book.bookId)
      })
    }
  },
  components: {
    AppCrud
  }
}
</script>
