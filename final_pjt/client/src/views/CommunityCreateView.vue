<template>
  <div class="background-blur">
    <div class="myModal noshow">
      <div class="ModalInnerbox">
        <div class="header">
          <button class="close-btn" style="color: #282828;">X</button>
          <h1 style="font-size: 2rem; font-weight: 400; margin: 0px;">영화 검색</h1>
          <button @click="closeModal" class="close-btn">X</button>
        </div>
        <div class="movie-search-input-box">
          <input type="text" @keyup.enter="getMovie" v-model="searchWord" class="movie-search-input" placeholder="영화를 검색해주세요">
        </div>
        <!-- 영화 카드 -->
        <div v-if="searchMovieList">
          <div class="movie-box" v-for="movie in searchMovieList" :key="movie.id" @click="selectMovie(movie)">
            <img class="movie-poster" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`">
            <div class="movie-info">
              <span class="main-info">{{ movie.title }}</span>
              <span class="sub-info">{{ movie.released_date }}</span>
              <span class="sub-info">{{ Math.round(movie.vote_average * 10) / 10 }}  /  5</span>
            </div>
          </div>
        </div>
        <!-- 영화 카드 end -->
      </div>
    </div>
    <div class="create-box">
      <h1 class="headline">게시글 작성하기</h1>
      <form @submit.prevent="createReview">
        <div class="textarea-box title-input-box">
          <textarea rows="1" placeholder="제목을 입력해주세요" v-model="title" maxlength="100" class="title-input" @input="resizeTextarea"></textarea>
        </div>
        <div class="textarea-box content-input-box">
          <textarea v-model="content" class="content-input" placeholder="본문을 입력해주세요" @input="resizeTextarea" rows="1"></textarea>
        </div>
        <div class="movie-and-rating">
          <div>
            <div @click="openModal" class="movie-hash"><i class="bi bi-hash" style="font-size: 1.2rem;"></i><span id="selectedMovie"></span></div> <span class="movie-choose-msg" id="movie-msg">영화를 선택해주세요</span>
          </div>
          <div style="line-height:1; display:flex; flex-direction: row; align-items: center;" v-if="movie">
            <star-rating :star-size="23" :increment="0.5" :show-rating="false" :animate="true" :active-color="['#9D0102','#9D0102']" :active-border-color="['#F6546A','#C3B1B1']" :border-width="2" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]" :active-on-click="true" :clearable="true" v-model="vote"></star-rating><span style="margin-left: 7px;" class="movie-choose-msg" v-if="!vote">평점을 선택해주세요</span>
          </div>
        </div>
        <button class="create-btn">제출</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityCreateView',
  components: {
    StarRating,
  },
  data() {
    return {
      title: null,
      content: null,
      vote: null,
      movie: null,
      searchWord: null,
      searchMovieList: [],
    }
  },
  methods: {
  createReview() {
    const API_URL = "http://127.0.0.1:8000"
    const title = this.title
    const content = this.content
    const vote = this.vote
    axios({
      method: 'post',
      url: `${API_URL}/community/review/create/`,
      data: {
        title,
        content,
        vote,
        movieId: this.movie?.id
      },
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      }
    })
      .then((res) => {
        axios({ // 조회수 초기화 해주는 요청
          method: 'POST',
          url: `${API_URL}/community/comment/visit/${res.data.id}/`,
          data: {
            count: 0
          }
        })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
        if (this.movie) {
          const vote_count = this.movie.vote_count + 1
          const vote_average = (this.movie.vote_average * this.movie.vote_count + this.vote) / vote_count
          axios({
            method: 'POST',
            url: `${API_URL}/movies/update_movie_vote/${this.movie.id}/`,
            data: {
              vote_average, 
              vote_count
            }
          })
            .then((res) => {
              console.log(res)
            })
            .catch((err) => {
              console.log(err)
            })
        }
      })
      .then(() => {
        this.$router.push({name: 'community'})
      })
      .catch((err) => {
        console.log(err)
      })
    }, 
    openModal() {
      const modalTag = document.querySelector('.myModal')
      modalTag.classList.remove('noshow')
      const bodyTag = document.querySelector('body')
      bodyTag.style.overflowY = 'hidden'
      
    },
    closeModal() {
      const bodyTag = document.querySelector('body')
      bodyTag.style.overflowY = 'scroll'
      const modalTag = document.querySelector('.myModal')
      modalTag.classList.add('noshow')
    },
    getMovie() {
      const searchWord = this.searchWord
      if (!searchWord) {
        this.searchMovieList = []
        return
      }
      axios({
        method: 'get',
        url: `${API_URL}/movies/get_search_movies/`,
        params: {
          searchWord
        },
      })
        .then((res) => {
          if (res.data.length > 10){
            this.searchMovieList = res.data.slice(0, 11)
          } else {
            this.searchMovieList = res.data
          }
          this.searchWord = null
        })
        .catch((err) => {
          console.log(err)
        })
    },
    selectMovie(movie) {
      this.movie = movie
      const pTag = document.querySelector('#selectedMovie')
      pTag.innerText = this.movie.title
      const spanTag = document.querySelector('#movie-msg')
      spanTag.innerText = null
      const modalTag = document.querySelector('.myModal')
      modalTag.classList.add('noshow')
      this.searchWord = null
      this.searchMovieList = []
    },
    resizeTextarea(event) {
      event.target.style.height = 'auto'
      event.target.style.height = `${event.target.scrollHeight}px`
    },
  }
}
</script>

<style scoped>
.create-box {
  background-color: #282828;
  width: 700px;
  border-radius: 10px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 30px;
  padding: 30px;
}

.myModal {
  background: rgba(0, 0, 0, 0.767);
  position: fixed;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
  z-index: 999;
  display: flex;
  justify-content: center;
  align-items: center;
}

.ModalInnerbox {
  background-color: #282828;
  width: 630px;
  height: 700px;
  border-radius: 20px;
  padding: 30px;
  overflow-x:hidden;
  overflow-y:scroll;
}

.ModalInnerbox{
  -ms-overflow-style: none;
}
.ModalInnerbox::-webkit-scrollbar{
  display:none;
}

.header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}


.headline {
  font-weight: 300;
  font-size: 2rem;
  margin-bottom: 20px;
}

.noshow {
  display: none;
}

.title-input {
  border: 0px;
  background-color: #282828;
  color: white;
  font-size: 1rem;
  font-weight: 100;
  overflow: visible;
  resize: none;
  width: 100%;
}

.title-input::placeholder {
  font-weight: 400;
}

.title-input:focus { 
  outline: none;  
}

.title-input-box {
  border-bottom: solid 1px rgba(255, 255, 255, 0.397);
  padding: 5px 2px 3px 2px;
}

.content-input {
  min-height: 400px;
  border: 0px;
  background-color: #282828;
  font-size: 1rem;
  font-weight: 100;
  color: white;
  resize: none;
  overflow: hidden;
  width: 100%;
}

.content-input::placeholder {
  font-weight: 400;
}

.content-input:focus { 
  outline: none;
}

.content-input-box {
  padding: 10px 2px 3px 2px;
}

.movie-hash {
  display: inline-block;
  border: solid 1px white;
  border-radius: 20px;
  padding: 2px 10px 2px 10px;
  outline: solid 2px #282828;
  margin-right: 5px;
  margin-bottom: 15px;
}

.movie-hash:hover {
  cursor: pointer;
  transform: scale(1.07);
  transition-duration: 0.2s;
  border: solid 1px #9d01018f;
  outline: solid 2px #9d010144;
}

.textarea-box {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}

.movie-and-rating {
  width: 90%;
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-items: flex-start;
  margin-left: auto;
  margin-right: auto;
  padding: 20px 2px 20px 2px;
  /* border-bottom: solid 1px rgba(255, 255, 255, 0.397); */
  /* border-top: solid 1px rgba(255, 255, 255, 0.397); */
}

.movie-choose-msg {
  font-weight: 200;
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.63);
}

.create-btn {
  appearance: none;
  width: 90%;
  padding: 10px 0px 10px 0px;
  border: none;
  border-radius: 10px;
  color: white;
  background-color: #9d0101b2;
}

.close-btn {
  appearance: none;
  background-color: #282828;
  color: white;
  font-weight: 400;
  border: none;
  font-size: 1.8rem;
}

.close-btn:hover {
  color: #9D0102;
  font-weight: 600;
  transition-duration: 0.2s;
}

.movie-search-input {
  appearance: none;
  border: none;
  background-color: #282828;
  color: white;
  width: 100%;
  font-weight: 200;
}

.movie-search-input:focus {
  outline: none;
}

.movie-search-input::placeholder {
  font-weight: 500;
}

.movie-search-input-box {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  margin-bottom: 20px;
  border-bottom: solid 1px rgba(255, 255, 255, 0.336);
  padding: 5px 2px 5px 2px;
}

.movie-poster {
  border-radius: 4px;
  width: 50px;
}

.movie-box {
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
  background-color: #444343;
  border-radius: 10px;
  padding: 8px 10px 8px 10px;
  margin: 0px 10px 20px 10px;
  border: solid 1px #383838;
  outline: solid 2px #444343;
  transition-duration: 0.3s;
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}

.movie-info {
  display: flex;
  flex-direction: column;
  justify-content: start;
  align-content: space-between;
  padding-left: 8px;
}

.movie-box:hover {
  cursor: pointer;
  transform: scale(1.05);
  border: solid 1px rgba(255, 0, 0, 0.233);
  outline: solid 2px rgba(255, 0, 0, 0.233);
}

.main-info {
  margin-bottom: 10px;
}

.sub-info {
  display: inline;
  font-size: 0.7rem;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.692);
}

</style>
