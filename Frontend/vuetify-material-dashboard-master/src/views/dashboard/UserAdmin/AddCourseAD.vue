<template>
  <v-row class="">
    <v-col>
      <v-sheet height="64">
        <v-toolbar
          flat
          color="white"
        >
          <v-spacer />
          <v-spacer />
          <v-btn
            outlined
            color="grey darken-2"
            @click="newCourseDialog = true"
          >
            New Course
          </v-btn>
          <v-menu
            bottom
            right
          />
        </v-toolbar>
      </v-sheet>
      <!--------------PUT the log here------------------------------------------------------>
      <v-sheet height="600">
        <v-data-table
          :headers="headers"
          :items="courses"
          class="elevation-1"
        />
        <v-dialog
          v-model="newCourseDialog"
          width="400"
        >
          <v-card
            class="mx-auto"
            max-width="400"
          >
            <v-img
              class="white--text align-end"
              height="20px"
              src=""
            />
            <v-text-field
              v-model="newCourseName"
              filled
              color="deep-blue"
              label="Name"
              type="text"
            />
            <v-text-field
              v-model="newCourseCode"
              filled
              color="deep-blue"
              label="Code"
              type="text"
            />
            <v-text-field
              v-model="newCourseGroup"
              filled
              color="deep-blue"
              label="Group No."
              type="text"
            />
            <v-card-actions>
              <v-btn
                color="blue"
                text
                @click="submitNewCourse()"
              >
                Add Course
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      newCourseName: '',
      newCourseCode: '',
      newCourseGroup: '',
      newCourseDialog: false,
      headers: [
        {
          text: 'Code',
          align: 'start',
          sortable: true,
          value: 'code',
        },
        { text: 'Name', value: 'name' },
        { text: 'Group', value: 'group' },
      ],
      courses: [],
    }),
    mounted () {
      this.getCourses()
    },
    methods: {
      async getCourses () {
        try {
          await this.$auth.getCourses().then(
            response => {
              var res = response.data
              this.courses = []
              console.log(res)
              for (var i = 0; i < res.length; i++) {
                this.courses.push({
                  code: res[i][0],
                  name: res[i][1],
                  group: res[i][2],
                })
              }
            })
        } catch (error) {
          this.error = true
        }
      },
      addNewCourse () {
        try {
          if (this.newCourseName !== '' & this.newCourseCode !== '' & this.newCourseGroup !== '') {
            this.submitNewCourse()
          } else {
            alert('Please fill out all fields')
          }
        } catch (error) {

        }
      },
      async submitNewCourse () {
        try {
          await this.$auth.submitNewCourse(this.newCourseName, this.newCourseCode, this.newCourseGroup)
          setTimeout(() => { this.getCourses() }, 1000)
          this.newCourseName = ''
          this.newCourseCode = ''
          this.newCourseGroup = ''
          this.newCourseDialog = false
        } catch (error) {
          this.error = true
          alert('Error submiting report')
        }
      },
    },
  }
</script>>
