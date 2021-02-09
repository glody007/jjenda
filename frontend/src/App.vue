<template>
  <v-app id="inspire">

    <router-view/>

    <v-footer
     dark
    >
      <v-container>
        <v-row justify="center">
          <v-snackbar
            :timeout="-1"
            :value="true"
            color="black"
            v-model="snackbar"
          >
            Pour vendre télécharger l'application

            <template v-slot:action="{ attrs }">
              <v-btn
                color="pink"
                v-bind="attrs"
                :href="link"
              >
                <v-icon>mdi-google-play</v-icon>
                TELECHARGER
              </v-btn>

              <v-btn
                color="pink"
                text
                v-bind="attrs"
                @click="snackbar = false"
              >
                Fermer
              </v-btn>
            </template>
          </v-snackbar>
        </v-row>
        <v-row justify="center" class="mt-1">
          <span>&copy; {{ new Date().getFullYear() }}</span>
        </v-row>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
import Main from './views/Main.vue'

export default {
  name: 'App',
  components: {
    Main
  },
  props: {
    source: String
  },
  data: () => ({
    drawer: false,
    snackbar: true,
    link: 'https://play.google.com/store/apps/details?id=com.jjenda',
    links: ['About']
  }),
  created () {
    this.$vuetify.theme.dark = false
  }
}
</script>
