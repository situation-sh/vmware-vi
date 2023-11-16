# ProfileProfileStructureProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** | Name of the property where this ProfileStructureProperty is being used  ***Since:*** vSphere API 5.0  | 
**array** | **bool** | Flag indicating if this property is an Array of profiles  ***Since:*** vSphere API 5.0  | 
**element** | [**ProfileProfileStructure**](ProfileProfileStructure.md) |  | 

## Example

```python
from vmware_vi.models.profile_profile_structure_property import ProfileProfileStructureProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileProfileStructureProperty from a JSON string
profile_profile_structure_property_instance = ProfileProfileStructureProperty.from_json(json)
# print the JSON string representation of the object
print ProfileProfileStructureProperty.to_json()

# convert the object into a dict
profile_profile_structure_property_dict = profile_profile_structure_property_instance.to_dict()
# create an instance of ProfileProfileStructureProperty from a dict
profile_profile_structure_property_form_dict = profile_profile_structure_property.from_dict(profile_profile_structure_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


