# EnumDescription

Static strings used for describing an enumerated type.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Type of enumeration being described.  ***Since:*** vSphere API 4.0  | 
**tags** | [**List[ElementDescription]**](ElementDescription.md) | Element descriptions of all the tags for that enumerated type.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.enum_description import EnumDescription

# TODO update the JSON string below
json = "{}"
# create an instance of EnumDescription from a JSON string
enum_description_instance = EnumDescription.from_json(json)
# print the JSON string representation of the object
print EnumDescription.to_json()

# convert the object into a dict
enum_description_dict = enum_description_instance.to_dict()
# create an instance of EnumDescription from a dict
enum_description_form_dict = enum_description.from_dict(enum_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


