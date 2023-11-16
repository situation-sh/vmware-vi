# CreateVAppRequestType

The parameters of *ResourcePool.CreateVApp*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the vApp container in the inventory  | 
**res_spec** | [**ResourceConfigSpec**](ResourceConfigSpec.md) |  | 
**config_spec** | [**VAppConfigSpec**](VAppConfigSpec.md) |  | 
**vm_folder** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.create_v_app_request_type import CreateVAppRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVAppRequestType from a JSON string
create_v_app_request_type_instance = CreateVAppRequestType.from_json(json)
# print the JSON string representation of the object
print CreateVAppRequestType.to_json()

# convert the object into a dict
create_v_app_request_type_dict = create_v_app_request_type_instance.to_dict()
# create an instance of CreateVAppRequestType from a dict
create_v_app_request_type_form_dict = create_v_app_request_type.from_dict(create_v_app_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


