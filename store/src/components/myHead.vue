<template>
  <div id="main">
    <div id="content">
      <span class="address"><i class="iconfont icon">&#xe6ad;</i>四川省</span>
      <ul class="choices">
        <li>admin</li>
        <li>注册</li>
        <li><img src="@/assets/gift_big.gif" alt="">签到有礼</li>
        <li>我的订单</li>
        <li>我的特卖</li>
        <li>客户服务</li>
        <li>更多</li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  name: 'myHead',
  data () {
    return {

    }
  }
}
</script>

<style scoped lang="less">
#main {
  width: 100%;
  height: 30px;
  background-color: #fff;
  font-size: 12px;
  box-shadow:0 15px 35px rgba(0,0,0,0.05),0 3px 10px rgba(0,0,0,0.05);
  .icon {
    color: red;
    font-size: 14px;
    margin-right: 2px;
  }
  #content {
    min-width: 1170px;
    max-width: 1170px;
    height: 30px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #333;
  }
  .choices {
    width: 771px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #666;
    margin: 0;
    padding: 0;
    li {
      height: 30px;
      padding: 0 30px;
      line-height: 30px;
      cursor: pointer;
      position: relative;
      a {
        color: #666;
        text-decoration: none;
      }
      img {
        position: relative;
        top: 2px;
        margin-right: 5px;
      }
      &:hover {
        color: #409EFF;
      }
      &:hover a{
        color: #409EFF;
      }
      &:after {
        content: '/';
        position: absolute;
        right: 0;
        color: #d8d8d8;
      }
    }
  }
}
</style>
