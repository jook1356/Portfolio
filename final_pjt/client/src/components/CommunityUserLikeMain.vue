<template>
  <div class="listBox">
    <h1>{{ userInfo.nickname }}님이 좋아요 한 게시글</h1>
    <hr style="width: 800px; margin: 0px 0px 25px 0px;">
    <CommunityMainArticleList :reviews="reviews"/>
  </div>
</template>

<script>
import CommunityMainArticleList from "@/components/CommunityMainArticleList"
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityUserLikeMain',
  data() {
    return {
      reviews: []  
    }
  },
  components: {
    CommunityMainArticleList,
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo
    }
  },
  methods: {
    moveTop() {
      window.scrollTo({top:0, left:0, behavior:'auto'})
    },
    get_like_reviews() {
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/like_reviews/${this.userInfo.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.reviews = [
            ...res.data
          ]
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.get_like_reviews()
  }
}
</script>

<style scoped>
.noshow {
  display: none;
}
.listBox {
  display: flex;
  flex-direction: column;
  align-items: center;
}

</style>