from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from acount.views import Login, signup, activate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('blog/', include('blog.urls')),
    path('', include('website.urls')),
    path('accounts/', include('acount.urls')),
    path('comment/', include('comment.urls')),
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
