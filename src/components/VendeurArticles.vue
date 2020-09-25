<template>
  <v-container>
      <v-row justify="center">
        <ListeArticles :articles="articles"/>
      </v-row>
  </v-container>
</template>

<script>
import ListeArticles from '../components/ListeArticles'
import $backend from '../backend'

export default {
  name: 'VendeurArticles',

  components: {
    ListeArticles
  },

  data: () => ({
    articles: [],
    error: ''
  }),

  props: ['vendeurId'],

  mounted () {
    this.fetchArticles()
  },

  methods: {
    fetchArticles () {
      $backend.fetchVendeurArticles(this.vendeurId)
        .then(responseData => {
          this.articles = responseData
        })
        .catch(error => {
          this.error = error
        })
    }
  }

}
</script>
