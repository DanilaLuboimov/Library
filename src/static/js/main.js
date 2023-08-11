export function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


function getUser () {
    return JSON.parse(
        document.getElementById('profile_user').textContent
    );
}


function getUserId() {
    return JSON.parse(
        document.getElementById('user_id').textContent
    );
}
export const user = getUser();
export const user_id = getUserId();

if (user !== "") {
        let profile = document.getElementById('profile');
        profile.innerText = user;
}
