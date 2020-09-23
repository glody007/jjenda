<template>
  <v-container fill-height fluid>
    <v-row justify="center">
      <v-col cols="12" sm="6">
        <router-link to="/about">
          <ArticleImage :article="article" :aspectRatio="2/3"/>
        </router-link>
      </v-col>

      <v-col cols="12" sm="4">
        <v-card
          class="mx-auto"
          max-width="400"
          outlined
          tile
          hover
        >
          <v-card-title class="ma-0">
            <div>{{article.categorie}}</div>
          </v-card-title>

          <v-card-text class="text--primary">

            <div>{{article.description}}</div>

            <div>{{article.created_at}}</div>

            <v-badge
              class="mt-5"
              color="black"
              inline
              :content="prix"
            >
            </v-badge>
          </v-card-text>

          <VendeurContact class="mt-6" :article= "article"/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ArticleImage from '../components/ArticleImage'
import VendeurContact from '../components/VendeurContact'
import $backend from '../backend'

export default {
  name: 'Article',

  components: {
    ArticleImage, VendeurContact
  },

  data: () => ({
    article: { prix: '20',
      categorie: 'Habille',
      description: 'polo rouge',
      created_at: '20/04/1994',
      url_photo: 'https://ik.imagekit.io/djenda/09-17-20_03-33-59_TUJ-4GDBm.jpg' },
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
        })
        .catch(error => {
          this.error = error
        })
    }
  },

  computed: {
    prix () {
      return `${this.article.prix}$`
    }
  }
}
</script>
