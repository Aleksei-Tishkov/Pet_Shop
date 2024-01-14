from User.models import User, UserTheme


def change_theme(user: User):
    theme, created = UserTheme.objects.get_or_create(user_theme_user=user)
    if created:
        theme.user_theme_theme = 1
    else:
        if theme.user_theme_theme:
            theme.user_theme_theme = 0
        else:
            theme.user_theme_theme = 1
    theme.save()
