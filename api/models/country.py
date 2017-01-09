# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers


class Country(models.Model):

    CATEGORIES = (('eu28','EU28'),('efta','EFTA'), )
    CURRENCIES = (('other','Other currency'),('EUR','Euro'),('GBP','British Pound'),('CAD', 'Canadian Dollar'),('DKK','Danish Krone'),('NOK','Norwegian Krone'),('RUB','Russian Rubel'),('SEK','Swedish Krona'),('CHF','Swiss Franken'),('USD','US Dollar'),)
    COUNTRIES = (('DE','Deutschland'),('CH','Schweiz'),('GB','United Kingdom'),('US','United States'),('IT','Italy'),('AT','Österreich'),('NL','Netherlands'),('DK','Denmark'),('AF','Afghanistan'),('AL','Albania'),('DZ','Algeria'),('AD','Andorra'),('AO','Angola'),('AG','Antigua and Barbuda'),('AR','Argentina'),('AM','Armenia'),('AU','Australia'),('AZ','Azerbaijan'),('BS','Bahamas, The'),('BH','Bahrain'),('BD','Bangladesh'),('BB','Barbados'),('BY','Belarus'),('BE','Belgium'),('BZ','Belize'),('BJ','Benin'),('BT','Bhutan'),('BO','Bolivia'),('BA','Bosnia and Herzegovina'),('BW','Botswana'),('BR','Brazil'),('BN','Brunei'),('BG','Bulgaria'),('BF','Burkina Faso'),('BI','Burundi'),('KH','Cambodia'),('CM','Cameroon'),('CA','Canada'),('CV','Cape Verde'),('CF','Central African Republic'),('TD','Chad'),('CL','Chile'),('CN','Chinaf'),('CO','Colombia'),('KM','Comoros'),('CD','Congo Kinshasa'),('CG','Congo Brazzaville'),('CR','Costa Rica'),('CI','Ivory Coast'),('HR','Croatia'),('CU','Cuba'),('CY','Cyprus'),('CZ','Czech Republic'),('DJ','Djibouti'),('DM','Dominica'),('DO','Dominican Republic'),('EC','Ecuador'),('EG','Egypt'),('SV','El Salvador'),('GQ','Equatorial Guinea'),('ER','Eritrea'),('EE','Estonia'),('ET','Ethiopia'),('FJ','Fiji'),('FI','Finland'),('FR','France'),('GA','Gabon'),('GM','Gambia, The'),('GE','Georgia'),('GH','Ghana'),('GR','Greece'),('GD','Grenada'),('GT','Guatemala'),('GN','Guinea'),('GW','Guinea-Bissau'),('GY','Guyana'),('HT','Haiti'),('HN','Honduras'),('HU','Hungary'),('IS','Iceland'),('IN','India'),('ID','Indonesia'),('IR','Iran'),('IQ','Iraq'),('IE','Ireland'),('IL','Israel'),('JM','Jamaica'),('JP','Japan'),('JO','Jordan'),('KZ','Kazakhstan'),('KE','Kenya'),('KI','Kiribati'),('KP','Korea, North'),('KR','Korea, South'),('KW','Kuwait'),('KG','Kyrgyzstan'),('LA','Laos'),('LV','Latvia'),('LB','Lebanon'),('LS','Lesotho'),('LR','Liberia'),('LY','Libya'),('LI','Liechtenstein'),('LT','Lithuania'),('LU','Luxembourg'),('MK','Macedonia'),('MG','Madagascar'),('MW','Malawi'),('MY','Malaysia'),('MV','Maldives'),('ML','Mali'),('MT','Malta'),('MH','Marshall Islands'),('MR','Mauritania'),('MU','Mauritius'),('MX','Mexico'),('FM','Micronesia'),('MD','Moldova'),('MC','Monaco'),('MN','Mongolia'),('ME','Montenegro'),('MA','Morocco'),('MZ','Mozambique'),('MM','Myanmar'),('NA','Namibia'),('NR','Nauru'),('NP','Nepal'),('NZ','New Zealand'),('NI','Nicaragua'),('NE','Niger'),('NG','Nigeria'),('NO','Norway'),('OM','Oman'),('PK','Pakistan'),('PW','Palau'),('PA','Panama'),('PG','Papua New Guinea'),('PY','Paraguay'),('PE','Peru'),('PH','Philippines'),('PL','Poland'),('PT','Portugal'),('QA','Qatar'),('RO','Romania'),('RU','Russia'),('RW','Rwanda'),('KN','Saint Kitts and Nevis'),('LC','Saint Lucia'),('VC','Saint Vincent and the Grenadines'),('WS','Samoa'),('SM','San Marino'),('ST','Sao Tome and Principe'),('SA','Saudi Arabia'),('SN','Senegal'),('RS','Serbia'),('SC','Seychelles'),('SL','Sierra Leone'),('SG','Singapore'),('SK','Slovakia'),('SI','Slovenia'),('SB','Solomon Islands'),('SO','Somalia'),('ZA','South Africa'),('ES','Spain'),('LK','Sri Lanka'),('SD','Sudan'),('SR','Suriname'),('SZ','Swaziland'),('SE','Sweden'),('SY','Syria'),('TJ','Tajikistan'),('TZ','Tanzania'),('TH','Thailand'),('TL','Timor-Leste (East Timor)'),('TG','Togo'),('TO','Tonga'),('TT','Trinidad and Tobago'),('TN','Tunisia'),('TR','Turkey'),('TM','Turkmenistan'),('TV','Tuvalu'),('UG','Uganda'),('UA','Ukraine'),('AE','United Arab Emirates'),('UY','Uruguay'),('UZ','Uzbekistan'),('VU','Vanuatu'),('VA','Vatican City'),('VE','Venezuela'),('VN','Vietnam'),('YE','Yemen'),('ZM','Zambia'),('ZW','Zimbabwe'),('GE','Abkhazia'),('TW','Taiwan'),('AZ','Nagorno-Karabakh'),('CY','Northern Cyprus'),('MD','Pridnestrovie (Transnistria)'),('SO','Somaliland'),('GE','South Ossetia'),('AU','Ashmore and Cartier Islands'),('CX','Christmas Island'),('CC','Cocos (Keeling) Islands'),('AU','Coral Sea Islands'),('HM','Heard Island and McDonald Islands'),('NF','Norfolk Island'),('NC','New Caledonia'),('PF','French Polynesia'),('YT','Mayotte'),('GP','Saint Barthelemy'),('GP','Saint Martin'),('PM','Saint Pierre and Miquelon'),('WF','Wallis and Futuna'),('TF','French Southern and Antarctic Lands'),('PF','Clipperton Island'),('BV','Bouvet Island'),('CK','Cook Islands'),('NU','Niue'),('TK','Tokelau'),('GG','Guernsey'),('IM','Isle of Man'),('JE','Jersey'),('AI','Anguilla'),('BM','Bermuda'),('IO','British Indian Ocean Territory'),('VG','British Virgin Islands'),('KY','Cayman Islands'),('FK','Falkland Islands (Islas Malvinas)'),('GI','Gibraltar'),('MS','Montserrat'),('PN','Pitcairn Islands'),('SH','Saint Helena'),('GS','South Georgia and South Sandwich Islands'),('TC','Turks and Caicos Islands'),('MP','Northern Mariana Islands'),('PR','Puerto Rico'),('AS','American Samoa'),('UM','Baker Island'),('GU','Guam'),('UM','Howland Island'),('UM','Jarvis Island'),('UM','Johnston Atoll'),('UM','Kingman Reef'),('UM','Midway Islands'),('UM','Navassa Island'),('UM','Palmyra Atoll'),('VI','US Virgin Islands'),('UM','Wake Island'),('HK','Hong Kong'),('MO','Macau'),('FO','Faroe Islands'),('GL','Greenland'),('GF','French Guiana'),('GP','Guadeloupe'),('MQ','Martinique'),('RE','Reunion'),('AX','Aland'),('AW','Aruba'),('AN','Netherlands Antilles'),('SJ','Svalbard'),('AC','Ascension'),('TA','Tristan da Cunha'),('AQ','Australian Antarctic Territory'),('AQ','Ross Dependency'),('AQ','Peter I Island'),('AQ','Queen Maud Land'),('AQ','British Antarctic Territory'),)

    name                = models.CharField(max_length=3, choices=COUNTRIES, primary_key=True, blank=False, default='DE')
    created             = models.DateTimeField(auto_now_add=True, blank=False)
    updated             = models.DateTimeField(auto_now_add=True, blank=True)
    vat_rate            = models.IntegerField(default=0, blank=True)
    category            = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
    currency            = models.CharField(max_length=3, choices=CURRENCIES, blank=True)

    def __unicode__(self):
        return self.get_name_display()

    class Meta:
        ordering            = ('name',)
        app_label           = 'api'
        verbose_name        = 'Country'
        verbose_name_plural = 'Countries'


class Country_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = (
                    'created',
                    'updated',
                    'name',
                    'vat_rate',
                    'category',
                    'currency'
                 )
