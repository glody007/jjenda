<template>
  <v-container fill-height fluid>
    <v-row v-if="loaded" justify="center" class="mb-5">
      <ArticleDetails :article="article"/>
    </v-row>

    <v-row class="text-center" justify="center">
      <h3 class="text-h5">
        Articles du même vendeur
      </h3>
    </v-row>

    <v-row v-if="loaded" justify="center">
      <VendeurArticles :vendeurId="article.vendeur_id"/>
    </v-row>
  </v-container>
</template>

<script>
import ArticleDetails from '../components/ArticleDetails'
import VendeurArticles from '../components/VendeurArticles'
import $backend from '../backend'

export default {
  name: 'Article',

  components: {
    ArticleDetails, VendeurArticles
  },

  data: () => ({
    article: {},
    loaded: false,
    error: ''
  }),

  mounted () {
    this.fetchArticle()
  },

  methods: {
    fetchArticle () {
      $backend.fetchArticle(this.$route.params.id)
        .then(responseData => {
          this.article = responseData
          this.loaded = true
        })
        .catch(error => {
          this.error = error
        })
    }
  }
}
</script>
