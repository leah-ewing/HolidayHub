# HolidayHub 🎉

---

## Description:

**HolidayHub** is a web application that showcases little-known daily holidays. The site includes the ability to utilize a calendar to view any day of the year and its holidays or view a random holiday. Currently in development is functionality to sign-up for daily emails that provides the user with the daily holiday with a short description. Subscribers and choose to unsubscribe at any time. 

The site is fully dynamic and is able to be viewed on any size screen or mobile device.

---

## Tech Stack
* [Back End](#back-end)
* [Front End](#front-end)
* [Relational Database](#database)
* [APIs](#apis)
* [Testing](#testing)
* [CronJobs](#cronjobs)
* [Deployment](#deployment)
* [Servers](#servers)
* [Network Specs](#network-specs)
* [Security](#security)

---

### <a name="back-end"></a>Back End

* **Language:** Python
* **Web Framework:** Flask

---

### <a name="front-end"></a>Front End

* **Languages:** HTML, CSS, Javascript
* **Template Engine:** Jinja2
* **Framework Library:** Bootstrap

---

### <a name="database"></a>Relational Database

* **Management System:** Postgresql
* **Database Client:** Postico

---

### <a name="apis"></a>APIs

* **ElasticEmail:** Sending automated emails to subscribed users *(currently in beta)*
* **OpenAI:** Creating holiday descriptions and daily emails

---

### <a name="testing"></a>Testing

* **Testing Framework:** Pytest
* **Tests Included:** Unit, Integration

---

### <a name="cronjobs"></a>CronJobs

* Sending daily emails *(once daily)*
* Purging database for unsubscribed emails *(twice daily)*

---

### <a name="deployment"></a>Deployment

* **Deployed via:** Github Actions
* **CI/CD:** Main > Development *(deploys to development environment)* > Production *(deploys to production environment)*

---

### <a name="servers"></a>Servers

* **Development Environment:** dev.holidayhub.app
* **Production Environment:** holidayhub.app

---

### <a name="network-specs"></a>Network Specs
* **Domain Host:** GoDaddy
* **Web Host:** AWS Lightsail (Ubuntu)
* **Event Scheduling:** AWS EventBridge
* **Event Handling:** AWS Lambda
* **Monitoring and Logging:** AWS CloudWatch
* **WSGI HTTP Server:** Gunicorn
* **Reverse Proxy/Load Balancer:** Nginx
* **SSL Certificate:** Certbot

---

### <a name="security"></a>Security
* **Email Security:** SPF, DKIM, CNAME, DMARC
* **Information Encryption:** Personal information is encrypted before being added to database