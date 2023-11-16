# ProfileCreateSpec

Specification describing the parameters during Profile creation  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the profile  ***Since:*** vSphere API 4.0  | [optional] 
**annotation** | **str** | User Provided description of the profile  ***Since:*** vSphere API 4.0  | [optional] 
**enabled** | **bool** | Flag indicating if the Profile is enabled  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.profile_create_spec import ProfileCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileCreateSpec from a JSON string
profile_create_spec_instance = ProfileCreateSpec.from_json(json)
# print the JSON string representation of the object
print ProfileCreateSpec.to_json()

# convert the object into a dict
profile_create_spec_dict = profile_create_spec_instance.to_dict()
# create an instance of ProfileCreateSpec from a dict
profile_create_spec_form_dict = profile_create_spec.from_dict(profile_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


