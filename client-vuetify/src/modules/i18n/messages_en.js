/**
 * The MIT License (MIT)
 *
 * Copyright (c) 2019 Jon Brule <brulejr@gmail.com>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the 'Software'), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

export const messagesEn = {
  appl: {
    page: {
      title: 'flask-vue-crud - {pageName}'
    },
    title: 'flask-vue-crud'
  },
  errors: {
    sessionExpired: {
      title: 'Session expired',
      details: 'Please login to Slidedeck again.'
    }
  },
  pages: {
    BooksPage: {
      title: 'Books',
      table: {
        headers: {
          author: 'Author',
          read: 'Read?',
          title: 'Title'
        },
        noData: 'No books available'
      }
    },
    HomePage: {
      title: 'Dashboard'
    },
    LoginPage: {
      title: 'Login',
      footer: 'Enter credentials and click \'Sign In\'',
      form: {
        fields: {
          username: {
            label: 'Username',
            placeholder: 'Your username',
            error: {
              alphaNum: 'Username must be alpha-numeric',
              minLength: 'Username must be at least 4 characters',
              required: 'Username is required'
            }
          },
          password: {
            label: 'Password',
            placeholder: 'Your password',
            error: {
              minLength: 'Password must be at least 8 characters',
              required: 'Password is required'
            }
          }
        },
        error: 'Credentials are invalid',
        buttons: {
          clear: 'Clear',
          login: 'Login'
        }
      }
    }
  },
  text: {
    no: 'No',
    ok: 'OK',
    yes: 'Yes',
    warning: 'Warning'
  }
}
