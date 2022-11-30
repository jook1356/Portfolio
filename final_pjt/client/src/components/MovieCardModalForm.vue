<template>
  <div @mouseenter="modalCardAnimationOn(propsMovie.id)" @mouseleave="modalCardAnimationOff(propsMovie.id)" :id="`modal-card-${identifier}-${propsMovie.id}`">
    <MovieCardDetail :props-movie="propsMovie" :identifier="identifier" ref="apiRequest"/>
    <div class="background" :id="`background-${identifier}-${propsMovie.id}`">

      <div class="modal-wrapper" :id="`modal-card-wrapper-${identifier}-${propsMovie.id}`" >
      
          <!-- <div v-if="propsMovie.logo_path" style="position:absolute; width:100%; height:100%; display:flex; justify-content:start; align-items:flex-end; padding-bottom:20px;  padding-left:20px; padding-right:20px;">
            <img style=" max-height:60px; max-width:120px;" :src="`https://image.tmdb.org/t/p/w500${propsMovie.logo_path}`" class="img-fluid logo-image">
          </div> -->
          <img :src="`https://image.tmdb.org/t/p/w500/${propsMovie.backdrop_path}`" class="img-fluid modal-image">
       
        
        <div class="wrapper" :id="`wrapper-${identifier}-${propsMovie.id}`">

          <div class="marquee-wrapper">
            <marquee class="marquee-h3">
              <b>{{ propsMovie.title }}</b>
            </marquee>
          </div>

          <div class="flex">
            <p class="release-date"><b>{{ propsMovie.released_date.substr(0,4) }}</b></p>


            <div style="line-height:1; margin-bottom: 0px;">
              <!-- <star-rating :star-size="24" :rating="3.8" :read-only="true" :increment="0.5" :show-rating="false" :animate="true" :active-color="['#ae0000','#003333']" :active-border-color="['#F6546A','#a8c3c0']" :border-width="4" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]" :active-on-click="true" :clearable="true"></star-rating> -->
              <star-rating :star-size="24" :rating="propsMovie.vote_average" :read-only="true" :increment="0.5" :show-rating="false" :animate="true" :active-color="['#520000','#520000']" :active-border-color="['#F6546A','#948989']" :border-width="4" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]" :active-on-click="true" :clearable="true"></star-rating>
            </div>
            
          </div>

          <div class="genre-wrapper" style="margin-top: -10px;">
              <div class="genre-decorator">{{ propsMovie.main_genre.name }}</div>
              <div v-for="(genre, index) in propsMovie.sub_genres" :key="index" class="genre-decorator">{{ genre.name }}</div>
              <div class="genre-decorator">인기 영화</div>
          </div>

          <!-- <h3>{{ propsMovie.title }}</h3> -->
          




          
      
      <div class="modal-button-wrapper">

        <div class="dislike-button" @click="toggleMovieDislike(false)">

          <div v-if="isDisliked">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
              <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
            </svg>
            <svg style="position: absolute; margin-left: -31px; margin-top: 10px; color:white;" xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" class="bi bi-hand-thumbs-down-fill" viewBox="0 0 16 16">
              <path d="M6.956 14.534c.065.936.952 1.659 1.908 1.42l.261-.065a1.378 1.378 0 0 0 1.012-.965c.22-.816.533-2.512.062-4.51.136.02.285.037.443.051.713.065 1.669.071 2.516-.211.518-.173.994-.68 1.2-1.272a1.896 1.896 0 0 0-.234-1.734c.058-.118.103-.242.138-.362.077-.27.113-.568.113-.856 0-.29-.036-.586-.113-.857a2.094 2.094 0 0 0-.16-.403c.169-.387.107-.82-.003-1.149a3.162 3.162 0 0 0-.488-.9c.054-.153.076-.313.076-.465a1.86 1.86 0 0 0-.253-.912C13.1.757 12.437.28 11.5.28H8c-.605 0-1.07.08-1.466.217a4.823 4.823 0 0 0-.97.485l-.048.029c-.504.308-.999.61-2.068.723C2.682 1.815 2 2.434 2 3.279v4c0 .851.685 1.433 1.357 1.616.849.232 1.574.787 2.132 1.41.56.626.914 1.28 1.039 1.638.199.575.356 1.54.428 2.591z"/>
            </svg>
          </div>
          <div v-else>
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
              <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
            </svg>
            
            <svg style="position: absolute; margin-left: -31px; margin-top: 10px; color:white;" xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" class="bi bi-hand-thumbs-down" viewBox="0 0 16 16">
              <path d="M8.864 15.674c-.956.24-1.843-.484-1.908-1.42-.072-1.05-.23-2.015-.428-2.59-.125-.36-.479-1.012-1.04-1.638-.557-.624-1.282-1.179-2.131-1.41C2.685 8.432 2 7.85 2 7V3c0-.845.682-1.464 1.448-1.546 1.07-.113 1.564-.415 2.068-.723l.048-.029c.272-.166.578-.349.97-.484C6.931.08 7.395 0 8 0h3.5c.937 0 1.599.478 1.934 1.064.164.287.254.607.254.913 0 .152-.023.312-.077.464.201.262.38.577.488.9.11.33.172.762.004 1.15.069.13.12.268.159.403.077.27.113.567.113.856 0 .289-.036.586-.113.856-.035.12-.08.244-.138.363.394.571.418 1.2.234 1.733-.206.592-.682 1.1-1.2 1.272-.847.283-1.803.276-2.516.211a9.877 9.877 0 0 1-.443-.05 9.364 9.364 0 0 1-.062 4.51c-.138.508-.55.848-1.012.964l-.261.065zM11.5 1H8c-.51 0-.863.068-1.14.163-.281.097-.506.229-.776.393l-.04.025c-.555.338-1.198.73-2.49.868-.333.035-.554.29-.554.55V7c0 .255.226.543.62.65 1.095.3 1.977.997 2.614 1.709.635.71 1.064 1.475 1.238 1.977.243.7.407 1.768.482 2.85.025.362.36.595.667.518l.262-.065c.16-.04.258-.144.288-.255a8.34 8.34 0 0 0-.145-4.726.5.5 0 0 1 .595-.643h.003l.014.004.058.013a8.912 8.912 0 0 0 1.036.157c.663.06 1.457.054 2.11-.163.175-.059.45-.301.57-.651.107-.308.087-.67-.266-1.021L12.793 7l.353-.354c.043-.042.105-.14.154-.315.048-.167.075-.37.075-.581 0-.211-.027-.414-.075-.581-.05-.174-.111-.273-.154-.315l-.353-.354.353-.354c.047-.047.109-.176.005-.488a2.224 2.224 0 0 0-.505-.804l-.353-.354.353-.354c.006-.005.041-.05.041-.17a.866.866 0 0 0-.121-.415C12.4 1.272 12.063 1 11.5 1z"/>
            </svg>
          </div>

        </div>


        <div class="like-button" @click="toggleMovieLike(false)">

          <div v-if="isLiked">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
              <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
            </svg>
            <svg style="position: absolute; margin-left: -31px; margin-top: 8px; color:white;" xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
              <path d="M6.956 1.745C7.021.81 7.908.087 8.864.325l.261.066c.463.116.874.456 1.012.965.22.816.533 2.511.062 4.51a9.84 9.84 0 0 1 .443-.051c.713-.065 1.669-.072 2.516.21.518.173.994.681 1.2 1.273.184.532.16 1.162-.234 1.733.058.119.103.242.138.363.077.27.113.567.113.856 0 .289-.036.586-.113.856-.039.135-.09.273-.16.404.169.387.107.819-.003 1.148a3.163 3.163 0 0 1-.488.901c.054.152.076.312.076.465 0 .305-.089.625-.253.912C13.1 15.522 12.437 16 11.5 16H8c-.605 0-1.07-.081-1.466-.218a4.82 4.82 0 0 1-.97-.484l-.048-.03c-.504-.307-.999-.609-2.068-.722C2.682 14.464 2 13.846 2 13V9c0-.85.685-1.432 1.357-1.615.849-.232 1.574-.787 2.132-1.41.56-.627.914-1.28 1.039-1.639.199-.575.356-1.539.428-2.59z"/>
            </svg>
          </div>
          <div v-else>
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
              <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
            </svg>
            <svg style="position: absolute; margin-left: -31px; margin-top: 8px; color:white;" xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" class="bi bi-hand-thumbs-up" viewBox="0 0 16 16">
              <path d="M8.864.046C7.908-.193 7.02.53 6.956 1.466c-.072 1.051-.23 2.016-.428 2.59-.125.36-.479 1.013-1.04 1.639-.557.623-1.282 1.178-2.131 1.41C2.685 7.288 2 7.87 2 8.72v4.001c0 .845.682 1.464 1.448 1.545 1.07.114 1.564.415 2.068.723l.048.03c.272.165.578.348.97.484.397.136.861.217 1.466.217h3.5c.937 0 1.599-.477 1.934-1.064a1.86 1.86 0 0 0 .254-.912c0-.152-.023-.312-.077-.464.201-.263.38-.578.488-.901.11-.33.172-.762.004-1.149.069-.13.12-.269.159-.403.077-.27.113-.568.113-.857 0-.288-.036-.585-.113-.856a2.144 2.144 0 0 0-.138-.362 1.9 1.9 0 0 0 .234-1.734c-.206-.592-.682-1.1-1.2-1.272-.847-.282-1.803-.276-2.516-.211a9.84 9.84 0 0 0-.443.05 9.365 9.365 0 0 0-.062-4.509A1.38 1.38 0 0 0 9.125.111L8.864.046zM11.5 14.721H8c-.51 0-.863-.069-1.14-.164-.281-.097-.506-.228-.776-.393l-.04-.024c-.555-.339-1.198-.731-2.49-.868-.333-.036-.554-.29-.554-.55V8.72c0-.254.226-.543.62-.65 1.095-.3 1.977-.996 2.614-1.708.635-.71 1.064-1.475 1.238-1.978.243-.7.407-1.768.482-2.85.025-.362.36-.594.667-.518l.262.066c.16.04.258.143.288.255a8.34 8.34 0 0 1-.145 4.725.5.5 0 0 0 .595.644l.003-.001.014-.003.058-.014a8.908 8.908 0 0 1 1.036-.157c.663-.06 1.457-.054 2.11.164.175.058.45.3.57.65.107.308.087.67-.266 1.022l-.353.353.353.354c.043.043.105.141.154.315.048.167.075.37.075.581 0 .212-.027.414-.075.582-.05.174-.111.272-.154.315l-.353.353.353.354c.047.047.109.177.005.488a2.224 2.224 0 0 1-.505.805l-.353.353.353.354c.006.005.041.05.041.17a.866.866 0 0 1-.121.416c-.165.288-.503.56-1.066.56z"/>
            </svg>
          </div>

        </div>
        
        <div class="add-favorite-button">
          <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-plus-circle" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
            <path style="color:white;" d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
          </svg>
        </div>
        
        <div class="show-detail-button" @click="showDetail(propsMovie.id)">
          <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-arrow-up-circle-fill" viewBox="0 0 16 16">
            <path d="M16 8A8 8 0 1 0 0 8a8 8 0 0 0 16 0zm-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707V11.5z"/>
          </svg>
        </div>

      </div>
      

    </div>
    
      
      
    </div>
    </div>
    
    
  </div>
  
