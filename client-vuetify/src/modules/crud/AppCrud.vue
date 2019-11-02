<template>
  <v-data-table :headers="headers"
                :items="items"
                hide-actions>
    <template slot="items" slot-scope="data">
      <slot name="items" :data="data">
        <tr>
          <td v-for='header in headers' :key='header.value'>
            {{ data.item[header.value] }}
          </td>
        </tr>
      </slot>
    </template>
  </v-data-table>
</template>

<script>
export default {
  props: [
    'headers',
    'items'
  ]
}
</script>