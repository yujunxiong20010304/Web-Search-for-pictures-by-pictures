<template>
  <el-space direction="vertical" alignment="flex-start">
    <el-skeleton style="width: 1190px;margin: 0 auto;" :loading="loading" animated :count="1">
      <template #template>
        <div class="commodity-display">
          <div style="width: 225px;height: 325px;margin: 0 6px 15px 7px;">
            <el-skeleton-item variant="image" style="width: 222px; height: 215px" />
            <el-skeleton-item variant="h1" style="width: 100%;height: 34px;margin-top: 7px;" />
            <el-skeleton-item variant="h1" style="width: 100%;height: 47px;" />
          </div>
        </div>
      </template>
      <template #default>
        <div class="main">
          <div class="commodity-display">
            <div class="shop" v-for="item in shops" :key="item.id">
              <img :src=item.goods_image alt=""/>
              <span class="price"><i>特卖价</i><span>¥{{item.price}}.00</span></span>
              <span class="introduce">{{item.title}}</span>
            </div>
          </div>
        </div>
      </template>
    </el-skeleton>
  </el-space>
</template>

<script>
import emitter from '@/utils/event'
export default {
  name: 'showShop',
  data () {
    return {
      total: 30,
      index: 1,
      shops: '',
      loading: false
    }
  },
  created () {
    emitter.on('shop', (e) => {
      this.shops = e.aim
    })
  }
}
</script>

<style scoped lang="less">
.main {
  width: 1201px;
  margin: 0 auto;
}
.commodity-display {
  width: 1201px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  .shop {
    width: 225px;
    height: 325px;
    border: 1px solid #E7E7E7;
    cursor: pointer;
    border-radius: 5px;
    overflow: hidden;
    margin: 0 6px 15px 7px;
    &:hover {
      border: 1px solid #409EFF;
    }
    img {
      width: 222px;
      height: 215px;
    }
    .price {
      display: flex;
      align-items: center;
      padding-left: 7px;
      margin-top: 7px;
      i {
        font-style: normal;
        color: #fff;
        display: inline-block;
        background-image: linear-gradient(270deg,#e456ff 0,#ff31a3 100%);
        font-size: 12px;
        padding: 2px 7px;
        border-radius: 15px;
        margin-right: 5px;
      }
      span {
        color: #333;
        font-weight: 700;
        font-size: 23px;
      }
    }
    .introduce {
      margin-top: 11px;
      font-size: 13px;
      text-align: left;
      padding: 0 7px;
      overflow: hidden;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      text-overflow: ellipsis;
      height: 36px;
    }
  }
}
:deep(.el-pagination) {
  margin: 45px auto 25px;
  justify-content: center;
}
</style>
