<template>
  <v-container>
    <v-row class="text-center" justify="center">
      <h1 class="text-h4 text-sm-h2 mb-5 mb-sm-10">
        Vendez et achetez où vous êtes avec Jjenda
      </h1>
    </v-row>
    <v-row justify="center">
      <ArticlesEnVente/>
    </v-row>
  </v-container>
</template>

<script>
import ArticlesEnVente from '../components/ArticlesEnVente'
import Article from '../components/Article'

export default {
  name: 'Home',

  components: {
    ArticlesEnVente, Article
  }
}
</script>
