<template>
  <v-container fill-height fluid>
    <v-row class="text-center" justify="center">
      <h1 class="text-h6 text-sm-h2 mb-5 mb-sm-10">
        Recherche
      </h1>
    </v-row>

    <v-row justify="center">
      <ais-instant-search
        :search-client="searchClient"
        index-name="dev_jjenda_articles"
      >
        <v-row justify="center">
          <v-col cols="10" md="12">
            <v-responsive>
              <ais-search-box
                submit-title="Submit the query"
                placeholder="Rechercher des articles"
                show-loading-indicator
              />
            </v-responsive>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col cols="10" md="4">
            <v-card class="mb-4">
`              <ais-numeric-menu
                attribute="prix"
                :items="[
                  { label: 'Tout' },
                  { label: '<= 10$', end: 10 },
                  { label: '10$ - 100$', start: 10, end: 100 },
                  { label: '100$ - 500$', start: 100, end: 500 },
                  { label: '>= 500$', start: 500 },
                ]"
              />`
            </v-card>

            <ais-state-results>
              <template slot-scope="{ state: { query } }">
                <v-card v-if="query.length > 0">
                  <ais-refinement-list attribute="categorie"/>
                </v-card>
                <div v-else></div>
              </template>
            </ais-state-results>
          </v-col>

          <v-col cols="10" md="8">
            <ais-state-results>
              <template slot-scope="{ state: { query }, results: { hits } }">
                <p v-if="query.length > 0 && !hits.length">
                  Pas de resultats pour cette recherche.
                </p>
                <p v-else-if="query.length == 0"></p>
                <ais-infinite-hits v-else>
                  <div slot-scope="{ items }">
                    <searchResults :articles="items"/>
                  </div>
                </ais-infinite-hits>
              </template>
            </ais-state-results>
          </v-col>
        </v-row>
      </ais-instant-search>
    </v-row>
  </v-container>
</template>

<script>
import algoliasearch from 'algoliasearch/lite'
import 'instantsearch.css/themes/algolia-min.css'
import searchResults from '../components/SearchResults'

export default {
  name: 'research',
  components: {
    searchResults
  },
  data () {
    return {
      searchClient: algoliasearch(
        'DXFE7YWBZJ',
        '818ca425222f19163d0e0201856e0ebc'
      )
    }
  },
  methods: {

  },
  mounted () {
    window.analytics.page('Research')
  }
}

</script>

<style lang="scss">
</style>
