# UpdateVAppConfigRequestType

The parameters of *VirtualApp.UpdateVAppConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**VAppConfigSpec**](VAppConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_v_app_config_request_type import UpdateVAppConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVAppConfigRequestType from a JSON string
update_v_app_config_request_type_instance = UpdateVAppConfigRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateVAppConfigRequestType.to_json()

# convert the object into a dict
update_v_app_config_request_type_dict = update_v_app_config_request_type_instance.to_dict()
# create an instance of UpdateVAppConfigRequestType from a dict
update_v_app_config_request_type_form_dict = update_v_app_config_request_type.from_dict(update_v_app_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


