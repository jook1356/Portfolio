<template>
  <div class="itemBox">
    <p class="username">{{ review?.user.nickname }}</p>
    <h3 class="title">{{ review?.title }}</h3>
    <div id="content">
      {{ review?.content }}
    </div>
    <div v-if="review.movie" class="movie"><i class="bi bi-camera-video-fill"></i> {{ review?.movie.title }}</div>
    <div class="icon">
      <div class="icon-item heart-box" @click.stop="clickHeart" v-if="userInfo">
        <i v-if="isliked" class="bi bi-heart-fill heart" @click.stop="clickHeart" :id="`heart-icon-${review.id}`"></i>
        <i v-else class="bi bi-heart heart" @click.stop="clickHeart" :id="`heart-icon-${review.id}`"></i>
        <span>{{ like_users_cnt }}</span>
      </div>
      <div class="icon-item" v-else>
        <i class="bi bi-heart heart"></i>
        <span>{{ like_users_cnt }}</span>
      </div>
      <div class="icon-item">
        <i class="bi bi-eye" style="color: #98A4B7; font-size: 1rem"></i> 
        <span>{{ review?.visit_set[0].count }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityMainArticleListItem',
  data() {
    return {
      isliked: false,
      like_users_cnt: this.review.like_users.length
    }
  },
  props: {
    review: Object,
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo
    }
  },
  methods: {
    getHeart(){
      for (const user of this.review.like_users) {
        if (user.username === this.userInfo.username) {
          this.isliked = true
          break
        }
      }
    },

    clickHeart() {
      axios({
        method: 'post',
        url: `${API_URL}/community/review/like/${this.review.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          const heartTag = document.querySelector(`#heart-icon-${this.review.id}`)
          heartTag.classList.toggle('bi-heart-fill')
          heartTag.classList.toggle('bi-heart')
          this.isliked = res.data.result
          if (this.isliked) {
            this.like_users_cnt += 1
          } else {
            this.like_users_cnt -= 1
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    this.getHeart()
  },
}
</script>

<style scoped>


.itemBox {
  width: 800px;
  background-color: #282828;
  border-radius: 10px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 20px;
  padding: 20px;
  text-align: left;
  transition: all 0.2s linear;
}

.itemBox:hover {
  transform: scale(1.02);
  cursor: pointer;
}

.heart{
  color: #9D0102;
}

.username {
  font-weight: 600;
  font-size: 0.8rem;
}

.title {
  font-weight: 500;
  font-size: 1.5rem;
}

#content {
  font-weight: 100;
  margin-bottom: 30px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}

.movie {
  display: inline-block;
  color: #98A4B7;
  border: solid 1px #98A4B7;
  border-radius: 30px;
  padding: 8px 16px 8px 16px;
  font-size: 0.8rem;
  font-weight: 500;
  margin-bottom: 20px;
  background-color: #282828;
}

.icon {
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
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

.heart-box {
  outline: solid 2px #282828;
  transition-duration: 0.3s;
}

.heart-box:hover {
  cursor: pointer;
  border: solid 1px rgba(255, 0, 0, 0.233);
  outline: solid 2px rgba(255, 0, 0, 0.233);
}
</style>