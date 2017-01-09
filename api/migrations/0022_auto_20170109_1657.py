# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='stores',
            field=models.ManyToManyField(blank=True, help_text=b'Select the stores which are connected to this agency', to='api.Store'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(choices=[(b'DE', b'Deutschland'), (b'CH', b'Schweiz'), (b'GB', b'United Kingdom'), (b'US', b'United States'), (b'IT', b'Italy'), (b'AT', b'\xc3\x96sterreich'), (b'NL', b'Netherlands'), (b'DK', b'Denmark'), (b'AF', b'Afghanistan'), (b'AL', b'Albania'), (b'DZ', b'Algeria'), (b'AD', b'Andorra'), (b'AO', b'Angola'), (b'AG', b'Antigua and Barbuda'), (b'AR', b'Argentina'), (b'AM', b'Armenia'), (b'AU', b'Australia'), (b'AZ', b'Azerbaijan'), (b'BS', b'Bahamas, The'), (b'BH', b'Bahrain'), (b'BD', b'Bangladesh'), (b'BB', b'Barbados'), (b'BY', b'Belarus'), (b'BE', b'Belgium'), (b'BZ', b'Belize'), (b'BJ', b'Benin'), (b'BT', b'Bhutan'), (b'BO', b'Bolivia'), (b'BA', b'Bosnia and Herzegovina'), (b'BW', b'Botswana'), (b'BR', b'Brazil'), (b'BN', b'Brunei'), (b'BG', b'Bulgaria'), (b'BF', b'Burkina Faso'), (b'BI', b'Burundi'), (b'KH', b'Cambodia'), (b'CM', b'Cameroon'), (b'CA', b'Canada'), (b'CV', b'Cape Verde'), (b'CF', b'Central African Republic'), (b'TD', b'Chad'), (b'CL', b'Chile'), (b'CN', b'Chinaf'), (b'CO', b'Colombia'), (b'KM', b'Comoros'), (b'CD', b'Congo \xc2\x96Kinshasa'), (b'CG', b'Congo \xc2\x96Brazzaville'), (b'CR', b'Costa Rica'), (b'CI', b'Ivory Coast'), (b'HR', b'Croatia'), (b'CU', b'Cuba'), (b'CY', b'Cyprus'), (b'CZ', b'Czech Republic'), (b'DJ', b'Djibouti'), (b'DM', b'Dominica'), (b'DO', b'Dominican Republic'), (b'EC', b'Ecuador'), (b'EG', b'Egypt'), (b'SV', b'El Salvador'), (b'GQ', b'Equatorial Guinea'), (b'ER', b'Eritrea'), (b'EE', b'Estonia'), (b'ET', b'Ethiopia'), (b'FJ', b'Fiji'), (b'FI', b'Finland'), (b'FR', b'France'), (b'GA', b'Gabon'), (b'GM', b'Gambia, The'), (b'GE', b'Georgia'), (b'GH', b'Ghana'), (b'GR', b'Greece'), (b'GD', b'Grenada'), (b'GT', b'Guatemala'), (b'GN', b'Guinea'), (b'GW', b'Guinea-Bissau'), (b'GY', b'Guyana'), (b'HT', b'Haiti'), (b'HN', b'Honduras'), (b'HU', b'Hungary'), (b'IS', b'Iceland'), (b'IN', b'India'), (b'ID', b'Indonesia'), (b'IR', b'Iran'), (b'IQ', b'Iraq'), (b'IE', b'Ireland'), (b'IL', b'Israel'), (b'JM', b'Jamaica'), (b'JP', b'Japan'), (b'JO', b'Jordan'), (b'KZ', b'Kazakhstan'), (b'KE', b'Kenya'), (b'KI', b'Kiribati'), (b'KP', b'Korea, North'), (b'KR', b'Korea, South'), (b'KW', b'Kuwait'), (b'KG', b'Kyrgyzstan'), (b'LA', b'Laos'), (b'LV', b'Latvia'), (b'LB', b'Lebanon'), (b'LS', b'Lesotho'), (b'LR', b'Liberia'), (b'LY', b'Libya'), (b'LI', b'Liechtenstein'), (b'LT', b'Lithuania'), (b'LU', b'Luxembourg'), (b'MK', b'Macedonia'), (b'MG', b'Madagascar'), (b'MW', b'Malawi'), (b'MY', b'Malaysia'), (b'MV', b'Maldives'), (b'ML', b'Mali'), (b'MT', b'Malta'), (b'MH', b'Marshall Islands'), (b'MR', b'Mauritania'), (b'MU', b'Mauritius'), (b'MX', b'Mexico'), (b'FM', b'Micronesia'), (b'MD', b'Moldova'), (b'MC', b'Monaco'), (b'MN', b'Mongolia'), (b'ME', b'Montenegro'), (b'MA', b'Morocco'), (b'MZ', b'Mozambique'), (b'MM', b'Myanmar'), (b'NA', b'Namibia'), (b'NR', b'Nauru'), (b'NP', b'Nepal'), (b'NZ', b'New Zealand'), (b'NI', b'Nicaragua'), (b'NE', b'Niger'), (b'NG', b'Nigeria'), (b'NO', b'Norway'), (b'OM', b'Oman'), (b'PK', b'Pakistan'), (b'PW', b'Palau'), (b'PA', b'Panama'), (b'PG', b'Papua New Guinea'), (b'PY', b'Paraguay'), (b'PE', b'Peru'), (b'PH', b'Philippines'), (b'PL', b'Poland'), (b'PT', b'Portugal'), (b'QA', b'Qatar'), (b'RO', b'Romania'), (b'RU', b'Russia'), (b'RW', b'Rwanda'), (b'KN', b'Saint Kitts and Nevis'), (b'LC', b'Saint Lucia'), (b'VC', b'Saint Vincent and the Grenadines'), (b'WS', b'Samoa'), (b'SM', b'San Marino'), (b'ST', b'Sao Tome and Principe'), (b'SA', b'Saudi Arabia'), (b'SN', b'Senegal'), (b'RS', b'Serbia'), (b'SC', b'Seychelles'), (b'SL', b'Sierra Leone'), (b'SG', b'Singapore'), (b'SK', b'Slovakia'), (b'SI', b'Slovenia'), (b'SB', b'Solomon Islands'), (b'SO', b'Somalia'), (b'ZA', b'South Africa'), (b'ES', b'Spain'), (b'LK', b'Sri Lanka'), (b'SD', b'Sudan'), (b'SR', b'Suriname'), (b'SZ', b'Swaziland'), (b'SE', b'Sweden'), (b'SY', b'Syria'), (b'TJ', b'Tajikistan'), (b'TZ', b'Tanzania'), (b'TH', b'Thailand'), (b'TL', b'Timor-Leste (East Timor)'), (b'TG', b'Togo'), (b'TO', b'Tonga'), (b'TT', b'Trinidad and Tobago'), (b'TN', b'Tunisia'), (b'TR', b'Turkey'), (b'TM', b'Turkmenistan'), (b'TV', b'Tuvalu'), (b'UG', b'Uganda'), (b'UA', b'Ukraine'), (b'AE', b'United Arab Emirates'), (b'UY', b'Uruguay'), (b'UZ', b'Uzbekistan'), (b'VU', b'Vanuatu'), (b'VA', b'Vatican City'), (b'VE', b'Venezuela'), (b'VN', b'Vietnam'), (b'YE', b'Yemen'), (b'ZM', b'Zambia'), (b'ZW', b'Zimbabwe'), (b'GE', b'Abkhazia'), (b'TW', b'Taiwan'), (b'AZ', b'Nagorno-Karabakh'), (b'CY', b'Northern Cyprus'), (b'MD', b'Pridnestrovie (Transnistria)'), (b'SO', b'Somaliland'), (b'GE', b'South Ossetia'), (b'AU', b'Ashmore and Cartier Islands'), (b'CX', b'Christmas Island'), (b'CC', b'Cocos (Keeling) Islands'), (b'AU', b'Coral Sea Islands'), (b'HM', b'Heard Island and McDonald Islands'), (b'NF', b'Norfolk Island'), (b'NC', b'New Caledonia'), (b'PF', b'French Polynesia'), (b'YT', b'Mayotte'), (b'GP', b'Saint Barthelemy'), (b'GP', b'Saint Martin'), (b'PM', b'Saint Pierre and Miquelon'), (b'WF', b'Wallis and Futuna'), (b'TF', b'French Southern and Antarctic Lands'), (b'PF', b'Clipperton Island'), (b'BV', b'Bouvet Island'), (b'CK', b'Cook Islands'), (b'NU', b'Niue'), (b'TK', b'Tokelau'), (b'GG', b'Guernsey'), (b'IM', b'Isle of Man'), (b'JE', b'Jersey'), (b'AI', b'Anguilla'), (b'BM', b'Bermuda'), (b'IO', b'British Indian Ocean Territory'), (b'VG', b'British Virgin Islands'), (b'KY', b'Cayman Islands'), (b'FK', b'Falkland Islands (Islas Malvinas)'), (b'GI', b'Gibraltar'), (b'MS', b'Montserrat'), (b'PN', b'Pitcairn Islands'), (b'SH', b'Saint Helena'), (b'GS', b'South Georgia and South Sandwich Islands'), (b'TC', b'Turks and Caicos Islands'), (b'MP', b'Northern Mariana Islands'), (b'PR', b'Puerto Rico'), (b'AS', b'American Samoa'), (b'UM', b'Baker Island'), (b'GU', b'Guam'), (b'UM', b'Howland Island'), (b'UM', b'Jarvis Island'), (b'UM', b'Johnston Atoll'), (b'UM', b'Kingman Reef'), (b'UM', b'Midway Islands'), (b'UM', b'Navassa Island'), (b'UM', b'Palmyra Atoll'), (b'VI', b'US Virgin Islands'), (b'UM', b'Wake Island'), (b'HK', b'Hong Kong'), (b'MO', b'Macau'), (b'FO', b'Faroe Islands'), (b'GL', b'Greenland'), (b'GF', b'French Guiana'), (b'GP', b'Guadeloupe'), (b'MQ', b'Martinique'), (b'RE', b'Reunion'), (b'AX', b'Aland'), (b'AW', b'Aruba'), (b'AN', b'Netherlands Antilles'), (b'SJ', b'Svalbard'), (b'AC', b'Ascension'), (b'TA', b'Tristan da Cunha'), (b'AQ', b'Australian Antarctic Territory'), (b'AQ', b'Ross Dependency'), (b'AQ', b'Peter I Island'), (b'AQ', b'Queen Maud Land'), (b'AQ', b'British Antarctic Territory')], default=b'DE', max_length=3, primary_key=True, serialize=False),
        ),
    ]