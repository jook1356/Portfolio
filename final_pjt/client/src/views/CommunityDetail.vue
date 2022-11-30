<template>
  <div class="background-blur">
    <div class="v-box">
      <div class="detail-block" :style="`min-height:${detailBoxMinHeight}vh;`">
        <div> 
          <p class="username">{{ review?.user.nickname }}</p>
          <h1 class="title">{{ review?.title }}</h1>
          <div style="line-height:1;" v-if="review?.movie" class="mb-4">
            <star-rating :star-size="19"
              :increment="0.5"
              :show-rating="true" :animate="true"
              :rating="review?.vote"
              :read-only="true"
              :active-color="['#9D0102','#9D0102']" :active-border-color="['#F6546A','#C3B1B1']" :border-width="2" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]" :active-on-click="true" :clearable="true" >
            </star-rating>
          </div>
          <div class="detail-content">{{ review?.content }}</div>
          <div class="icon-and-update">
            <div class="icon">
              <div class="icon-item heart-box" @click.stop="clickHeart" v-if="userInfo">
                <i v-if="isliked" class="bi bi-heart-fill heart" @click.stop="clickHeart" :id="`heart-icon-detail-${review?.id}`"></i>
                <i v-else class="bi bi-heart heart" @click.stop="clickHeart" :id="`heart-icon-detail-${review?.id}`"></i>
                <span>{{ like_users_count }}</span>
              </div>
              <div class="icon-item" v-else>
                <i class="bi bi-heart heart"></i>
                <span>{{ like_users_count }}</span>
              </div>
              <div class="icon-item">
                <i class="bi bi-eye" style="color: #98A4B7; font-size: 1rem"></i> 
                <span>{{ visit_count }}</span>
              </div>
            </div>
            <div v-if="userInfo?.id === review?.user.id">
              <button @click="deleteReview" class="update-review-btn">게시글 삭제</button>
              <button @click="updateReview(id)" class="update-review-btn">게시글 수정</button>
            </div>
          </div>
          <div v-if="movie" class="movie-block">
            <hr>
            <h6 style="margin: 0px 10px 15px 12px;">{{ review?.user.nickname }}님이 게시글에 연결한 영화</h6>
            <!-- 영화 디테일 페이지 연결할 부분 -->
            <div class="movie-box" style="position:relative;">
              
              <img class="movie-poster" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`">
              <CommunityMovieDetailAdapter :movie="movie" :identifier="identifier"/>
              <div class="movie-info">
                
                <span class="main-info">{{ movie.title }}</span>
                <span class="sub-info">{{ movie.released_date }}</span>
                <span class="sub-info">{{ Math.round(movie.vote_average * 10) / 10 }}  /  5</span>
              </div>
            </div>
            <!--         끝               -->
          </div>
        </div>
        <hr>
        <div>
          <p style="font-size: 1.3rem; font-weight: 200;">댓글 {{ comments.length }}</p>
          <div v-if="comments.length">
            <div v-for="(comment, idx) in comments" :key="comment.id" class="comment-box">
              <div style="padding: 0px 10px 0px 10px;">
                <p class="username" style="margin-bottom: 7px">{{ comment?.user.nickname }}</p>
                <div :id="`comment-block-${comment.id}`" class="comment-content">
                  <p style="margin-bottom: 5px">{{ comment?.content }}</p>
                  <div v-if="userInfo?.id === comment?.user.id">
                    <button @click="showUpdateForm(comment)" class="update-review-btn">수정</button>
                    <button @click="deleteComment(comment, idx)" class="update-review-btn">삭제</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="non-chat">
            <span class="non-chat-icon"><i class="bi bi-chat-dots-fill"></i></span>
            <span class="non-chat-msg">댓글이 없습니다.</span>
          </div>
        </div>
        <div class="form-box" id="comment-create-form-box">
          <form id="comment-form" @submit.prevent="createComment" class="form" v-if="userInfo">
            <textarea class="comment-input" v-model="content" placeholder="댓글을 작성해주세요." rows="1" @input="resizeTextarea"></textarea>
            <button class="comment-btn">작성</button>
          </form>
          <form id="comment-form" @submit.prevent="createComment" class="form" v-else>
            <textarea class="comment-input" v-model="content" placeholder="로그인이 필요한 서비스입니다. " rows="1" @input="resizeTextarea" disabled></textarea>
            <button class="disabled-comment-btn">작성</button>
          </form>
        </div>
        <div class="form-box noshow" id="comment-update-form-box">
          <form class="form" @submit.prevent="updateComment($event)" id="comment-update-form">
            <textarea class="comment-input" @input="resizeTextarea" rows="1" type="text"></textarea>
            <button class="comment-update-btn">수정</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
import CommunityMovieDetailAdapter from '@/components/CommunityMovieDetailAdapter'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityDetail',
  components: {
    StarRating,
    CommunityMovieDetailAdapter,
  },
  data() {
    return {
      id: this.$route.params["id"],
      review: null,
      content: null,
      comments: [],
      isliked: false,
      movie: null,
      backgroundImangeUrl: "https://image.tmdb.org/t/p/original/t3LicFpYHeYpwqm7L5wDpd22hL5.jpg",
      like_users_count: null,
      visit_count: null,
      update_target_comment: null,
      identifier: 'communityDetail-fade'
    }
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo
    },
    detailBoxMinHeight() {
      return 100 - (122 /screen.availHeight * 100)
    }
  },
  methods: {
    getReview() {
      axios({
        method: 'get',
        url: `${API_URL}/community/review/${this.id}`
      })
        .then((res) => {
          this.review = res.data
          // 방문횟수랑 좋아요 개수 가지고 변수에 할당해주기
          this.visit_count = res.data.visit_set[0].count
          this.like_users_count = res.data.like_users.length
          const like_users = res.data.like_users
          if (this.userInfo) {
            for (const user of like_users) {
              if (user.username === this.userInfo.username) {
                this.isliked = true
                break
              }
            }
          }
          if (res.data.movie) {
            axios({
              method: 'GET',
              url: `${API_URL}/movies/movie_detail/${res.data.movie.id}/`
            })
              .then((res) => {
                this.movie = res.data
              })
              .catch((err) => {
                console.log(err)
              })
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    back() {
      this.$router.go(-1)
    },
    createComment(event) {
      const content = this.content
      axios({
        method: 'post',
        url: `${API_URL}/community/comment/create/`,
        data: {
          content,
          review: this.review.id
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.comments.push(res.data)
          const textareaTag = document.querySelector('.comment-input')
          textareaTag.style.height = '28px'
        })
        .catch((err) => {
          console.log(err)
        })
      this.content = null
      event.target.reset()
    },
    getComment() {
      axios({
        method: 'get',
        url: `${API_URL}/community/comment/list/${this.id}/`,
      })
        .then((res) => {
          this.comments = [
            ...this.comments,
            ...res.data,
          ]
        })
        .catch((err) => {
          console.log(err)
        })
    },
    clickHeart() {
      // 사용자가 좋아요를 누른 경우, 좋아요 정보를 업데이트하는 axios요청을 보내는 함수
      axios({
        method: 'post',
        url: `${API_URL}/community/review/like/${this.review.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          const heartTag = document.querySelector(`#heart-icon-detail-${this.review.id}`)
          heartTag.classList.toggle('bi-heart-fill')
          heartTag.classList.toggle('bi-heart')
          this.isliked = res.data.result
          if (this.isliked) {
            this.like_users_count += 1
          } else {
            this.like_users_count -= 1
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    getHeart(){
      // 사용자가 좋아요를 누른 상태인지 아닌지 정보를 가지고 와서 isliked에 저장 하는 함수
      axios({
        method: 'get',
        url: `${API_URL}/community/review/like/${this.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          const like_users = res.data.like_users
          for (const user of like_users) {
            if (user.username === this.userInfo.username) {
              this.isliked = true
              break
            }
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReview(){
      axios({
        method: 'DELETE',
        url: `${API_URL}/community/review/${this.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          if (this.review.movie) {
            const movieId = this.review.movie.id
            axios({
              method: 'GET',
              url: `${API_URL}/movies/update_movie_vote/${movieId}/`
            })
            .then((res) => {
              const vote_count = res.data.vote_count - 1
              const vote_average = (res.data.vote_average * res.data.vote_count - this.review.vote) / vote_count
              axios({
                method: 'POST',
                url: `${API_URL}/movies/update_movie_vote/${movieId}/`,
                data: {
                  vote_average,
                  vote_count
                }
              })
                .catch((err) => {
                  console.log(err)
                })
            })
          }
          this.$router.push({name: 'community'})
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateReview(id) {
      this.$router.push({name: 'update', params: {id: id}})
    },
    deleteComment(comment, idx) {
      axios({
        method: 'DELETE',
        url: `${API_URL}/community/comment/${comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.comments.splice(idx, 1)
        })
        .catch(err => {
          console.log(err)
        })
    },
    showUpdateForm(comment) {
      const updateForm = document.querySelector(`#comment-update-form-box`)
      const createForm = document.querySelector(`#comment-create-form-box`)
      const inputTag = updateForm.childNodes[0].childNodes[0]
      inputTag.value = comment.content
      updateForm.classList.toggle('noshow')
      createForm.classList.toggle('noshow')
      inputTag.style.height = `${inputTag.scrollHeight}px`
      this.update_target_comment = comment
    },
    updateComment(event) {
      const inputTag = event.target.childNodes[0]
      const content = inputTag.value
      axios({
        method: 'put',
        url: `${API_URL}/community/comment/${this.update_target_comment.id}/`,
        data: {
          content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() =>{
          this.update_target_comment.content = content
          const updateForm = document.querySelector(`#comment-update-form-box`)
          const createForm = document.querySelector(`#comment-create-form-box`)
          updateForm.classList.toggle('noshow')
          createForm.classList.toggle('noshow')
          this.update_target_comment = null
        })
        .catch((err) => {
          console.log(err)
        }) 
    },
    countVisit() {
      axios({
        method: 'GET',
        url: `${API_URL}/community/comment/visit/${this.id}/`,
      })
        .then((res) => {
          axios({
            method: 'put',
            url: `${API_URL}/community/comment/visit/${this.id}/`,
            data: {
              count: res.data.count + 1
            }
          })
            .catch((err) => {
              console.log(err)
            })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    resizeTextarea(event) {
      event.target.style.height = 'auto'
      event.target.style.height = `${event.target.scrollHeight}px`
    },
  },
  created() {
    this.$store.commit('IS_DETAIL_MODE', false)
    this.getReview()  // 게시글 정보 가지고 오기
    this.getComment()  // 댓글 정보 가지고 오기
    this.countVisit()  // 조회수 세기
  },
}
</script>

<style scoped>

.detail-block {
  background-color: #282828;
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 56px;
  margin-top: 30px;
  padding: 25px 30px 81px 30px;
  text-align: left;
}

.back-btn {
  appearance: none;
}

.back-icon {
  font-size: 1.5rem;
}

.comment-form {
  position: fixed;
  bottom: 0px;
}

#heart {
  color: red;
}

.comment-box {
  border-bottom: 0.5px solid gray;
  margin-bottom: 20px;
}

.noshow {
  display: none;
}

.username {
  font-size: 0.8rem;
  font-weight: 500;
}

.title {
  font-size: 2rem;
  font-weight: 300;
  margin-bottom: 15px;
}

.detail-content {
  font-weight: 200;
  line-height: 28px;
  margin-bottom: 35px;
}


.icon-item {
  border: solid 1px #98A4B7;
  width: 45px;
  height: 25px;
  border-radius: 20px;
  margin-right: 5px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 3px 0px 3px 0px;
  font-size: 0.5rem;
}

.icon-item > span {
  margin-left: 7px;
}

.heart{
  color: #9D0102;
}

.icon {
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
}

.heart-box {
  outline: solid 2px #282828;
  transition-duration: 0.3s;
}

.heart-box:hover {
  cursor: pointer;
  border: solid 1px rgba(255, 0, 0, 0.233);
  outline: solid 2px rgba(255, 0, 0, 0.233);
  
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
  background-color: #383838;
  border-radius: 10px;
  padding: 8px 10px 8px 10px;
  margin: 0px 10px 0px 10px;
  border: solid 1px #383838;
  outline: solid 2px #383838;
  transition-duration: 0.3s;
}

.movie-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: space-between;
  padding-left: 8px;
}

.movie-box:hover {
  cursor: pointer;
  /* transform: scale(1.01); */
  border: solid 1px rgba(255, 0, 0, 0.233);
  outline: solid 2px rgba(255, 0, 0, 0.233);
  
}

.main-info {
  margin-bottom: 10px;
}

.sub-info {
  font-size: 0.7rem;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.692);
}

.update-review-btn {
  appearance: none;
  border: none;
  font-size: 0.7rem;
  font-weight: 500;
  background-color: #282828;
  color: rgba(255, 255, 255, 0.575);
  border: solid 1px #282828;
  transition-duration: 0.3s;
}

.update-review-btn:hover {
  border-top: solid 1px #9d0101c0;
  border-bottom: solid 1px #9d0101c0;
  
}

.icon-and-update {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.form-box {
  position: fixed;
  width: 800px;
  margin-left: -30px;
  bottom: 0px;
  background-color: #383838;
  padding: 5px 10px 5px 10px;
}

.form {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 5px 10px 5px 10px;
}


.comment-input {
  background-color: #383838;
  width: 90%;
  height: 28px;
  border: none;
  color: white;
  resize: none;
  overflow: visible;
  font-size: 1rem;
  font-weight: 300;
}

.update-input {
  resize: none;
  overflow: visible;
}

.update-input:focus { 
  outline: none; 
}

.comment-input::placeholder {
  font-size: 1rem;
  font-weight: 600;
  align-content: center;
}

.comment-input:focus { 
  outline: none;  
}

.comment-btn {
  appearance: none;
  border-radius: 7px;
  color: rgb(173, 171, 171);
  background-color: #282828;
  font-size: 1rem;
  font-weight: 400;
  padding: 6px 16px 6px 16px;
  border: none;
  transition-duration: 0.3s;
}

.disabled-comment-btn{
  appearance: none;
  border-radius: 7px;
  color: rgb(173, 171, 171);
  background-color: #282828;
  font-size: 1rem;
  font-weight: 400;
  padding: 6px 16px 6px 16px;
  border: none;
}

.comment-update-btn {
  appearance: none;
  border-radius: 7px;
  color: rgb(221, 217, 217);
  background-color: #9d0101b2;
  font-size: 1rem;
  font-weight: 400;
  padding: 6px 16px 6px 16px;
  border: solid 1px #383838;
  outline: solid 2px #383838;
  transition-duration: 0.2s;
}

.comment-update-btn:hover {
  border: solid 1px rgba(255, 0, 0, 0.233);
  outline: solid 2px rgba(255, 0, 0, 0.233);
  
}

.comment-btn:hover {
  background-color: #9d0101b2;
  color: rgb(221, 217, 217);
  
}

.non-chat {
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  color: #535353;
}

.non-chat-icon {
  font-size: 4rem;
}

.non-chat-msg {
  font-size: 1rem;
  font-weight: 700;
}

.comment-content {
  font-weight: 200;
  padding: 0px 0px 15px 0px;
}

</style>