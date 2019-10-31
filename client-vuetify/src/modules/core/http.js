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

import axios from 'axios'
import _ from 'lodash'

import store from '@/modules/store'

const ROOT_URL = process.env.VUE_APP_ROOT_URL

export async function HTTP (token) {
  const headers = {}
  const effectiveToken = token || store.getters.getToken
  if (effectiveToken) {
    headers.Authorization = 'Bearer ' + effectiveToken
  }

  const instance = axios.create({
    baseURL: ROOT_URL,
    headers: headers
  })

  instance.interceptors.response.use(function (response) {
    return response
  }, function (error) {
    const status = _.get(error, 'response.status')
    if (status === 401 || status === 403) {
      window.$bus.emit(window.$events.LOGOUT, { force: true })
    } else {
      console.error('Unexpected error', error)
    }
    return Promise.reject(error)
  })

  return instance
}
