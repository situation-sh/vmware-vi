# StructuredCustomizations

Implementation of *HostProfilesEntityCustomizations* that maps a cluster or host profile to the *AnswerFile* object containing the host profiles customizations for that entity.  This object will be used as elements of the *HostProfilesEntityCustomizations*.{vim.profile.host.ProfileManager.EntityCustomizations#entityCustomizations} when the *HostProfilesEntityCustomizations*.{vim.profile.host.ProfileManager.EntityCustomizations#customizationsFormat} value is \"structured\".  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**customizations** | [**AnswerFile**](AnswerFile.md) |  | [optional] 

## Example

```python
from vmware_vi.models.structured_customizations import StructuredCustomizations

# TODO update the JSON string below
json = "{}"
# create an instance of StructuredCustomizations from a JSON string
structured_customizations_instance = StructuredCustomizations.from_json(json)
# print the JSON string representation of the object
print StructuredCustomizations.to_json()

# convert the object into a dict
structured_customizations_dict = structured_customizations_instance.to_dict()
# create an instance of StructuredCustomizations from a dict
structured_customizations_form_dict = structured_customizations.from_dict(structured_customizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


