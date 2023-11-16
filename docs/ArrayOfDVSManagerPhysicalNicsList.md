# ArrayOfDVSManagerPhysicalNicsList

A boxed array of *DVSManagerPhysicalNicsList*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSManagerPhysicalNicsList]**](DVSManagerPhysicalNicsList.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_manager_physical_nics_list import ArrayOfDVSManagerPhysicalNicsList

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSManagerPhysicalNicsList from a JSON string
array_of_dvs_manager_physical_nics_list_instance = ArrayOfDVSManagerPhysicalNicsList.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSManagerPhysicalNicsList.to_json()

# convert the object into a dict
array_of_dvs_manager_physical_nics_list_dict = array_of_dvs_manager_physical_nics_list_instance.to_dict()
# create an instance of ArrayOfDVSManagerPhysicalNicsList from a dict
array_of_dvs_manager_physical_nics_list_form_dict = array_of_dvs_manager_physical_nics_list.from_dict(array_of_dvs_manager_physical_nics_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


