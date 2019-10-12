import json

INIT_ICON_SQL = 'UPDATE arc_sys_menu SET icon_cls = \'{}\' WHERE href = \'{}\';'
INIT_SQL_USE_ID = 'UPDATE arc_sys_menu SET href = \'{}\' WHERE id = {};'


def read_menu_from_json(menus):
    result = []
    for menu in menus:
        identify = menu['node']['name']
        if menu['node']['scriptid']:
            identify = identify + str(menu['node']['scriptid'])
        temp_menu = {
            'identify': identify,
            'id': menu['node']['id'],
            'name': menu['node']['name'],
            'iconCls': menu['node']['iconCls'],
            'scriptid': menu['node']['scriptid'],
            'remark': menu['node']['remark'],
            'href': menu['node']['href']
        }
        result.append(temp_menu)
        if menu['children'] and len(menu['children']) > 0:
            child_menu = read_menu_from_json(menu['children'])
            [result.append(child) for child in child_menu]
    return result


def read_menu_file(menu_file):
    with open(menu_file, mode="r", encoding='utf-8') as f:
        menu_arr = json.load(f)
        return read_menu_from_json(menu_arr)


def print_update_icon_sql(menus):
    for menu in menus:
        if menu['iconCls']:
            print(INIT_ICON_SQL.format(menu['iconCls'], menu['href']))


def print_update_href_sql(menus):
    for menu in menus:
        print(INIT_SQL_USE_ID.format(menu['href'], menu['id']))


def print_name_href(menus):
    for menu in menus:
        print(menu['name'] + ':' + menu['href'])


def print_id_name(menus):
    for menu in menus:
        print(str(menu['id']) + ':' + menu['name'])


menu_file_name = "./list.json"
all_menu_file_name = "./all_menu.json"

menu_list = read_menu_file(menu_file_name)
all_menu_list = read_menu_file(all_menu_file_name)
menu_list.sort(key=lambda m: m['id'])
# print_update_icon_sql(menu_list)
# print_update_icon_sql(all_menu_list)
print_id_name(all_menu_list)
# print_name_href(menu_list)
