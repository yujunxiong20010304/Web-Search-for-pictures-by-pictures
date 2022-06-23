<template>
  <div>
    <my-head></my-head>
    <my-search></my-search>
    <show-shop></show-shop>
    <my-tail></my-tail>
  </div>
</template>

<script>
import myHead from '@/components/myHead'
import mySearch from '@/components/mySearch'
import myTail from '@/components/myTail'
import showShop from '@/components/showShop'
export default {
  name: 'myHome',
  components: { 'my-head': myHead, 'my-search': mySearch, 'my-tail': myTail, 'show-shop': showShop }
}
</script>

<style scoped lang="less">

</style>
