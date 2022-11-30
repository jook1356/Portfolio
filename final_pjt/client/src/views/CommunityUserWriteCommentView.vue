<template>
  <div class="background-blur">
    <div class="box">
      <div><CommunitySidebar class="side-bar"/></div>
      <CommunityUserWriteCommentMain class="main-bar"/>
      <button class="top-btn" @click="moveTop"><i class="bi bi-arrow-up"></i></button>
    </div>
  </div>
</template>

<script>
import CommunitySidebar from '@/components/CommunitySidebar'
import CommunityUserWriteCommentMain from '@/components/CommunityUserWriteCommentMain'


export default {
  name: 'CommunityUserWriteCommentView',
  components: {
    CommunitySidebar,
    CommunityUserWriteCommentMain,
  },
  methods: {
    moveTop() {
      window.scrollTo({top:0, left:0, behavior:'auto'})
    },
  },
}
</script>

<style scoped>
</style>