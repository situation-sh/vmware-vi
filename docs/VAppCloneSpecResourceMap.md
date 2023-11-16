# VAppCloneSpecResourceMap

Maps source child entities to destination resource pools and resource settings.  If a mapping is not specified, a child is copied as a direct child of the parent.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**parent** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**resource_spec** | [**ResourceConfigSpec**](ResourceConfigSpec.md) |  | [optional] 
**location** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.v_app_clone_spec_resource_map import VAppCloneSpecResourceMap

# TODO update the JSON string below
json = "{}"
# create an instance of VAppCloneSpecResourceMap from a JSON string
v_app_clone_spec_resource_map_instance = VAppCloneSpecResourceMap.from_json(json)
# print the JSON string representation of the object
print VAppCloneSpecResourceMap.to_json()

# convert the object into a dict
v_app_clone_spec_resource_map_dict = v_app_clone_spec_resource_map_instance.to_dict()
# create an instance of VAppCloneSpecResourceMap from a dict
v_app_clone_spec_resource_map_form_dict = v_app_clone_spec_resource_map.from_dict(v_app_clone_spec_resource_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


