<template>
  <v-container fill-height fluid>
    <v-row>
      <v-app-bar
        app
      >
        <v-toolbar-title>Products from crawler</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn
          color="primary"
          rounded
          @click="dialogArticle = true"
        >
          <v-icon>mdi-plus</v-icon>
          Single
        </v-btn>

        <v-btn
          color="error"
          rounded
          class="ml-3"
          @click="dialogFile = true"
        >
          <v-icon>mdi-plus</v-icon>
          Multiple
        </v-btn>

      </v-app-bar>
    </v-row>
    <v-row justify="center">
      <DialogAjouterArticleRaw
        :dialog="dialogArticle"
        v-on:closeDialog="dialogArticle = false"
      />
      <DialogAjouterArticlesRawFromFile
        :dialog="dialogFile"
        v-on:closeDialog="dialogFile = false"
      />
      <ListeProductsFromCrawler :articles="articles" v-on:loadMore="loadMore()"/>
    </v-row>
  </v-container>
</template>

<script>
import $backend from '../backend'
import ListeProductsFromCrawler from '../components/ListeProductsFromCrawler'
import DialogAjouterArticleRaw from '../components/dialog/DialogAjouterArticleRaw'
import DialogAjouterArticlesRawFromFile from '../components/dialog/DialogAjouterArticlesRawFromFile'

export default {
  name: 'ProductFromCrawler',
  components: {
    ListeProductsFromCrawler,
    DialogAjouterArticleRaw,
    DialogAjouterArticlesRawFromFile
  },
  data () {
    return {
      name: 'Products from crawler',
      articles: [],
      page: 1,
      nbreArticlesPerPage: 10,
      error: '',
      dialogArticle: false,
      dialogFile: false
    }
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
  },
  mounted () {

  }
}
</script>
