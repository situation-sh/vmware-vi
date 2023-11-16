# ServiceProfile

The *ServiceProfile* data object controls the configuration of a service.  Use the *ApplyProfile.policy* list for access to configuration data for the service profile. Use the *ApplyProfile.property* list for access to subprofiles, if any.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.service_profile import ServiceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfile from a JSON string
service_profile_instance = ServiceProfile.from_json(json)
# print the JSON string representation of the object
print ServiceProfile.to_json()

# convert the object into a dict
service_profile_dict = service_profile_instance.to_dict()
# create an instance of ServiceProfile from a dict
service_profile_form_dict = service_profile.from_dict(service_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


