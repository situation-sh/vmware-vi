# VirtualAppLinkInfo

Deprecated as of vSphere API 5.1.  Linked child information.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**destroy_with_parent** | **bool** | Whether the entity should be removed, when this vApp is removed  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.virtual_app_link_info import VirtualAppLinkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAppLinkInfo from a JSON string
virtual_app_link_info_instance = VirtualAppLinkInfo.from_json(json)
# print the JSON string representation of the object
print VirtualAppLinkInfo.to_json()

# convert the object into a dict
virtual_app_link_info_dict = virtual_app_link_info_instance.to_dict()
# create an instance of VirtualAppLinkInfo from a dict
virtual_app_link_info_form_dict = virtual_app_link_info.from_dict(virtual_app_link_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


