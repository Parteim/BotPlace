import {Request} from './requests.js';

class BotInstance {
    botName = NaN;
    botSlug = NaN;
    botFor = NaN;
    dateOfCreation = NaN;

    static revealFlag = false;
    static url = 'http://127.0.0.1:8000/'

    botList = document.getElementById('existing_bot_list');

    botItem = document.createElement('li');
    botLogoContainer = document.createElement('div');
    botTitle = document.createElement('h2');
    botBar = document.createElement('ul');
    botBarItem = document.createElement('li');
    botBarSettingsBtn = document.createElement('button');

    constructor(botName, botSlug, botFor, dateOfCreation) {
        this.botName = botName;
        this.botSlug = botSlug;
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

    botPanel() {
        document.getElementById('bot_panel_title').innerHTML = this.botName;

        let botPanelBody = document.getElementById('bot_panel_body');
        botPanelBody.innerHTML = '';

        console.log('call botPanel');
    }

    botSettings(obj) {
        console.log('call settings');

        let request = new Request();
        let url = BotInstance.url;

        if (obj.botFor == 'vk') {
            url += 'vk/' + 'get-vk-bot/' + obj.botSlug;
        }

        request.get(
            url,
            function (response) {
                let botSettings = new BotSettings(obj, response[0].fields)

            }
        );
    }

    insertToBotList(obj) {
        this.botList.appendChild(this.botItem);

        this.botTitle.addEventListener("click", function () {
            obj.botPanel();
        })

        this.botBarSettingsBtn.addEventListener("click", function () {
            obj.botSettings(obj);
        })
    }
}

class BotSettings {
    botPanelBody = NaN;

    form = NaN;
    botNameField = NaN;
    botAppIdField = NaN;
    botProtectionKeyField = NaN;
    botServicesKeyField = NaN;
    settingsBotUpdateBtn = NaN;

    botName = NaN;
    botSlug = NaN;
    appId = NaN;
    protectionKey = NaN;
    servicesKey = NaN;

    constructor(bot, settings) {
        this.botName = bot.botName;
        this.botSlug = bot.botSlug;

        this.appId = settings.bot_id;
        this.protectionKey = settings.protection_key;
        this.servicesKey = settings.services_key_accessing;

        this.createBotSettingsForm();
        this.insertSettingsValue();
    }

    createBotSettingsForm() {
        document.getElementById('bot_panel_title').innerHTML = this.botName;

        this.botPanelBody = document.getElementById('bot_panel_body');
        this.botPanelBody.innerHTML = '';

        this.form = document.createElement('form');
        this.botNameField = document.createElement('input');
        this.botAppIdField = document.createElement('input');
        this.botProtectionKeyField = document.createElement('input');
        this.botServicesKeyField = document.createElement('input');
        this.settingsBotUpdateBtn = document.createElement('button');
        let formLabel = document.createElement('label');

        this.form.className = 'settings_bot_form';
        this.botNameField.className = 'settings_bot_field';
        this.botAppIdField.className = 'settings_bot_field';
        this.botProtectionKeyField.className = 'settings_bot_field';
        this.botServicesKeyField.className = 'settings_bot_field';
        this.settingsBotUpdateBtn.className = 'setting_bot_update_btn';
        formLabel.className = 'bot_settings_label';

        this.botNameField.name = 'bot_name';
        this.botAppIdField.name = 'bot_id';
        this.botProtectionKeyField.name = 'protection_key';
        this.botServicesKeyField.name = 'services_key_accessing';


        this.botNameField.placeholder = 'Bot name';
        this.botAppIdField.placeholder = 'Application id';
        this.botProtectionKeyField.placeholder = 'Protection key';
        this.botServicesKeyField.placeholder = 'Services key of accessing';

        this.settingsBotUpdateBtn.innerText = 'Update';

        this.form.appendChild(this.botNameField);
        this.form.appendChild(this.botAppIdField);
        this.form.appendChild(this.botProtectionKeyField);
        this.form.appendChild(this.botServicesKeyField);
        this.form.appendChild(this.settingsBotUpdateBtn);

        this.botPanelBody.appendChild(this.form);
    }

    insertSettingsValue() {
        this.botNameField.value = this.botName;
        this.botAppIdField.value = this.appId;
        this.botProtectionKeyField.value = this.protectionKey;
        this.botServicesKeyField.value = this.servicesKey;
    }
}

function getBotList() {
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

                    bot.insertToBotList(bot);
                }
            }
        },
        1,
    );
}

getBotList();