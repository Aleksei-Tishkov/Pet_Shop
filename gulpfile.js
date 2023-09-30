var gulp = require('gulp'), // Подключаем Gulp
		sass = require('gulp-sass')(require('sass')); // Подключаем Sass пакет
 
gulp.task('sass', function() { // Создаем таск "sass"
	return gulp.src(['templates/static/sass/**/*.sass', 'templates/static/sass/**/*.scss']) // Берем источник
		.pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError)) // Преобразуем Sass в CSS посредством gulp-sass
		.pipe(gulp.dest('templates/static/css')) // Выгружаем результата в папку css
	});
 
gulp.task('watch', function() {
	gulp.watch(['templates/static/sass/**/*.sass', 'templates/static/sass/**/*.scss'], gulp.series('sass')); // Наблюдение за sass файлами в папке sass
});
 
gulp.task('default', gulp.series('watch'));