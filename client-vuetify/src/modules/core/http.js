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
import createAuthRefreshInterceptor from 'axios-auth-refresh'
import _ from 'lodash'

import store from '@/modules/store'

const ROOT_URL = process.env.VUE_APP_ROOT_URL

const refreshAuthLogic = failedRequest => {
  const currentRefreshToken = store.getters.getRefreshToken
  return axios.post('/api/v1/auth/refresh', {
    refresh_token: currentRefreshToken
  }).then(response => {
    const accessToken = _.get(response, 'data.access_token')
    const refreshToken = _.get(response, 'data.refresh_token')
    store.commit('refreshToken', { access_token: accessToken, refresh_token: refreshToken })
    failedRequest.response.config.headers['Authorization'] = 'Bearer ' + accessToken
    return Promise.resolve()
  }).catch(error => {
    window.$bus.emit(window.$events.LOGOUT, { force: true })
    throw error
  })
}

export async function HTTP () {
  const instance = axios.create({
    baseURL: ROOT_URL,
    headers: {
      Authorization: 'Bearer ' + store.getters.getToken
    }
  })

  createAuthRefreshInterceptor(instance, refreshAuthLogic)

  return instance
}
