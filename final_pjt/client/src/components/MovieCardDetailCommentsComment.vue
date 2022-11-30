<template>
  <li class="comment-li">
    
    
    <div style="display:flex; align-items:center; justify-content:space-between; margin-top:10px; margin-bottom:10px; padding-right:32px;">
      <div>
        <span><b>{{comment.user.nickname}}</b></span>
        <span style="margin-left:10px; font-size:14px; color:rgb(150,150,150)">{{comment.created_at}}</span>
      </div>
      
      <div style="display:flex; margin-left:10px;">
        <div v-if="this.$store.state.userInfo.username === comment.user.username">
          <a class="delete-comment" @click="deleteComment">삭제</a>
        </div>
        
        <star-rating v-if="comment.vote" style="margin-left: 16px;" read-only="true" :star-size="18" :rating="comment.vote" :increment="0.5" :show-rating="false" :animate="true" :active-color="['#520000','#520000']" :active-border-color="['#F6546A','#948989']" :border-width="4" :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]" :active-on-click="true" :clearable="true"></star-rating>
        <span v-if="comment.vote" style="margin-left:10px;"><b>{{comment.vote}}</b></span>
      </div>
      
      
    </div>

    
    <span>{{comment.content}}</span>
    <hr style="margin-left:-32px;">
  </li>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
export default {
  name: 'MovieCardDetailCommentsComment',
  components: {
    StarRating,
  },
  props: {
    comment: Object,
    idx: Number,
  },
  methods: {
    
    deleteComment() {
      const API_URL = "http://127.0.0.1:8000"
      axios({
        method: 'delete',
        url: `${API_URL}/movies/comment_detail/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(response => {
          this.$emit('idx', this.idx)
          console.log(response)

        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
.comment-li {
  list-style-type:none;
}
.delete-comment {
  font-size:14px; 
  color:rgb(150,150,150);
  transition-duration:0.4s;
  transition-property: color;
  text-decoration: none;
  cursor: pointer;
}
.delete-comment:hover {
  color:white;
}
</style>