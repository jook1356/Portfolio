<template>
  <div class="background-blur">
    <div class="box">
      <div><CommunitySidebar class="side-bar"/></div>
      <CommunityUserLikeMain class="main-bar"/>
      <button class="top-btn" @click="moveTop"><i class="bi bi-arrow-up"></i></button>
    </div>
  </div>
</template>

<script>
import CommunitySidebar from '@/components/CommunitySidebar'
import CommunityUserLikeMain from '@/components/CommunityUserLikeMain'

export default {
  name: 'CommunityUserLikeView',
  components: {
    CommunitySidebar,
    CommunityUserLikeMain,
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