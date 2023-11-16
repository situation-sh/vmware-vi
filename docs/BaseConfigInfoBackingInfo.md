# BaseConfigInfoBackingInfo

The data object type is a base type of backing of a virtual storage object.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.base_config_info_backing_info import BaseConfigInfoBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConfigInfoBackingInfo from a JSON string
base_config_info_backing_info_instance = BaseConfigInfoBackingInfo.from_json(json)
# print the JSON string representation of the object
print BaseConfigInfoBackingInfo.to_json()

# convert the object into a dict
base_config_info_backing_info_dict = base_config_info_backing_info_instance.to_dict()
# create an instance of BaseConfigInfoBackingInfo from a dict
base_config_info_backing_info_form_dict = base_config_info_backing_info.from_dict(base_config_info_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


