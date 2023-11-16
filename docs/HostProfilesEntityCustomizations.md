# HostProfilesEntityCustomizations

Data type used to contain a representation of host or cluster customization data in a *HostProfilesCustomizationData* object.  Subclasses of this must be defined to provide host or cluster customization data in specific formats.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_profiles_entity_customizations import HostProfilesEntityCustomizations

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfilesEntityCustomizations from a JSON string
host_profiles_entity_customizations_instance = HostProfilesEntityCustomizations.from_json(json)
# print the JSON string representation of the object
print HostProfilesEntityCustomizations.to_json()

# convert the object into a dict
host_profiles_entity_customizations_dict = host_profiles_entity_customizations_instance.to_dict()
# create an instance of HostProfilesEntityCustomizations from a dict
host_profiles_entity_customizations_form_dict = host_profiles_entity_customizations.from_dict(host_profiles_entity_customizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


