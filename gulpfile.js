var gulp = require('gulp');
var sass = require('gulp-sass');
var connect = require('gulp-connect');

gulp.task('connect', function() {
	connect.server({
		root: '.',
		livereload: true
	});
});

gulp.task('sass', function() {
	return gulp.src('./assets/sass/**/*.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(gulp.dest('./public/css'));
});

gulp.task('js', function() {
	return gulp.src('./assets/js/**/*.js')
		.pipe(gulp.dest('./public/js'));
});

gulp.task('livereload', function() {
	connect.reload();
});

gulp.task('watch', function() {
	gulp.watch('./assets/js/**/*.js', ['js']);
	gulp.watch('./assets/sass/**/*.scss', ['sass']);
	gulp.watch(['./public/**/*.css', './public/**/*.js'], ['livereload']);
	gulp.watch('./templates/**/**/*.html', ['livereload']);
});

gulp.task('default', ['connect', 'watch', 'sass', 'js'])