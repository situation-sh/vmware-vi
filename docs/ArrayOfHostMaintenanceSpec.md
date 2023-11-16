# ArrayOfHostMaintenanceSpec

A boxed array of *HostMaintenanceSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostMaintenanceSpec]**](HostMaintenanceSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_maintenance_spec import ArrayOfHostMaintenanceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostMaintenanceSpec from a JSON string
array_of_host_maintenance_spec_instance = ArrayOfHostMaintenanceSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostMaintenanceSpec.to_json()

# convert the object into a dict
array_of_host_maintenance_spec_dict = array_of_host_maintenance_spec_instance.to_dict()
# create an instance of ArrayOfHostMaintenanceSpec from a dict
array_of_host_maintenance_spec_form_dict = array_of_host_maintenance_spec.from_dict(array_of_host_maintenance_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


