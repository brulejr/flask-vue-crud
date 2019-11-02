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

import { HTTP } from './http'
import format from 'string-format'

async function create (uri, object) {
  try {
    const http = await HTTP()
    const response = await http.post(format('{0}', uri), object)
    return response.data
  } catch (error) {
    throw error.message
  }
}

async function deleteById (uri, id) {
  try {
    const http = await HTTP()
    const response = await http.delete(format('{0}/{1}', uri, id))
    return response.data
  } catch (error) {
    throw error.message
  }
}

async function findAll (uri) {
  try {
    const http = await HTTP()
    const response = await http.get(format('{0}', uri))
    return response.data
  } catch (error) {
    throw error.message
  }
}

async function findById (uri, id) {
  try {
    const http = await HTTP()
    const response = await http.get(format('{0}/{1}', uri, id))
    return response.data
  } catch (error) {
    throw error.message
  }
}

async function update (uri, object) {
  try {
    const http = await HTTP()
    const id = _.get(object, 'id')
    const objectData = _.omit(object, 'id')
    const response = await http.put(format('{0}/{1}', uri, id), objectData)
    return response.data
  } catch (error) {
    throw error.message
  }
}

export default {
  create,
  deleteById,
  findAll,
  findById,
  update
}
