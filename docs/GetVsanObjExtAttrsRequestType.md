# GetVsanObjExtAttrsRequestType

The parameters of *HostVsanInternalSystem.GetVsanObjExtAttrs*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | List of object UUIDs.  | 

## Example

```python
from vmware_vi.models.get_vsan_obj_ext_attrs_request_type import GetVsanObjExtAttrsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GetVsanObjExtAttrsRequestType from a JSON string
get_vsan_obj_ext_attrs_request_type_instance = GetVsanObjExtAttrsRequestType.from_json(json)
# print the JSON string representation of the object
print GetVsanObjExtAttrsRequestType.to_json()

# convert the object into a dict
get_vsan_obj_ext_attrs_request_type_dict = get_vsan_obj_ext_attrs_request_type_instance.to_dict()
# create an instance of GetVsanObjExtAttrsRequestType from a dict
get_vsan_obj_ext_attrs_request_type_form_dict = get_vsan_obj_ext_attrs_request_type.from_dict(get_vsan_obj_ext_attrs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


