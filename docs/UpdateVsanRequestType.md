# UpdateVsanRequestType

The parameters of *HostVsanSystem.UpdateVsan_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**VsanHostConfigInfo**](VsanHostConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.update_vsan_request_type import UpdateVsanRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVsanRequestType from a JSON string
update_vsan_request_type_instance = UpdateVsanRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateVsanRequestType.to_json()

# convert the object into a dict
update_vsan_request_type_dict = update_vsan_request_type_instance.to_dict()
# create an instance of UpdateVsanRequestType from a dict
update_vsan_request_type_form_dict = update_vsan_request_type.from_dict(update_vsan_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


