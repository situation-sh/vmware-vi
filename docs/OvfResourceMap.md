# OvfResourceMap

Deprecated as of vSphere API 5.1.  Maps source child entities to destination resource pools and resource settings.  If a mapping is not specified, a child is copied as a direct child of the parent.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Identifies a source VirtualSystem or VirtualSystemCollection in an OVF descriptor.  The source cannot be the root VirtualSystem or VirtualSystemCollection of the OVF. This is a path created by concatenating the OVF ids for each entity, e.g., \&quot;vm1\&quot;, \&quot;WebTier/vm2\&quot;, etc.  ***Since:*** vSphere API 4.1  | 
**parent** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**resource_spec** | [**ResourceConfigSpec**](ResourceConfigSpec.md) |  | [optional] 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.ovf_resource_map import OvfResourceMap

# TODO update the JSON string below
json = "{}"
# create an instance of OvfResourceMap from a JSON string
ovf_resource_map_instance = OvfResourceMap.from_json(json)
# print the JSON string representation of the object
print OvfResourceMap.to_json()

# convert the object into a dict
ovf_resource_map_dict = ovf_resource_map_instance.to_dict()
# create an instance of OvfResourceMap from a dict
ovf_resource_map_form_dict = ovf_resource_map.from_dict(ovf_resource_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


