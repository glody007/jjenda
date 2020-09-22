<template>
  <v-container>
    <v-row justify="center" class="text-center">
      <h3 class="headline font-weight-bold">
        Vendez et achetez où vous êtes avec Jjenda
      </h3>
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
