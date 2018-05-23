from django.shortcuts import render,HttpResponse
from django.views import View
import json
# Create your views here.

class AssetView(View):
    def get(self, request, *args, **kwargs):

        return render(request,'asset.html')

class AssetJsonView(View):
    def get(self, request, *args, **kwargs):
        # table_config = [
        #     {
        #         'q': 'device_type_id',
        #         'title': '资产类型',
        #         'display': True,
        #         'text': {'content': "{n}", 'kwargs': {'n': "@@device_type_choices"}},
        #         'attrs': {}
        #     },
        #     {
        #         'q': 'id',
        #         'title':'ID',
        #         'display':0,
        #         'text': {'content': '{n}-{m}', 'kwargs': {'n': '@ID', 'm': 'xx'}}
        #     },
        #     {
        #         'q': 'cabinet_num',
        #         'title': '机柜号',
        #         'display': 1,
        #         'text': {'content': '{n}', 'kwargs': { 'n': '@cabinet_num'}}
        #     },
        #     {
        #         'q': 'idc__name',
        #         'title': 'IDC',
        #         'display': True,
        #         'text': {'content': "{n}", 'kwargs': {'n': "@idc__name"}},
        #         'attrs': {'edit-enable': 'true', 'edit-type': 'select'}
        #     },
        #     {
        #         'q': 'cabinet_order',
        #         'title': '机柜位置',
        #         'display': 1,
        #         'text': {'content': '{n}', 'kwargs': {'n': '@cabinet_order'}}
        #     },
        #
        #     {
        #         'q': 'device_status_id',
        #         'title': '状态',
        #         'display': True,
        #         'text': {'content': "{n}", 'kwargs': {'n': "@@device_status_choices"}},
        #         'attrs': {'edit-enable': 'true', 'edit-type': 'select'}
        #     },
        #     {
        #         'q': None,
        #         'title': '操作',
        #         'display': True,
        #         'text': {'content': "<a href='/assetdetail-{m}.html'>{n}</a>", 'kwargs': {'n': '查看详细', 'm': '@id'}},
        #     }
        # ]
        table_config = [
            {
                'q': None,
                'title': '选项',
                'display': True,
                'text': {'content': "<input type='checkbox'/>", 'kwargs': {}},
                'attrs': {}
            },
            {
                'q': 'id',
                'title': 'ID',
                'display': False,
                'text': {},
                'attrs': {}
            },
            {
                'q': 'device_type_id',
                'title': '资产类型',
                'display': True,
                'text': {'content': "{n}", 'kwargs': {'n': "@@device_type_choices"}},
                'attrs': {'origin':'@device_type_id','edit-enable': 'true', 'edit-type': 'select','global_name':'device_type_choices'}
            },
            {
                'q': 'device_status_id',
                'title': '状态',
                'display': True,
                'text': {'content': "{n}", 'kwargs': {'n': "@@device_status_choices"}},
                'attrs': {'origin':'@device_status_id','edit-enable': 'true', 'edit-type': 'select','global_name':'device_status_choices'}
            },
            {
                'q': 'idc__id',
                'title': 'IDC',
                'display': False,
                'text': {},
                'attrs': {}
            },
            {
                'q': 'idc__name',
                'title': 'IDC',
                'display': True,
                'text': {'content': "{n}", 'kwargs': {'n': "@idc__name"}},
                'attrs': {'origin':'@idc__id','edit-enable': 'true', 'edit-type': 'select','global_name':'idc_status_choices'}
            },
            {
                'q': 'cabinet_order',
                'title': '机柜位置',
                'display': True,
                'text': {'content': "{n}", 'kwargs': {'n': "@cabinet_order"}},
                'attrs': {'origin':'@cabinet_order','edit-enable': 'true', 'edit-type': 'input'}
            },
            {
                'q': 'cabinet_num',
                'title': '机柜号',
                'display': True,
                'text': {'content': "{n}", 'kwargs': {'n': "@cabinet_num"}},
                'attrs': {},
            },
            {
                'q': None,
                'title': '操作',
                'display': True,
                'text': {'content': "<a href='/assetdetail-{m}.html'>{n}</a>", 'kwargs': {'n': '查看详细', 'm': '@id'}},
                'attrs': {},
            }
        ]
        q_list = []
        for i in table_config:
            if not i['q']:
                continue
            q_list.append(i['q'])
        print(q_list)
        from repository import models
        data_list = models.Asset.objects.all().values(*q_list)
        data_list = list(data_list)
        print(data_list)
        global_dict = {
            'device_type_choices':models.Asset.device_type_choices,
            'device_status_choices':models.Asset.device_status_choices,
            'idc_status_choices':list(models.IDC.objects.values_list('id', 'name'))

        }
        result = {
            'table_config':table_config,
            'data_list':data_list,
            'global_dict':global_dict
        }
        return HttpResponse(json.dumps(result))



