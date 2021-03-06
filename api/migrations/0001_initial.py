# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Core_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=250)),
                ('logo', models.ImageField(upload_to=b'images', blank=True)),
                ('contact_person', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=125)),
                ('zip_code', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, blank=True)),
                ('website', models.URLField(max_length=250, blank=True)),
                ('banking_account_recipient', models.CharField(max_length=100, blank=True)),
                ('banking_account_bank', models.CharField(max_length=100, blank=True)),
                ('banking_account_iban', models.CharField(max_length=100, blank=True)),
                ('banking_account_bic', models.CharField(max_length=100, blank=True)),
                ('tax_number', models.CharField(max_length=100, verbose_name=b'Tax number', blank=True)),
                ('vat_number', models.CharField(max_length=100, verbose_name=b'VAT number', blank=True)),
                ('eori_number', models.CharField(help_text=b'Economic Operators\xe2\x80\x99 Registration and Identification number used in customs declarations', max_length=100, verbose_name=b'EORI number', blank=True)),
            ],
            options={
                'verbose_name': 'Core_data',
                'verbose_name_plural': 'Core data',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(default=b'DE', max_length=3, serialize=False, primary_key=True, choices=[(b'DE', b'Deutschland'), (b'CH', b'Schweiz'), (b'GB', b'United Kingdom'), (b'US', b'United States'), (b'IT', b'Italy'), (b'AT', b'\xc3\x96sterreich'), (b'NL', b'Netherlands'), (b'DK', b'Denmark'), (b'AF', b'Afghanistan'), (b'AL', b'Albania'), (b'DZ', b'Algeria'), (b'AD', b'Andorra'), (b'AO', b'Angola'), (b'AG', b'Antigua and Barbuda'), (b'AR', b'Argentina'), (b'AM', b'Armenia'), (b'AU', b'Australia'), (b'AZ', b'Azerbaijan'), (b'BS', b'Bahamas, The'), (b'BH', b'Bahrain'), (b'BD', b'Bangladesh'), (b'BB', b'Barbados'), (b'BY', b'Belarus'), (b'BE', b'Belgium'), (b'BZ', b'Belize'), (b'BJ', b'Benin'), (b'BT', b'Bhutan'), (b'BO', b'Bolivia'), (b'BA', b'Bosnia and Herzegovina'), (b'BW', b'Botswana'), (b'BR', b'Brazil'), (b'BN', b'Brunei'), (b'BG', b'Bulgaria'), (b'BF', b'Burkina Faso'), (b'BI', b'Burundi'), (b'KH', b'Cambodia'), (b'CM', b'Cameroon'), (b'CA', b'Canada'), (b'CV', b'Cape Verde'), (b'CF', b'Central African Republic'), (b'TD', b'Chad'), (b'CL', b'Chile'), (b'CN', b'Chinaf'), (b'CO', b'Colombia'), (b'KM', b'Comoros'), (b'CD', b'Congo \xc2\x96Kinshasa'), (b'CG', b'Congo \xc2\x96Brazzaville'), (b'CR', b'Costa Rica'), (b'CI', b'Ivory Coast'), (b'HR', b'Croatia'), (b'CU', b'Cuba'), (b'CY', b'Cyprus'), (b'CZ', b'Czech Republic'), (b'DJ', b'Djibouti'), (b'DM', b'Dominica'), (b'DO', b'Dominican Republic'), (b'EC', b'Ecuador'), (b'EG', b'Egypt'), (b'SV', b'El Salvador'), (b'GQ', b'Equatorial Guinea'), (b'ER', b'Eritrea'), (b'EE', b'Estonia'), (b'ET', b'Ethiopia'), (b'FJ', b'Fiji'), (b'FI', b'Finland'), (b'FR', b'France'), (b'GA', b'Gabon'), (b'GM', b'Gambia, The'), (b'GE', b'Georgia'), (b'GH', b'Ghana'), (b'GR', b'Greece'), (b'GD', b'Grenada'), (b'GT', b'Guatemala'), (b'GN', b'Guinea'), (b'GW', b'Guinea-Bissau'), (b'GY', b'Guyana'), (b'HT', b'Haiti'), (b'HN', b'Honduras'), (b'HU', b'Hungary'), (b'IS', b'Iceland'), (b'IN', b'India'), (b'ID', b'Indonesia'), (b'IR', b'Iran'), (b'IQ', b'Iraq'), (b'IE', b'Ireland'), (b'IL', b'Israel'), (b'JM', b'Jamaica'), (b'JP', b'Japan'), (b'JO', b'Jordan'), (b'KZ', b'Kazakhstan'), (b'KE', b'Kenya'), (b'KI', b'Kiribati'), (b'KP', b'Korea, North'), (b'KR', b'Korea, South'), (b'KW', b'Kuwait'), (b'KG', b'Kyrgyzstan'), (b'LA', b'Laos'), (b'LV', b'Latvia'), (b'LB', b'Lebanon'), (b'LS', b'Lesotho'), (b'LR', b'Liberia'), (b'LY', b'Libya'), (b'LI', b'Liechtenstein'), (b'LT', b'Lithuania'), (b'LU', b'Luxembourg'), (b'MK', b'Macedonia'), (b'MG', b'Madagascar'), (b'MW', b'Malawi'), (b'MY', b'Malaysia'), (b'MV', b'Maldives'), (b'ML', b'Mali'), (b'MT', b'Malta'), (b'MH', b'Marshall Islands'), (b'MR', b'Mauritania'), (b'MU', b'Mauritius'), (b'MX', b'Mexico'), (b'FM', b'Micronesia'), (b'MD', b'Moldova'), (b'MC', b'Monaco'), (b'MN', b'Mongolia'), (b'ME', b'Montenegro'), (b'MA', b'Morocco'), (b'MZ', b'Mozambique'), (b'MM', b'Myanmar'), (b'NA', b'Namibia'), (b'NR', b'Nauru'), (b'NP', b'Nepal'), (b'NZ', b'New Zealand'), (b'NI', b'Nicaragua'), (b'NE', b'Niger'), (b'NG', b'Nigeria'), (b'NO', b'Norway'), (b'OM', b'Oman'), (b'PK', b'Pakistan'), (b'PW', b'Palau'), (b'PA', b'Panama'), (b'PG', b'Papua New Guinea'), (b'PY', b'Paraguay'), (b'PE', b'Peru'), (b'PH', b'Philippines'), (b'PL', b'Poland'), (b'PT', b'Portugal'), (b'QA', b'Qatar'), (b'RO', b'Romania'), (b'RU', b'Russia'), (b'RW', b'Rwanda'), (b'KN', b'Saint Kitts and Nevis'), (b'LC', b'Saint Lucia'), (b'VC', b'Saint Vincent and the Grenadines'), (b'WS', b'Samoa'), (b'SM', b'San Marino'), (b'ST', b'Sao Tome and Principe'), (b'SA', b'Saudi Arabia'), (b'SN', b'Senegal'), (b'RS', b'Serbia'), (b'SC', b'Seychelles'), (b'SL', b'Sierra Leone'), (b'SG', b'Singapore'), (b'SK', b'Slovakia'), (b'SI', b'Slovenia'), (b'SB', b'Solomon Islands'), (b'SO', b'Somalia'), (b'ZA', b'South Africa'), (b'ES', b'Spain'), (b'LK', b'Sri Lanka'), (b'SD', b'Sudan'), (b'SR', b'Suriname'), (b'SZ', b'Swaziland'), (b'SE', b'Sweden'), (b'SY', b'Syria'), (b'TJ', b'Tajikistan'), (b'TZ', b'Tanzania'), (b'TH', b'Thailand'), (b'TL', b'Timor-Leste (East Timor)'), (b'TG', b'Togo'), (b'TO', b'Tonga'), (b'TT', b'Trinidad and Tobago'), (b'TN', b'Tunisia'), (b'TR', b'Turkey'), (b'TM', b'Turkmenistan'), (b'TV', b'Tuvalu'), (b'UG', b'Uganda'), (b'UA', b'Ukraine'), (b'AE', b'United Arab Emirates'), (b'UY', b'Uruguay'), (b'UZ', b'Uzbekistan'), (b'VU', b'Vanuatu'), (b'VA', b'Vatican City'), (b'VE', b'Venezuela'), (b'VN', b'Vietnam'), (b'YE', b'Yemen'), (b'ZM', b'Zambia'), (b'ZW', b'Zimbabwe'), (b'GE', b'Abkhazia'), (b'TW', b'Taiwan'), (b'AZ', b'Nagorno-Karabakh'), (b'CY', b'Northern Cyprus'), (b'MD', b'Pridnestrovie (Transnistria)'), (b'SO', b'Somaliland'), (b'GE', b'South Ossetia'), (b'AU', b'Ashmore and Cartier Islands'), (b'CX', b'Christmas Island'), (b'CC', b'Cocos (Keeling) Islands'), (b'AU', b'Coral Sea Islands'), (b'HM', b'Heard Island and McDonald Islands'), (b'NF', b'Norfolk Island'), (b'NC', b'New Caledonia'), (b'PF', b'French Polynesia'), (b'YT', b'Mayotte'), (b'GP', b'Saint Barthelemy'), (b'GP', b'Saint Martin'), (b'PM', b'Saint Pierre and Miquelon'), (b'WF', b'Wallis and Futuna'), (b'TF', b'French Southern and Antarctic Lands'), (b'PF', b'Clipperton Island'), (b'BV', b'Bouvet Island'), (b'CK', b'Cook Islands'), (b'NU', b'Niue'), (b'TK', b'Tokelau'), (b'GG', b'Guernsey'), (b'IM', b'Isle of Man'), (b'JE', b'Jersey'), (b'AI', b'Anguilla'), (b'BM', b'Bermuda'), (b'IO', b'British Indian Ocean Territory'), (b'VG', b'British Virgin Islands'), (b'KY', b'Cayman Islands'), (b'FK', b'Falkland Islands (Islas Malvinas)'), (b'GI', b'Gibraltar'), (b'MS', b'Montserrat'), (b'PN', b'Pitcairn Islands'), (b'SH', b'Saint Helena'), (b'GS', b'South Georgia and South Sandwich Islands'), (b'TC', b'Turks and Caicos Islands'), (b'MP', b'Northern Mariana Islands'), (b'PR', b'Puerto Rico'), (b'AS', b'American Samoa'), (b'UM', b'Baker Island'), (b'GU', b'Guam'), (b'UM', b'Howland Island'), (b'UM', b'Jarvis Island'), (b'UM', b'Johnston Atoll'), (b'UM', b'Kingman Reef'), (b'UM', b'Midway Islands'), (b'UM', b'Navassa Island'), (b'UM', b'Palmyra Atoll'), (b'VI', b'US Virgin Islands'), (b'UM', b'Wake Island'), (b'HK', b'Hong Kong'), (b'MO', b'Macau'), (b'FO', b'Faroe Islands'), (b'GL', b'Greenland'), (b'GF', b'French Guiana'), (b'GP', b'Guadeloupe'), (b'MQ', b'Martinique'), (b'RE', b'Reunion'), (b'AX', b'Aland'), (b'AW', b'Aruba'), (b'AN', b'Netherlands Antilles'), (b'SJ', b'Svalbard'), (b'AC', b'Ascension'), (b'TA', b'Tristan da Cunha'), (b'AQ', b'Australian Antarctic Territory'), (b'AQ', b'Ross Dependency'), (b'AQ', b'Peter I Island'), (b'AQ', b'Queen Maud Land'), (b'AQ', b'British Antarctic Territory')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('vat_rate', models.IntegerField(default=0, blank=True)),
                ('category', models.CharField(blank=True, max_length=20, choices=[(b'eu28', b'EU28'), (b'efta', b'EFTA')])),
                ('currency', models.CharField(blank=True, max_length=3, choices=[(b'other', b'Other currency'), (b'EUR', b'Euro'), (b'GBP', b'British Pound'), (b'CAD', b'Canadian Dollar'), (b'DKK', b'Danish Krone'), (b'NOK', b'Norwegian Krone'), (b'RUB', b'Russian Rubel'), (b'SEK', b'Swedish Krona'), (b'CHF', b'Swiss Franken'), (b'USD', b'US Dollar')])),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('items_bought', models.IntegerField(default=0, blank=True)),
                ('wants_newsletter', models.BooleanField(default=True)),
                ('language', models.CharField(default=b'DE', max_length=2, choices=[(b'DE', b'German'), (b'EN', b'English')])),
                ('gender', models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('given_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50, blank=True)),
                ('email', models.EmailField(max_length=50, blank=True)),
                ('address', models.CharField(max_length=125, blank=True)),
                ('zip_code', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
                ('facebook', models.URLField(max_length=250, blank=True)),
                ('twitter', models.URLField(max_length=250, blank=True)),
                ('instagram', models.URLField(max_length=250, blank=True)),
                ('pinterest', models.URLField(max_length=250, blank=True)),
                ('country', models.ForeignKey(to='api.Country', blank=True)),
            ],
            options={
                'ordering': ('given_name', 'surname'),
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('color_1_en', models.CharField(max_length=50, verbose_name=b'Main color in English')),
                ('color_2_en', models.CharField(max_length=50, verbose_name=b'Second color in English', blank=True)),
                ('image', models.ImageField(upload_to=b'images', blank=True)),
                ('perspective', models.CharField(blank=True, max_length=10, choices=[(b'front', b'Front'), (b'side', b'Side'), (b'back', b'Back'), (b'detail', b'Detail')])),
                ('photographer', models.CharField(max_length=50, blank=True)),
                ('year', models.SmallIntegerField(help_text=b'When was this photo taken?', blank=True)),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Invoice_address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('recipient', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=125, blank=True)),
                ('zip_code', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=50)),
                ('vat_number', models.CharField(max_length=250, blank=True)),
                ('tax_number', models.CharField(max_length=250, blank=True)),
            ],
            options={
                'ordering': ('recipient',),
                'verbose_name': 'Invoice address',
                'verbose_name_plural': 'Invoice addresses',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=0, blank=True)),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listings',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField(default=0)),
                ('body', models.TextField()),
                ('content_type', models.ForeignKey(default=0, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Internal note',
                'verbose_name_plural': 'Internal notes',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('language', models.CharField(default=b'DE', max_length=2, choices=[(b'DE', b'German'), (b'EN', b'English')])),
                ('partner_type', models.CharField(default=b'seller', max_length=25, choices=[(b'seller', b'Seller'), (b'producer', b'Producer'), (b'agency', b'Agent'), (b'other', b'Other')])),
                ('gender', models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('given_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('phone_1', models.CharField(max_length=50, blank=True)),
                ('phone_2', models.CharField(max_length=50, blank=True)),
                ('email_1', models.EmailField(max_length=50, blank=True)),
                ('email_2', models.EmailField(max_length=50, blank=True)),
            ],
            options={
                'ordering': ('given_name', 'surname'),
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50, choices=[(b'coat', b'Coat'), (b'dress', b'Dress'), (b'jacket', b'Jacket'), (b'longsleeve', b'Longsleeve'), (b'pullover', b'Pullover'), (b'shirt', b'Shirt'), (b'skirt', b'Skirt'), (b'trousers', b'Trousers'), (b'other', b'Other')])),
                ('target_group', models.CharField(default=b'unisex', max_length=6, choices=[(b'women', b'Women'), (b'men', b'Men'), (b'unisex', b'unisex')])),
                ('description_de', models.TextField(max_length=500, verbose_name=b'German description', blank=True)),
                ('description_en', models.TextField(max_length=500, verbose_name=b'English description', blank=True)),
                ('description_it', models.TextField(max_length=500, verbose_name=b'Italian description', blank=True)),
            ],
            options={
                'ordering': ('-name',),
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Product_move',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('move_date', models.DateTimeField(default=datetime.datetime.now)),
                ('move_type', models.CharField(max_length=20, choices=[(b'moved_to_store', b'Moved to store'), (b'non_saleable', b'Marked as non-saleable')])),
            ],
            options={
                'ordering': ('move_date',),
                'verbose_name': 'Product move',
                'verbose_name_plural': 'Product moves',
            },
        ),
        migrations.CreateModel(
            name='Product_variant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_organic', models.BooleanField(default=False, help_text=b'Is this product variant made from organic materials?', verbose_name=b'Organic')),
                ('rec_gross_sale_price_default', models.DecimalField(default=0, verbose_name=b'Recommended default gross sale price in EURO', max_digits=6, decimal_places=2, blank=True)),
                ('size', models.CharField(default=b'unisize', max_length=7, choices=[(b'unisize', b'Unisize'), (b's', b'S'), (b'xs', b'XS'), (b'm', b'M'), (b'l', b'L'), (b'xl', b'XL'), (b'xxl', b'XXL'), (b'ws', b'Women S'), (b'wxs', b'Women XS'), (b'wm', b'Women M'), (b'wl', b'Women L'), (b'wxl', b'Women XL'), (b'ms', b'Men S'), (b'mxs', b'Men XS'), (b'mm', b'Men M'), (b'ml', b'Men L'), (b'mxl', b'Men XL'), (b'mxxl', b'Men XXL')])),
                ('description_de', models.TextField(max_length=500, verbose_name=b'German description', blank=True)),
                ('description_en', models.TextField(max_length=500, verbose_name=b'English description', blank=True)),
                ('description_it', models.TextField(max_length=500, verbose_name=b'Italian description', blank=True)),
                ('care_instructions_de', models.TextField(max_length=250, verbose_name=b'German care instructions', blank=True)),
                ('care_instructions_en', models.TextField(max_length=250, verbose_name=b'English care instructions', blank=True)),
                ('care_instructions_it', models.TextField(max_length=250, verbose_name=b'Italian care instructions', blank=True)),
                ('color_1_de', models.CharField(max_length=50, verbose_name=b'Main color in German')),
                ('color_1_en', models.CharField(max_length=50, verbose_name=b'Main color in English')),
                ('color_1_it', models.CharField(max_length=50, verbose_name=b'Main color in Italian')),
                ('color_2_de', models.CharField(max_length=50, verbose_name=b'2nd color in German', blank=True)),
                ('color_2_en', models.CharField(max_length=50, verbose_name=b'2nd color in English', blank=True)),
                ('color_2_it', models.CharField(max_length=50, verbose_name=b'2nd color in Italian', blank=True)),
                ('color_3_de', models.CharField(max_length=50, verbose_name=b'3rd color in German', blank=True)),
                ('color_3_en', models.CharField(max_length=50, verbose_name=b'3rd color in English', blank=True)),
                ('color_3_it', models.CharField(max_length=50, verbose_name=b'3rd color in Italian', blank=True)),
                ('color_4_de', models.CharField(max_length=50, verbose_name=b'4th color in German', blank=True)),
                ('color_4_en', models.CharField(max_length=50, verbose_name=b'4th color in English', blank=True)),
                ('color_4_it', models.CharField(max_length=50, verbose_name=b'4th color in Italian', blank=True)),
                ('fabric_1_de', models.CharField(max_length=50, verbose_name=b'Main fabric in German')),
                ('fabric_1_en', models.CharField(max_length=50, verbose_name=b'Main fabric in English')),
                ('fabric_1_it', models.CharField(max_length=50, verbose_name=b'Main fabric in Italian')),
                ('fabric_2_de', models.CharField(max_length=50, verbose_name=b'2nd fabric in German', blank=True)),
                ('fabric_2_en', models.CharField(max_length=50, verbose_name=b'2nd fabric in English', blank=True)),
                ('fabric_2_it', models.CharField(max_length=50, verbose_name=b'2nd fabric in Italian', blank=True)),
                ('fabric_3_de', models.CharField(max_length=50, verbose_name=b'3nd fabric in German', blank=True)),
                ('fabric_3_en', models.CharField(max_length=50, verbose_name=b'3nd fabric in English', blank=True)),
                ('fabric_3_it', models.CharField(max_length=50, verbose_name=b'3nd fabric in Italian', blank=True)),
                ('fabric_4_de', models.CharField(max_length=50, verbose_name=b'4nd fabric in German', blank=True)),
                ('fabric_4_en', models.CharField(max_length=50, verbose_name=b'4nd fabric in English', blank=True)),
                ('fabric_4_it', models.CharField(max_length=50, verbose_name=b'4nd fabric in Italian', blank=True)),
                ('fabric_1_percentage', models.IntegerField(default=100, help_text=b'Percentage of the main fabric in %', verbose_name=b'Percentage main fabric', blank=True)),
                ('fabric_2_percentage', models.IntegerField(default=0, help_text=b'Percentage of 2nd fabric in %', verbose_name=b'Percentage 2nd fabric', blank=True)),
                ('fabric_3_percentage', models.IntegerField(default=0, help_text=b'Percentage of 3rd fabric in %', verbose_name=b'Percentage 3rd fabric', blank=True)),
                ('fabric_4_percentage', models.IntegerField(default=0, help_text=b'Percentage of 4th fabric in %', verbose_name=b'Percentage 4th fabric', blank=True)),
                ('weight', models.SmallIntegerField(default=0, help_text=b'Product weight in grams', blank=True)),
                ('surface_weight', models.SmallIntegerField(default=0, help_text=b'Product surface weight in grams/m\xc2\xb2', blank=True)),
                ('images', models.ManyToManyField(to='api.Image', blank=True)),
                ('product', models.ForeignKey(default=1, to='api.Product')),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': 'Product variant',
                'verbose_name_plural': 'Product variants',
            },
        ),
        migrations.CreateModel(
            name='Product_variant_price_per_country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('rec_gross_sale_price', models.DecimalField(default=0, verbose_name=b'Recommended gross sale price in the currency of the country', max_digits=6, decimal_places=2)),
                ('country', models.ForeignKey(to='api.Country')),
                ('product_variant', models.ForeignKey(to='api.Product_variant')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Product variant price per country',
                'verbose_name_plural': 'Product variant prices per country',
            },
        ),
        migrations.CreateModel(
            name='Product_variant_price_per_store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('rec_gross_sale_price', models.DecimalField(default=0, verbose_name=b'Recommended gross sale price in this store and in the currency of the stores country', max_digits=6, decimal_places=2)),
                ('product_variant', models.ForeignKey(to='api.Product_variant')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Product variant price per store',
                'verbose_name_plural': 'Product variant prices per store',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('sale_date', models.DateTimeField(default=datetime.datetime.now)),
                ('sale_type', models.CharField(max_length=20, choices=[(b'direct-sale-to-customer', b'Direct sale to customer'), (b'online-sale', b'Online sale'), (b'commission-sale', b'Commission sale'), (b'sale-to-store', b'Sale to store'), (b'sale-to-store-via-agency', b'Sale to store via agency'), (b'other', b'Other')])),
                ('sold_to_customer', models.ForeignKey(related_name='soldtocustomer', blank=True, to='api.Customer', null=True)),
            ],
            options={
                'ordering': ('sale_date',),
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='Shipping_address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('recipient', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=125, blank=True)),
                ('addition_to_address', models.CharField(max_length=200, blank=True)),
                ('zip_code', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=50)),
                ('contact_person', models.ForeignKey(default=1, to='api.Person')),
                ('country', models.ForeignKey(to='api.Country', blank=True)),
            ],
            options={
                'ordering': ('recipient',),
                'verbose_name': 'Shipping address',
                'verbose_name_plural': 'Shipping addresses',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_online_shop', models.BooleanField(default=False)),
                ('in_acquisition', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=125, blank=True)),
                ('zip_code', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=50)),
                ('shipping_agrement', models.CharField(default=b'split', max_length=20, blank=True, choices=[(b'store_pays', b'Store pays shippings costs'), (b'split', b'Shipping costs are split'), (b'we_pay', b'We pay shipping costs')])),
                ('partner_type', models.CharField(blank=True, max_length=20, choices=[(b'commission', b'Commission'), (b'direct_buyer', b'Direct buyer'), (b'mixed', b'Mixed')])),
                ('commission_rate', models.IntegerField(default=50, help_text=b'Commmission as charged by the store in %', blank=True)),
                ('website', models.URLField(max_length=250, blank=True)),
                ('facebook', models.URLField(max_length=250, blank=True)),
                ('twitter', models.URLField(max_length=250, blank=True)),
                ('instagram', models.URLField(max_length=250, blank=True)),
                ('pinterest', models.URLField(max_length=250, blank=True)),
                ('country', models.ForeignKey(to='api.Country', blank=True)),
                ('invoice_address', models.ForeignKey(default=1, blank=True, to='api.Invoice_address')),
                ('shipping_address', models.ForeignKey(default=1, blank=True, to='api.Shipping_address')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
            },
        ),
        migrations.AddField(
            model_name='sale',
            name='sold_to_store',
            field=models.ForeignKey(related_name='soldtostore', blank=True, to='api.Store', null=True),
        ),
        migrations.AddField(
            model_name='product_variant_price_per_store',
            name='store',
            field=models.ForeignKey(to='api.Store'),
        ),
        migrations.AddField(
            model_name='product_move',
            name='move_to',
            field=models.ForeignKey(related_name='moveto', verbose_name=b'Move from store', blank=True, to='api.Store', null=True),
        ),
        migrations.AddField(
            model_name='product_move',
            name='remove_from',
            field=models.ForeignKey(verbose_name=b'Remove from store', blank=True, to='api.Store', null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='product_move_id',
            field=models.ForeignKey(blank=True, to='api.Product_move', null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='product_variant',
            field=models.ForeignKey(blank=True, to='api.Product_variant', null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='sale_id',
            field=models.ForeignKey(blank=True, to='api.Sale', null=True),
        ),
        migrations.AddField(
            model_name='invoice_address',
            name='contact_person',
            field=models.ForeignKey(default=1, to='api.Person'),
        ),
        migrations.AddField(
            model_name='invoice_address',
            name='country',
            field=models.ForeignKey(to='api.Country', blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(default=1, to='api.Product'),
        ),
        migrations.AddField(
            model_name='core_data',
            name='country',
            field=models.ForeignKey(default=b'DE', blank=True, to='api.Country'),
        ),
    ]
