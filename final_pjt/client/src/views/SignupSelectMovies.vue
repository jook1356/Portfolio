<template>

  <div style="margin-top:-72px; padding-top: 72px; width:100vw; height:auto; background-color: rgba(0, 0, 0, 0.6); position:relative;">
    <div class="select-fade-in-animation"></div>
    <div style="display:flex; justify-content:space-between">
      <div style="margin-left:85px; text-align:left;">
        <p class="descryption"><b>선호하는 영화를 선택하세요.</b></p>
        <p>선택하신 영화를 기반으로 영화를 추천해 드립니다.</p>
      </div>
      <div style="margin-right:85px; padding-top:50px;">
        <div class="background-movie-button" @click="submitSelectedMovies">
            <span class="background-movie-button-font"><b>다음</b></span>
        </div>
      </div>
    </div>
    

    <div v-for="genre in moviesByGenreList" :key="genre.name">
      <div v-if="'movies' in genre && genre.movies.length >= cardSplitter">
        <SignupSelectMoviesCard :movieList="genre.movies" :identifier="`${genre.name}`" :card-splitter="cardSplitter" :selected-movies="selectedMovies" @select-movie="selectMovie"/>
        <br>
      </div>
    </div>

    
  </div>
</template>

<script>
import axios from 'axios'


import SignupSelectMoviesCard from '@/components/SignupSelectMoviesCard'

export default {
  name: 'SignupSelectMovies',
  components: {
    SignupSelectMoviesCard

  },
  data() {
    return {
      browserWidth: null,
      browserHeight: null,
      cardSplitter: null,
      selectedMovies: [],
      selectedGenres: {main_genres: [], sub_genres: [], main_genre_score: 10, sub_genre_score: 5}
    }
  },
  computed: {
    moviesByGenreList() {
      return this.$store.state.moviesByGenreList
    },
    backgroundMovie() {
      const movie = this.$store.state.backgroundMovie
      return movie
    },
  },
  methods: {
    receiveMoviesByGenreData() {
      this.$store.dispatch('receiveMoviesByGenreData')
    },
    selectMovie(childData) {
      const classify = this.selectedMovies.indexOf(childData)
      if (classify === -1) {
        this.selectedMovies.push(childData)
        this.selectedGenres.sub_genres.push(childData.sub_genres)
        this.selectedGenres.main_genres.push(childData.main_genre)
        console.log('추가')
      } else {
        this.selectedMovies.splice(classify, 1)
        
        console.log('삭제')
      }
      
    },
    submitSelectedMovies() {
      const API_URL = "http://127.0.0.1:8000"
      const selectedMovies = this.selectedMovies
      
      const userId = this.$store.state.userInfo.id
      axios({
        method: 'post',
        url: `${API_URL}/movies/store_selected_movies/${userId}/`,
        data: {
          selectedMovies,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          console.log(selectedMovies)
        })
        .catch((err) => {
          console.log('submitSelectedMovies =>', err)
        })

      

      const genreScoreSet = this.selectedGenres

      axios({
        method: 'post',
        url: `${API_URL}/movies/calculate_score/`,
        data: {
          genreScoreSet,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          
          axios({
            method: 'post',
            url: `${API_URL}/movies/off_new_user/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then((res) => {
              console.log(res)
              this.$router.push({name: 'movie'})
            })
            .catch((err) => {
              console.log(err)
            })

          
          
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.receiveMoviesByGenreData()
    this.browserWidth = document.body.offsetWidth
    this.browserHeight = window.innerHeight
  },
  mounted() {
    this.$store.dispatch('login')
    
    this.cardSplitter = parseInt(document.body.offsetWidth / 320) + 1
    window.onresize = (() => {
      this.browserWidth = document.body.offsetWidth //event.delegateTarget.innerWidth
      this.browserHeight = window.innerHeight
      this.cardSplitter = parseInt(document.body.offsetWidth / 320) + 1 //event.delegateTarget.innerWidth
    });


    if (this.$store.state.wallpaperFix === true) {
      // const bodyTag = document.querySelector('.movie-view')
      // bodyTag.setAttribute(`style`, `background-image:url('https://image.tmdb.org/t/p/original${this.backgroundMovie.backdrop_path}'); width: 100vw; background-size:100vw; background-color: black; background-repeat:no-repeat; `)

      const viewTag = document.querySelector('.select-fade-in-animation')
      viewTag.setAttribute(`style`, `background-image:url('https://image.tmdb.org/t/p/original${this.backgroundMovie.backdrop_path}'); width: 100vw; height: 100vh; z-index:99999; background-size:cover; background-color: black; background-repeat:no-repeat; `)

      setTimeout(() => {
        viewTag.style.opacity = 0
      }, 10);
      
      setTimeout(() => {
        viewTag.style.display = 'none'
      }, 1010);
    }



  }
}
</script>

<style>
.descryption {
  font-size: 48px;
}

.select-fade-in-animation {
    transition-duration: 1s;
    width: 100vw;
    height: auto;
    position:fixed;
    left: 0%;
    top: 0%;
    transition-property: width height opacity;
    z-index:9999999;
}
</style>