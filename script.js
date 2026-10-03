function fetchURL(){


    return "https://www.w3schools.com/howto/howto_js_redirect_webpage.asp";
}

let goal_url = fetchURL();

window.location.replace(goal_url);