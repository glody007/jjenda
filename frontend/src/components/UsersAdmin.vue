<template>
  <v-container fill-height fluid>
    <v-row class="text-center" justify="center">
      <h1 class="text-h4 text-sm-h2 mb-5 mb-sm-10">
        Dashboard
      </h1>
    </v-row>
    <v-row justify="center">
      <v-col cols="8" md="6">
        <div
          v-for="(user, i) in users"
          :key="i"
          v-on:click="onClickUser(user)"
        >
          {{user.nom}}
        </div>
      </v-col>

      <v-col cols="8" md="6">
        <div v-if="planGetted">
          <div>
            {{userSelected.nom}} {{userSelected.email}}
          </div>
          <div>
              Forfait {{plan.type}}
          </div>
          <div>
              Articles restants {{plan.nbr_articles_restant}}
          </div>
          <v-btn
            color="#c2185b"
            v-on:click="addPlan"
          >
            AJOUTER UN FORFAIT
          </v-btn>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import $backend from '../backend'

export default {
  name: 'UsersAdmin',
  data () {
    return {
      users: [],
      userSelected: {},
      plan: {},
      planGetted: false,
      error: ''
    }
  },
  methods: {
    fetchUsers () {
      $backend.fetchUsers()
        .then(responseData => {
          this.users = responseData
        })
        .catch(error => {
          this.error = error
        })
    },
    fetchVendeurPlan (id) {
      $backend.fetchVendeurPlan(id)
        .then(responseData => {
          this.plan = responseData
          this.planGetted = true
        })
        .catch(error => {
          this.error = error
        })
    },
    onClickUser (user) {
      this.userSelected = user
      this.fetchVendeurPlan(user.unique_id)
    },
    addPlan () {
      $backend.vendeurAddPlan(this.userSelected.unique_id)
        .then(responseData => {
          this.fetchVendeurPlan(this.userSelected.unique_id)
        })
        .catch(error => {
          this.error = error
        })
    }
  },
  mounted () {
    this.fetchUsers()
  }
}

</script>
