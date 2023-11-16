# ArrayOfAboutInfo

A boxed array of *AboutInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AboutInfo]**](AboutInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_about_info import ArrayOfAboutInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAboutInfo from a JSON string
array_of_about_info_instance = ArrayOfAboutInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfAboutInfo.to_json()

# convert the object into a dict
array_of_about_info_dict = array_of_about_info_instance.to_dict()
# create an instance of ArrayOfAboutInfo from a dict
array_of_about_info_form_dict = array_of_about_info.from_dict(array_of_about_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


