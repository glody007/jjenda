<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <v-card>
        <v-card-title>
          <span class="headline">Add raw product</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  label="Categorie*"
                  required
                  v-model="data.categorie"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  label="Saler's name*"
                  required
                  v-model="data.saler_name"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="4"
              >
                <v-text-field
                  label="Saler's number*"
                  required
                  v-model="data.saler_number"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
              >
                <v-text-field
                  label="Location*"
                  required
                  v-model="data.location"
                ></v-text-field>
              </v-col>
              <v-col
                cols="12"
                sm="6"
              >
                <v-text-field
                  label="Prix*"
                  type="number"
                  required
                  v-model="data.prix"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Url photo*"
                  required
                  v-model="data.url_photo"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea
                  label="Description*"
                  required
                  rows="2"
                  v-model="data.description"
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="closeDialog"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="postArticleRaw"
          >
            Add
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import $backend from '../../backend'

export default {
  name: 'DialogAjouterArticleRaw',
  data: () => ({
    data: {
      'categorie': '',
      'prix': '',
      'description': '',
      'url_photo': '',
      'location': '',
      'saler_number': '',
      'saler_name': ''
    },
    error: ''
  }),
  props: ['dialog'],
  methods: {
    postArticleRaw () {
      $backend.postArticleRaw(this.data)
        .then(responseData => {
          this.closeDialog()
        })
        .catch(error => {
          this.error = error
        })
    },
    closeDialog () {
      this.$emit('closeDialog')
    }
  }
}
</script>
