from random import choice

import faker

f = faker.Faker('zh_CN')

# address
print('f.country(): {}'.format(f.country()))
print('f.country_code(): {}'.format(f.country_code()))
print('f.address(): {}'.format(f.address()))
print('f.city: {}'.format(f.city()))
print('f.city_name: {}'.format(f.city_name()))
print('f.city_suffix: {}'.format(f.city_suffix()))
print('f.street_name: {}'.format(f.street_name()))
print('f.postcode: {}'.format(f.postcode()))

# text
print('f.text: {}'.format(f.text(20)))
print('f.words: {}'.format(f.words(4)))

# person
print()
print('f.name: {}'.format(f.name()))
print('f.first_name: {}'.format(f.first_name()))
print('f.first_name_male: {}'.format(f.first_name_male()))
print('f.first_name_female: {}'.format(f.first_name_female()))
print('f.last_name: {}'.format(f.last_name()))
print('f.last_name_male: {}'.format(f.last_name_male()))
print('f.last_name_female: {}'.format(f.last_name_female()))
# phone
print()
print('f.phone_number: {}'.format(f.phone_number()))

# python
print()
print('f.pyfloat:{}'.format(f.pyfloat()))
print('f.pyint:{}'.format(f.pyint()))
print('f.pylist: {}'.format(f.pylist(3)))
print('f.py str: {}'.format(f.pystr()))
print('f.pydict: {}'.format(f.pydict(3)))

# job
print('f.job: {}'.format(f.job()))

# uuid
print('f.uuid4():{}'.format(f.uuid4()))
print('f.uuid4(cast_to=int):{}'.format(f.uuid4(cast_to=int)))
print('f.uuid4(cast_to=lambda x: x):{}'.format(f.uuid4(cast_to=lambda x: x)))

# internet
print('网络')
print('f.image_url(200, 300):{}'.format(f.image_url(200, 300)))
print('f.hostname():{}'.format(f.hostname()))
print('f.url():{}'.format(f.url()))
schemes_sets = [['usb'], ['ftp', 'file'], ['usb', 'telnet', 'http']]
print('f.url(schemes=): {}'.format(f.url(schemes=choice(schemes_sets))))
print('f.domain_name(): {}'.format(f.domain_name(10)))
print('f.tld(): {}'.format(f.tld()))
print('f.email(): {}'.format(f.email()))
print('f.domain_word(): {}'.format(f.domain_word()))

# geo
print('地理位置')
print('f.local_latlng(country_code=\'CN\'): {}'.format(f.local_latlng(country_code='CN')))
print('f.local_latlng(country_code=\'CN\', coords_only=True): {}'.format(
    f.local_latlng(country_code='US', coords_only=True)))
print('factory.longitude(): {}'.format(f.longitude()))
print('factory.latitude(): {}'.format(f.latitude()))
print('factory.coordinate(): {}'.format(f.coordinate()))
print('factory.coordinate(center=23): {}'.format(f.coordinate(center=23)))
print('factory.location_on_land(): {}'.format(f.location_on_land()))
print('f.location_on_land(coords_only=True): {}'.format(f.location_on_land(coords_only=True)))

# file
print('文件')
print('f.file_path(): {}'.format(f.file_path()))
print('f.unix_device(\'sdas\'): {}'.format(f.unix_device('sdas')))
print('f.file_path(category=\'image\'): {}'.format(f.file_path(category='image')))
print('f.file_path(depth=3): {}'.format(f.file_path(depth=4)))
print('f.file_path(extension=\'pdf\')): {}'.format(f.file_path(extension='pdf')))

print('f.unix_device(): {}'.format(f.unix_device()))
print('f.unix_partition(): {}'.format(f.unix_partition()))
print('f.unix_partition(\'sff\'): {}'.format(f.unix_partition('sff')))

# datetime
print('日期')
print('f.date_of_birth(minimum_age=0): {}'.format(f.date_of_birth(minimum_age=0)))
print('f.date_of_birth(minimum_age=20, maximum_age=22): {}'.format(f.date_of_birth(minimum_age=20, maximum_age=22)))

# 公司
print('公司')
print('f.company(): {}'.format(f.company()))
print('f.company_prefix(): {}'.format(f.company_prefix()))
print('f.company_suffix(): {}'.format(f.company_suffix()))

# color
print('颜色')
print('f.color_name(): {}'.format(f.color_name()))
print('f.safe_color_name(): {}'.format(f.safe_color_name()))
print('f.rgb_css_color(): {}'.format(f.rgb_css_color()))
print('f.hex_color(): {}'.format(f.hex_color()))
print('f.safe_hex_color(): {}'.format(f.safe_hex_color()))

# bank
print('银行账户')
print('f.bban(): {}'.format(f.bban()))
print('f.iban(): {}'.format(f.iban()))

# automotive
print('汽车')
print('f.license_plate(): {}'.format(f.license_plate()))
