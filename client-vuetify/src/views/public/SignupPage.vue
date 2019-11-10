<template>
  <v-form ref="form" @submit.prevent="signup">
    <v-card>
      <v-toolbar dark color="primary">
        <v-toolbar-title>{{$t('appl.title')}} &ndash; {{$t('pages.SignupPage.title')}}</v-toolbar-title>
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
            :label="$t('pages.SignupPage.form.fields.username.label')"
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
            :label="$t('pages.SignupPage.form.fields.password.label')"
            :error-messages="errorMessage('password')"
            @change="$v.password.$touch()"
            @blur="$v.password.$touch()"
            @click:append="showPassword = !showPassword"></v-text-field>
        <v-text-field
            name="confirmPassword"
            prepend-icon="lock"
            v-model.trim='confirmPassword'
            autocomplete="off"
            clearable
            :append-icon="showConfirmPassword ? 'visibility' : 'visibility_off'"
            :type="showConfirmPassword ? 'text' : 'password'"
            :label="$t('pages.SignupPage.form.fields.confirmPassword.label')"
            :error-messages="errorMessage('confirmPassword')"
            @change="$v.confirmPassword.$touch()"
            @blur="$v.confirmPassword.$touch()"
            @click:append="showConfirmPassword = !showConfirmPassword"></v-text-field>
        <v-text-field
            name="email"
            type="text"
            prepend-icon="email"
            v-model.trim='email'
            autocomplete="off"
            clearable
            :label="$t('pages.SignupPage.form.fields.email.label')"
            :error-messages="errorMessage('email')"
            @change="$v.email.$touch()"
            @blur="$v.email.$touch()"></v-text-field>
        <v-alert :value="!!error" type="error" outlined>
          {{error}}
        </v-alert>
      </v-card-text>
      <v-card-actions class="justify-center">
        <v-btn
            type="submit"
            color="primary"
            :disabled="$v.$invalid"
            :loading="loading">{{$t('pages.SignupPage.form.buttons.signup')}}</v-btn>
        <v-btn
            text
            @click="clear">{{$t('pages.SignupPage.form.buttons.clear')}}</v-btn>
        <v-spacer/>
        <v-btn
            text
            to="/login">{{$t('pages.SignupPage.form.buttons.login')}}</v-btn>
      </v-card-actions>
    </v-card>
  </v-form>
</template>

<script>
import _ from 'lodash'
import { mapGetters } from 'vuex'
import { validationMixin } from 'vuelidate'
import { alphaNum, email, minLength, required, sameAs } from 'vuelidate/lib/validators'
import { AuthService } from '@/modules/auth'
import { PageMixin } from '@/modules/core'
export default {
  name: 'SignupPage',
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
      confirmPassword: '',
      email: '',
      error: '',
      showPassword: false,
      showConfirmPassword: false
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
          'alphaNum',
          'sameAsPassword',
          'email'
        ], k)))
        if (!_.isEmpty(errorTypes)) {
          const msgId = 'pages.SignupPage.form.fields.' + field + '.error'
          return this.$t(msgId + '.' + errorTypes[0])
        }
      }
    },
    async signup () {
      this.$store.commit('setLoading', true)
      try {
        await AuthService.signup(_.pick(this, ['username', 'password', 'email']))
        this.$router.replace({ name: 'login' })
      } catch {
        this.error = this.$t('pages.SignupPage.form.error')
        this.$store.commit('setLoading', false)
      }
    }
  },
  mounted () {
    this.$refs.username.focus()
  },
  validations: {
    username: { required, minLength: minLength(4), alphaNum },
    password: { required, minLength: minLength(8) },
    confirmPassword: { sameAsPassword: sameAs('password') },
    email: { required, email }
  }
}
</script>
