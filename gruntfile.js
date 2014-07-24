module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
      watch: {
      options: {
          livereload: 22220
      },
      livereload: {
          files: ['**/*.html', '**/*.css', '**/*.js']
      }
    }
  });

  // Load the plugin that provides the "uglify" task.

  // Default task(s).
  grunt.registerTask('default', [
      // add all tasks you need including watch
      'watch',
  ]);

  grunt.loadNpmTasks('grunt-contrib-watch');

};
