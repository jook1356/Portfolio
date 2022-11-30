<template>
  <div class="detail-form-wrapper" :id="`detail-form-wrapper-${identifier}-${propsMovie.id}`">
    <div class="fixed-toggle-form" :id="`fixed-toggle-form-${identifier}-${propsMovie.id}`">
      <div class="blur-effect-wrapper">
        <div class="blur-effect"></div>
      </div>
      <div class="relative-toggle-form" :id="`relative-toggle-form-${identifier}-${propsMovie.id}`">
        <div class="detail-form" :id="`detail-form-${identifier}-${propsMovie.id}`">

          <img :src="`https://image.tmdb.org/t/p/w1280/${propsMovie.backdrop_path}`" class="img-fluid detail-image">
          <div class="hide-button" @click="hideDetail">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-x-circle-fill hide-icon" viewBox="0 0 16 16">
              <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"/>
            </svg>
          </div>
          <div class="content" :id="`content-${identifier}-${propsMovie.id}`">
            
            <p class="detail-title"><b>{{propsMovie.title}}</b></p>

            <div class="tab">
              <div class="tab-button" @click="selectTab('info')">
                <div class="tab-selected" :id="`tab-selected-info-${identifier}-${propsMovie.id}`">
                  <span>기본 정보</span>
                </div>
                <span>기본 정보</span>
              </div>
            
              <div class="tab-button" @click="selectTab('casts')">
                <div class="tab-selected" :id="`tab-selected-casts-${identifier}-${propsMovie.id}`">
                  <span>출연진</span>
                </div>
                <span>출연진</span>
                
              </div>

            </div>

            <div class="tab-content-wrapper">

              <div class="tab-content" :id="`tab-info-${identifier}-${propsMovie.id}`">
                <p class="detail-overview">{{propsMovie.overview}}</p>

                <div class="additional-info-wrapper">
                  <div style="display:flex;">
                    <span style="margin-top: 2px; margin-right: 8px; color:rgb(150,150,150); font-size: 14px;">평점</span>
                    <star-rating :star-size="18" :rating="propsMovie.vote_average" :read-only="true" :increment="0.5" :show-rating="false" :animate="true" :active-color="['#520000','#520000']" :active-border-color="['#F6546A','#948989']" :border-width="4" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]" :active-on-click="true" :clearable="true"></star-rating>
                    <span style="margin-left:10px;"><b>{{propsMovie.vote_average.toFixed(2)}}점</b></span>
                  </div>
                  
                  <p style="margin-top:14px; color:rgb(150,150,150); font-size: 14px;">개봉일{{'\u00a0'}} <b>{{propsMovie.released_date}}</b></p>
                </div>
                



                <div class="rating-zone-wrapper">

                  <div style="margin-left: -10px; margin-top: 18px;">
                    <div class="detail-genre-decorator">{{ propsMovie.main_genre.name }}</div>
                    <div v-for="(genre, index) in propsMovie.sub_genres" :key="index" class="detail-genre-decorator">{{ genre.name }}</div>
                    <div class="detail-genre-decorator">인기 영화</div>
                  </div>
                    <div class="detail-button-wrapper">

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



                    </div>
                  </div>



              </div>


              <div class="tab-content" :id="`tab-casts-${identifier}-${propsMovie.id}`">

                
                <div class="container text-center">
                  <div class="row row-cols-2">
                    <div class="col" v-for="cast in movieCasts" :key="cast.id" style="display:flex; align-items: center; margin-bottom: 24px;">
                      <img v-if="cast.profile_path" class="detail-profile-image" :src="`https://image.tmdb.org/t/p/w500/${cast.profile_path}`" alt="">
                      
                      <img v-if="!cast.profile_path" class="detail-profile-image" :src="require(`../images/no_profile.jpg`)" alt="">
                      
                      <div style="margin-left: 10px; text-align:left;">
                        <span><b>{{cast.name}}</b></span>
                        <br>
                        <span>{{cast.character}}</span>
                      </div>
                      
                    </div>
                  </div>
                </div>
                <!-- <div v-for="cast in movieCasts" :key="cast.id">
                  <img class="detail-profile-image" :src="`https://image.tmdb.org/t/p/w500/${cast.profile_path}`" alt="">
                  <p>{{cast.name}}</p>
                </div> -->


              </div>


            </div>
            

            <div class="temp">

              
              <MovieCardDetailComments :props-movie="propsMovie"/>
            </div>
            

            
          </div>

          

        </div>
      </div>
      
    </div>
    
    


  </div>
</template>


<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
import MovieCardDetailComments from '@/components/MovieCardDetailComments'

