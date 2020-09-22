<template>
  <v-card
    class="mx-auto"
    max-width="400"
    outlined
    tile
  >
    <v-row align="center" justify="center">
      <v-img
        class="white--text align-end grey lighten-2"
        :aspect-ratio="1"
        :src="article.url_photo"
        :lazy-src="article.url_thumbnail_photo"
      >
        <template v-slot:placeholder>
          <v-row
            class="fill-height ma-0"
            align="center"
            justify="center"
          >
            <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
          </v-row>
        </template>
      </v-img>
  ``</v-row>

    <v-card-title class="ma-0">{{article.categorie}}</v-card-title>

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
    MESSSAGE
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
