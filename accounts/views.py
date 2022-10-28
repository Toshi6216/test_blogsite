from django.shortcuts import render, redirect
from allauth.account import views
from .forms import SignupForm, ProfileForm
from django.urls import reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login


#ログイン
class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

#ログアウト
class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/blog/')

##サインアップ
#class SignupView(views.SignupView):
#    template_name = 'accounts/signup.html'

def newSignupView(request):
    user_form = SignupForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    
    if request.method == 'POST' and user_form.is_valid() and profile_form.is_valid():
        
        user = user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        user.profile.save()
        
        login(request, user)
       
        return redirect('/accounts/login/')

    ctx = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
  
    return render(request, 'blog/signup_form.html', ctx)

#class NewSignupView(CreateView):
#    template_name = 'blog/signup_form.html'
#    form_class = SignupForm
##    success_url = '/accounts/login/'
#
#    def get_success_url(self): 
#        return reverse("account_login") #入力フォーム内容がセーブできた時の遷#移先
#
#    def get_context_data(self, **kwargs):
#        ctx=super().get_context_data(**kwargs)
#
#        if self.request.method=="POST": #"POST"が呼び出されたときの処理
#                ctx["user_form"] = SignupForm(self.request.POST)
#                ctx["profile_form"] = ProfileForm(self.request.POST)
#
#        else:
#            ctx["user_form"] = SignupForm()
#            ctx["profile_form"] = ProfileForm()
#        
#        return ctx
#        
#    def form_valid(self, form):
#        ctx = self.get_context_data()
#        user_form = ctx["user_form"]
#        profile_form = ctx["profile_form"]
#       # forms = (user_form, profile_form)
#
#        if user_form.is_valid() and profile_form.is_valid():
#            user=user_form.save(commit=False)
#            
#            profile = profile_form.save(commit=False)
#            profile.user = user
#            profile.save()
#            user.save()
#
#        #    return redirect(to='/login_app/user/')
#            return redirect(self.get_success_url())
#
#        else:
#            ctx["forms"] = form
#            return self.render_to_response(ctx)

