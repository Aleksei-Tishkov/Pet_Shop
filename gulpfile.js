var gulp = require('gulp'), // Подключаем Gulp
		sass = require('gulp-sass')(require('sass')); // Подключаем Sass пакет
 
gulp.task('css', function() { // Создаем таск "css"
	return gulp.src(['static/static/css/**/*.css', 'static/static/css/**/*.scss']) // Берем источник
		.pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError)) // Преобразуем Sass в CSS посредством gulp-css
		.pipe(gulp.dest('static/static/css')) // Выгружаем результата в папку css
	});
 
gulp.task('watch', function() {
	gulp.watch(['static/static/css/**/*.css', 'static/static/css/**/*.scss'], gulp.series('css')); // Наблюдение за css файлами в папке css
});
 
gulp.task('default', gulp.series('watch'));