<template>
  <v-container fill-height fluid>
    <v-row class="text-center" justify="center">
      <h1 class="text-h4 text-sm-h2 mb-5 mb-sm-10">
        À propos de Jjenda
      </h1>
    </v-row>
  </v-container>
</template>

<script>

export default {
  name: 'about',
  data () {
    return {

    }
  },
  methods: {

  },
  mounted () {
    window.analytics.page('About')
  }
}

</script>

<style lang="scss">
</style>
