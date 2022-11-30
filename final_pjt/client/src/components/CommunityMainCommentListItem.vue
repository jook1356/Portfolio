<template>
  <div class="itemBox">
    <p class="username">{{ userInfo?.nickname }}</p>
    <p class="comment-content">{{ comment.content }}</p>
    <p class="review-title">
      <span>{{ comment.review.title }}</span>
      <span class="comment_count">
        <i class="bi bi-chat-fill"></i> 
        {{ comment.review.comment_count }}
      </span>
    </p>
  </div>
</template>

<script>
export default {
  name: 'CommunityMainCommentListItem',
  data() {
    return {
    }
  },
  props: {
    comment: Object,
  },
  computed: {
    userInfo() {
      return this.$store.state.userInfo
    }
  },
  methods: {
  },
  created() {
    console.log(this.comment)
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


.username {
  font-weight: 600;
  font-size: 0.8rem;
}

.comment-content {
  font-size: 1.4rem;
  font-weight: 300;
  margin-bottom: 8px;
}

.review-title {
  font-size: 0.9rem;
  font-weight: 300;
  color: #98a4b7be;
  margin-bottom: 0px;
}

.comment_count {
  border: solid 1px #98A4B7;
  border-radius: 10px;
  padding: 2px 5px 2px 5px;
  margin-left: 5px;
  font-size: 0.6rem;
  display: inline-block;
}
</style>