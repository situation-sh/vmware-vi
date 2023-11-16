# ArrayOfHostProfilesEntityCustomizations

A boxed array of *HostProfilesEntityCustomizations*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostProfilesEntityCustomizations]**](HostProfilesEntityCustomizations.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_profiles_entity_customizations import ArrayOfHostProfilesEntityCustomizations

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostProfilesEntityCustomizations from a JSON string
array_of_host_profiles_entity_customizations_instance = ArrayOfHostProfilesEntityCustomizations.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostProfilesEntityCustomizations.to_json()

# convert the object into a dict
array_of_host_profiles_entity_customizations_dict = array_of_host_profiles_entity_customizations_instance.to_dict()
# create an instance of ArrayOfHostProfilesEntityCustomizations from a dict
array_of_host_profiles_entity_customizations_form_dict = array_of_host_profiles_entity_customizations.from_dict(array_of_host_profiles_entity_customizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


