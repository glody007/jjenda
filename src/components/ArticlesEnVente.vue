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

export default {
  name: 'ArticlesEnVente',

  components: {
    Article
  },
  data: () => ({
    articles: [
      {
        prix: '100$',
        categorie: 'Phone',
        description: 'Iphone x 128 Gb',
        url_photo: 'https://ik.imagekit.io/djenda/Djenda_M8A0w1OWcA',
        url_thumbnail_photo: 'https://ik.imagekit.io/djenda/tr:n-media_library_thumbnail/Djenda_M8A0w1OWcA',
        created_at: '21/09/2020',
        location: [10, 45]
      },
      {
        prix: '65$',
        categorie: 'Phone',
        description: 'Iphone x 128 Gb',
        url_photo: 'https://ik.imagekit.io/djenda/Djenda_M8A0w1OWcA',
        url_thumbnail_photo: 'https://ik.imagekit.io/djenda/tr:n-media_library_thumbnail/Djenda_M8A0w1OWcA',
        created_at: '21/09/2020',
        location: [10, 45]
      },
      {
        prix: '80$',
        categorie: 'Phone',
        description: 'Iphone x 128 Gb',
        url_photo: 'https://ik.imagekit.io/djenda/Djenda_M8A0w1OWcA',
        url_thumbnail_photo: 'https://ik.imagekit.io/djenda/tr:n-media_library_thumbnail/Djenda_M8A0w1OWcA',
        created_at: '21/09/2020',
        location: [10, 45]
      },
      {
        prix: '200$',
        categorie: 'Phone',
        description: 'Iphone x 128 Gb',
        url_photo: 'https://ik.imagekit.io/djenda/Djenda_M8A0w1OWcA',
        url_thumbnail_photo: 'https://ik.imagekit.io/djenda/tr:n-media_library_thumbnail/Djenda_M8A0w1OWcA',
        created_at: '21/09/2020',
        location: [10, 45]
      }
    ]
  })
}
</script>
