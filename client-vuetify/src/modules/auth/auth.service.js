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

import { HTTP } from '@/modules/core'
import store from '@/modules/store'

export default {

  async login (username, password) {
    try {
      const http = await HTTP()
      const response = await http.post('/api/v1/auth/login', {
        username: username,
        password: password
      })
      const auth = {
        access_token: response.data.access_token,
        refresh_token: response.data.refresh_token,
        user: username
      }
      store.commit('setAuthentication', auth)
      return auth
    } catch (error) {
      store.commit('clearAuthentication')
      throw error.message
    }
  },

  async logout () {
    store.commit('clearAuthentication')
  },

  async signup (username, password) {
    try {
      const http = await HTTP()
      const response = await http.post('/api/v1/auth/login', {
        username: username,
        password: password
      })
      return response.data.username
    } catch (error) {
      throw error.message
    }
  }

}
