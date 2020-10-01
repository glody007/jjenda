import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/v1/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

/* Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
}) */

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  fetchArticles () {
    return $axios.get(`best_match_produits`)
      .then(response => response.data)
  },
  fetchArticle (id) {
    return $axios.get(`produits/${id}`)
      .then(response => response.data)
  },
  fetchVendeurArticles (id) {
    return $axios.get(`users/${id}/produits`)
      .then(response => response.data)
  },
  fetchVendeur (id) {
    return $axios.get(`users/${id}`)
      .then(response => response.data)
  }
}
