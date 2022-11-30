<template>
  <div class="background-blur">
    <div class="box">
      <div><CommunitySidebar class="side-bar"/></div>
      <CommunityUserWriteMain class="main-bar"/>
      <button class="top-btn" @click="moveTop"><i class="bi bi-arrow-up"></i></button>
    </div>
  </div>
</template>

<script>
import CommunitySidebar from '@/components/CommunitySidebar'
import CommunityUserWriteMain from '@/components/CommunityUserWriteMain'

export default {
  name: 'CommunityUserwriteView',
  components: {
    CommunitySidebar,
    CommunityUserWriteMain,
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