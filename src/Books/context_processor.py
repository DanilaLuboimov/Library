from app_user.forms import AuthForm, FeedbackForm


def get_context_data(request):
    if request.user.is_authenticated:
        initial_data = {
            "email": request.user.email,
            "first_name": request.user.first_name,
            "phone_number": request.user.phone_number,
        }
        feedback_form = FeedbackForm(initial=initial_data)
    else:
        feedback_form = FeedbackForm()

    context = {
        "login_form": AuthForm(),
        "feedback_form": feedback_form,
    }
    return context