</template>

<script>
import MovieCardDetail from '@/components/MovieCardDetail'
import StarRating from 'vue-star-rating'
import axios from 'axios'

export default {
  name:'MovieCardModalForm',
  components: {
    MovieCardDetail,
    StarRating
  },
  props: {
    propsMovie: Object,
    identifier: String,
  },
  data() {
    return {
      movieLikes: [],
      movieDislikes: [],
      cardWidth: 240,
      cardHeight: 140,
      modalWidth: 290,
      modalHeight: 400,
      mouseOnCard: false,
      
    }
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo
    },
    isLiked() {
      return this.movieLikes.includes(this.userInfo.id)
    },
    isDisliked() {
      return this.movieDislikes.includes(this.userInfo.id)
    },
    isDetailMode() {
      return this.$store.state.isDetailMode
    },
    genreList() {
      return this.$store.state.genreList
    },
    // movieGenre() {
      
    // }
    
  },
  methods: {
    // getModalXY(idx) {

    //   const modalTag = document.querySelector(`#modal-card-${idx}`)
    //   const modalX = modalTag.getBoundingClientRect().left;
    //   const modalY = modalTag.getBoundingClientRect().top;
    //   const modalXY = {modalX:modalX, modalY:modalY}
    //   this.$store.commit('GET_MODAL_XY', modalXY)

    //   //   alert(this.$store.state.cardXY.cardX)
    //   //   alert(this.$store.state.cardXY.cardY)

    // },
    modalCardAnimationOn(idx) {
      const API_URL = "http://127.0.0.1:8000"
      axios({
      method: 'get',
      url: `${API_URL}/movies/get_movie_likes/${this.propsMovie.id}/`,
      })
        .then((res) => {
          console.log(res)
          this.movieLikes = res.data.like_users
          this.movieDislikes = res.data.dislike_users
          console.log(this.movieLikes)



      })
        .catch((err) => {
          console.log(err)
      })
      


      
      const modalTags = document.querySelectorAll('.modal-card')
      if (this.isDetailMode === false) {
        modalTags.forEach((elem) => {
          if (elem.id != `modal-card-${this.identifier}-${idx}`) {
            elem.style.width = '100%'
            elem.style.height = '100%'
            elem.style.visibility = 'hidden'
          }
        })
      } else {
        const modalTag = document.getElementById(`modal-card-${this.identifier}-${idx}`)
        modalTag.style.visibility = 'hidden'
        }


        if (this.isDetailMode === false && this.mouseOnCard === false) {
        this.mouseOnCard = true
        const wrapperTag = document.getElementById(`wrapper-${this.identifier}-${idx}`)
        const modalTag = document.getElementById(`modal-card-${this.identifier}-${idx}`)
        const backgroundTag = document.getElementById(`background-${this.identifier}-${idx}`)
        // modalTag.style.opacity = 255
        backgroundTag.style.opacity = 255
        wrapperTag.style.opacity = 255

        modalTag.style.visibility = 'visible'
        // modalTag.boxShadow = '0px 0px 5px 1px rgba(0, 0, 0, 0.700)'
        modalTag.style.width = this.cardWidth + 'px'
        modalTag.style.height = this.cardheight + 'px'

        // modalTag.setAttribute('style', `width: ${this.cardWidth}px; height: ${this.cardHeight}px;`)

        
     
        modalTag.style.width = this.modalWidth + 'px'
        modalTag.style.height = this.modalHeight + 'px'
        
        
      } 

      

    },
    modalCardAnimationOff(idx) {
      if (this.isDetailMode === false && this.mouseOnCard === true) {
        const modalTags = document.querySelectorAll('.modal-card')
        if (this.isDetailMode === false) {
          modalTags.forEach((elem) => {
            if (elem.id != `modal-card-${this.identifier}-${idx}`) {
              elem.style.width = '100%'
              elem.style.height = '100%'
              elem.style.visibility = 'hidden'
            }
          })
        }

        const wrapperTag = document.getElementById(`wrapper-${this.identifier}-${idx}`)
        wrapperTag.style.opacity = 0
        const modalTag = document.getElementById(`modal-card-${this.identifier}-${idx}`)
        modalTag.style.width = '100%'
        modalTag.style.height = '100%'
        modalTag.style.visibility = 'hidden'


        setTimeout(() => {
          this.mouseOnCard = false
        }, 700);
        

      } else {
        const modalTag = document.getElementById(`modal-card-${this.identifier}-${idx}`)
        modalTag.style.visibility = 'hidden'
      }
      
    },



    showDetail(idx) {
      const modalTag = document.getElementById(`modal-card-${this.identifier}-${idx}`)
      modalTag.setAttribute('style', '0px 0px 0px 0px rgba(0, 0, 0, 0)')
      this.$parent.getCardXY(idx)
      const backgroundTag = document.getElementById(`background-${this.identifier}-${idx}`)
      backgroundTag.style.opacity = 0
      this.$store.commit('IS_DETAIL_MODE', true)
      this.mouseOnCard = false
      this.$refs.apiRequest.showDetail();
    },

    toggleMovieLike(opposite) {
      const API_URL = "http://127.0.0.1:8000"

      axios({
        method: 'post',
        url: `${API_URL}/movies/like_movie/${this.propsMovie.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          if (this.isDisliked && opposite === false) {
            this.toggleMovieDislike(true)
          }

          if (this.isLiked) {
            const genreScoreSet = {main_genres: [], sub_genres: [], main_genre_score: -2, sub_genre_score: -1}
            genreScoreSet.sub_genres.push(this.propsMovie.sub_genres)
            genreScoreSet.main_genres.push(this.propsMovie.main_genre)
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
                // this.$router.push({name: 'movie'})
                
              })
              .catch((err) => {
                console.log(err)
              })
          } else {
            const genreScoreSet = {main_genres: [], sub_genres: [], main_genre_score: 2, sub_genre_score: 1}
            genreScoreSet.sub_genres.push(this.propsMovie.sub_genres)
            genreScoreSet.main_genres.push(this.propsMovie.main_genre)
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
                // this.$router.push({name: 'movie'})
                
              })
              .catch((err) => {
                console.log(err)
              })
          }


          this.movieLikes = res.data.like_users
          
      })
        .catch((err) => {
          console.log(err)
      })
    },

    toggleMovieDislike(opposite) {
      const API_URL = "http://127.0.0.1:8000"

      axios({
        method: 'post',
        url: `${API_URL}/movies/dislike_movie/${this.propsMovie.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          if (this.isLiked && opposite === false) {
            this.toggleMovieLike(true)
          }


          if (this.isDisliked) {
            const genreScoreSet = {main_genres: [], sub_genres: [], main_genre_score: 2, sub_genre_score: 1}
            genreScoreSet.sub_genres.push(this.propsMovie.sub_genres)
            genreScoreSet.main_genres.push(this.propsMovie.main_genre)
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
                // this.$router.push({name: 'movie'})
                
              })
              .catch((err) => {
                console.log(err)
              })
          } else {
            const genreScoreSet = {main_genres: [], sub_genres: [], main_genre_score: -2, sub_genre_score: -1}
            genreScoreSet.sub_genres.push(this.propsMovie.sub_genres)
            genreScoreSet.main_genres.push(this.propsMovie.main_genre)
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
                // this.$router.push({name: 'movie'})
                
              })
              .catch((err) => {
                console.log(err)
              })
          }

          this.movieDislikes = res.data.dislike_users
          
      })
        .catch((err) => {
          console.log(err)
      })
    }


  },
  created() {
    const API_URL = "http://127.0.0.1:8000"

      axios({
        method: 'get',
        url: `${API_URL}/movies/get_movie_likes/${this.propsMovie.id}/`,
      })
        .then((res) => {
          console.log(res)
          this.movieLikes = res.data.like_users
          this.movieDislikes = res.data.dislike_users
      })
        .catch((err) => {
          console.log(err)
      })

  },


}
</script>

