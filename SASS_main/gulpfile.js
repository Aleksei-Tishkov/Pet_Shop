var gulp = require('gulp'), // Подключаем Gulp
		sass = require('gulp-sass')(require('sass')); // Подключаем Sass пакет
 
gulp.task('css', function() { // Создаем таск "css"
	return gulp.src(['css/**/*.css', 'css/**/*.scss']) // Берем источник
		.pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError)) // Преобразуем Sass в CSS посредством gulp-css
		.pipe(gulp.dest('css')) // Выгружаем результата в папку css
	});
 
gulp.task('watch', function() {
	gulp.watch(['css/**/*.css', 'css/**/*.scss'], ['css']); // Наблюдение за css файлами в папке css
});
 
gulp.task('default', ['watch']);