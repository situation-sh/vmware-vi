# ProfileProfileStructure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type_name** | **str** | Identifier for the profile type  ***Since:*** vSphere API 5.0  | 
**child** | [**List[ProfileProfileStructureProperty]**](ProfileProfileStructureProperty.md) | SubProfile properties available for this profile  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.profile_profile_structure import ProfileProfileStructure

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileProfileStructure from a JSON string
profile_profile_structure_instance = ProfileProfileStructure.from_json(json)
# print the JSON string representation of the object
print ProfileProfileStructure.to_json()

# convert the object into a dict
profile_profile_structure_dict = profile_profile_structure_instance.to_dict()
# create an instance of ProfileProfileStructure from a dict
profile_profile_structure_form_dict = profile_profile_structure.from_dict(profile_profile_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


