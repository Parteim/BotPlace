import {Request} from './requests.js';

class BotInstance {
    botName = NaN;
    uniqueBotId = NaN;
    botFor = NaN;
    dateOfCreation = NaN;

    static revealFlag = false;

    botLisat = document.getElementById('existing_bot_list');

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

        this.creteItemOfListBot();
    }

    creteItemOfListBot() {
        this.botItem.className = 'existing_bot ';
        this.botLogoContainer.className = 'existing_bot_logo ';
        this.botTitle.className = 'exiting_bot_title ';
        this.botBar.className = 'exiting_bot_bar ';
        this.botBarItem.className = 'exiting_bot_bar_item ';
        this.botBarSettingsBtn.className = 'exiting_bot_bar_btn ';
        this.botBarSettingsBtn.className += 'exiting_bot_bar_settings ';

        if (this.botFor == 'vk') {
            this.botItem.className += 'vk_bot ';
            this.botTitle.className += 'exiting_vk_bot_title ';
            this.botBarSettingsBtn.className += 'exiting_vk_bot_bar_btn ';

            this.botLogoContainer.innerHTML = '<i class="fab fa-vk"></i>';
        }

        this.botBarSettingsBtn.innerHTML = '<i class="fas fa-cog"></i>';

        this.botItem.appendChild(this.botLogoContainer);
        this.botItem.appendChild(this.botTitle);
        this.botItem.appendChild(this.botBar);

        this.botBar.appendChild(this.botBarItem);

        this.botBarItem.appendChild(this.botBarSettingsBtn);

        this.botTitle.innerText = this.botName;

    }

    botPanel () {
        console.log('call botPanel');
        BotInstance.revealFlag = false;
    }

    botSettings () {
        console.log('call botSettings');
        BotInstance.revealFlag = false;
    }

    insertToBotlist(obj) {
        this.botLisat.appendChild(this.botItem);

        this.botTitle.addEventListener("click", function () {
            if (!BotInstance.revealFlag) {
                BotInstance.revealFlag = true;
                obj.botPanel();
            }
        })

        this.botBarSettingsBtn.addEventListener("click", function () {
            if (!BotInstance.revealFlag) {
                BotInstance.revealFlag = true;
                obj.botSettings();
            }
        })
    }



}

function getBotList () {
    let request = new Request();

    request.get(
        'http://127.0.0.1:8000/get-list-bots',
        function (response) {
            if (response) {
                document.getElementById('existing_bot_list').innerHTML = '';

                for (let i in response) {
                    let botData = response[i].fields;
                    let bot = new BotInstance(
                        botData.bot_name,
                        botData.unique_bot_id,
                        botData.bot_for,
                        botData.date_of_creation,
                    );
    
                    bot.insertToBotlist(bot);
                }
            }
        },
        1,
    );
} 

getBotList();