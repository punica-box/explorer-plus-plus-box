<template>
  <div class="container container-margin-top">
    <return-home></return-home>
    <list-title :name="$t('ontIdList.name')"></list-title>

    <div class="row justify-content-center">
      <div class="col">
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
            <tr>
              <th class="font-size18" scope="col">{{ $t('all.hash') }}</th>
              <th class="font-size18" scope="col">{{ $t('all.ontId') }}</th>
              <th class="font-size18" scope="col">{{ $t('all.content') }}</th>
              <th class="font-size18" scope="col">{{ $t('all.height') }}</th>
              <th class="font-size18" scope="col">{{ $t('all.fee') }}</th>
              <th class="font-size18" scope="col">{{ $t('all.time') }}</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="OntId in OntIdListDetail.info">
              <td class="font-size14 font-Regular important_color pointer" @click="toTransactionDetailPage(OntId.TxnHash)">{{OntId.TxnHash.substr(0,8) + '...' + OntId.TxnHash.substr(56)}}</td>
              <td class="font-size14 font-Regular important_color pointer" @click="toOntIdDetailPage(OntId.OntId)">{{OntId.OntId.substr(0,10)}}...{{OntId.OntId.substr(35,46)}}</td>
              <td class="font-size14 font-Regular normal_color">{{getOntIDEvent(OntId.Description)}}</td>
              <td class="font-size14 font-Regular normal_color">{{OntId.Height}}</td>
              <td class="font-size14 font-Regular normal_color">{{Number(OntId.Fee)}}</td>
              <td class="font-size14 font-Regular normal_color">{{$HelperTools.getTransDate(OntId.TxnTime)}}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <turn-the-page :pagesInfo="OntIdListDetail" :pagesName="'OntIdListDetail'"></turn-the-page>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  import GetTransactionType from './../../common/OntMsg/GetTransactionType.js'

  export default {
    name: "ont-id-list-page",
    created() {
      this.getOntIdListPage()
    },
    watch: {
      '$route': 'getOntIdListPage'
    },
    computed: {
      ...mapState({
        OntIdListDetail: state => state.OntIdListPage.OntIdListDetail,
      })
    },
    methods: {
      getOntIdListPage() {
        this.$store.dispatch('getOntIdListPage', this.$route.params).then()
      },
      getTransactionType($case) {
        return GetTransactionType.getTransactionType($case)
      },
      toTransactionDetailPage($TxnId) {
        if (this.$route.params.net == undefined) {
          this.$router.push({name: 'TransactionDetail', params: {txnHash: $TxnId}})
        } else {
          this.$router.push({name: 'TransactionDetailTest', params: {txnHash: $TxnId, net: "testnet"}})
        }
      },
      toOntIdDetailPage($OntId) {
        if (this.$route.params.net == undefined) {
          this.$router.push({name: 'OntIdDetail', params: {ontid: $OntId}})
        } else {
          this.$router.push({name: 'OntIdDetailTest', params: {ontid: $OntId, net: "testnet"}})
        }
      },
      getOntIDEvent: function ($event) {
        switch ($event.substr(0, 12)) {
          case "register Ont":
            return "Register ONT ID"
          case "add publicKe":
            return "Add publickey"
          case "remove publi":
            return "Remove publickey"
          case "add attribut":
            return "Add identity attribute"
          case "update attri":
            return "Update identity attribute"
          case "delete attri":
            return "Delete identity attribute"
          case "change recov":
            return "Change recovery"
          case "add recovery":
            return "Add recovery"
          case "remove attri":
            return "Remove attribute"
        }
      }
    }
  }
</script>

<style scoped>

</style>
