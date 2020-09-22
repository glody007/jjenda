<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      :src="article.url_thumbnail_phot"
    >

    </v-img>

    <v-card-title>{{article.categorie}}</v-card-title>

    <v-card-text class="text--primary">
      <div>{{article.description}}</div>

      <div>{{article.created_at}}</div>

      <div>{{article.prix}}</div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="#c2185b"
        text
      >
        APPEL
      </v-btn>

      <v-btn
        color="#c2185b"
        text
      >
        MESSAGE
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>

export default {
  name: 'Article',

  props: ['article']
}
</script>
