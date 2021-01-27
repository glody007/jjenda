<template>
  <v-container>
      <v-row justify="center">
        <ListeArticles :articles="articles" v-on:loadMore="loadMore()"/>
      </v-row>
  </v-container>
</template>

<script>
import ListeArticles from '../components/ListeArticles'
import $backend from '../backend'

export default {
  name: 'ArticlesEnVente',

  components: {
    ListeArticles
  },

  data: () => ({
    articles: [],
    page: 1,
    nbreArticlesPerPage: 10,
    error: ''
  }),

  mounted () {

  },

  methods: {
    fetchArticles () {
      $backend.fetchArticles(this.page)
        .then(responseData => {
          this.articles = this.articles.concat(responseData)
          this.page++
        })
        .catch(error => {
          this.error = error
        })
    },
    loadMore () {
      this.fetchArticles()
    }
  }

}
</script>