export default {
  name: 'MovieCardDetail',
  components: {
    StarRating,
    MovieCardDetailComments,
  },
  props: {
    propsMovie: Object,
    identifier: String,
    effectElement: String,
  },
  data() {
    return{
      movieCasts: null,
      movieLikes: [],
      movieDislikes: [],

      cardWidth: 240,
      cardHeight: 140,
      modalWidth: 290,
      modalHeight: 400,
      // detailWidth: 40,
      detailWidth: 800, // px
      detailHeight: 100,  // vh
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
  },
  
  methods: {

    
    showDetail() {

      // if (this.identifier === 'searchMovie') {
      //   const searchForm = document.querySelector('.search-inner-form')
      //   searchForm.scrollTo(0,0)
      // }

      const API_URL = "http://127.0.0.1:8000"

      axios({
        method: 'GET',
        url: `${API_URL}/movies/get_movie_casts/${this.propsMovie.id}/`,
      })
        .then(response => {
          this.movieCasts = response.data
          console.log(this.movieCasts)

        })
        .catch(error => {
          console.log(error)
        })
    
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

      const movieId = this.propsMovie.id
      const userId = this.$store.state.userInfo.id
      axios({
        method: 'post',
        url: `${API_URL}/movies/store_viewed_movies/${userId}/`,
        data: {
          movieId,
          userId,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          
        })
        .catch((err) => {
          console.log(err)
        })


      const genreScoreSet = {main_genres: [], sub_genres: [], main_genre_score: 0.5, sub_genre_score: 0.1}
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

      

      this.$store.commit('IS_DETAIL_MODE', true)

      const bodyTag = document.querySelector('body')
      bodyTag.style.overflow = 'hidden'

      const fixedToggleForm = document.querySelector(`#fixed-toggle-form-${this.identifier}-${this.propsMovie.id}`)
      fixedToggleForm.style.display = 'block'

      

      setTimeout(() => {
        fixedToggleForm.style.backgroundColor = 'rgba(0, 0, 0, 0.5)'
      }, 10);
      

      const contentTag = document.querySelector(`#content-${this.identifier}-${this.propsMovie.id}`)
      contentTag.style.opacity = 255


      const detailFormWrapper = document.querySelector(`#detail-form-wrapper-${this.identifier}-${this.propsMovie.id}`)
      detailFormWrapper.style.visibility = 'visible'
      

      

      // this.$parent.getModalXY(this.propsMovie.id)
      // const wrapperX = this.$store.state.modalXY.modalX
      // const wrapperY = this.$store.state.modalXY.modalY


      const wrapperX = detailFormWrapper.getBoundingClientRect().left
      const wrapperY = detailFormWrapper.getBoundingClientRect().top


      const detailForm = document.querySelector(`#detail-form-${this.identifier}-${this.propsMovie.id}`)
      
      // if (this.identifier.indexOf('-fade') !== -1) {
      //   setTimeout(() => {
      //     detailForm.style.opacity = 255
      //   }, 100);
      // }
      // if (this.identifier === 'background') {
      //   const button = document.querySelector('.background-movie-button')
      //   detailForm.style.opacity = 0
      //   detailForm.style.opacity = 255
      //   const buttonX = button.getBoundingClientRect().left
      //   const buttonY = button.getBoundingClientRect().top
      //   detailForm.style.left = (buttonX / window.innerWidth * 100) + 'vw'
      //   detailForm.style.top = (buttonY / window.innerHeight * 100) + 'vh'
      // } else {
      //   detailForm.style.left = (wrapperX / window.innerWidth * 100) + 'vw'
      //   detailForm.style.top = (wrapperY / window.innerHeight * 100) + 'vh'
      //   // detailForm.setAttribute('style', `width:${this.modalWidth}vw; height:${this.modalHeight}vh;  top:${wrapperY}px; left:${wrapperX}px;`)
        
      // }
      detailForm.style.left = (wrapperX / window.innerWidth * 100) + 'vw'
      detailForm.style.top = (wrapperY / window.innerHeight * 100) + 'vh'
      detailForm.style.visibility = 'visible'
      
      
      

      


      const size = {
        width: window.innerWidth || document.body.clientWidth,
        height: window.innerHeight || document.body.clientHeight 
      };


      const left = ((size.width / 2) - detailForm.getBoundingClientRect().left) - ((this.detailWidth) / 2)
      // const top = -detailForm.getBoundingClientRect().top
      const leftPer = left / document.body.offsetWidth * 100
      // const topPer = top / window.innerHeight * 100

      detailForm.style.width = this.detailWidth + 'px'
      detailForm.style.height = this.detailHeight + 'vh'
      
      detailForm.style.top = 0 + 'px'
      detailForm.style.transform = `translate( ${leftPer}vw , 0 )`


    },
    hideDetail() {
      if (this.identifier !== 'searchMovie') {
        const bodyTag = document.querySelector('body')
        bodyTag.style.overflowY = 'scroll'
      }
      
   
      const detailForm = document.querySelector(`#detail-form-${this.identifier}-${this.propsMovie.id}`)
      const detailFormWrapper = document.querySelector(`#detail-form-wrapper-${this.identifier}-${this.propsMovie.id}`)
      const fixedToggleForm = document.querySelector(`#fixed-toggle-form-${this.identifier}-${this.propsMovie.id}`)
      const wrapperX = detailFormWrapper.getBoundingClientRect().left;
      // const wrapperY = detailFormWrapper.getBoundingClientRect().top;

      const contentTag = document.querySelector(`#content-${this.identifier}-${this.propsMovie.id}`)
      contentTag.style.opacity = 0
      fixedToggleForm.style.backgroundColor = 'rgba(0, 0, 0, 0)'

      if (this.identifier.indexOf('-fade') !== -1) {
        setTimeout(() => {
          detailForm.style.opacity = 0
        }, 100);
      }
      // if (this.identifier === 'background') {
      //   const button = document.querySelector('.background-movie-button')
      //   const buttonX = button.getBoundingClientRect().left
      //   const buttonY = button.getBoundingClientRect().top
      //   detailForm.setAttribute('style', `width:${this.cardWidth}px; height:${this.cardHeight}px; left:${buttonX}px; top:${buttonY}px; opacity: 0;`)
      // } else {
      //   setTimeout(() => {
        
      //   detailForm.setAttribute('style', `width:${this.cardWidth}px; height:${this.cardHeight}px; left:${this.$store.state.cardXY.cardX}px; top:${this.$store.state.cardXY.cardY}px;`)
      //   }, 10);
      // }
      setTimeout(() => {
        
        detailForm.setAttribute('style', `width:${this.cardWidth}px; height:${this.cardHeight}px; left:${this.$store.state.cardXY.cardX}px; top:${this.$store.state.cardXY.cardY}px;`)
        }, 10);
      

      setTimeout(() => {
        detailFormWrapper.style.visibility = 'hidden'
        this.$store.commit('IS_DETAIL_MODE', false)
        // detailForm.setAttribute('style', `width:${this.modalWidth}vw; height:${this.modalHeight}vh;  top:${wrapperY}px; left:${wrapperX}px;`)
        // if (this.identifier !== 'background') {
        //   detailForm.setAttribute('style', `width:${this.modalWidth}px; height:${this.modalHeight}px; left:${wrapperX}px;`)
        // }
        detailForm.setAttribute('style', `width:${this.modalWidth}px; height:${this.modalHeight}px; left:${wrapperX}px;`)
        this.scrollValue = window.pageYOffset

        
        fixedToggleForm.style.display = 'none'
      }, 410);
      
    },

    selectTab(tabName) {
      const allSelected = document.querySelectorAll('.tab-selected')
      const allContent = document.querySelectorAll('.tab-content')
      allSelected.forEach((elem) => {
        if (elem.id !== `tab-selected-${tabName}-${this.identifier}-${this.propsMovie.id}`) {
          elem.style.opacity = 0
        }
        
      })
      allContent.forEach((elem) => {
        if (elem.id !== `tab-${tabName}-${this.identifier}-${this.propsMovie.id}`) {
          elem.style.position = 'absolute'
          elem.style.height = '0px'
          elem.style.opacity = 0
          setTimeout(() => {
            elem.style.display = 'none'
          }, 410);
        }
        
      })

      const selected = document.querySelector(`#tab-selected-${tabName}-${this.identifier}-${this.propsMovie.id}`)
      const content = document.querySelector(`#tab-${tabName}-${this.identifier}-${this.propsMovie.id}`)
      selected.style.opacity = 255
      content.style.position = 'static'
      content.style.display = 'block'
      content.style.height = 'auto'
      content.style.opacity = 255

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
    },

  },
  mounted() {
    const selected = document.querySelector(`#tab-selected-info-${this.identifier}-${this.propsMovie.id}`)
    selected.style.opacity = 255

    const content = document.querySelector(`#tab-info-${this.identifier}-${this.propsMovie.id}`)
    content.style.position = 'static'
    content.style.display = 'block'
    content.style.height = 'auto'
    content.style.opacity = 255

  }

}
</script>

<style>
  .detail-form-wrapper {
    
    
    cursor:default;
    width: 100%;
    height: 100%;
    position: absolute;

    /* background-color: rgba(43, 226, 64, 0.473); */

    
  }
  .fixed-toggle-form {
    left:0%;
    top:0%;
    width:100vw;
    height:100%;

    /* visibility: 'hidden'; */
    display: none;
    background-color: rgba(0, 0, 0, 0);
    /* opacity: 0; */
    transition-property: background-color opacity;;
    transition-duration: 0.4s;
    position:fixed;

    /* backdrop-filter: blur(10px); */
    
  }

  /* .relative-toggle-form {
    width:100vw;
    height:100vh;
    left: 0%;
    top: 0%;
    position: relative;
  } */

  .detail-form {
    width: 22vw;
    height: 48vh;
    background-color: rgb(10, 10, 10);
    position: fixed;
    visibility: hidden;

    transition-property: opacity width height transform left top 2s ease 0s;
    transition-duration: 0.4s;
    box-shadow: 0px 0px 5px 1px rgba(0, 0, 0, 0.700);
    user-select: none;
    overflow: scroll;
    overflow-x: hidden; 
    text-align: left;

  }



  .content {
    /* margin: 24px; */
    transition-property: opacity;
    transition-duration: 0.4s;
    opacity: 0%;
  }

  .detail-image {
    width:100%;
    height:auto;
  }

  .detail-profile-image {
    width: 60px;
    height: auto;
    border-radius: 10px;
  }

  .detail-title {
    margin:24px;
    font-size: 32px;;
    width: 592px;
    
  }

  .tab {
    display: flex;
    width:100%;
    height:48px;
    
  }

  .tab-button {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100px;
    height: 100%;
    position: relative;
    cursor: pointer;
    transition-property: color;
    transition-duration: 0.4s;
    color: rgb(150, 150, 150);
    /* background-color: rgba(30, 30, 30); */

  }

  .tab-button:hover {
    background-color: rgba(20, 20, 20);
  }

  .tab-selected {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    width:100%;
    height:100%;
    color: white;
    background-color: rgba(30, 30, 30);
    opacity: 0;
    transition-property: opacity;
    transition-duration: 0.4s;
    
  }
  .tab-content-wrapper {
    width:100%;
    height:auto;
    position:relative;
  }
  .tab-content {
    position:absolute;
    width:100%;
    height: 0px;
    background-color: rgba(30, 30, 30);
    padding:24px;
    display: none;
    opacity: 0;
    transition-property: opacity height;
    transition-duration: 0.4s;
    
  }


  .detail-genre-decorator {
    border-radius: 20px;
    display: inline-block;
    margin-left: 5px;
    margin-right: 5px;
    padding: 6px 15px 6px 15px ;
    background-color: rgb(50, 50, 50);
    box-shadow: 0px 0px 5px 1px rgba(0, 0, 0, 0.200);

  }

  .detail-overview {
    width: 752px;
    
  }

  .additional-info-wrapper {
    width:100%;
    display: flex;
    /* flex-direction: column; */
    justify-content: space-between;
    align-items: center;
  }
     
  .rating-zone-wrapper {
    /* padding: 48px; */
    width:100%;
    display: flex;
    /* flex-direction: column; */
    justify-content: space-between;
    align-items: center;
  }

  .temp {
    margin-top: 16px;
    width:100%;
    height: auto;
    background-color: rgba(255, 255, 255, 0.07);

  }

  .detail-button-wrapper {

    display: flex;
    justify-content: center;
    margin-top: 15px;
  }
  .dislike-button {
    margin-right: 7px;
  margin-left: 7px;
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

    margin-right: 7px;
    margin-left: 7px;
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


  .add-favorite-button{

    margin-right: 7px;
  margin-left: 7px;
    display: inline-block;
    cursor: pointer;
    color: rgb(150, 150, 150);
    transition-duration: 0.5s;
    transition-property: color;
  }
  .add-favorite-button:hover {
    color: rgb(240, 240, 240);
  }

  .hide-button {
    
    position: absolute;
    top: 2vh;
    left: 1vw;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 30px;;
    box-shadow: 0px 0px 5px 1px rgba(0, 0, 0, 0.200);
  }


  .hide-icon {
    transition-duration: 0.5s;
    transition-property: opacity color;
    color: rgba(255, 255, 255, 0.7);
    cursor: pointer;
  }
  .hide-icon:hover {
    color: rgba(255, 255, 255, 1);
  }

  
  
</style>