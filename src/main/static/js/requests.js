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

export {Request};