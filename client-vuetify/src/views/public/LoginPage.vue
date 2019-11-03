<template>
  <v-app>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-form ref="form" @submit.prevent="login">
            <v-card>
              <v-toolbar dark color="primary">
                <v-toolbar-title>{{$t('appl.title')}}</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-text-field
                    name="username"
                    ref="username"
                    type="text"
                    prepend-icon="person"
                    v-model.trim='username'
                    autocomplete="off"
                    clearable
                    :label="$t('pages.LoginPage.form.fields.username.label')"
                    :error-messages="errorMessage('username')"
                    @change="$v.username.$touch()"
                    @blur="$v.username.$touch()"></v-text-field>
                <v-text-field
                    name="password"
                    prepend-icon="lock"
                    v-model.trim='password'
                    autocomplete="off"
                    clearable
                    :append-icon="showPassword ? 'visibility' : 'visibility_off'"
                    :type="showPassword ? 'text' : 'password'"
                    :label="$t('pages.LoginPage.form.fields.password.label')"
                    :error-messages="errorMessage('password')"
                    @change="$v.password.$touch()"
                    @blur="$v.password.$touch()"
                    @click:append="showPassword = !showPassword"></v-text-field>
                <v-alert :value="!!error" type="error" outlined>
                  {{error}}
                </v-alert>
              </v-card-text>
              <v-card-actions class="justify-center">
                <v-btn
                    type="submit"
                    color="primary"
                    :disabled="$v.$invalid"
                    :loading="loading">{{$t('pages.LoginPage.form.buttons.login')}}</v-btn>
                <v-btn
                    text
                    :disabled="!$v.$dirty"
                    @click="clear">{{$t('pages.LoginPage.form.buttons.clear')}}</v-btn>
              </v-card-actions>
            </v-card>
          </v-form>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import _ from 'lodash'
import { mapGetters } from 'vuex'
import { validationMixin } from 'vuelidate'
import { alphaNum, minLength, required } from 'vuelidate/lib/validators'
import { AuthService } from '@/modules/auth'
import { PageMixin } from '@/modules/core'
export default {
  name: 'LoginPage',
  mixins: [
    PageMixin(),
    validationMixin
  ],
  computed: {
    ...mapGetters(['getUser', 'loading'])
  },
  data () {
    return {
      username: '',
      password: '',
      error: '',
      showPassword: false
    }
  },
  methods: {
    clear () {
      this.$refs.form.reset()
      this.error = ''
      this.$refs.username.focus()
    },
    errorMessage (field) {
      const check = this.$v[field]
      if (check.$error) {
        var errorTypes = _.keys(_.pickBy(check, (v, k) => !v && _.includes([
          'required',
          'minLength',
          'alphaNum'
        ], k)))
        if (!_.isEmpty(errorTypes)) {
          const msgId = 'pages.LoginPage.form.fields.' + field + '.error'
          return this.$t(msgId + '.' + errorTypes[0])
        }
      }
    },
    async login () {
      this.$store.commit('setLoading', true)
      try {
        await AuthService.login(this.username, this.password)
        this.$router.replace({ name: 'home' })
      } catch {
        this.error = this.$t('pages.LoginPage.form.error')
        this.$store.commit('setLoading', false)
      }
    }
  },
  mounted () {
    this.$refs.username.focus()
  },
  validations: {
    username: { required, minLength: minLength(4), alphaNum },
    password: { required, minLength: minLength(8) }
  }
}
</script>
