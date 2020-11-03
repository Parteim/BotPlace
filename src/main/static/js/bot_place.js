import {Request} from './requests.js';

class BotInstance {
    botName = NaN;
    botSlug = NaN;
    botFor = NaN;
    dateOfCreation = NaN;
    botSettingsInfo = NaN;

    static revealFlag = false;
    static url = 'http://127.0.0.1:8000/'

    botLisat = document.getElementById('existing_bot_list');

    botItem = document.createElement('li');
    botLogoContainer = document.createElement('div');
    botTitle = document.createElement('h2');
    botBar = document.createElement('ul');
    botBarItem = document.createElement('li');
    botBarSettingsBtn = document.createElement('button');

    constructor (botName, botSlug, botFor, dateOfCreation) {
        this.botName = botName;
        this.botSlug = botSlug;
        this.botFor = botFor;
        this.dateOfCreation = dateOfCreation;

        this.creteItemOfListBot();
        this.getBotSettings();
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
        document.getElementById('bot_panel_title').innerHTML = this.botName;

        let botPanelBody = document.getElementById('bot_panel_body');
        botPanelBody.innerHTML = '';

        console.log('call botPanel');
    }

    botSettings () {
        document.getElementById('bot_panel_title').innerHTML = this.botName;

        console.log('call botSettings');

        let botPanelBody = document.getElementById('bot_panel_body');
        botPanelBody.innerHTML = '';

        let form = document.createElement('form');
        let botNameField = document.createElement('input');
        let botAppIdField = document.createElement('input');
        let botProtectionKeyField = document.createElement('input');
        let botServecesKeyField = document.createElement('input');
        let settingsBotUpdateBtn  = document.createElement('button');

        form.className = 'settings_bot_form';
        botNameField.className = 'settings_bot_field';
        botAppIdField.className = 'settings_bot_field';
        botProtectionKeyField.className = 'settings_bot_field';
        botServecesKeyField.className = 'settings_bot_field';
        settingsBotUpdateBtn.className = 'setting_bot_update_btn';

        botNameField.placeholder = 'Bot name';
        botAppIdField.placeholder = 'Application id';
        botProtectionKeyField.placeholder = 'Protection key';
        botServecesKeyField.placeholder = 'Services key of accessing';

        settingsBotUpdateBtn.innerText = 'Update';

        form.appendChild(botNameField);
        form.appendChild(botAppIdField);
        form.appendChild(botProtectionKeyField);
        form.appendChild(botServecesKeyField);
        form.appendChild(settingsBotUpdateBtn);

        if (this.botSettingsInfo) {
            botNameField.value = this.botName;
            botAppIdField.value = botSettingsInfo.bot_id;
            botProtectionKeyField.value = botSettingsInfo.protection_key;
            botServecesKeyField.value = botSettingsInfo.services_key_accessing;

            botPanelBody.appendChild(form);
        }
        else {
            return;
        }

    }

    insertToBotlist(obj) {
        this.botLisat.appendChild(this.botItem);

        this.botTitle.addEventListener("click", function () {
            obj.botPanel();
        })

        this.botBarSettingsBtn.addEventListener("click", function () {
            obj.botSettings();
        })
    }

    getBotSettings() {
        let request = new Request();
        let url = BotInstance.url;

        if (this.botFor == 'vk') {
            url += 'vk/' + 'get-vk-bot/' + this.botSlug;
        }

        request.get(
            url,
            this.saveSettingsInfo
        );
    }

    saveSettingsInfo(settings) {
        console.log(settings[0]);
        this.botSettingsInfo = 1;
    }



}

function getBotList () {
    let request = new Request();

    request.get(
        'http://127.0.0.1:8000/get-list-bots',
        function (response) {
            if (response.length !== 0) {
                document.getElementById('existing_bot_list').innerHTML = '';

                for (let i in response) {
                    let botData = response[i].fields;
                    let bot = new BotInstance(
                        botData.bot_name,
                        botData.bot_slug,
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