<template>
  <div class="animated fadeIn">
    <div class="row">
      <div class="col-md-12">
        <b-card header="Real time data">
          <b-table class="table-outline table-responsive-sm mb-0" hover
            :items="tableItems"
            :fields="tableFields"
            head-variant="light"
            >
            <div slot="avatar" class="avatar" slot-scope="item">
              <img :src="item.value.url" class="img-avatar" alt="">
              <span class="avatar-status" v-bind:class="{ 'bg-success': item.value.status == 'success',  'bg-warning': item.value.status == 'warning', 'bg-danger': item.value.status == 'danger', 'bg-secondary': item.value.status == '' }"></span>
            </div>
            <div slot="user" slot-scope="item">
              <div>{{item.value.name}}</div>
              <div class="small text-muted">
                <span>
                  <template v-if="item.value.new">New</template>
                  <template v-else>Recurring</template>
                </span> | Registered: {{item.value.registered}}
              </div>
            </div>
            <img slot="country" slot-scope="item" :src="item.value.flag" :alt="item.value.name" style="height:24px;">
            <div slot="usage" slot-scope="item">
              <div class="clearfix">
                <div class="float-left">
                  <strong>{{item.value.value}}%</strong>
                </div>
                <div class="float-right">
                  <small class="text-muted">{{item.value.period}}</small>
                </div>
              </div>
              <b-progress class="progress-xs" v-model="item.value.value" </b-progress>
            </div>
            <i slot="payment" slot-scope="item" :class="item.value.icon" style="font-size:24px"></i>
            <div slot="activity" slot-scope="item">
              <div class="small text-muted">Last login</div>
              <strong>{{item.value}}</strong>
            </div>
          </b-table>
        </b-card>
      </div><!--/.col-->
    </div><!--/.row-->
  </div>
</template>

<script>

export default {
  name: 'realtime',
  computed: {
    tableItems: function () {
      console.log(this.$store)
      return this.$store.state.realtime.messages
    }
  },
  data: function () {
    return {
      tableFields: {
        article_id: {
          label: 'Article id',
          class: 'text-center'
        },
        source: {
          label: 'Source'
        },
        timestamp: {
          label: 'Timestamp'
        },
        title: {
          label: 'Title'
        }
      }
    }
  }
}
</script>
