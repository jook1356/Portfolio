import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import CommunityView from '@/views/CommunityView'
import CommunityCreateView from '@/views/CommunityCreateView'
import LoginView from '@/views/LoginView'
import SignupView from '@/views/SignupView'
import ChangePasswordView from '@/views/ChangePasswordView'
import CommunityDetail from '@/views/CommunityDetail'
import SignupSelectMovies from '@/views/SignupSelectMovies'
import CommunityUpdateView from '@/views/CommunityUpdateView'
import CommunityUserLikeView from '@/views/CommunityUserLikeView'
import CommunityUserWriteView from '@/views/CommunityUserWriteView'
import CommunityUserWriteCommentView from '@/views/CommunityUserWriteCommentView'


Vue.use(VueRouter)

const routes = [

  {
    path: '/',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/signup/select_movies',
    name: 'SignupSelectMovies',
    component: SignupSelectMovies
  },
  {
    path: '/commuity',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/community/create',
    name: 'create',
    component: CommunityCreateView
  },
  {
    path: '/community/update/:id',
    name: 'update',
    component: CommunityUpdateView
  },
  {
    path: '/community/user/like',
    name: 'community_user_like',
    component: CommunityUserLikeView
  },
  {
    path: '/community/user/reviews/',
    name: 'community_user_reviews',
    component: CommunityUserWriteView
  },
  {
    path: '/community/user/comments/',
    name: 'community_user_comments',
    component: CommunityUserWriteCommentView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/detail/:id',
    name: 'detail',
    component: CommunityDetail,
  },
  {
    path: '/change_password',
    name: 'change_password',
    component: ChangePasswordView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