<style>
  .marquee-wrapper {
    width: 250px;
    z-index:99999;
    /* -webkit-mask-image: -webkit-gradient(linear, left 20%, right bottom, from(rgba(0,0,0,1)), to(rgba(0,0,0,0))) */

    -webkit-mask-image: -webkit-radial-gradient(circle, rgba(0,0,0,1), rgba(0,0,0,0))
    
    /* -webkit-mask-image: -webkit-gradient(linear, left, right bottom, from(rgba(0,0,0,1)), to(rgba(0,0,0,0))); */
  }
  .marquee-h3 {
      font-size: 32px;
      z-index:-1;
      width: 250px;
    
      
  }

  .modal-image {
    border-radius: 10px 10px 0px 0px;
  }

  .modal-card {
    width:17vw;
    height:100%;
    border-radius: 10px;
    z-index: 9999;
    visibility: hidden;
    transition-property: opacity width height left top;
    transition-duration: 0.25s;
    position:absolute;
    /* opacity: 0; */
    box-shadow: 0px 0px 5px 1px rgba(0, 0, 0, 0.700);
    user-select: none;
  }
  .background {
    width: 100%;
    height: 100%;
    border-radius: 10px;
    background-color: rgb(10, 10, 10);
  }

  /* .modal-wrapper {

    transition-property: opacity width height;
    transition-duration: 0.5s;
    opacity: 0;


  }
  .modal-wrapper:hover {
    opacity: 100;
    width:100%;
    height:100%;
  } */

  .wrapper {
    transition-duration: 0.5s;
    transition-property: opacity width height;
    opacity: 0%;
    padding: 20px;
    white-space: nowrap;
    position: relative;
  }

  .flex {
    margin: 7px;
    display: flex;
    justify-content: space-between
  }
  .modal-button-wrapper {
    width: 100%;
    display: flex;
    justify-content: end;
    margin-top: 15px;
  }
  .dislike-button {

  margin-left: 15px;
  display: inline-block;
  cursor: pointer;
  color: rgb(150, 150, 150);
  position: relative;
  transition-duration: 0.5s;
  transition-property: color;
  }
  .dislike-button:hover {
  color: rgb(240, 240, 240);
  }


  .like-button {

    margin-left: 15px;
    display: inline-block;
    cursor: pointer;
    color: rgb(150, 150, 150);
    position: relative;
    transition-duration: 0.5s;
    transition-property: color;
  }
  .like-button:hover {
    color: rgb(240, 240, 240);
  }

  .show-detail-button {

    margin-left: 15px;
    display: inline-block;
    cursor: pointer;
    color: rgb(150, 150, 150);
    transition-duration: 0.5s;
    transition-property: color;
  }
  .show-detail-button:hover {
  color: rgb(240, 240, 240);
  }
  .add-favorite-button{

    margin-left: 15px;
    display: inline-block;
    cursor: pointer;
    color: rgb(150, 150, 150);
    transition-duration: 0.5s;
    transition-property: color;
  }
  .add-favorite-button:hover {
    color: rgb(240, 240, 240);
  }
  .release-date {
    color: gray;
  }

  .genre-decorator {
    border-radius: 20px;
    display: inline-block;
    margin: 5px;
    padding: 3px 10px 3px 10px ;
    background-color: rgb(40, 40, 40);

  }

  .genre-wrapper {
    overflow-y: scroll;
    overflow-x: hidden;
    -webkit-mask-image: -webkit-gradient(linear, left 20%, right bottom, from(rgb(0, 0, 0, 1)), to(rgba(0, 0, 0, 0)))

  }
  .genre-wrapper::-webkit-scrollbar{
    display: none; 
}
  
</style>