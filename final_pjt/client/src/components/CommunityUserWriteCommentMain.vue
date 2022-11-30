<template>
  <div class="listBox"> 
    <h1>{{ userInfo.nickname }}님이 작성한 댓글</h1>
    <hr style="width: 800px; margin: 0px 0px 25px 0px;">
    <CommunityMainCommentList :comments="comments"/>
  </div>
</template>

<script>
import CommunityMainCommentList from "@/components/CommunityMainCommentList"
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityUserWriteCommentMain',
  data() {
    return {
      comments: []  
    }
  },
  components: {
    CommunityMainCommentList,
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
    get_comments() {
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/comment/${this.userInfo.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.comments = [
            ...res.data
          ]
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.get_comments()
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