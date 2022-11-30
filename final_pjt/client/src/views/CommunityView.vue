<template>
  <div class="background-blur">
    <div class="box">
      <div><CommunitySidebar class="side-bar"/></div>
      <CommunityMain class="main-bar"/>
      <button class="top-btn" @click="moveTop"><i class="bi bi-arrow-up"></i></button>
    </div>
  </div> 
</template>

<script>
import CommunitySidebar from '@/components/CommunitySidebar'
import CommunityMain from '@/components/CommunityMain'

export default {
  name: 'CommunityView',
  components: {
    CommunitySidebar,
    CommunityMain,
  },
  data() {
    return {
    }
  },
  computed: {
  },
  methods: {
    moveTop() {
      window.scrollTo({top:0, left:0, behavior:'auto'})
    },
  },
}
</script>

<style>

.box {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin-top: -72px;
  padding-top: 72px;
  min-height: 100vh;
}

.background-blur {
  background-color: rgba(0, 0, 0, 0.9);
  min-height: 100vh;
  margin-top: -72px;
  padding-top: 72px;
}

.block {
  background-color: #282828;
  border-radius: 10px;
}


.side-bar {
  position: fixed;
  top: 158px;
  width: 300px;
}

.main-bar {
  margin-left: 320px;
  margin-top: 30px;
  width: 900px;
}

.top-btn {
  position: fixed;
  right: 15px;
  bottom: 15px;
  appearance: none;
  font-size: 25px;
  border-radius: 20px;
  background-color: #282828bd;
  border: solid 1px #282828bd;
  color: white;
}

.top-btn:hover {
  border: 1px solid rgba(255, 0, 0, 0.295);
  outline: 3px solid rgba(255, 0, 0, 0.247);
}
</style>