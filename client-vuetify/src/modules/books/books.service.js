/**
 * The MIT License (MIT)
 *
 * Copyright (c) 2019 Jon Brule <brulejr@gmail.com>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
import _ from 'lodash'

import CRUD from '@/modules/core/httpCrud'
import { HTTP } from '@/modules/core/http'
import format from 'string-format'
import store from '@/modules/store'

const API = '/api/v1/book/'

export default {

  async createBook (book) {
    return CRUD.create(API, book)
  },

  async deleteBook (bookId) {
    return CRUD.deleteById(API, bookId)
  },

  async findAllBooks () {
    const results = await CRUD.findAll(API)
    const books = _.get(results, 'books') || []
    store.commit('setBooks', books)
  },

  async findBookById (bookId) {
    return CRUD.findById(API, bookId)
  },

  async getBookGenres () {
    try {
      const http = await HTTP()
      const response = await http.get(format('{0}/genres', API))
      const genres = _.get(response.data, 'genres')
      store.commit('setBookGenres', genres)
    } catch (error) {
      throw error.message
    }
  },

  async updateBook (book) {
    return CRUD.update(API, book)
  }

}
