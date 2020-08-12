<template>
  <v-card>
    <v-list-item three-line>
      <v-list-item-content>
        <v-list-item-title
          class="headline mb-1"
        >
          Information
        </v-list-item-title>
        <v-list-item-subtitle>Name</v-list-item-subtitle>
        <v-list-item-subtitle>Last Name</v-list-item-subtitle>
        <v-list-item-subtitle>Second Last Name</v-list-item-subtitle>
        <v-list-item-subtitle>ID Number</v-list-item-subtitle>
        <v-list-item-subtitle>Student ID</v-list-item-subtitle>
        <v-list-item-subtitle>Email:</v-list-item-subtitle>
        <v-list-item-subtitle>Phone Number:</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-card-actions>
      <v-btn
        block
        color="primary"
      >
        All-Nighter Requests
      </v-btn>
      <v-btn
        text
      >
        Disable Account
      </v-btn>
      <v-btn
        text
      >
        Edit
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  export default {}
</script>

<style scoped>
.controls {
  position: relative;
}
</style>
