<template>
  <div style="z-index:9999;">
    <div class="block user-block">
      <div class="profile">
        <!-- <div class="profile-image">
        </div> -->
        <i class="bi bi-person-circle person"></i>
        <span v-if="userInfo">{{ userInfo?.nickname }}</span>
        <span v-else>Anonymous</span>
      </div>
      <div v-if="userInfo" class="user-item-box">
        <div @click="goLikeReviews" class="user-item">
          <span>좋아요</span> 
          <span>{{ like_reviews_cnt }}</span>
        </div>
        <div class="line"></div>
        <div @click="goReviews" class="user-item">
          <span>게시글</span> 
          <span>{{ reviews_cnt }}</span> 
        </div>
        <div class="line"></div>
        <div @click="goComments" class="user-item">
          <span>댓글</span> 
          <span>{{ comments_cnt }} </span> 
        </div>
      </div>
      <div v-else>
        로그인이 필요한 서비스입니다.  
      </div>
    </div>
    <div class="block movie-block">
      <h5 class="movie-head">인기 영화 순위</h5>
      <hr style="width: 250px; margin-left: auto; margin-right: auto; margin-bottom:6px;">
      <ul >
        <li v-for="(movie, idx) in popularMovies" :key="movie.id" class="highlight" :id="`li-${movie.id}`">
          
          <span class="movie-rank">{{ idx + 1 }}.</span>
          <span class="movie-title">{{ movie.title }}</span>
          <span class="movie-genre">{{ movie.main_genre.name }}</span>
          <CommunityMovieDetailAdapter :movie="movie" :identifier="identifier"/>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommunityMovieDetailAdapter from '@/components/CommunityMovieDetailAdapter'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunitySidebar',
  components: {
    CommunityMovieDetailAdapter,
  },
  data() {
    return {
      comments_cnt: null,
      reviews_cnt: null,
      like_reviews_cnt: null,
      popularMovies: [],
      identifier: 'sidebarMovie-fade',
    }
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo
    }
  },
  methods: {
    getcommand() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/comment/${this.userInfo.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(res => {
          this.comments_cnt = res.data.length
        })
        .catch(err => {
          console.log(err)
        })
    },
    getReviews() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/reviews/${this.userInfo.id}/`
      })
        .then((res) => {
          this.reviews_cnt = res.data.length
        })
        .catch(err => {
          console.log(err)
        })
    },
    getLikeReviews() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/like_reviews/${this.userInfo.id}/`
      })
        .then((res) => {
          this.like_reviews_cnt = res.data.length
        })
        .catch(err => {
          console.log(err)
        })
    },
    goLikeReviews(){
      this.$router.push({name: 'community_user_like'})
    },
    goReviews() {
      this.$router.push({name: 'community_user_reviews'})
    },
    goComments() {
      this.$router.push({name: 'community_user_comments'})
    },
    getPopularMovie() {
      axios({
        method: 'GET',
        url: `${API_URL}/movies/get_top_rated_movies/`,
      })
        .then((res) => {
          this.popularMovies = res.data.splice(0, 10)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.$store.commit('IS_DETAIL_MODE', false)
    if (this.userInfo) {
      this.getcommand()
      this.getReviews()
      this.getLikeReviews()
    }
    this.getPopularMovie()
  }
}
</script>

<style scoped>
i {
  font-size: 30px;
}


.user-block {
  padding: 20px 0px 20px 0px;
  margin-bottom: 25px;
}

.movie-block {
  padding: 20px 0px 20px 0px;

}

.profile {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.person {
  padding: 5px;
}

.user-item-box {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.user-item {
  display: flex;
  flex-direction: column;
  padding-left: 15px;
  padding-right: 15px;
  transition: all 0.2s linear;
  font-weight: 500;
  border-bottom: solid 3px #282828;
}

.user-item:hover {
  cursor: pointer;
  /* transform: scale(1.05); */
  border-bottom: solid 3px #9d01017e;
}

.line {
  border-left: solid 2px #242323;
}

ul {
  list-style:none;
  text-align: left;
  margin: 0px;
  padding: 0px
}

li {
  padding: 10px 0px 10px 7px;
  width: 250px;
  border-bottom: solid 1px #242323;
  margin-left: auto;
  margin-right: auto;
  position: relative;

}

li::after {
  content: "";
  display: inline-block;
  height: 100%;
  width: 0%;
  border-bottom: solid 2px #9d01019f;
  /* z-index: -1; */
  position: absolute;
  left: 0px;
  top: 0px;
}

li:hover::after {
  content: "";
  display: inline-block;
  height: 100%;
  width: 100%;
  border-bottom: solid 2px #9d01019f;
  /* z-index: -1; */
  position: absolute;
  left: 0px;
  top: 0px;
  transition: 0.6s all;
}

li:hover {
  cursor: pointer;
  /* transform: scale(1.02); */
}

.movie-block {
  z-index: -2;
}

.movie-title {
  margin: 0px 7px 0px 7px;
}

.movie-genre {
  border: solid 1px #98A4B7;
  border-radius: 20px;
  font-size: 0.7rem;
  padding: 3px 4px 3px 4px;
  color: #98A4B7;
}
</style>