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

import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'

import { BooksStore } from '@/modules/books'

Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
  reducer: (state) => ({
    access_token: state.access_token,
    navMenuActive: state.navMenuActive,
    navMenuCollapsed: state.navMenuCollapsed,
    refresh_token: state.refresh_token,
    user: state.user
  })
})

export default new Vuex.Store({
  modules: {
    books: BooksStore
  },
  state: {
    access_token: undefined,
    loading: false,
    navMenuActive: true,
    navMenuCollapsed: true,
    refresh_token: undefined,
    user: undefined
  },
  getters: {
    getRefreshToken: state => state.refresh_token,
    getToken: state => state.access_token,
    getUser: state => state.user,
    isAuthenticated: state => !!state.access_token && !!state.refresh_token && !!state.user,
    isNavMenuActive: state => state.navMenuActive,
    isNavMenuCollapsed: state => state.navMenuCollapsed,
    loading: state => state.loading
  },
  mutations: {
    clearAuthentication: (state) => {
      state.access_token = undefined
      state.refresh_token = undefined
      state.user = undefined
    },
    refreshToken: (state, auth) => {
      state.access_token = auth.access_token
      state.refresh_token = auth.refresh_token
    },
    setAuthentication: (state, auth) => {
      state.access_token = auth.access_token
      state.refresh_token = auth.refresh_token
      state.user = auth.user
    },
    setLoading: (state, bool) => {
      state.loading = bool
    },
    setNavMenuCollapsed: (state, navMenuCollapsed) => {
      state.navMenuCollapsed = navMenuCollapsed
    },
    toggleNavMenuActive: (state) => {
      state.navMenuActive = !state.navMenuActive
    },
    toggleNavMenuCollapsed: (state) => {
      state.navMenuCollapsed = !state.navMenuCollapsed
    }
  },
  actions: {
  },
  plugins: [vuexLocal.plugin]
})
