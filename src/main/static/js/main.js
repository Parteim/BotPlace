class Request {
    static hostName = 'http://127.0.0.1:8000/';
    httpRequest = NaN;

    constructor() {

        if (window.XMLHttpRequest) { // for Mazilla, Safari
            this.httpRequest = new XMLHttpRequest();
            if (this.httpRequest.overrideMimeType) {
                this.httpRequest.overrideMimeType('text/xml');
            }
        } else if (window.ActiveXObject) { // IE
            try {
                this.httpRequest = new ActiveXObject('Msxml2.XMLHTTP');
            } catch (error) {
                try {
                    this.httpRequest = new ActiveXObject('Microsoft.XMLHTTP');
                } catch (error) {
                    console.log(error)
                }
            }
        }

        if (!this.httpRequest) {
            console.log("Can't create instance of class XMLHTTP");
            return false;
        }

        console.log(this.httpRequest)
    }

    post(url, data, func) {
        let httpR = this.httpRequest;
        this.httpRequest.onreadystatechange = function () {
            Request.sendRequest(httpR, func);
        }
        this.httpRequest.open('POST', url, true);
        this.httpRequest.setRequestHeader('Content-Type', 'application/json');
        this.httpRequest.send(data);
    }


    get(url, func, data) {
        let httpR = this.httpRequest;
        this.httpRequest.onreadystatechange = function () {
            Request.sendRequest(httpR, func);
        }
        this.httpRequest.open('GET', url, true);
        this.httpRequest.send(data);
    }

    static sendRequest(httpRequest, func) {
        if (httpRequest.readyState == 4) {
            if (httpRequest.status == 200) {
                let response = JSON.parse(httpRequest.response);
                func(response)
            } else {
                console.log('Something wrong');
            }
        }
    }
}


class BotInstance {
    botName = NaN;
    uniqueBotId = NaN;
    botFor = NaN;
    dateOfCreation = NaN;

    static revealFlag = false;

    wall = document.getElementById('existing_bot_list');

    botItem = document.createElement('li');
    botLogoContainer = document.createElement('div');
    botTitle = document.createElement('h2');
    botBar = document.createElement('ul');
    botBarItem = document.createElement('li');
    botBarSettingsBtn = document.createElement('button');

    constructor (botName, uniqueBotId, botFor, dateOfCreation) {
        this.botName = botName;
        this.uniqueBotId = uniqueBotId;
        this.botFor = botFor;
        this.dateOfCreation = dateOfCreation;

        this.creteItemOfListBot()
    }

    creteItemOfListBot() {
        this.botItem.className = 'existing_bot ';
        this.botLogoContainer.className = 'existing_bot_logo ';
        this.botTitle.className = 'exiting_bot_title ';
        this.botBar.className = 'exiting_bot_bar ';
        this.botBarItem.className = 'exiting_bot_bar_item ';
        this.botBarSettingsBtn.className = 'exiting_bot_bar_btn ';
        this.botBarSettingsBtn.className = 'exiting_bot_bar_settings ';

        if (this.botFor == 'vk') {
            this.botItem.className += 'vk_bot ';
            this.botTitle.className += 'exiting_vk_bot_title ';
            this.botBarSettingsBtn.className += 'exiting_vk_bot_bar_btn ';
        }

        this.botBarSettingsBtn.innerHTMl = '<i class="fas fa-cog"></i>';
        this.botLogoContainer.innerHTMl = '<i class="fab fa-vk"></i>';

        this.botItem.appendChild(this.botLogoContainer);
        this.botItem.appendChild(this.botTitle);
        this.botItem.appendChild(this.botBar);

        this.botBar.appendChild(this.botBarItem);

        this.botBarItem.appendChild(this.botBarSettingsBtn);

        this.botTitle.innerText = this.botName;

    }

    botPanel () {

    }

    botSettings () {
        
    }

    insertToBotlist(obj) {
        this.wall.appendChild(this.botItem);

        this.botTitle.addEventListener("click", function () {
            if (!BotInstance.revealFlag) {
                obj.botPanel();
                BotInstance.revealFlag = true;
            }
        })

        this.botBarSettingsBtn.addEventListener("click", function () {
            if (!BotInstance.revealFlag) {
                obj.botSettings();
                BotInstance.revealFlag = true;
            }
        })
    }



}