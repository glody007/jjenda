<template>
  <v-container>
      <v-row justify="center">
        <v-col
          v-for="(article, i) in articles"
          :key="i"
          cols="9" sm="4" md="3"
          class="mb-5"
        >
          <Article :article="article"/>
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
import Article from '../components/Article'
import $backend from '../backend'

export default {
  name: 'ArticlesEnVente',

  components: {
    Article
  },

  data: () => ({
    articles: [],
    error: ''
  }),

  mounted () {
    this.fetchArticles()
  },

  methods: {
    fetchArticles () {
      $backend.fetchArticles()
        .then(responseData => {
          this.articles = responseData
        }).catch(error => {
          this.error = error
        })
    }
  }
}
</script>
